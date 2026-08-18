const PAGE_SIZE = 50;
let currentCat = '';
let currentSub = '';
let currentPage = 1;
let filtered = [];

function init() {
  buildIndex();
  renderHome();
}

function buildIndex() {
  window.catIndex = {};
  linksData.forEach(l => {
    if (!catIndex[l.category]) catIndex[l.category] = {};
    const s = l.subcategory || 'General';
    catIndex[l.category][s] = (catIndex[l.category][s] || 0) + 1;
  });
  window.totalCats = Object.keys(catIndex).length;
  window.totalSubs = Object.values(catIndex).reduce((a, c) => a + Object.keys(c).length, 0);
  document.getElementById('nav-meta').textContent = `${linksData.length} links`;
}

// ── Home ──────────────────────────────────
function renderHome() {
  showPage('home');
  setActive('home');
  const picks = [...linksData].sort(() => 0.5 - Math.random()).slice(0, 8);

  document.getElementById('page-home').innerHTML = `
    <div class="home-hero">
      <h1>A<span>ion</span></h1>
      <p>A curated collection of interesting websites, tools, and resources across the internet.</p>
    </div>
    <div class="home-stats">
      <div class="home-stat"><div class="num">${linksData.length.toLocaleString()}</div><div class="label">Links</div></div>
      <div class="home-stat"><div class="num">${totalCats}</div><div class="label">Categories</div></div>
      <div class="home-stat"><div class="num">${totalSubs}</div><div class="label">Subcategories</div></div>
    </div>
    <div class="section-title">Random picks</div>
    <div class="link-list">${picks.map(renderCard).join('')}</div>
  `;
}

// ── Links page ─────────────────────────────
function renderLinksPage() {
  showPage('links');
  setActive('links');
  currentPage = 1;
  currentCat = '';
  currentSub = '';
  filtered = linksData;
  renderLinksUI();
}

function renderLinksUI() {
  const page = document.getElementById('page-links');
  const cats = Object.keys(catIndex).sort();

  page.innerHTML = `
    <div class="links-header">
      <h1>Links</h1>
      <div class="search-row">
        <input class="search-input" id="search" placeholder="Search..." oninput="onSearch()">
        <span class="result-count" id="count">${filtered.length}</span>
      </div>
    </div>
    <div class="cat-bar" id="cat-bar">
      <button class="cat-pill ${!currentCat ? 'active' : ''}" onclick="pickCat('')">All</button>
      ${cats.map(c => {
        const n = Object.values(catIndex[c]).reduce((a, b) => a + b, 0);
        return `<button class="cat-pill ${c === currentCat ? 'active' : ''}" onclick="pickCat('${esc(c)}')">${esc(c)}<span class="count">${n}</span></button>`;
      }).join('')}
    </div>
    ${currentCat ? renderSubBar() : ''}
    <div class="link-list" id="list">${filtered.slice(0, PAGE_SIZE).map(renderCard).join('')}</div>
    <div class="pager" id="pager"></div>
  `;
  renderPager();
}

function renderSubBar() {
  const subs = catIndex[currentCat] || {};
  return `<div class="sub-bar">
    <button class="sub-pill ${!currentSub ? 'active' : ''}" onclick="pickSub('')">All ${esc(currentCat)}</button>
    ${Object.keys(subs).sort().map(s =>
      `<button class="sub-pill ${s === currentSub ? 'active' : ''}" onclick="pickSub('${esc(s)}')">${esc(s)}</button>`
    ).join('')}
  </div>`;
}

function pickCat(cat) {
  currentCat = cat;
  currentSub = '';
  currentPage = 1;
  applyFilter();
  renderLinksUI();
}

function pickSub(sub) {
  currentSub = sub;
  currentPage = 1;
  applyFilter();
  renderLinksUI();
}

function onSearch() {
  currentPage = 1;
  applyFilter();
  document.getElementById('list').innerHTML = filtered.slice(0, PAGE_SIZE).map(renderCard).join('');
  document.getElementById('count').textContent = filtered.length;
  renderPager();
}

function applyFilter() {
  const q = (document.getElementById('search')?.value || '').toLowerCase().trim();
  filtered = linksData.filter(l => {
    if (currentCat && l.category !== currentCat) return false;
    if (currentSub && (l.subcategory || 'General') !== currentSub) return false;
    if (q) {
      const h = (l.name + ' ' + l.desc + ' ' + l.url).toLowerCase();
      if (!q.split(/\s+/).every(w => h.includes(w))) return false;
    }
    return true;
  });
  document.getElementById('count').textContent = filtered.length;
}

// ── Card ──────────────────────────────────
function renderCard(l) {
  return `<div class="link-card">
    <a class="name" href="${esc(l.url)}" target="_blank" rel="noopener">${esc(l.name)}</a>
    <span class="sep">&mdash;</span>
    <span class="desc">${esc(l.desc)}</span>
    ${l.subcategory ? `<span class="tag">${esc(l.subcategory)}</span>` : ''}
  </div>`;
}

// ── Pager ─────────────────────────────────
function renderPager() {
  const total = Math.ceil(filtered.length / PAGE_SIZE);
  const el = document.getElementById('pager');
  if (!el || total <= 1) { if (el) el.innerHTML = ''; return; }

  let h = '';
  h += `<button ${currentPage === 1 ? 'disabled' : ''} onclick="goPage(${currentPage - 1})">&larr;</button>`;
  const r = 2;
  const s = Math.max(1, currentPage - r);
  const e = Math.min(total, currentPage + r);
  if (s > 1) h += `<button onclick="goPage(1)">1</button><button disabled>&hellip;</button>`;
  for (let i = s; i <= e; i++) h += `<button class="${i === currentPage ? 'active' : ''}" onclick="goPage(${i})">${i}</button>`;
  if (e < total) h += `<button disabled>&hellip;</button><button onclick="goPage(${total})">${total}</button>`;
  h += `<button ${currentPage === total ? 'disabled' : ''} onclick="goPage(${currentPage + 1})">&rarr;</button>`;
  el.innerHTML = h;
}

function goPage(p) {
  currentPage = p;
  const el = document.getElementById('list');
  el.innerHTML = filtered.slice((p - 1) * PAGE_SIZE, p * PAGE_SIZE).map(renderCard).join('');
  renderPager();
  el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ── Nav helpers ────────────────────────────
function showPage(name) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById('page-' + name).classList.add('active');
}

function setActive(name) {
  document.querySelectorAll('nav a').forEach(a => a.classList.remove('active'));
  document.getElementById('nav-' + name)?.classList.add('active');
}

function esc(s) {
  if (!s) return '';
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT') return;
  if (e.key === 'h') renderHome();
  if (e.key === 'l') renderLinksPage();
});

document.addEventListener('DOMContentLoaded', init);
