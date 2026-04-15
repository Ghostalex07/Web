/**
 * Aion - Links Hub
 * Main application logic
 */

class AionApp {
  constructor() {
    this.currentSection = 'index';
    this.currentCategoryFilter = '';
    this.links = [];
  }

  init() {
    this.links = window.linksData || [];
    this.bindEvents();
    this.goHome();
  }

  bindEvents() {
    document.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT') return;
      if (e.key === 'h' || e.key === 'H') this.goHome();
      else if (e.key === 'l') this.showLinks();
      else if (e.key === 'Escape') this.clearFilters();
    });
  }

  goHome() {
    this.currentSection = 'index';
    this.showPage('index');
    this.renderFeatured();
  }

  showLinks() {
    this.currentSection = 'links';
    this.currentCategoryFilter = '';
    this.showPage('links');
    this.renderCategoryFilters();
    this.renderLinks();
  }

  showPage(pageName) {
    document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
    document.getElementById('page-' + pageName)?.classList.add('active');
  }

  renderFeatured() {
    const shuffled = [...this.links].sort(() => Math.random() - 0.5);
    const selected = shuffled.slice(0, 6);
    const html = `
      <div class="featured-section">
        <h2>// Featured Links</h2>
        <div class="board-section">
          ${selected.map(link => this.renderLinkCard(link)).join('')}
        </div>
      </div>
    `;
    document.getElementById('featured-links').innerHTML = html;
  }

  renderCategoryFilters() {
    const categories = [...new Set(this.links.map(l => l.category))].sort();
    let html = '<span style="color: #009933; font-size: 12px; margin-right: 10px;">Filter:</span>';
    
    html += `<span class="cat-filter active" data-cat="">All</span>`;
    categories.forEach(cat => {
      html += `<span class="cat-filter" data-cat="${this.escapeHtml(cat)}">${this.escapeHtml(cat)}</span>`;
    });
    
    document.getElementById('category-filters').innerHTML = html;

    document.querySelectorAll('.cat-filter').forEach(el => {
      el.addEventListener('click', () => {
        const cat = el.dataset.cat;
        this.filterByCategory(cat);
      });
    });
  }

  filterByCategory(cat) {
    this.currentCategoryFilter = cat;
    
    document.querySelectorAll('.cat-filter').forEach(el => {
      el.classList.toggle('active', el.dataset.cat === cat);
    });
    
    this.renderLinks();
  }

  clearFilters() {
    document.getElementById('search-input').value = '';
    this.filterByCategory('');
  }

  searchLinks() {
    const query = document.getElementById('search-input').value;
    this.renderLinks(query);
  }

  renderLinks(searchFilter = '', categoryFilter = '') {
    const container = document.getElementById('links-content');
    const categories = {};
    
    const finalFilter = searchFilter || '';
    const finalCategory = categoryFilter || this.currentCategoryFilter || '';

    this.links.forEach(link => {
      const searchStr = (link.name + ' ' + link.desc + ' ' + link.category).toLowerCase();
      const matchesSearch = !finalFilter || searchStr.includes(finalFilter.toLowerCase());
      const matchesCategory = !finalCategory || link.category === finalCategory;
      
      if (matchesSearch && matchesCategory) {
        if (!categories[link.category]) categories[link.category] = [];
        categories[link.category].push(link);
      }
    });

    if (Object.keys(categories).length === 0) {
      container.innerHTML = `
        <div class="no-results">
          <p>No links found matching your criteria.</p>
          <p style="font-size: 11px; margin-top: 10px;">Try a different search or <a href="#" onclick="app.clearFilters(); return false;">clear filters</a></p>
        </div>
      `;
      return;
    }

    let html = '';
    Object.keys(categories).sort().forEach(cat => {
      html += `
        <div class="board-section">
          <h2>// ${this.escapeHtml(cat)} (${categories[cat].length})</h2>
          ${categories[cat].map(link => this.renderLinkCard(link)).join('')}
        </div>
      `;
    });

    container.innerHTML = html;
  }

  renderLinkCard(link) {
    return `
      <div class="link-card">
        <p class="link-title">
          <a href="${this.escapeHtml(link.url)}" target="_blank" rel="noopener">${this.escapeHtml(link.name)}</a>
        </p>
        <p class="link-desc">${this.escapeHtml(link.desc)}</p>
      </div>
    `;
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  getStats() {
    return {
      total: this.links.length,
      categories: [...new Set(this.links.map(l => l.category))].length
    };
  }
}

const app = new AionApp();
document.addEventListener('DOMContentLoaded', () => app.init());
