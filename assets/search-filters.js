/**
 * Smart Filters - Dynamic Faceted Search
 * Only shows relevant filters based on current results
 * Multi-select with AND/OR logic, instant AJAX filtering
 */

class SearchFilters {
  constructor() {
    this.filters = {
      category: [],
      brand: [],
      room: [],
      characteristics: [],
      priceMin: null,
      priceMax: null
    };
    
    this.products = [];
    this.filteredProducts = [];
    this.currentPage = 1;
    this.productsPerPage = 24;
    this.sortBy = 'relevance';
    this.viewMode = 'grid';
    
    this.init();
  }

  init() {
    this.cacheElements();
    this.attachEventListeners();
    this.loadFromURL();
    this.performSearch();
  }

  cacheElements() {
    this.filterGroups = document.querySelectorAll('[data-filter-group]');
    this.activeFiltersContainer = document.querySelector('[data-active-filters]');
    this.filterChipsContainer = document.querySelector('[data-filter-chips]');
    this.clearAllBtn = document.querySelector('[data-clear-all]');
    this.productGrid = document.querySelector('[data-product-grid]');
    this.loadingState = document.querySelector('[data-loading-state]');
    this.emptyState = document.querySelector('[data-empty-state]');
    this.loadMoreBtn = document.querySelector('[data-load-more-btn]');
    this.loadMoreContainer = document.querySelector('[data-load-more]');
    this.resultCount = document.querySelector('[data-result-count]');
    this.resultQuery = document.querySelector('[data-result-query]');
    this.sortSelect = document.querySelector('[data-sort-select]');
    this.viewToggles = document.querySelectorAll('[data-view]');
  }

  attachEventListeners() {
    // Filter group toggles
    this.filterGroups.forEach(group => {
      const toggle = group.querySelector('.filter-group__toggle');
      toggle?.addEventListener('click', () => this.toggleFilterGroup(group));
    });

    // Clear all filters
    this.clearAllBtn?.addEventListener('click', () => this.clearAllFilters());

    // Price inputs
    const priceMin = document.querySelector('[data-price-min]');
    const priceMax = document.querySelector('[data-price-max]');
    
    priceMin?.addEventListener('change', (e) => {
      this.filters.priceMin = e.target.value ? parseFloat(e.target.value) : null;
      this.applyFilters();
    });
    
    priceMax?.addEventListener('change', (e) => {
      this.filters.priceMax = e.target.value ? parseFloat(e.target.value) : null;
      this.applyFilters();
    });

    // Sort dropdown
    this.sortSelect?.addEventListener('change', (e) => {
      this.sortBy = e.target.value;
      this.applyFilters();
    });

    // View toggles
    this.viewToggles.forEach(btn => {
      btn.addEventListener('click', () => this.toggleView(btn.dataset.view));
    });

    // Load more
    this.loadMoreBtn?.addEventListener('click', () => this.loadMore());

    // Infinite scroll (optional)
    window.addEventListener('scroll', () => this.handleScroll());
  }

  toggleFilterGroup(group) {
    const toggle = group.querySelector('.filter-group__toggle');
    const content = group.querySelector('.filter-group__content');
    const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
    
    toggle.setAttribute('aria-expanded', !isExpanded);
    content.hidden = isExpanded;
  }

  async performSearch() {
    this.showLoading();
    
    const query = new URLSearchParams(window.location.search).get('q') || '';
    this.resultQuery.textContent = query ? `for "${query}"` : '';
    
    try {
      // Get search results from Shopify
      const response = await fetch(
        `/search/suggest.json?q=${encodeURIComponent(query)}&resources[type]=product&resources[limit]=250`
      );
      
      const data = await response.json();
      this.products = data.resources.results.products || [];
      
      // Build dynamic filters based on results
      this.buildDynamicFilters();
      
      // Apply any existing filters
      this.applyFilters();
      
    } catch (error) {
      console.error('Search error:', error);
      this.showEmpty();
    }
  }

