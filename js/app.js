const PAGE_SIZE = 50;
let currentCategory = '';
let currentSub = '';
let currentPage = 1;
let filteredLinks = [];

function init() {
  buildStats();
  buildCatTree();
  renderHome();
}

// ── Stats ──────────────────────────────────
function buildStats() {
  const cats = {};
  const subs = {};
  linksData.forEach(l => {
    cats[l.category] = (cats[l.category] || 0) + 1;
    const key = l.category + '|' + (l.subcategory || '');
    subs[key] = (subs[key] || 0) + 1;
  });
  window.totalCats = Object.keys(cats).length;
  window.totalSubs = Object.keys(subs).length;
  window.totalLinks = linksData.length;
}

function renderHome() {
  showPage('home');
  setActiveNav('home');

  const el = document.getElementById('home-content');
  const featured = [...linksData].sort(() => 0.5 - Math.random()).slice(0, 12);
  el.innerHTML = `
    <div class="hero">
      <pre>┌────────────────────────────┐
│                            │
│   NO LOGGING               │
│   NO TRACKING              │
│   NO CENSORSHIP            │
│                            │
└────────────────────────────┘</pre>
      <p>Welcome to Aion — ${window.totalLinks} curated links across ${window.totalCats} categories.</p>
    </div>
    <div class="stats-grid">
      <div class="stat-card"><div class="num">${window.totalLinks}</div><div class="label">Links</div></div>
      <div class="stat-card"><div class="num">${window.totalCats}</div><div class="label">Categories</div></div>
      <div class="stat-card"><div class="num">${window.totalSubs}</div><div class="label">Subcategories</div></div>
    </div>
    <h2>Random Picks</h2>
    ${featured.map(l => renderLinkCard(l)).join('')}
  `;
}

// ── Category tree ──────────────────────────
function buildCatTree() {
  const tree = {};
  linksData.forEach(l => {
    if (!tree[l.category]) tree[l.category] = {};
    const sub = l.subcategory || 'General';
    tree[l.category][sub] = (tree[l.category][sub] || 0) + 1;
  });
  window.catTree = tree;
}

function renderCatTree() {
  const tree = window.catTree;
  const el = document.getElementById('cat-tree');
  let html = `<div class="cat-group"><div class="cat-parent ${!currentCategory ? 'active' : ''}" onclick="selectCat('')" style="color: #569cd6;">All Categories <span class="count">${linksData.length}</span></div></div>`;

  Object.keys(tree).sort().forEach(cat => {
    const total = Object.values(tree[cat]).reduce((a, b) => a + b, 0);
    const isOpen = cat === currentCategory;
    html += `<div class="cat-group">
      <div class="cat-parent ${isOpen ? 'active' : ''}" onclick="selectCat('${esc(cat)}')">${esc(cat)} <span class="count">${total}</span></div>
      <div class="cat-subs ${isOpen ? 'open' : ''}">`;

    Object.keys(tree[cat]).sort().forEach(sub => {
      const isActive = cat === currentCategory && sub === currentSub;
      html += `<div class="cat-sub ${isActive ? 'active' : ''}" onclick="selectSub('${esc(cat)}','${esc(sub)}')">${esc(sub)} <span class="count">${tree[cat][sub]}</span></div>`;
    });

    html += `</div></div>`;
  });
  el.innerHTML = html;
}

function selectCat(cat) {
  currentCategory = cat;
  currentSub = '';
  currentPage = 1;
  applyFilter();
  renderCatTree();
}

function selectCatFromFilter(cat) {
  currentCategory = cat;
  currentSub = '';
  currentPage = 1;
  applyFilter();
  renderCatTree();
  showPage('links');
  setActiveNav('links');
}

function selectSub(cat, sub) {
  currentCategory = cat;
  currentSub = sub;
  currentPage = 1;
  applyFilter();
  renderCatTree();
}

