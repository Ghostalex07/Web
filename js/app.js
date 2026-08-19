const PAGE_SIZE = 50;
let currentCat = '';
let currentSub = '';
let currentPage = 1;
let filtered = [];

const catIcons = {
  'Security Forums': { icon: '🛡️', color: 'rgba(239, 68, 68, 0.12)' },
  'Books': { icon: '📚', color: 'rgba(59, 130, 246, 0.12)' },
  'Business': { icon: '💼', color: 'rgba(168, 85, 247, 0.12)' },
  'Design': { icon: '🎨', color: 'rgba(236, 72, 153, 0.12)' },
  'Development': { icon: '💻', color: 'rgba(34, 197, 94, 0.12)' },
  'Education': { icon: '🎓', color: 'rgba(234, 179, 8, 0.12)' },
  'Entertainment': { icon: '🎮', color: 'rgba(249, 115, 22, 0.12)' },
  'Finance': { icon: '💰', color: 'rgba(20, 184, 166, 0.12)' },
  'Food': { icon: '🍔', color: 'rgba(244, 63, 94, 0.12)' },
  'Gaming': { icon: '🕹️', color: 'rgba(139, 92, 246, 0.12)' },
  'Health': { icon: '🏥', color: 'rgba(16, 185, 129, 0.12)' },
  'Humor': { icon: '😄', color: 'rgba(251, 191, 36, 0.12)' },
  'Lifestyle': { icon: '🌿', color: 'rgba(34, 197, 94, 0.12)' },
  'Music': { icon: '🎵', color: 'rgba(236, 72, 153, 0.12)' },
  'News': { icon: '📰', color: 'rgba(107, 114, 128, 0.12)' },
  'Other': { icon: '🔗', color: 'rgba(156, 163, 175, 0.12)' },
  'Photography': { icon: '📷', color: 'rgba(245, 158, 11, 0.12)' },
  'Science': { icon: '🔬', color: 'rgba(6, 182, 212, 0.12)' },
  'Shopping': { icon: '🛒', color: 'rgba(244, 63, 94, 0.12)' },
  'Social': { icon: '💬', color: 'rgba(59, 130, 246, 0.12)' },
  'Sports': { icon: '⚽', color: 'rgba(34, 197, 94, 0.12)' },
  'Tech': { icon: '⚡', color: 'rgba(99, 102, 241, 0.12)' },
  'Tools': { icon: '🛠️', color: 'rgba(107, 114, 128, 0.12)' },
  'Travel': { icon: '✈️', color: 'rgba(14, 165, 233, 0.12)' },
  'Video': { icon: '🎬', color: 'rgba(239, 68, 68, 0.12)' },
};

function init() {
  buildIndex();
  loadTheme();
  renderHome();
  setupScrollListener();
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
  document.getElementById('nav-meta').textContent = `${linksData.length.toLocaleString()} links`;
}

function getCatIcon(cat) {
  return catIcons[cat] || { icon: '🔗', color: 'rgba(156, 163, 175, 0.12)' };
}

// ── Theme ─────────────────────────────────
function loadTheme() {
  const saved = localStorage.getItem('aion-theme');
  if (saved) {
    document.documentElement.setAttribute('data-theme', saved);
  } else {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
  }
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('aion-theme', next);
}

// ── Scroll ─────────────────────────────────
function setupScrollListener() {
  const btn = document.getElementById('back-to-top');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ── Home ──────────────────────────────────
function renderHome() {
  showPage('home');
  setActive('home');

  const featured = [...linksData]
    .sort((a, b) => (b.name.length + b.desc.length) - (a.name.length + a.desc.length))
    .slice(0, 12);

  const cats = Object.keys(catIndex).sort();
  const topCats = cats.slice(0, 8);

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
    <div class="section-header">
      <div class="section-title">Browse Categories</div>
    </div>
    <div class="cat-grid">
      ${topCats.map(c => {
        const info = getCatIcon(c);
        const n = Object.values(catIndex[c]).reduce((a, b) => a + b, 0);
        return `<div class="cat-card" onclick="jumpToCategory('${esc(c)}')">
          <div class="cat-icon" style="background:${info.color}">${info.icon}</div>
          <div class="cat-info">
            <div class="cat-name">${esc(c)}</div>
            <div class="cat-count">${n} links</div>
          </div>
        </div>`;
      }).join('')}
    </div>
    <div class="section-header">
      <div class="section-title">Featured Links</div>
      <button class="section-action" onclick="refreshFeatured()">Refresh</button>
    </div>
    <div class="link-list" id="featured-list">${featured.map(renderCard).join('')}</div>
  `;
}

function refreshFeatured() {
  const picks = [...linksData].sort(() => 0.5 - Math.random()).slice(0, 12);
  const el = document.getElementById('featured-list');
  if (el) {
    el.style.opacity = '0';
    setTimeout(() => {
      el.innerHTML = picks.map(renderCard).join('');
      el.style.opacity = '1';
    }, 150);
  }
}

function jumpToCategory(cat) {
  renderLinksPage();
  setTimeout(() => pickCat(cat), 10);
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
        <input class="search-input" id="search" placeholder="Search links..." oninput="onSearch()">
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

// ── About ─────────────────────────────────
function renderAbout() {
  showPage('about');
  setActive('about');

  document.getElementById('page-about').innerHTML = `
    <div class="about-content">
      <h1>About Aion</h1>
      <p>Aion is a curated collection of interesting websites, tools, and resources across the internet. No algorithms, no tracking, no censorship — just a hand-picked list of useful links.</p>
      <p>Every link has been selected for its quality and usefulness. Whether you're looking for development tools, educational resources, or creative inspiration, you'll find something valuable here.</p>

      <div class="about-section">
        <h2>Keyboard Shortcuts</h2>
        <ul class="about-list">
          <li><span class="kbd">h</span> Go to Home</li>
          <li><span class="kbd">l</span> Go to Links</li>
          <li><span class="kbd">a</span> Go to About</li>
          <li><span class="kbd">/</span> Focus search</li>
          <li><span class="kbd">?</span> Show shortcuts modal</li>
          <li><span class="kbd">t</span> Toggle dark/light theme</li>
          <li><span class="kbd">r</span> Refresh random picks</li>
          <li><span class="kbd">Esc</span> Close modal / Clear search</li>
        </ul>
      </div>

      <div class="about-section">
        <h2>Data</h2>
        <p>All link data is stored locally in your browser. No external requests are made except for the font files. Your browsing activity is completely private.</p>
      </div>
    </div>
  `;
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

// ── Shortcuts Modal ────────────────────────
function openShortcuts() {
  document.getElementById('shortcuts-modal').classList.add('open');
}

function closeShortcuts() {
  document.getElementById('shortcuts-modal').classList.remove('open');
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

// ── Keyboard shortcuts ─────────────────────
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT') {
    if (e.key === 'Escape') {
      e.target.value = '';
      e.target.blur();
      if (document.getElementById('page-links').classList.contains('active')) {
        onSearch();
      }
    }
    return;
  }

  switch (e.key) {
    case 'h': renderHome(); break;
    case 'l': renderLinksPage(); break;
    case 'a': renderAbout(); break;
    case '/': e.preventDefault(); document.getElementById('search')?.focus(); break;
    case '?': openShortcuts(); break;
    case 't': toggleTheme(); break;
    case 'r':
      if (document.getElementById('page-home').classList.contains('active')) {
        refreshFeatured();
      }
      break;
    case 'Escape': closeShortcuts(); break;
  }
});

document.addEventListener('DOMContentLoaded', init);
