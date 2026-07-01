// 工作流触发面板：用于从前端触发 GitHub Actions workflow，并展示运行进度
// 依赖：GitHub Token（Classic PAT），需要 repo + workflow 权限

window.DPRWorkflowRunner = (function () {
  const WORKFLOWS = [
    {
      key: 'daily-now',
      id: 'daily-paper-reader.yml',
      name: '立即爬取并处理论文',
      desc: '触发 daily-paper-reader 工作流（抓取→召回→重排→生成 docs）。',
      dispatchInputs: {
        run_enrich: 'false',
      },
    },
    {
      key: 'sync',
      id: 'sync.yml',
      name: '同步上游代码',
      desc: '触发 Upstream Sync 工作流（合并上游 main 到当前仓库）。',
    },
    {
      key: 'reset-content',
      id: 'reset-content.yml',
      name: '重置 content（docs + archive）',
      desc: '将 docs 恢复为 docs_init 基线，并清空 archive。该操作为危险操作。',
    },
    {
      key: 'conference-retrieval',
      id: 'conference-paper-retrieval.yml',
      name: '会议论文检索',
      desc: '按会议和年份触发 Supabase BM25/Embedding 候选召回与 RRF 融合。',
      dispatchInputs: {
        top_k: '50',
        rrf_top_n: '200',
        run_rerank: 'true',
        reranker_profile: 'public-zwwen-rerank',
        run_llm_refine: 'true',
      },
    },
    {
      key: 'manual-paper-upload',
      id: 'manual-paper-upload.yml',
      name: '上传 PDF 解析',
      desc: '上传 PDF/ZIP，生成与每日论文相同格式的阅读页面。',
    },
    {
      key: 'hot-paper-scout',
      id: 'hot-paper-scout.yml',
      name: '热点论文筛选',
      desc: '按领域和选中词条从 OpenAlex 筛选最近 7/14/30 天高热论文。',
      dispatchInputs: {
        domain_query: 'embodied intelligence; embodied AI; embodied agents; vision-language-action model; robot foundation model; generalist robot policy; humanoid robot policy; robot learning foundation model',
        days_window: '30',
        institution_filter: 'company',
        max_results: '30',
      },
    },
  ];

  const QUICK_FETCH_PRESETS = {
    '10': {
      key: 'daily-now',
      dispatchInputs: {
        run_enrich: 'false',
        fetch_days: '10',
      },
    },
    '30': {
      key: 'daily-now',
      dispatchInputs: {
        run_enrich: 'false',
        fetch_days: '30',
        fetch_mode: 'skims',
      },
    },
    '30-skims': {
      key: 'daily-now',
      dispatchInputs: {
        run_enrich: 'false',
        fetch_days: '30',
        fetch_mode: 'skims',
      },
    },
    '30-standard': {
      key: 'daily-now',
      dispatchInputs: {
        run_enrich: 'false',
        fetch_days: '30',
        fetch_mode: 'standard',
      },
    },
  };

  const MANUAL_UPLOAD_MAX_BYTES = 500 * 1024 * 1024;
  const MANUAL_UPLOAD_MAX_MB = Math.round(MANUAL_UPLOAD_MAX_BYTES / 1024 / 1024);
  const MANUAL_UPLOAD_CHUNK_BYTES = 4 * 1024 * 1024;
  const MANUAL_UPLOAD_CONTENT_API_SAFE_BYTES = 0;
  const MANUAL_UPLOAD_ACTIVE_RUN_KEY = 'dpr_manual_upload_active_run_v1';
  const MANUAL_UPLOAD_ACTIVE_RUN_TTL_MS = 36 * 60 * 60 * 1000;

  let overlay = null;
  let panel = null;
  let statusEl = null;
  let runsEl = null;
  let recentEl = null;
  let refreshTimer = null;
  let activeRun = null;
  let selectedRun = null;
  let currentPanelMode = 'workflows';
  const lastRunStateById = {};
  let repoContextCache = null;
  let lastValidatedGithubToken = '';

  const escapeHtml = (str) => {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  };

  const pushGithubTokenCandidate = (candidates, seen, token, source) => {
    const value = String(token || '').trim();
    if (!value || seen.has(value)) return;
    seen.add(value);
    candidates.push({ token: value, source });
  };

  const loadGithubTokenCandidates = () => {
    const candidates = [];
    const seen = new Set();
    try {
      const secret = window.decoded_secret_private || {};
      if (secret.github && secret.github.token) {
        pushGithubTokenCandidate(
          candidates,
          seen,
          secret.github.token,
          '密钥配置',
        );
      }
    } catch {
      // ignore
    }
    try {
      const raw = window.localStorage
        ? window.localStorage.getItem('github_token_data')
        : '';
      if (!raw) return candidates;
      const obj = JSON.parse(raw);
      pushGithubTokenCandidate(
        candidates,
        seen,
        obj && obj.token,
        '本地 GitHub Token',
      );
    } catch {
      // ignore
    }
    return candidates;
  };

  const loadGithubToken = () => {
    if (lastValidatedGithubToken) return lastValidatedGithubToken;
    const first = loadGithubTokenCandidates()[0];
    return first ? first.token : '';
  };

  const isGithubAuthStatus = (status) => status === 401 || status === 403;

  const createGithubAuthError = (message) => {
    const err = new Error(message);
    err.isGithubAuthError = true;
    return err;
  };

  const formatGithubApiError = (res, bodyText) => {
    const status = res && res.status ? `HTTP ${res.status}` : 'HTTP 请求失败';
    const statusText = res && res.statusText ? ` ${res.statusText}` : '';
    const body = String(bodyText || '').trim();
    return body ? `${status}${statusText} - ${body}` : `${status}${statusText}`;
  };
  const loadRerankerProfile = () => {
    try {
      const secret = window.decoded_secret_private || {};
      const reranker = secret.rerankerLLM || {};
      const profile = String(reranker.profile || '').trim();
      if (profile) return profile;
      if (isLocalDebugPage()) return 'public-zwwen-rerank';
      return '';
    } catch {
      return isLocalDebugPage() ? 'public-zwwen-rerank' : '';
    }
  };

  const resolveRepoFromUrl = async (token) => {
    const currentUrl = window.location.href || '';
    const githubPagesMatch = currentUrl.match(
      /https?:\/\/([^.]+)\.github\.io\/([^\/]+)/,
    );
    if (githubPagesMatch) {
      return { owner: githubPagesMatch[1], repo: githubPagesMatch[2] };
    }

    // 非 GitHub Pages URL：回退到「Token 对应的用户 + daily-paper-reader」作为默认目标仓库
    try {
      const userRes = await ghFetch(token, 'https://api.github.com/user');
      if (userRes.ok) {
        const user = await userRes.json();
        const login = (user && user.login) ? String(user.login) : '';
        if (login) {
          return { owner: login, repo: 'daily-paper-reader' };
        }
      }
    } catch {
      // ignore
    }

    return { owner: '', repo: '' };
  };

  const resolveRepoContext = async (token, options = {}) => {
    const { forceRefresh = false } = options || {};
    const { owner, repo } = await resolveRepoFromUrl(token);
    if (!owner || !repo) {
      return { owner: '', repo: '', isFork: null, defaultBranch: 'main' };
    }

    const cacheKey = `${owner}/${repo}`;
    if (!forceRefresh && repoContextCache && repoContextCache.key === cacheKey && repoContextCache.value) {
      return repoContextCache.value;
    }
    if (!forceRefresh && repoContextCache && repoContextCache.key === cacheKey && repoContextCache.promise) {
      return repoContextCache.promise;
    }

    const fetchPromise = (async () => {
      try {
        const repoUrl = `https://api.github.com/repos/${owner}/${repo}`;
        const res = await ghFetch(token, repoUrl);
        if (!res.ok) {
          const txt = await res.text().catch(() => '');
          if (isGithubAuthStatus(res.status)) {
            throw createGithubAuthError(
              `GitHub Token 无效或权限不足：读取 ${owner}/${repo} 失败，${formatGithubApiError(
                res,
                txt,
              )}。请重新保存密钥配置中的 GitHub Token，需具备 repo、workflow 权限。`,
            );
          }
          return { owner, repo, isFork: null, defaultBranch: 'main' };
        }
        const data = await res.json().catch(() => null);
        if (
          data &&
          data.permissions &&
          Object.prototype.hasOwnProperty.call(data.permissions, 'push') &&
          data.permissions.push === false
        ) {
          throw createGithubAuthError(
            `GitHub Token 可以读取 ${owner}/${repo}，但没有写入权限。请重新生成或保存具备 repo、workflow 权限的 Token。`,
          );
        }
        return {
          owner,
          repo,
          isFork: !!(data && data.fork),
          defaultBranch: String((data && data.default_branch) || 'main'),
        };
      } catch (e) {
        if (e && e.isGithubAuthError) throw e;
        return { owner, repo, isFork: null, defaultBranch: 'main' };
      }
    })();

    repoContextCache = { key: cacheKey, promise: fetchPromise, value: null };
    try {
      const value = await fetchPromise;
      repoContextCache = { key: cacheKey, promise: null, value };
      return value;
    } catch (e) {
      if (repoContextCache && repoContextCache.promise === fetchPromise) {
        repoContextCache = null;
      }
      throw e;
    }
  };

  const resolveRepoContextFromAvailableToken = async () => {
    const candidates = loadGithubTokenCandidates();
    if (!candidates.length) {
      lastValidatedGithubToken = '';
      throw createGithubAuthError(
        '未检测到 GitHub Token：请在密钥配置中保存具备 repo、workflow 权限的 GitHub Token。',
      );
    }

    let lastError = null;
    for (const candidate of candidates) {
      try {
        // 每个候选 token 都强制校验一次，避免坏 token 复用前一次缓存。
        const repoContext = await resolveRepoContext(candidate.token, {
          forceRefresh: true,
        });
        if (repoContext.owner && repoContext.repo) {
          lastValidatedGithubToken = candidate.token;
          return {
            ...repoContext,
            token: candidate.token,
            tokenSource: candidate.source,
          };
        }
        lastError = createGithubAuthError(
          `无法用${candidate.source}推断目标仓库，请确认当前访问地址和 Token 配置。`,
        );
      } catch (e) {
        lastError = e;
      }
    }

    lastValidatedGithubToken = '';
    throw createGithubAuthError(
      lastError && lastError.message
        ? lastError.message
        : 'GitHub Token 无效或权限不足，请重新保存具备 repo、workflow 权限的 Token。',
    );
  };

  const ghFetch = async (token, url, init) => {
    const res = await fetch(url, {
      ...(init || {}),
      headers: {
        Authorization: `token ${token}`,
        Accept: 'application/vnd.github.v3+json',
        ...(init && init.headers ? init.headers : {}),
      },
    });
    return res;
  };

  const isLocalDebugPage = () => {
    if (window.DPR_LOCAL_API_BASE) return true;
    const host = String((window.location && window.location.hostname) || '').toLowerCase();
    if (host === 'localhost' || host === '127.0.0.1' || host === '0.0.0.0') return true;
    if (/^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$/.test(host)) return true;
    if (/^192\.168\.\d{1,3}\.\d{1,3}$/.test(host)) return true;
    if (/^172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}$/.test(host)) return true;
    return false;
  };

  const getLocalApiUrl = (path) => {
    const base = String(window.DPR_LOCAL_API_BASE || '').trim().replace(/\/$/, '');
    if (!base && isLocalDebugPage()) {
      const protocol = String((window.location && window.location.protocol) || 'http:');
      const hostname = String((window.location && window.location.hostname) || '127.0.0.1');
      return `${protocol}//${hostname}:8567${path}`;
    }
    if (!base) return path;
    return `${base}${path}`;
  };

  const localApiFetch = async (path, init) => {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 10000);
    try {
      const res = await fetch(getLocalApiUrl(path), {
        ...(init || {}),
        signal: controller.signal,
        headers: {
          'Content-Type': 'application/json',
          ...(init && init.headers ? init.headers : {}),
        },
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || !data.ok) {
        throw new Error((data && data.error) || `本地调试后端请求失败：HTTP ${res.status}`);
      }
      return data;
    } catch (e) {
      if (e && e.name === 'AbortError') {
        throw new Error('本地调试后端请求超时，请确认 8567 端口服务正在运行。');
      }
      throw e;
    } finally {
      clearTimeout(timeout);
    }
  };

  const localUploadFetch = async (path, formData) => {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 180000);
    try {
      const res = await fetch(getLocalApiUrl(path), {
        method: 'POST',
        body: formData,
        signal: controller.signal,
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || !data.ok) {
        throw new Error((data && data.error) || `本地上传失败：HTTP ${res.status}`);
      }
      return data;
    } catch (e) {
      if (e && e.name === 'AbortError') {
        throw new Error('本地上传超时，请减少单次文件数量或确认 8567 端口服务正在运行。');
      }
      throw e;
    } finally {
      clearTimeout(timeout);
    }
  };

  const pad2 = (value) => String(value).padStart(2, '0');

  const buildManualBatchDefaults = () => {
    const d = new Date();
    const yyyy = d.getFullYear();
    const mm = pad2(d.getMonth() + 1);
    const dd = pad2(d.getDate());
    const hh = pad2(d.getHours());
    const mi = pad2(d.getMinutes());
    const ss = pad2(d.getSeconds());
    return {
      token: `manual-${yyyy}${mm}${dd}-${hh}${mi}${ss}`,
      label: `手动上传 · ${yyyy}-${mm}-${dd} ${hh}:${mi}`,
    };
  };

  const safeUploadFileName = (file, index) => {
    const raw = String((file && file.name) || `upload-${index + 1}`).trim();
    const lower = raw.toLowerCase();
    const suffix = lower.endsWith('.zip') ? '.zip' : '.pdf';
    const stem = raw.replace(/\.[^.]+$/, '');
    const safeStem = stem
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^a-z0-9._-]+/g, '-')
      .replace(/^-+|-+$/g, '') || `upload-${index + 1}`;
    return `${String(index + 1).padStart(3, '0')}-${safeStem}${suffix}`;
  };

  const readFileAsBase64 = (file) =>
    new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => {
        const text = String(reader.result || '');
        resolve(text.includes(',') ? text.split(',', 2)[1] : text);
      };
      reader.onerror = () => reject(reader.error || new Error('读取文件失败'));
      reader.readAsDataURL(file);
    });

  const stringToBase64 = (text) => {
    const bytes = new TextEncoder().encode(String(text || ''));
    let binary = '';
    bytes.forEach((byte) => {
      binary += String.fromCharCode(byte);
    });
    return btoa(binary);
  };

  const normalizeManualUploadOptions = (options) => {
    const defaults = buildManualBatchDefaults();
    const section = String((options && options.section) || 'deep').trim().toLowerCase() === 'quick' ? 'quick' : 'deep';
    const label = String((options && options.label) || '').trim() || defaults.label;
    const tag = String((options && options.tag) || '').trim() || '手动上传';
    const docsConcurrency = String((options && options.docsConcurrency) || '2').trim() || '2';
    return {
      batchToken: defaults.token,
      label,
      section,
      tag,
      docsConcurrency,
    };
  };

  const explainFetchFailure = (error) => {
    const msg = error && error.message ? String(error.message) : String(error || '');
    if (
      error &&
      error.isGithubAuthError
    ) {
      return msg;
    }
    if (/bad credentials|http\s+401|http\s+403/i.test(msg)) {
      return `${msg}（GitHub Token 无效、已过期或权限不足；请重新保存具备 repo、workflow 权限的 Token 后再上传。）`;
    }
    if (!/failed to fetch|networkerror/i.test(msg)) return msg;
    return `${msg}（浏览器没有收到接口响应。若发生在在线上传阶段，通常是网络/代理中断、刷新取消上传，或 GitHub 上传接口跨域/请求被中断；此时解析一般还没有开始。）`;
  };

  const extractManualBatchToken = (dispatchInputs) => {
    const ref = String((dispatchInputs && dispatchInputs.upload_ref) || '').replace(/\/+$/g, '');
    const parts = ref.split('/').filter(Boolean);
    const token = parts.length ? parts[parts.length - 1] : '';
    return /^manual-[a-z0-9._-]+$/i.test(token) ? token : '';
  };

  const getBrowserStorage = () => {
    try {
      return window.localStorage || null;
    } catch {
      return null;
    }
  };

  const normalizePersistedManualRun = (run) => {
    if (!run || typeof run !== 'object') return null;
    const runId = String(run.runId || '').trim();
    const manualBatchToken = String(run.manualBatchToken || '').trim();
    if (!runId || !/^manual-[a-z0-9._-]+$/i.test(manualBatchToken)) return null;
    const local = !!run.local;
    const owner = String(run.owner || '').trim();
    const repo = String(run.repo || '').trim();
    if (!local && (!owner || !repo)) return null;
    const savedAt = Number(run.savedAt || 0) || Date.now();
    if (Date.now() - savedAt > MANUAL_UPLOAD_ACTIVE_RUN_TTL_MS) return null;
    return { local, owner, repo, runId, manualBatchToken, savedAt };
  };

  const persistManualActiveRun = (run) => {
    const storage = getBrowserStorage();
    if (!storage) return;
    const normalized = normalizePersistedManualRun({
      ...(run || {}),
      savedAt: Date.now(),
    });
    if (!normalized) return;
    try {
      storage.setItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY, JSON.stringify(normalized));
    } catch {
      // ignore storage errors in private browsing or locked-down environments
    }
  };

  const loadPersistedManualActiveRun = () => {
    const storage = getBrowserStorage();
    if (!storage) return null;
    try {
      const raw = storage.getItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY);
      if (!raw) return null;
      const normalized = normalizePersistedManualRun(JSON.parse(raw));
      if (!normalized) {
        storage.removeItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY);
        return null;
      }
      return normalized;
    } catch {
      try {
        storage.removeItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY);
      } catch {
        // ignore
      }
      return null;
    }
  };

  const clearPersistedManualActiveRun = (runId) => {
    const storage = getBrowserStorage();
    if (!storage) return;
    try {
      if (!runId) {
        storage.removeItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY);
        return;
      }
      const raw = storage.getItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY);
      if (!raw) return;
      const saved = JSON.parse(raw);
      if (String((saved && saved.runId) || '') === String(runId || '')) {
        storage.removeItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY);
      }
    } catch {
      try {
        storage.removeItem(MANUAL_UPLOAD_ACTIVE_RUN_KEY);
      } catch {
        // ignore
      }
    }
  };

  const manualResultHash = (batchToken) => `#/manual/${encodeURIComponent(batchToken)}/README`;

  const manualResultMarkdownUrl = (batchToken) =>
    `docs/manual/${encodeURIComponent(batchToken)}/README.md?dpr_manual_result=${Date.now()}`;

  const renderManualResultNotice = (batchToken, state) => {
    if (!runsEl || !batchToken) return;
    const existing = document.getElementById('dpr-manual-result-notice');
    if (existing) existing.remove();
    const hash = manualResultHash(batchToken);
    const isReady = state === 'ready';
    const title = isReady ? '解析结果已发布' : '解析已完成，正在等待网页发布';
    const hint = isReady
      ? '点击下面按钮查看本次上传生成的日报与论文页。'
      : 'GitHub Pages 有几十秒部署延迟，发布完成后这个按钮就能打开结果。';
    runsEl.insertAdjacentHTML(
      'afterbegin',
      `
        <div id="dpr-manual-result-notice" style="margin-bottom:10px; padding:10px 12px; border:1px solid rgba(46,125,50,0.18); border-radius:8px; background:#f0fdf4;">
          <div style="font-weight:700; color:#166534;">${escapeHtml(title)}</div>
          <div style="margin-top:4px; color:#3f5f46;">${escapeHtml(hint)}</div>
          <div style="margin-top:8px; display:flex; gap:8px; flex-wrap:wrap; align-items:center;">
            <a class="arxiv-tool-btn" style="padding:6px 10px; text-decoration:none;" href="${hash}">打开解析结果</a>
            <code style="font-size:12px; color:#456;">${escapeHtml(hash)}</code>
          </div>
        </div>
      `,
    );
  };

  const waitForManualDocsPublication = async (batchToken) => {
    if (!batchToken) return false;
    renderManualResultNotice(batchToken, 'pending');
    for (let i = 0; i < 30; i += 1) {
      try {
        // eslint-disable-next-line no-await-in-loop
        const res = await fetch(manualResultMarkdownUrl(batchToken), { cache: 'no-store' });
        if (res.ok) {
          renderManualResultNotice(batchToken, 'ready');
          setStatus('解析完成，结果页已发布。', '#080');
          return true;
        }
      } catch {
        // ignore transient network errors while Pages is deploying
      }
      // eslint-disable-next-line no-await-in-loop
      await new Promise((resolve) => setTimeout(resolve, 5000));
    }
    renderManualResultNotice(batchToken, 'pending');
    setStatus('解析完成，但 GitHub Pages 可能仍在部署；稍后刷新后打开结果页。', '#c90');
    return false;
  };

  const uploadFilesToGithub = async (owner, repo, token, branch, batchToken, files) => {
    const uploaded = [];
    for (let i = 0; i < files.length; i += 1) {
      const file = files[i];
      const name = safeUploadFileName(file, i);
      const path = `uploads/manual-papers/${batchToken}/${name}`;
      setStatus(`正在上传文件 ${i + 1}/${files.length}：${name}`, '#1565c0', { waiting: true });
      // eslint-disable-next-line no-await-in-loop
      const content = await readFileAsBase64(file);
      const url = `https://api.github.com/repos/${owner}/${repo}/contents/${encodeURIComponent(path).replace(/%2F/g, '/')}`;
      // eslint-disable-next-line no-await-in-loop
      const res = await ghFetch(token, url, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: `[chore] upload manual PDFs ${batchToken}`,
          branch,
          content,
        }),
      });
      if (!res.ok) {
        const txt = await res.text().catch(() => '');
        throw new Error(`上传 ${name} 失败：HTTP ${res.status} ${res.statusText} - ${txt}`);
      }
      uploaded.push(path);
    }
    return uploaded;
  };

  const encodeGithubPath = (path) => encodeURIComponent(path).replace(/%2F/g, '/');

  const uploadContentToGithubBranch = async (owner, repo, token, branch, path, content, message) => {
    const url = `https://api.github.com/repos/${owner}/${repo}/contents/${encodeGithubPath(path)}`;
    const res = await ghFetch(token, url, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message,
        branch,
        content,
      }),
    });
    if (!res.ok) {
      const txt = await res.text().catch(() => '');
      throw new Error(`上传分片失败：HTTP ${res.status} ${res.statusText} - ${txt}`);
    }
    return res.json();
  };

  const deleteGithubBranch = async (owner, repo, token, branchName) => {
    if (!branchName) return;
    try {
      await ghFetch(
        token,
        `https://api.github.com/repos/${owner}/${repo}/git/refs/heads/${encodeURIComponent(branchName)}`,
        { method: 'DELETE' },
      );
    } catch {
      // Best-effort cleanup. The workflow deletes the temp branch after it fetches chunks.
    }
  };

  const createTempUploadBranch = async (owner, repo, token, baseBranch, batchToken) => {
    const branchName = `dpr-manual-upload-${batchToken}`.replace(/[^A-Za-z0-9._-]+/g, '-');
    const refUrl = `https://api.github.com/repos/${owner}/${repo}/git/ref/heads/${encodeURIComponent(baseBranch)}`;
    const refRes = await ghFetch(token, refUrl);
    if (!refRes.ok) {
      const txt = await refRes.text().catch(() => '');
      throw new Error(`读取默认分支失败：HTTP ${refRes.status} ${refRes.statusText} - ${txt}`);
    }
    const refData = await refRes.json();
    const sha = refData && refData.object && refData.object.sha ? String(refData.object.sha) : '';
    if (!sha) throw new Error('读取默认分支失败：未获得 commit sha。');

    const create = async () => ghFetch(token, `https://api.github.com/repos/${owner}/${repo}/git/refs`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ref: `refs/heads/${branchName}`,
        sha,
      }),
    });

    let createRes = await create();
    if (!createRes.ok && createRes.status === 422) {
      await deleteGithubBranch(owner, repo, token, branchName);
      createRes = await create();
    }
    if (!createRes.ok) {
      const txt = await createRes.text().catch(() => '');
      throw new Error(`创建临时上传分支失败：HTTP ${createRes.status} ${createRes.statusText} - ${txt}`);
    }
    return branchName;
  };

  const uploadFilesToTempBranchChunks = async (owner, repo, token, baseBranch, batchToken, files) => {
    const branchName = await createTempUploadBranch(owner, repo, token, baseBranch, batchToken);
    const manifest = {
      version: 1,
      batchToken,
      chunkBytes: MANUAL_UPLOAD_CHUNK_BYTES,
      files: [],
    };
    let uploadedChunks = 0;
    const totalChunks = files.reduce(
      (sum, file) => sum + Math.max(1, Math.ceil(Number(file.size || 0) / MANUAL_UPLOAD_CHUNK_BYTES)),
      0,
    );

    for (let i = 0; i < files.length; i += 1) {
      const file = files[i];
      const name = safeUploadFileName(file, i);
      const fileId = `${String(i + 1).padStart(3, '0')}-${name.replace(/[^A-Za-z0-9._-]+/g, '-')}`;
      const chunks = [];
      const chunkCount = Math.max(1, Math.ceil(Number(file.size || 0) / MANUAL_UPLOAD_CHUNK_BYTES));
      for (let chunkIndex = 0; chunkIndex < chunkCount; chunkIndex += 1) {
        const start = chunkIndex * MANUAL_UPLOAD_CHUNK_BYTES;
        const end = Math.min(Number(file.size || 0), start + MANUAL_UPLOAD_CHUNK_BYTES);
        const relPath = `${fileId}/chunk-${String(chunkIndex + 1).padStart(5, '0')}.part`;
        const path = `.manual-upload-chunks/${batchToken}/${relPath}`;
        uploadedChunks += 1;
        setStatus(`正在上传分片 ${uploadedChunks}/${totalChunks}：${name}`, '#1565c0', { waiting: true });
        // eslint-disable-next-line no-await-in-loop
        const content = await readFileAsBase64(file.slice(start, end));
        // eslint-disable-next-line no-await-in-loop
        await uploadContentToGithubBranch(
          owner,
          repo,
          token,
          branchName,
          path,
          content,
          `[chore] upload manual PDF chunk ${batchToken}`,
        );
        chunks.push(relPath);
      }
      manifest.files.push({
        name,
        size: Number(file.size || 0),
        type: String(file.type || ''),
        chunks,
      });
    }

    setStatus('正在上传分片清单...', '#1565c0', { waiting: true });
    await uploadContentToGithubBranch(
      owner,
      repo,
      token,
      branchName,
      `.manual-upload-chunks/${batchToken}/manifest.json`,
      stringToBase64(JSON.stringify(manifest, null, 2)),
      `[chore] upload manual PDF manifest ${batchToken}`,
    );
    return { branchName };
  };

  const createManualUploadRelease = async (owner, repo, token, branch, batchToken, label) => {
    const tagName = `dpr-manual-upload-${batchToken}`;
    const res = await ghFetch(token, `https://api.github.com/repos/${owner}/${repo}/releases`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tag_name: tagName,
        target_commitish: branch,
        name: label || `Manual upload ${batchToken}`,
        body: 'Temporary upload release for daily-paper-reader manual PDF parsing.',
        draft: true,
        prerelease: true,
      }),
    });
    if (!res.ok) {
      const txt = await res.text().catch(() => '');
      throw new Error(`创建临时 Release 失败：HTTP ${res.status} ${res.statusText} - ${txt}`);
    }
    return res.json();
  };

  const deleteManualUploadRelease = async (owner, repo, token, releaseId) => {
    if (!releaseId) return;
    try {
      await ghFetch(token, `https://api.github.com/repos/${owner}/${repo}/releases/${encodeURIComponent(releaseId)}`, {
        method: 'DELETE',
      });
    } catch {
      // Best-effort cleanup only. The workflow also deletes the release after success.
    }
  };

  const uploadFilesToGithubReleaseAssets = async (owner, repo, token, branch, batchToken, files, label) => {
    const release = await createManualUploadRelease(owner, repo, token, branch, batchToken, label);
    const releaseId = release && release.id ? String(release.id) : '';
    const uploadUrlBase = String((release && release.upload_url) || '').replace(/\{.*$/g, '');
    if (!releaseId || !uploadUrlBase) {
      throw new Error('创建临时 Release 后未获得有效 upload_url。');
    }

    const assets = [];
    for (let i = 0; i < files.length; i += 1) {
      const file = files[i];
      const name = safeUploadFileName(file, i);
      const uploadUrl = `${uploadUrlBase}?name=${encodeURIComponent(name)}`;
      setStatus(`正在上传大文件 ${i + 1}/${files.length}：${name}`, '#1565c0', { waiting: true });
      // eslint-disable-next-line no-await-in-loop
      const res = await fetch(uploadUrl, {
        method: 'POST',
        headers: {
          Authorization: `token ${token}`,
          Accept: 'application/vnd.github+json',
          'Content-Type': file.type || 'application/octet-stream',
          'X-GitHub-Api-Version': '2022-11-28',
        },
        body: file,
      });
      if (!res.ok) {
        const txt = await res.text().catch(() => '');
        throw new Error(`上传 ${name} 到临时 Release 失败：HTTP ${res.status} ${res.statusText} - ${txt}`);
      }
      // eslint-disable-next-line no-await-in-loop
      const asset = await res.json();
      assets.push({
        id: String((asset && asset.id) || ''),
        name: String((asset && asset.name) || name),
      });
    }
    return { releaseId, assets };
  };

  const isWorkflowLogNearBottom = (logEl) => {
    if (!logEl) return true;
    const distance =
      Number(logEl.scrollHeight || 0) -
      Number(logEl.scrollTop || 0) -
      Number(logEl.clientHeight || 0);
    return distance <= 24;
  };

  const scrollWorkflowLogToBottom = (shouldScroll) => {
    if (!runsEl || !shouldScroll) return;
    requestAnimationFrame(() => {
      const logEl = runsEl.querySelector('[data-dpr-workflow-log]');
      if (logEl) {
        logEl.scrollTop = logEl.scrollHeight;
      }
    });
  };

  const renderLocalRun = (run, logText) => {
    if (!runsEl || !run) return;
    const previousLogEl = runsEl.querySelector('[data-dpr-workflow-log]');
    const shouldFollowLog = isWorkflowLogNearBottom(previousLogEl);
    const status = run.status || '';
    const conclusion = run.conclusion || '';
    const badgeColor =
      conclusion === 'success'
        ? '#2e7d32'
        : conclusion === 'failure'
          ? '#c00'
          : status === 'in_progress'
            ? '#1565c0'
            : '#666';
    const command = Array.isArray(run.command) ? run.command.join(' ') : '';
    const logHtml = logText
      ? `<pre data-dpr-workflow-log="1" style="white-space:pre-wrap; max-height:360px; overflow:auto; background:#111; color:#ddd; padding:10px; border-radius:6px; font-size:12px;">${escapeHtml(logText)}</pre>`
      : '<div style="color:#999;">暂无日志。</div>';
    runsEl.innerHTML = `
      <div style="margin-bottom:8px;">
        <div style="font-weight:600;">本地运行 #${escapeHtml(run.run_number || run.id)}</div>
        <div style="color:#666; margin-top:2px;">
          <span style="display:inline-block; padding:1px 6px; border-radius:999px; background:rgba(0,0,0,0.06); color:${badgeColor};">
            ${escapeHtml(formatRunBadgeText(status, conclusion))}
          </span>
          <span style="margin-left:8px;">${escapeHtml(formatRunTime(run.created_at))}</span>
        </div>
      </div>
      <div style="font-size:12px; color:#666; margin-bottom:8px;">${escapeHtml(command)}</div>
      ${logHtml}
    `;
    scrollWorkflowLogToBottom(shouldFollowLog);
  };

  const refreshLocalRun = async (runId) => {
    try {
      const data = await localApiFetch(`/api/local/runs/${encodeURIComponent(runId)}/log`);
      const run = data.run || {};
      renderLocalRun(run, data.log || '');
      if (run.status === 'completed') {
        stopPolling();
        setStatus(
          `本地运行已结束：${run.conclusion || 'completed'}`,
          run.conclusion === 'success' ? '#080' : '#c00',
        );
        if (run.conclusion === 'success' && activeRun && activeRun.manualBatchToken) {
          renderManualResultNotice(activeRun.manualBatchToken, 'ready');
        }
        clearPersistedManualActiveRun(runId);
        return false;
      } else {
        setStatus('本地运行中：每 5 秒自动刷新...', '#1565c0', { waiting: true });
        return true;
      }
    } catch (e) {
      console.error(e);
      setStatus(`刷新本地运行失败：${explainFetchFailure(e)}`, '#c00');
      return false;
    }
  };

  const dispatchLocalAndMonitor = async (wf, workflowFile, dispatchInputs) => {
    stopPolling();
    activeRun = null;
    setStatus(`正在触发本地调试任务：${wf.name || workflowFile} ...`, '#666', { waiting: true });
    runsEl.innerHTML = '<div style="color:#999;">正在请求本地后端，请稍候...</div>';
    const localConfigOverride = window.SubscriptionsGithubToken &&
      typeof window.SubscriptionsGithubToken.loadLocalConfigOverride === 'function'
      ? window.SubscriptionsGithubToken.loadLocalConfigOverride()
      : null;
    const localSecret = window.decoded_secret_private && typeof window.decoded_secret_private === 'object'
      ? window.decoded_secret_private
      : null;
    const data = await localApiFetch('/api/local/workflows/dispatch', {
      method: 'POST',
      body: JSON.stringify({
        workflowKey: wf.key || '',
        workflowFile,
        inputs: dispatchInputs || {},
        config: localConfigOverride && localConfigOverride.config ? localConfigOverride.config : null,
        secret: localSecret,
      }),
    });
    const run = data.run || {};
    activeRun = { local: true, runId: run.id, manualBatchToken: extractManualBatchToken(dispatchInputs) };
    selectedRun = activeRun;
    if (activeRun.manualBatchToken) {
      persistManualActiveRun(activeRun);
    }
    setStatus(`本地运行已创建：run_id=${run.id}`, '#080', { waiting: true });
    const shouldPoll = await refreshLocalRun(run.id);
    if (shouldPoll) {
      refreshTimer = setInterval(() => {
        const r = selectedRun || activeRun;
        if (!r || !r.local) return;
        refreshLocalRun(r.runId);
      }, 5000);
    }
  };

  const dispatchLocalManualUploadAndMonitor = async (files, options) => {
    stopPolling();
    activeRun = null;
    const wf = getWorkflowByKey('manual-paper-upload') || { name: '上传 PDF 解析' };
    const normalized = normalizeManualUploadOptions(options);
    setStatus('正在上传到本地调试后端...', '#1565c0', { waiting: true });
    runsEl.innerHTML = '<div style="color:#999;">正在上传文件，请稍候...</div>';

    const form = new FormData();
    files.forEach((file) => form.append('files', file, file.name));
    form.append('batchToken', normalized.batchToken);
    form.append('label', normalized.label);
    form.append('section', normalized.section);
    form.append('tag', normalized.tag);
    form.append('docsConcurrency', normalized.docsConcurrency);

    const localConfigOverride = window.SubscriptionsGithubToken &&
      typeof window.SubscriptionsGithubToken.loadLocalConfigOverride === 'function'
      ? window.SubscriptionsGithubToken.loadLocalConfigOverride()
      : null;
    if (localConfigOverride && localConfigOverride.config) {
      form.append('config', JSON.stringify(localConfigOverride.config));
    }
    const localSecret = window.decoded_secret_private && typeof window.decoded_secret_private === 'object'
      ? window.decoded_secret_private
      : null;
    if (localSecret) {
      form.append('secret', JSON.stringify(localSecret));
    }

    const data = await localUploadFetch('/api/local/manual-papers/upload', form);
    const run = data.run || {};
    activeRun = { local: true, runId: run.id, manualBatchToken: normalized.batchToken };
    selectedRun = activeRun;
    persistManualActiveRun(activeRun);
    setStatus(`${wf.name}已创建：run_id=${run.id}`, '#080', { waiting: true });
    const shouldPoll = await refreshLocalRun(run.id);
    if (shouldPoll) {
      refreshTimer = setInterval(() => {
        const r = selectedRun || activeRun;
        if (!r || !r.local) return;
        refreshLocalRun(r.runId);
      }, 5000);
    }
  };

  const resolveWorkflowRunInputs = async (owner, repo, token, runId) => {
    if (!owner || !repo || !runId || !token) return null;
    const runUrl = `https://api.github.com/repos/${owner}/${repo}/actions/runs/${runId}`;
    try {
      const res = await ghFetch(token, runUrl);
      if (!res.ok) return null;
      const data = await res.json().catch(() => null);
      if (!data || typeof data !== 'object') return null;
      if (data.inputs && typeof data.inputs === 'object') {
        return data.inputs;
      }
      return null;
    } catch {
      return null;
    }
  };

  const resolveRecentRunTag = async (owner, repo, token, run) => {
    if (!run) return 'daily-now';
    // 统一归类到 daily-now，触发面板不再单独展示一个月/一个月标准入口
    if (run.inputs && typeof run.inputs === 'object') return 'daily-now';
    await resolveWorkflowRunInputs(owner, repo, token, run.id);
    return 'daily-now';
  };

  const setStatus = (text, color, options = {}) => {
    if (!statusEl) return;
    statusEl.textContent = text || '';
    statusEl.style.color = color || '#666';
    statusEl.classList.toggle('is-waiting', !!(options && options.waiting));
  };

  const ensureOverlay = () => {
    if (overlay && panel) return;
    overlay = document.getElementById('dpr-workflow-overlay');
    if (overlay) {
      panel = document.getElementById('dpr-workflow-panel');
      statusEl = document.getElementById('dpr-workflow-status');
      runsEl = document.getElementById('dpr-workflow-runs');
      recentEl = document.getElementById('dpr-workflow-recent');
      return;
    }

    overlay = document.createElement('div');
    overlay.id = 'dpr-workflow-overlay';
    overlay.innerHTML = `
      <div id="dpr-workflow-panel">
        <div id="dpr-workflow-header">
          <div id="dpr-workflow-title" style="font-weight:600;">工作流触发</div>
          <div style="display:flex; gap:8px; align-items:center;">
            <button id="dpr-workflow-refresh-btn" class="arxiv-tool-btn" style="padding:2px 10px;">刷新</button>
            <button id="dpr-workflow-close-btn" class="arxiv-tool-btn" style="padding:2px 6px;">关闭</button>
          </div>
        </div>
        <div id="dpr-workflow-body">
          <div id="dpr-workflow-status" style="font-size:12px; color:#666; margin-bottom:10px;">准备就绪。</div>
          <div id="dpr-manual-upload-card" class="dpr-wf-card dpr-manual-upload-card">
            <div class="dpr-manual-upload-head">
              <div>
                <div class="dpr-manual-upload-title">上传 PDF 解析</div>
              </div>
              <button id="dpr-manual-upload-run" class="arxiv-tool-btn dpr-manual-upload-run">开始解析</button>
            </div>
            <div class="dpr-manual-upload-grid">
              <label class="dpr-manual-file-pick">
                <input id="dpr-manual-upload-files" type="file" accept=".pdf,.zip,application/pdf,application/zip" multiple />
                <span>选择 PDF/ZIP</span>
              </label>
              <select id="dpr-manual-upload-section" class="dpr-manual-upload-input" aria-label="输出区域">
                <option value="deep">精读区</option>
                <option value="quick">速读区</option>
              </select>
              <input id="dpr-manual-upload-label" class="dpr-manual-upload-input" type="text" placeholder="批次标题" />
              <input id="dpr-manual-upload-tag" class="dpr-manual-upload-input" type="text" value="手动上传" aria-label="标签" />
            </div>
            <div id="dpr-manual-upload-file-list" class="dpr-manual-upload-file-list">尚未选择文件。</div>
          </div>
          <div id="dpr-workflow-recent-title" style="font-weight:600; font-size:13px; margin-bottom:6px;">最近运行（各取 3 条）</div>
          <div id="dpr-workflow-recent" style="font-size:12px; color:#333; border:1px solid #eee; border-radius:8px; background:#fff; padding:10px; margin-bottom:12px;">
            <div style="color:#999;">加载中...</div>
          </div>
          <div id="dpr-workflow-runs-title" style="font-weight:600; font-size:13px; margin-bottom:6px;">执行过程</div>
          <div id="dpr-workflow-runs" style="font-size:12px; color:#333; border:1px solid #eee; border-radius:8px; background:#fff; padding:10px; min-height:120px;">
            <div style="color:#999;">尚未触发工作流。</div>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(overlay);

    panel = document.getElementById('dpr-workflow-panel');
    statusEl = document.getElementById('dpr-workflow-status');
    runsEl = document.getElementById('dpr-workflow-runs');
    recentEl = document.getElementById('dpr-workflow-recent');

    const closeBtn = document.getElementById('dpr-workflow-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', close);
    }
    overlay.addEventListener('mousedown', (e) => {
      if (e.target === overlay) close();
    });

    const refreshBtn = document.getElementById('dpr-workflow-refresh-btn');
    if (refreshBtn) {
      refreshBtn.addEventListener('click', () => {
        const r = selectedRun || activeRun;
        if (r && r.local && r.runId) {
          refreshLocalRun(r.runId);
        } else if (r && r.owner && r.repo && r.runId) {
          refreshRun(r.owner, r.repo, r.runId);
        } else {
          setStatus('暂无可刷新的运行记录。', '#666');
        }
      });
    }

    const fileInput = document.getElementById('dpr-manual-upload-files');
    const fileList = document.getElementById('dpr-manual-upload-file-list');
    const runUploadBtn = document.getElementById('dpr-manual-upload-run');
    const sectionSelect = document.getElementById('dpr-manual-upload-section');
    const labelInput = document.getElementById('dpr-manual-upload-label');
    const tagInput = document.getElementById('dpr-manual-upload-tag');
    const updateManualFileList = () => {
      if (!fileInput || !fileList) return;
      const files = Array.from(fileInput.files || []);
      if (!files.length) {
        fileList.textContent = '尚未选择文件。';
        return;
      }
      const total = files.reduce((sum, file) => sum + Number(file.size || 0), 0);
      const names = files.slice(0, 3).map((file) => file.name).join('、');
      const more = files.length > 3 ? ` 等 ${files.length} 个文件` : '';
      fileList.textContent = `${names}${more} · ${(total / 1024 / 1024).toFixed(1)} MB`;
    };
    if (fileInput) {
      fileInput.addEventListener('change', updateManualFileList);
    }
    if (runUploadBtn) {
      runUploadBtn.addEventListener('click', async () => {
        const files = fileInput ? Array.from(fileInput.files || []) : [];
        await runManualUpload(files, {
          section: sectionSelect ? sectionSelect.value : 'deep',
          label: labelInput ? labelInput.value : '',
          tag: tagInput ? tagInput.value : '手动上传',
          docsConcurrency: '2',
        });
      });
    }

  };

  const setPanelMode = (mode) => {
    currentPanelMode = mode === 'manual-upload' ? 'manual-upload' : 'workflows';
    if (!overlay) return;
    const isManualUpload = currentPanelMode === 'manual-upload';
    overlay.classList.toggle('is-manual-upload', isManualUpload);
    overlay.classList.toggle('is-workflow-panel', !isManualUpload);
    const titleEl = document.getElementById('dpr-workflow-title');
    if (titleEl) {
      titleEl.textContent = isManualUpload ? '上传 PDF 解析' : '工作流触发';
    }
    const runsTitleEl = document.getElementById('dpr-workflow-runs-title');
    if (runsTitleEl) {
      runsTitleEl.textContent = isManualUpload ? '解析进度' : '执行过程';
    }
  };

  const open = (options = {}) => {
    ensureOverlay();
    if (!overlay) return;
    const requestedMode =
      typeof options === 'string'
        ? options
        : String((options && options.mode) || 'workflows');
    setPanelMode(requestedMode);
    overlay.style.display = 'flex';
    requestAnimationFrame(() => overlay.classList.add('show'));
    if (currentPanelMode === 'manual-upload') {
      const fileInput = document.getElementById('dpr-manual-upload-files');
      if (fileInput && typeof fileInput.focus === 'function') {
        requestAnimationFrame(() => fileInput.focus());
      }
    } else {
      // 打开面板时尝试加载最近运行（不依赖触发）
      loadRecentRuns();
    }
    return true;
  };

  const openManualUpload = (options = {}) => {
    const opened = open({ mode: 'manual-upload' });
    if (opened && !(options && options.skipResume)) {
      resumePersistedManualUploadRun();
    }
    return opened;
  };

  const close = () => {
    if (!overlay) return;
    overlay.classList.remove('show');
    setTimeout(() => {
      overlay.style.display = 'none';
    }, 160);
    stopPolling();
  };

  const stopPolling = () => {
    if (refreshTimer) {
      clearInterval(refreshTimer);
      refreshTimer = null;
    }
  };

  const badgeColorFor = (status, conclusion) => {
    if (conclusion === 'success') return '#2e7d32';
    if (conclusion === 'failure') return '#c00';
    if (conclusion === 'cancelled') return '#666';
    if (status === 'in_progress') return '#1565c0';
    return '#666';
  };

  const formatRunBadgeText = (status, conclusion) => {
    const s = String(status || '');
    const c = String(conclusion || '');
    // 用户希望 completed / success 这种冗余展示去掉：优先展示 conclusion，其次 status
    return c || s || '';
  };

  const formatRunTime = (isoTime) => {
    if (!isoTime) return '';
    try {
      const d = new Date(isoTime);
      if (Number.isNaN(d.getTime())) {
        return String(isoTime).replace('T', ' ').replace('Z', '');
      }
      return d.toLocaleString('zh-CN', {
        timeZone: 'Asia/Shanghai',
        hour12: false,
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });
    } catch {
      return String(isoTime || '');
    }
  };

  const renderRecentRuns = (owner, repo, byWorkflow, errText, repoContext = null) => {
    if (!recentEl) return;
    recentEl.classList.remove('is-loading');
    if (errText) {
      recentEl.innerHTML = `<div style="color:#c00;">${escapeHtml(errText)}</div>`;
      return;
    }
    const blocks = WORKFLOWS.map((wf) => {
      if (wf.key === 'sync' && repoContext && repoContext.isFork === false) {
        return `
          <div class="dpr-wf-recent-block">
            <div class="dpr-wf-recent-block-title">${escapeHtml(wf.name)}</div>
            <div style="color:#c90;">当前仓库不是 GitHub Fork，已禁用上游同步。</div>
          </div>
        `;
      }
      const list = (byWorkflow && byWorkflow[String(wf.key || wf.id || '')]) || [];
      const items = Array.isArray(list) ? list : [];
      const lines = items
        .map((r) => {
          const status = r.status || '';
          const conclusion = r.conclusion || '';
          const color = badgeColorFor(status, conclusion);
          const isActive =
            selectedRun &&
            String(selectedRun.runId || '') === String(r.id || '');
          const createdAt = formatRunTime(r.created_at);
          const badge = formatRunBadgeText(status, conclusion);
          const title = `#${r.run_number || r.id}${badge ? ` ${badge}` : ''}`;
          return `
            <button class="dpr-wf-recent-item ${isActive ? 'is-active' : ''}" data-run-id="${escapeHtml(
              String(r.id || ''),
            )}" style="text-align:left;">
              <div class="dpr-wf-recent-title">
                <span class="dpr-wf-recent-badge" style="color:${color};">${escapeHtml(
                  title,
                )}</span>
                <span class="dpr-wf-recent-time">${escapeHtml(createdAt)}</span>
              </div>
              <div class="dpr-wf-recent-sub">${escapeHtml(wf.name)}</div>
            </button>
          `;
        })
        .join('');
      return `
        <div class="dpr-wf-recent-block">
          <div class="dpr-wf-recent-block-title">${escapeHtml(wf.name)}</div>
          ${lines || '<div style="color:#999;">暂无运行记录</div>'}
        </div>
      `;
    }).join('');

    recentEl.innerHTML = blocks;

    recentEl.querySelectorAll('.dpr-wf-recent-item').forEach((btn) => {
      if (btn._bound) return;
      btn._bound = true;
      btn.addEventListener('click', async () => {
        const runId = btn.getAttribute('data-run-id') || '';
        if (!runId) return;
        stopPolling();
        recentEl
          .querySelectorAll('.dpr-wf-recent-item.is-active')
          .forEach((n) => n.classList.remove('is-active'));
        btn.classList.add('is-active');
        selectedRun = { owner, repo, runId, token: loadGithubToken() };
        setStatus(`正在加载运行详情：run_id=${runId}`, '#666', { waiting: true });
        await refreshRun(owner, repo, runId);
        refreshTimer = setInterval(() => {
          if (!selectedRun) return;
          refreshRun(selectedRun.owner, selectedRun.repo, selectedRun.runId);
        }, 5000);
      });
    });
  };

  const loadRecentRuns = async () => {
    ensureOverlay();
    if (!recentEl) return;

    try {
      const repoContext = await resolveRepoContextFromAvailableToken();
      const { token } = repoContext;
      const { owner, repo } = repoContext;
      if (!owner || !repo) {
        renderRecentRuns(owner, repo, null, '无法推断目标仓库，无法加载最近运行记录。');
        return;
      }

      const hasRendered = !!recentEl.querySelector('.dpr-wf-recent-block');
      if (!hasRendered) {
        recentEl.innerHTML = '<div style="color:#999;">正在加载最近运行记录...</div>';
      } else {
        // 刷新时不要清空现有内容，避免“闪一下再出现”的观感
        recentEl.classList.add('is-loading');
      }
      const byWorkflow = {};
      const runsByWorkflowId = {};
      const uniqueWorkflowIds = Array.from(
        new Set(WORKFLOWS.map((wf) => String(wf.id || ''))),
      );

      for (const wfId of uniqueWorkflowIds) {
        const url = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${encodeURIComponent(
          wfId,
        )}/runs?per_page=12`;
        const res = await ghFetch(token, url);
        if (!res.ok) {
          const txt = await res.text().catch(() => '');
          throw new Error(
            `读取最近运行失败(${wfId})：HTTP ${res.status} ${res.statusText} - ${txt}`,
          );
        }
        const data = await res.json();
        runsByWorkflowId[wfId] = Array.isArray(data.workflow_runs)
          ? data.workflow_runs
          : [];
      }

      const dailyFileRuns = runsByWorkflowId['daily-paper-reader.yml'] || [];
      const dailyNowRuns = [];
      if (dailyFileRuns.length > 0) {
        const tagged = await Promise.all(
          dailyFileRuns.map((run) =>
            resolveRecentRunTag(owner, repo, token, run).then((runTag) => ({ run, runTag })),
          ),
        );
        tagged.forEach(({ run }) => {
          dailyNowRuns.push(run);
        });
      }

      WORKFLOWS.forEach((wf) => {
        const wfId = String(wf.id || '');
        if (wf.id === 'daily-paper-reader.yml' && wf.key === 'daily-now') {
          byWorkflow[String(wf.key)] = dailyNowRuns.slice(0, 3);
          return;
        }
        byWorkflow[String(wf.key || wfId)] = (runsByWorkflowId[wfId] || []).slice(0, 3);
      });

      renderRecentRuns(owner, repo, byWorkflow, '', repoContext);
    } catch (e) {
      console.error(e);
      if (recentEl) recentEl.classList.remove('is-loading');
      renderRecentRuns('', '', null, explainFetchFailure(e), null);
    }
  };

  const getWorkflowByKey = (workflowKey) =>
    WORKFLOWS.find((wf) => String(wf.key || '') === String(workflowKey || ''));

  const combineInputs = (baseInputs, extraInputs) => {
    const merged = {};
    const mergeOne = (source) => {
      if (!source || typeof source !== 'object') return;
      Object.keys(source).forEach((k) => {
        const v = source[k];
        if (typeof v === 'undefined' || v === null) return;
        const txt = String(v).trim();
        if (!txt) return;
        merged[String(k)] = txt;
      });
    };
    mergeOne(baseInputs);
    mergeOne(extraInputs);
    return merged;
  };

  const dispatchAndMonitor = async (workflow, extraInputs) => {
    const wf = workflow || {};
    const workflowFile = String(wf.id || '');
    if (!workflowFile) {
      setStatus('工作流配置缺失，无法触发。', '#c00');
      return;
    }
    const dynamicInputs = { ...(wf.dispatchInputs || {}) };
    const rerankerProfile = loadRerankerProfile();
    if (
      rerankerProfile &&
      (workflowFile === 'daily-paper-reader.yml' ||
        workflowFile === 'conference-paper-retrieval.yml')
    ) {
      dynamicInputs.reranker_profile = rerankerProfile;
    }
    const dispatchInputs = combineInputs(dynamicInputs, extraInputs);
    if (isLocalDebugPage()) {
      try {
        return await dispatchLocalAndMonitor(wf, workflowFile, dispatchInputs);
      } catch (e) {
        console.error(e);
        const msg = explainFetchFailure(e);
        setStatus(`本地触发失败：${msg}`, '#c00');
        runsEl.innerHTML = `<div style="color:#c00;">${escapeHtml(msg)}<br/>请确认本地后端已启动：<code>scripts/local_debug.sh</code> 或 <code>python src/local_debug_server.py --port 8567</code></div>`;
        return;
      }
    }
    let repoContext = null;
    try {
      repoContext = await resolveRepoContextFromAvailableToken();
    } catch (e) {
      const msg = explainFetchFailure(e);
      setStatus(msg, '#c00');
      runsEl.innerHTML = `<div style="color:#c00;">${escapeHtml(msg)}</div>`;
      return;
    }
    const { token } = repoContext;
    const { owner, repo } = repoContext;
    if (!owner || !repo) {
      setStatus('无法推断目标仓库：请确认 GitHub Token 有效，或使用 xxx.github.io/仓库名/ 访问。', '#c00');
      return;
    }
    if (wf.key === 'sync' && repoContext.isFork === false) {
      setStatus('当前仓库不是 GitHub Fork，无法使用上游同步。', '#c00');
      runsEl.innerHTML =
        '<div style="color:#c00;">当前仓库不是 Fork 仓库，Upstream Sync 不会运行。</div>' +
        `<div style="margin-top:8px;"><a class="arxiv-tool-btn" style="padding:6px 10px; text-decoration:none;" target="_blank" href="https://github.com/${owner}/${repo}/fork">前往 Fork 当前仓库</a></div>`;
      return;
    }

    setStatus(`正在检查工作流状态：${wf.name || workflowFile} ...`, '#666', { waiting: true });
    runsEl.innerHTML = '<div style="color:#999;">正在检查是否有运行中的工作流...</div>';
    stopPolling();
    activeRun = null;

    try {
      // 检查是否有正在运行中的同名工作流（防止误触重复触发）
      const activeStatuses = new Set(['queued', 'in_progress', 'waiting']);
      const statusZhMap = { queued: '排队中', in_progress: '运行中', waiting: '等待中' };
      const checkUrl = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${encodeURIComponent(
        workflowFile,
      )}/runs?per_page=5`;
      const checkRes = await ghFetch(token, checkUrl);
      if (checkRes.ok) {
        const checkData = await checkRes.json();
        const runs = Array.isArray(checkData.workflow_runs) ? checkData.workflow_runs : [];
        const activeRuns = runs.filter((r) => activeStatuses.has(r.status));
        if (activeRuns.length > 0) {
          const r = activeRuns[0];
          const runUrl = `https://github.com/${owner}/${repo}/actions/runs/${r.id}`;
          const statusText = statusZhMap[r.status] || r.status;
          setStatus(
            `已有正在运行的工作流（#${r.run_number || r.id}，状态：${statusText}），请等待完成后再触发。`,
            '#c00',
          );
          runsEl.innerHTML =
            `<div style="color:#c00;">同一时间只允许运行一个该工作流实例，请等待当前运行结束。</div>` +
            `<div style="margin-top:8px;"><a class="arxiv-tool-btn" style="padding:6px 10px; text-decoration:none;" target="_blank" href="${runUrl}">查看当前运行</a></div>`;
          return;
        }
      }

      setStatus(`正在触发工作流：${wf.name || workflowFile} ...`, '#666', { waiting: true });
      runsEl.innerHTML = '<div style="color:#999;">正在触发，请稍候...</div>';

      const createdAt = new Date();

      // 触发 dispatch
      const dispatchUrl = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${encodeURIComponent(
        workflowFile,
      )}/dispatches`;
      const dispatchBody = {
        ref: String(repoContext.defaultBranch || 'main'),
      };
      if (Object.keys(dispatchInputs).length > 0) {
        dispatchBody.inputs = dispatchInputs;
      }

      const res = await ghFetch(token, dispatchUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dispatchBody),
      });
      if (!res.ok) {
        const txt = await res.text().catch(() => '');
        if (res.status === 422 && txt.includes('disabled workflow')) {
          const err = new Error('触发失败：该 Workflow 当前处于禁用状态，请先前往 Actions 页面启用该工作流。');
          err.workflowEnableUrl = `https://github.com/${owner}/${repo}/actions/workflows/${encodeURIComponent(workflowFile)}`;
          throw err;
        }
        throw new Error(`触发失败：HTTP ${res.status} ${res.statusText} - ${txt}`);
      }

      setStatus('已触发，正在等待运行记录创建...', '#666', { waiting: true });

      // 轮询找到本次 dispatch 对应的 run
      const lookup = async () => {
        const runsUrl = `https://api.github.com/repos/${owner}/${repo}/actions/workflows/${encodeURIComponent(
          workflowFile,
        )}/runs?event=workflow_dispatch&per_page=10`;
        const runsRes = await ghFetch(token, runsUrl);
        if (!runsRes.ok) {
          const txt = await runsRes.text().catch(() => '');
          throw new Error(`读取 workflow runs 失败：HTTP ${runsRes.status} ${runsRes.statusText} - ${txt}`);
        }
        const data = await runsRes.json();
        const list = Array.isArray(data.workflow_runs) ? data.workflow_runs : [];
        const found = list.find((r) => {
          try {
            const t = new Date(r.created_at);
            return t.getTime() >= createdAt.getTime() - 5000;
          } catch {
            return false;
          }
        });
        return found || null;
      };

      let run = null;
      for (let i = 0; i < 18; i += 1) {
        // 最多等 ~90 秒
        // eslint-disable-next-line no-await-in-loop
        run = await lookup();
        if (run) break;
        // eslint-disable-next-line no-await-in-loop
        await new Promise((r) => setTimeout(r, 5000));
      }

      if (!run || !run.id) {
        setStatus('已触发，但未能在短时间内找到对应的运行记录。建议打开 Actions 页面查看。', '#c00');
        runsEl.innerHTML = `<div style="color:#666;">请在 GitHub Actions 查看：<a target="_blank" href="https://github.com/${owner}/${repo}/actions">打开 Actions</a></div>`;
        return;
      }

      activeRun = {
        owner,
        repo,
        runId: run.id,
        token,
        manualBatchToken: workflowFile === 'manual-paper-upload.yml'
          ? extractManualBatchToken(dispatchInputs)
          : '',
      };
      selectedRun = activeRun;
      if (activeRun.manualBatchToken) {
        persistManualActiveRun(activeRun);
      }
      setStatus(`运行已创建：run_id=${run.id}，开始拉取进度...`, '#080', { waiting: true });
      const shouldPoll = await refreshRun(owner, repo, run.id);
      if (shouldPoll) {
        refreshTimer = setInterval(() => {
          const r = selectedRun || activeRun;
          if (!r) return;
          refreshRun(r.owner, r.repo, r.runId);
        }, 5000);
      }

      // 触发后刷新最近运行列表
      loadRecentRuns();
    } catch (e) {
      console.error(e);
      const msg = explainFetchFailure(e);
      setStatus(`触发失败：${msg}`, '#c00');
      if (e.workflowEnableUrl) {
        runsEl.innerHTML =
          `<div style="color:#c00;">${escapeHtml(msg)}<br/>` +
          `👉 <a href="${e.workflowEnableUrl}" target="_blank" style="color:#1a73e8;">前往 Actions 页面启用工作流</a></div>`;
      } else {
        runsEl.innerHTML = `<div style="color:#c00;">${escapeHtml(msg)}</div>`;
      }
    }
  };

  const renderRun = (owner, repo, run, jobs) => {
    const runUrl = `https://github.com/${owner}/${repo}/actions/runs/${run.id}`;
    const status = run.status || '';
    const conclusion = run.conclusion || '';

    const badgeColor =
      conclusion === 'success'
        ? '#2e7d32'
        : conclusion === 'failure'
          ? '#c00'
          : status === 'in_progress'
            ? '#1565c0'
            : '#666';
    const badgeText = formatRunBadgeText(status, conclusion);

    const jobList = Array.isArray(jobs) ? jobs : [];
    const jobHtml = jobList
      .map((j) => {
        const steps = Array.isArray(j.steps) ? j.steps : [];
        const stepLines = steps
          .map((s) => {
            const c = s.conclusion || s.status || '';
            const icon =
              c === 'success'
                ? '✅'
                : c === 'failure'
                  ? '❌'
                  : c === 'skipped'
                    ? '⏭'
                    : c === 'in_progress'
                      ? '⏳'
                      : '•';
            return `<div class="dpr-wf-step">${icon} ${escapeHtml(
              s.name || '',
            )}</div>`;
          })
          .join('');
        const jobId = j.id ? String(j.id) : '';
        return `
          <div class="dpr-wf-job">
            <div class="dpr-wf-job-title">${escapeHtml(j.name || '')}</div>
            <div class="dpr-wf-job-meta">
              <span class="dpr-wf-job-meta-text">${escapeHtml(j.status || '')}${j.conclusion ? ` / ${escapeHtml(j.conclusion)}` : ''}</span>
            </div>
            <div class="dpr-wf-steps">${stepLines || '<div style="color:#999;">暂无步骤信息</div>'}</div>
          </div>
        `;
      })
      .join('');

    runsEl.innerHTML = `
      <div style="display:flex; justify-content:space-between; gap:10px; align-items:center; margin-bottom:8px;">
        <div style="min-width:0;">
          <div style="font-weight:600;">Run #${run.run_number || run.id}</div>
          <div style="color:#666; margin-top:2px;">
            <span style="display:inline-block; padding:1px 6px; border-radius:999px; background:rgba(0,0,0,0.06); color:${badgeColor};">
              ${escapeHtml(badgeText)}
            </span>
            <span style="margin-left:8px;">${escapeHtml(
              formatRunTime(run.created_at),
            )}</span>
          </div>
        </div>
        <div style="flex-shrink:0; display:flex; gap:8px;">
          <a class="arxiv-tool-btn" style="padding:6px 10px; text-decoration:none;" target="_blank" href="${runUrl}">打开 Actions</a>
        </div>
      </div>
      ${jobHtml || '<div style="color:#999;">暂无 Job 信息</div>'}
    `;
  };

  const refreshRun = async (owner, repo, runId) => {
    const token = activeRun && activeRun.token ? activeRun.token : loadGithubToken();
    if (!token) return false;

    try {
      const runUrl = `https://api.github.com/repos/${owner}/${repo}/actions/runs/${runId}`;
      const res = await ghFetch(token, runUrl);
      if (!res.ok) {
        const txt = await res.text().catch(() => '');
        throw new Error(`读取 run 失败：HTTP ${res.status} ${res.statusText} - ${txt}`);
      }
      const run = await res.json();
      const stateKey = `${run.status || ''}/${run.conclusion || ''}`;
      const prevStateKey = lastRunStateById[String(runId)];
      lastRunStateById[String(runId)] = stateKey;

      const jobsUrl = `https://api.github.com/repos/${owner}/${repo}/actions/runs/${runId}/jobs?per_page=100`;
      const jobsRes = await ghFetch(token, jobsUrl);
      let jobs = [];
      if (jobsRes.ok) {
        const jobsData = await jobsRes.json();
        jobs = Array.isArray(jobsData.jobs) ? jobsData.jobs : [];
      }

      renderRun(owner, repo, run, jobs);

      if (run.status === 'completed') {
        stopPolling();
        setStatus(
          `运行已结束：${run.conclusion || 'completed'}`,
          run.conclusion === 'success' ? '#080' : '#c00',
        );
        if (run.conclusion === 'success' && activeRun && activeRun.manualBatchToken) {
          setStatus('运行成功，正在等待 GitHub Pages 发布解析结果...', '#080', { waiting: true });
          waitForManualDocsPublication(activeRun.manualBatchToken)
            .finally(() => clearPersistedManualActiveRun(runId));
        } else {
          clearPersistedManualActiveRun(runId);
        }
        // run 状态结束后，刷新“最近运行”列表，确保 completed/success 等状态能及时反映
        if (prevStateKey !== stateKey) {
          loadRecentRuns();
        }
        return false;
      } else {
        setStatus('运行中：每 5 秒自动刷新...', '#1565c0', { waiting: true });
        return true;
      }
    } catch (e) {
      console.error(e);
      setStatus(`刷新失败：${explainFetchFailure(e)}`, '#c00');
      return false;
    }
  };

  const resumePersistedManualUploadRun = async () => {
    const saved = loadPersistedManualActiveRun();
    if (!saved) return false;
    if (
      activeRun &&
      activeRun.manualBatchToken &&
      String(activeRun.runId || '') === String(saved.runId || '')
    ) {
      return false;
    }

    stopPolling();
    let token = '';
    if (!saved.local) {
      try {
        token = (await resolveRepoContextFromAvailableToken()).token;
      } catch (e) {
        const msg = explainFetchFailure(e);
        setStatus(`检测到未完成的上传解析任务，但无法恢复进度：${msg}`, '#c00');
        return false;
      }
    }

    activeRun = saved.local
      ? { ...saved }
      : { ...saved, token };
    selectedRun = activeRun;
    setStatus(
      `已恢复上传解析任务：run_id=${saved.runId}`,
      '#1565c0',
      { waiting: true },
    );

    const shouldPoll = saved.local
      ? await refreshLocalRun(saved.runId)
      : await refreshRun(saved.owner, saved.repo, saved.runId);
    if (shouldPoll) {
      refreshTimer = setInterval(() => {
        const r = selectedRun || activeRun;
        if (!r) return;
        if (r.local) {
          refreshLocalRun(r.runId);
        } else {
          refreshRun(r.owner, r.repo, r.runId);
        }
      }, 5000);
    }
    return true;
  };

  const runWorkflowByKey = async (workflowKey, extraInputs) => {
    const wf = getWorkflowByKey(workflowKey);
    if (!wf) {
      setStatus('未找到对应的工作流配置。', '#c00');
      return;
    }
    open();
    return dispatchAndMonitor(wf, extraInputs);
  };

  const runQuickFetchByDays = async (days, extra) => {
    const parsed = parseInt(days, 10);
    const normalized = Number.isFinite(parsed) && parsed > 0 ? String(Math.max(1, parsed)) : '10';
    const options = extra && typeof extra === 'object' ? extra : {};
    const fetchMode = (typeof options.fetchMode === 'string' ? options.fetchMode : '').trim().toLowerCase();
    const presetKey = fetchMode ? `${normalized}-${fetchMode}` : normalized;
    const preset = QUICK_FETCH_PRESETS[presetKey] || QUICK_FETCH_PRESETS[normalized] || {
      key: 'daily-now',
      dispatchInputs: {
        run_enrich: 'false',
        fetch_days: normalized,
      },
    };
    const mergedInputs = combineInputs(preset.dispatchInputs, options.dispatchInputs);
    return runWorkflowByKey(preset.key, mergedInputs);
  };

  const validateManualUploadFiles = (files) => {
    const list = Array.from(files || []).filter(Boolean);
    if (!list.length) return { files: [], error: '请选择 PDF 或 ZIP 文件。' };
    const bad = list.find((file) => {
      const name = String(file.name || '').toLowerCase();
      return !(name.endsWith('.pdf') || name.endsWith('.zip'));
    });
    if (bad) return { files: list, error: `暂不支持该文件类型：${bad.name}` };
    return { files: list, error: '' };
  };

  const runManualUpload = async (files, options = {}) => {
    openManualUpload({ skipResume: true });
    const checked = validateManualUploadFiles(files);
    if (checked.error) {
      setStatus(checked.error, '#c00');
      return false;
    }
    const selectedFiles = checked.files;
    const normalized = normalizeManualUploadOptions(options);

    if (isLocalDebugPage()) {
      try {
        await dispatchLocalManualUploadAndMonitor(selectedFiles, normalized);
        return true;
      } catch (e) {
        console.error(e);
        const msg = explainFetchFailure(e);
        setStatus(`本地上传失败：${msg}`, '#c00');
        runsEl.innerHTML = `<div style="color:#c00;">${escapeHtml(msg)}<br/>请确认本地后端已启动：<code>scripts/local_debug.sh</code> 或 <code>python src/local_debug_server.py --port 8567</code></div>`;
        return false;
      }
    }

    const totalBytes = selectedFiles.reduce((sum, file) => sum + Number(file.size || 0), 0);
    const tooLarge = selectedFiles.find((file) => Number(file.size || 0) > MANUAL_UPLOAD_MAX_BYTES);
    if (tooLarge || totalBytes > MANUAL_UPLOAD_MAX_BYTES) {
      setStatus(`在线上传单次限制为 ${MANUAL_UPLOAD_MAX_MB}MB；超过请使用本地调试入口。`, '#c00');
      return false;
    }

    let repoContext = null;
    try {
      repoContext = await resolveRepoContextFromAvailableToken();
    } catch (e) {
      const msg = explainFetchFailure(e);
      setStatus(msg, '#c00');
      runsEl.innerHTML = `<div style="color:#c00;">${escapeHtml(msg)}</div>`;
      return false;
    }
    const { token } = repoContext;
    const { owner, repo } = repoContext;
    if (!owner || !repo) {
      setStatus('无法推断目标仓库：请确认 GitHub Token 有效，或使用 xxx.github.io/仓库名/ 访问。', '#c00');
      return false;
    }

    let pendingUploadBranch = '';
    try {
      stopPolling();
      activeRun = null;
      runsEl.innerHTML = '<div style="color:#999;">正在准备上传文件...</div>';
      const branch = String(repoContext.defaultBranch || 'main');
      const wf = getWorkflowByKey('manual-paper-upload');
      const useChunkUpload = totalBytes > MANUAL_UPLOAD_CONTENT_API_SAFE_BYTES ||
        selectedFiles.some((file) => Number(file.size || 0) > MANUAL_UPLOAD_CONTENT_API_SAFE_BYTES);
      if (useChunkUpload) {
        runsEl.innerHTML = '<div style="color:#999;">正在上传到 GitHub 临时分支，大文件不会写入 main 历史...</div>';
        const chunkUpload = await uploadFilesToTempBranchChunks(
          owner,
          repo,
          token,
          branch,
          normalized.batchToken,
          selectedFiles,
        );
        pendingUploadBranch = chunkUpload.branchName;
        await dispatchAndMonitor(wf, {
          upload_ref: normalized.batchToken,
          upload_source: 'temp_branch_chunks',
          upload_branch: chunkUpload.branchName,
          section: normalized.section,
          label: normalized.label,
          tag: normalized.tag,
          docs_concurrency: normalized.docsConcurrency,
          cleanup_upload: 'true',
        });
        if (!activeRun || activeRun.manualBatchToken !== normalized.batchToken) {
          await deleteGithubBranch(owner, repo, token, chunkUpload.branchName);
          pendingUploadBranch = '';
          return false;
        }
        pendingUploadBranch = '';
      } else {
        runsEl.innerHTML = '<div style="color:#999;">正在上传文件到仓库临时目录...</div>';
        await uploadFilesToGithub(owner, repo, token, branch, normalized.batchToken, selectedFiles);
        await dispatchAndMonitor(wf, {
          upload_ref: `uploads/manual-papers/${normalized.batchToken}`,
          upload_source: 'repo',
          section: normalized.section,
          label: normalized.label,
          tag: normalized.tag,
          docs_concurrency: normalized.docsConcurrency,
          cleanup_upload: 'true',
        });
      }
      return true;
    } catch (e) {
      if (pendingUploadBranch) {
        await deleteGithubBranch(owner, repo, token, pendingUploadBranch);
      }
      console.error(e);
      const msg = explainFetchFailure(e);
      setStatus(`上传或触发失败：${msg}`, '#c00');
      runsEl.innerHTML = `<div style="color:#c00;">${escapeHtml(msg)}</div>`;
      return false;
    }
  };

  const normalizeConferenceName = (value) => {
    const text = String(value || '').trim();
    const lower = text.toLowerCase();
    if (lower === 'nips' || lower === 'neurips') return 'NeurIPS';
    if (lower === 'icml') return 'ICML';
    return '';
  };

  const normalizeConferenceYears = (values) => {
    const raw = Array.isArray(values) ? values : [values];
    const out = [];
    const seen = new Set();
    raw.forEach((item) => {
      const year = parseInt(item, 10);
      if (!Number.isFinite(year) || year <= 0 || seen.has(year)) return;
      seen.add(year);
      out.push(String(year));
    });
    return out;
  };

  const runConferenceRetrieval = async (conference, years, options = {}) => {
    const normalizedConference = normalizeConferenceName(conference);
    const normalizedYears = normalizeConferenceYears(years);
    if (!normalizedConference || !normalizedYears.length) {
      open();
      setStatus('请先选择支持的会议和年份。', '#c00');
      return false;
    }
    const extraInputs =
      options && typeof options === 'object' && options.dispatchInputs
        ? options.dispatchInputs
        : {};
    return runWorkflowByKey('conference-retrieval', {
      conference: normalizedConference,
      years: normalizedYears.join(','),
      ...extraInputs,
    });
  };

  const runConferenceMaintain = async (conference, years) =>
    runConferenceRetrieval(conference, years);

  const runHotPaperScout = async (options = {}) => {
    const opts = options && typeof options === 'object' ? options : {};
    const profileTag = String(opts.profile_tag || opts.profileTag || '').trim();
    const domainQuery = String(opts.domain_query || opts.domainQuery || '').trim();
    const daysText = String(opts.days_window || opts.daysWindow || '30').trim();
    const daysWindow = ['7', '14', '30'].includes(daysText) ? daysText : '30';
    const institutionRaw = String(opts.institution_filter || opts.institutionFilter || 'company').trim().toLowerCase();
    const institutionFilter = ['all', 'company', 'university'].includes(institutionRaw)
      ? institutionRaw
      : 'company';
    const maxResults = String(opts.max_results || opts.maxResults || '30').trim() || '30';
    return runWorkflowByKey('hot-paper-scout', {
      profile_tag: profileTag,
      domain_query: domainQuery,
      days_window: daysWindow,
      institution_filter: institutionFilter,
      max_results: maxResults,
    });
  };

  if (!document._dprManualUploadOpenEventBound) {
    document._dprManualUploadOpenEventBound = true;
    document.addEventListener('dpr-open-manual-upload', () => {
      window.__dprManualUploadOpenRequested = false;
      openManualUpload();
    });
  }

  if (window.__dprManualUploadOpenRequested) {
    window.__dprManualUploadOpenRequested = false;
    setTimeout(openManualUpload, 0);
  }

  return {
    open,
    openManualUpload,
    runWorkflowByKey,
    runQuickFetchByDays,
    runManualUpload,
    runConferenceRetrieval,
    runConferenceMaintain,
    runHotPaperScout,
  };
})();