  buildDynamicFilters() {
    // Extract unique values from products
    const categories = new Set();
    const brands = new Set();
    const rooms = new Set();
    const characteristics = new Set();
    let minPrice = Infinity;
    let maxPrice = -Infinity;

    this.products.forEach(product => {
      // Category from product type
      if (product.product_type) {
        categories.add(product.product_type);
      }

      // Brand from vendor
      if (product.vendor) {
        brands.add(product.vendor);
      }

      // Price range
      const price = product.price / 100;
      minPrice = Math.min(minPrice, price);
      maxPrice = Math.max(maxPrice, price);

      // Extract from tags
      product.tags?.forEach(tag => {
        // Room tags
        if (tag.includes('room:') || tag.includes('ruimte:') || tag.includes('raum:')) {
          rooms.add(tag.split(':')[1]);
        }
        // Characteristic tags
        if (tag.includes('feature:') || tag.includes('eigenschap:')) {
          characteristics.add(tag.split(':')[1]);
        }
      });
    });

    // Render filter options
    this.renderFilterOptions('category', Array.from(categories));
    this.renderFilterOptions('brand', Array.from(brands));
    this.renderFilterOptions('room', Array.from(rooms));
    this.renderFilterOptions('characteristics', Array.from(characteristics));
    
    // Set price range
    this.setPriceRange(minPrice, maxPrice);
  }