// ── Links page ─────────────────────────────
function renderLinksPage() {
  showPage('links');
  setActiveNav('links');
  renderCatTree();
  document.getElementById('search-input').value = '';
  currentPage = 1;
  applyFilter();
}

function applyFilter() {
  const query = (document.getElementById('search-input')?.value || '').toLowerCase().trim();

  filteredLinks = linksData.filter(l => {
    if (currentCategory && l.category !== currentCategory) return false;
    if (currentSub && (l.subcategory || 'General') !== currentSub) return false;
    if (query) {
      const haystack = (l.name + ' ' + l.desc + ' ' + l.url + ' ' + (l.subcategory || '')).toLowerCase();
      const words = query.split(/\s+/);
      if (!words.every(w => haystack.includes(w))) return false;
    }
    return true;
  });

  renderLinkList();
  renderPagination();

  const countEl = document.getElementById('result-count');
  if (countEl) countEl.textContent = `${filteredLinks.length} links`;
}

function renderLinkList() {
  const el = document.getElementById('links-list');
  const start = (currentPage - 1) * PAGE_SIZE;
  const page = filteredLinks.slice(start, start + PAGE_SIZE);

  if (page.length === 0) {
    el.innerHTML = '<div style="color:#444; padding:20px; text-align:center;">No results found.</div>';
    return;
  }

  el.innerHTML = page.map(l => renderLinkCard(l)).join('');
}

function renderLinkCard(l) {
  const sub = l.subcategory ? `<span class="cat-label">${esc(l.subcategory)}</span>` : '';
  return `<div class="link-card">
    <a class="name" href="${esc(l.url)}" target="_blank">${esc(l.name)}</a>
    <div class="desc">${esc(l.desc)}</div>
    <div class="meta">${sub}</div>
  </div>`;
}

// ── Pagination ─────────────────────────────
function renderPagination() {
  const el = document.getElementById('pagination');
  const totalPages = Math.ceil(filteredLinks.length / PAGE_SIZE);
  if (totalPages <= 1) { el.innerHTML = ''; return; }

  let html = '';
  html += `<button ${currentPage === 1 ? 'disabled' : ''} onclick="goPage(${currentPage - 1})">&laquo;</button>`;

  const range = 3;
  let startP = Math.max(1, currentPage - range);
  let endP = Math.min(totalPages, currentPage + range);

  if (startP > 1) html += `<button onclick="goPage(1)">1</button><button disabled>...</button>`;
  for (let i = startP; i <= endP; i++) {
    html += `<button class="${i === currentPage ? 'active' : ''}" onclick="goPage(${i})">${i}</button>`;
  }
  if (endP < totalPages) html += `<button disabled>...</button><button onclick="goPage(${totalPages})">${totalPages}</button>`;

  html += `<button ${currentPage === totalPages ? 'disabled' : ''} onclick="goPage(${currentPage + 1})">&raquo;</button>`;
  el.innerHTML = html;
}

function goPage(p) {
  currentPage = p;
  renderLinkList();
  renderPagination();
  document.getElementById('links-list').scrollIntoView({ behavior: 'smooth' });
}

function onSearch() {
  currentPage = 1;
  applyFilter();
}

// ── Navigation ─────────────────────────────
function showPage(name) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  const el = document.getElementById('page-' + name);
  if (el) el.classList.add('active');
}

function setActiveNav(name) {
  document.querySelectorAll('nav a').forEach(a => a.classList.remove('active'));
  const el = document.getElementById('nav-' + name);
  if (el) el.classList.add('active');
}

function esc(s) {
  if (!s) return '';
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#039;');
}

// ── Keyboard shortcuts ─────────────────────
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
  if (e.key === 'h' || e.key === 'H') renderHome();
  if (e.key === 'l' || e.key === 'L') renderLinksPage();
});

// ── Start ──────────────────────────────────
document.addEventListener('DOMContentLoaded', init);