  renderFilterOptions(filterType, options) {
    const container = document.querySelector(`[data-filter-content="${filterType}"]`);
    if (!container || options.length === 0) return;

    // Sort options alphabetically
    options.sort();

    const html = options.map(option => {
      const id = `filter-${filterType}-${option.replace(/\s+/g, '-')}`;
      const count = this.products.filter(p => this.productMatchesFilter(p, filterType, option)).length;
      
      return `
        <label class="filter-option">
          <input 
            type="checkbox" 
            class="filter-option__checkbox" 
            id="${id}"
            data-filter-type="${filterType}"
            data-filter-value="${option}"
          >
          <span class="filter-option__label">${option}</span>
          <span class="filter-option__count">(${count})</span>
        </label>
      `;
    }).join('');

    container.innerHTML = html;

    // Attach change listeners
    container.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.addEventListener('change', (e) => {
        this.handleFilterChange(e.target);
      });
    });
  }

  productMatchesFilter(product, filterType, value) {
    switch (filterType) {
      case 'category':
        return product.product_type === value;
      case 'brand':
        return product.vendor === value;
      case 'room':
        return product.tags?.some(tag => tag.includes(value));
      case 'characteristics':
        return product.tags?.some(tag => tag.includes(value));
      default:
        return false;
    }
  }

  setPriceRange(min, max) {
    const minInput = document.querySelector('[data-price-min]');
    const maxInput = document.querySelector('[data-price-max]');
    
    if (minInput) {
      minInput.min = Math.floor(min);
      minInput.placeholder = `€${Math.floor(min)}`;
    }
    
    if (maxInput) {
      maxInput.max = Math.ceil(max);
      maxInput.placeholder = `€${Math.ceil(max)}`;
    }
  }

  handleFilterChange(checkbox) {
    const filterType = checkbox.dataset.filterType;
    const filterValue = checkbox.dataset.filterValue;
    
    if (checkbox.checked) {
      if (!this.filters[filterType].includes(filterValue)) {
        this.filters[filterType].push(filterValue);
      }
    } else {
      this.filters[filterType] = this.filters[filterType].filter(v => v !== filterValue);
    }
    
    this.applyFilters();
  }

  applyFilters() {
    // Filter products
    this.filteredProducts = this.products.filter(product => {
      // Category filter
      if (this.filters.category.length > 0) {
        if (!this.filters.category.includes(product.product_type)) return false;
      }

      // Brand filter
      if (this.filters.brand.length > 0) {
        if (!this.filters.brand.includes(product.vendor)) return false;
      }

      // Room filter
      if (this.filters.room.length > 0) {
        const hasRoom = this.filters.room.some(room =>
          product.tags?.some(tag => tag.includes(room))
        );
        if (!hasRoom) return false;
      }

      // Characteristics filter
      if (this.filters.characteristics.length > 0) {
        const hasChar = this.filters.characteristics.some(char =>
          product.tags?.some(tag => tag.includes(char))
        );
        if (!hasChar) return false;
      }

      // Price filter
      const price = product.price / 100;
      if (this.filters.priceMin !== null && price < this.filters.priceMin) return false;
      if (this.filters.priceMax !== null && price > this.filters.priceMax) return false;

      return true;
    });

    // Sort products
    this.sortProducts();

    // Reset pagination
    this.currentPage = 1;

    // Update UI
    this.updateActiveFilters();
    this.updateResultCount();
    this.renderProducts();
    this.updateURL();
  }

  sortProducts() {
    switch (this.sortBy) {
      case 'price-asc':
        this.filteredProducts.sort((a, b) => a.price - b.price);
        break;
      case 'price-desc':
        this.filteredProducts.sort((a, b) => b.price - a.price);
        break;
      case 'newest':
        this.filteredProducts.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
        break;
      case 'relevance':
      default:
        // Keep original search relevance order
        break;
    }
  }

  renderProducts() {
    if (this.filteredProducts.length === 0) {
      this.showEmpty();
      return;
    }

    this.hideLoading();
    this.hideEmpty();

    const endIndex = this.currentPage * this.productsPerPage;
    const productsToShow = this.filteredProducts.slice(0, endIndex);

    const html = productsToShow.map(product => this.renderProductCard(product)).join('');
    this.productGrid.innerHTML = html;

    // Show/hide load more button
    if (this.filteredProducts.length > endIndex) {
      this.loadMoreContainer.hidden = false;
    } else {
      this.loadMoreContainer.hidden = true;
    }
  }

  renderProductCard(product) {
    const price = (product.price / 100).toFixed(2);
    const currency = '€'; // Get from shop settings
    
    return `
      <article class="product-card" data-view-mode="${this.viewMode}">
        <a href="${product.url}" class="product-card__link">
          <div class="product-card__image">
            <img 
              src="${product.featured_image || '/assets/placeholder.svg'}" 
              alt="${product.title}"
              loading="lazy"
            >
          </div>
          <div class="product-card__content">
            <h3 class="product-card__title">${product.title}</h3>
            <p class="product-card__vendor">${product.vendor}</p>
            <div class="product-card__price">
              <span class="product-card__price-value">${currency}${price}</span>
            </div>
            ${product.available ? 
              '<span class="product-card__availability product-card__availability--in-stock">In Stock</span>' :
              '<span class="product-card__availability product-card__availability--out-of-stock">Out of Stock</span>'
            }
          </div>
        </a>
      </article>
    `;
  }

  updateActiveFilters() {
    const hasFilters = Object.values(this.filters).some(f => 
      Array.isArray(f) ? f.length > 0 : f !== null
    );

    this.activeFiltersContainer.hidden = !hasFilters;

    if (!hasFilters) return;

    const chips = [];

    // Add filter chips
    Object.entries(this.filters).forEach(([type, values]) => {
      if (Array.isArray(values)) {
        values.forEach(value => {
          chips.push(this.createFilterChip(type, value));
        });
      } else if (values !== null) {
        if (type === 'priceMin') {
          chips.push(this.createFilterChip('price', `Min: €${values}`));
        } else if (type === 'priceMax') {
          chips.push(this.createFilterChip('price', `Max: €${values}`));
        }
      }
    });

    this.filterChipsContainer.innerHTML = chips.join('');

    // Attach remove listeners
    this.filterChipsContainer.querySelectorAll('.filter-chip__remove').forEach(btn => {
      btn.addEventListener('click', () => {
        const filterType = btn.dataset.filterType;
        const filterValue = btn.dataset.filterValue;
        this.removeFilter(filterType, filterValue);
      });
    });
  }

  createFilterChip(type, value) {
    return `
      <div class="filter-chip">
        <span>${value}</span>
        <button 
          type="button" 
          class="filter-chip__remove"
          data-filter-type="${type}"
          data-filter-value="${value}"
          aria-label="Remove filter"
        >
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
            <path d="M3 3L11 11M11 3L3 11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
    `;
  }

  removeFilter(type, value) {
    if (Array.isArray(this.filters[type])) {
      this.filters[type] = this.filters[type].filter(v => v !== value);
      
      // Uncheck the checkbox
      const checkbox = document.querySelector(
        `input[data-filter-type="${type}"][data-filter-value="${value}"]`
      );
      if (checkbox) checkbox.checked = false;
    } else {
      this.filters[type] = null;
      
      // Clear price input
      if (type === 'priceMin') {
        document.querySelector('[data-price-min]').value = '';
      } else if (type === 'priceMax') {
        document.querySelector('[data-price-max]').value = '';
      }
    }
    
    this.applyFilters();
  }

  clearAllFilters() {
    this.filters = {
      category: [],
      brand: [],
      room: [],
      characteristics: [],
      priceMin: null,
      priceMax: null
    };

    // Uncheck all checkboxes
    document.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = false);
    
    // Clear price inputs
    document.querySelector('[data-price-min]').value = '';
    document.querySelector('[data-price-max]').value = '';

    this.applyFilters();
  }

  updateResultCount() {
    this.resultCount.textContent = this.filteredProducts.length;
  }

  toggleView(view) {
    this.viewMode = view;
    this.productGrid.dataset.viewMode = view;
    
    this.viewToggles.forEach(btn => {
      btn.classList.toggle('view-toggle__btn--active', btn.dataset.view === view);
    });
  }

  loadMore() {
    this.currentPage++;
    this.renderProducts();
  }

  handleScroll() {
    // Optional infinite scroll
    const scrollPosition = window.innerHeight + window.scrollY;
    const threshold = document.documentElement.scrollHeight - 800;
    
    if (scrollPosition >= threshold && !this.loadMoreContainer.hidden) {
      this.loadMore();
    }
  }

  showLoading() {
    this.loadingState.hidden = false;
    this.productGrid.hidden = true;
    this.emptyState.hidden = true;
  }

  hideLoading() {
    this.loadingState.hidden = true;
    this.productGrid.hidden = false;
  }

  showEmpty() {
    this.emptyState.hidden = false;
    this.productGrid.hidden = true;
    this.loadingState.hidden = true;
    this.loadMoreContainer.hidden = true;
  }

  hideEmpty() {
    this.emptyState.hidden = true;
  }

  updateURL() {
    const params = new URLSearchParams(window.location.search);
    
    // Update filter params
    Object.entries(this.filters).forEach(([type, values]) => {
      if (Array.isArray(values) && values.length > 0) {
        params.set(type, values.join(','));
      } else if (values !== null) {
        params.set(type, values);
      } else {
        params.delete(type);
      }
    });

    // Update sort param
    if (this.sortBy !== 'relevance') {
      params.set('sort', this.sortBy);
    } else {
      params.delete('sort');
    }

    // Update URL without reload
    const newURL = `${window.location.pathname}?${params.toString()}`;
    history.replaceState({}, '', newURL);
  }

  loadFromURL() {
    const params = new URLSearchParams(window.location.search);
    
    // Load filters from URL
    ['category', 'brand', 'room', 'characteristics'].forEach(type => {
      const value = params.get(type);
      if (value) {
        this.filters[type] = value.split(',');
      }
    });

    this.filters.priceMin = params.get('priceMin') ? parseFloat(params.get('priceMin')) : null;
    this.filters.priceMax = params.get('priceMax') ? parseFloat(params.get('priceMax')) : null;
    
    this.sortBy = params.get('sort') || 'relevance';
    if (this.sortSelect) {
      this.sortSelect.value = this.sortBy;
    }
  }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new SearchFilters();
  });
} else {
  new SearchFilters();
}
