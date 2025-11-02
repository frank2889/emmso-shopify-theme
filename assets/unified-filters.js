/**
 * Unified Filter System
 * Works seamlessly across Collections, Products (related), and Search
 * Single codebase, context auto-detection, smart behavior
 */

class UnifiedFilters {
  constructor(config = {}) {
    // Auto-detect context
    this.context = this.detectContext();
    
    // Configuration
    this.config = {
      mode: config.mode || 'full', // 'full', 'compact', 'collapsed'
      enableSmartRedirect: config.enableSmartRedirect !== false, // Default true
      productsPerPage: config.productsPerPage || 24,
      enableInfiniteScroll: config.enableInfiniteScroll || false,
      enableComparison: config.enableComparison || false,
      ...config
    };
    
    // Filter state
    this.filters = {
      category: [],
      brand: [],
      room: [],
      characteristics: [],
      priceMin: null,
      priceMax: null
    };
    
    // Product data
    this.products = [];
    this.filteredProducts = [];
    this.currentPage = 1;
    this.sortBy = 'relevance';
    this.viewMode = 'grid';
    
    this.init();
  }

  /**
   * Auto-detect context: collection, product, or search
   */
  detectContext() {
    const path = window.location.pathname;
    
    if (path.includes('/collections/')) {
      return 'collection';
    } else if (path.includes('/products/')) {
      return 'product';
    } else if (path.includes('/search')) {
      return 'search';
    }
    
    return 'unknown';
  }

  /**
   * Initialize based on context
   */
  init() {
    this.cacheElements();
    this.attachEventListeners();
    this.loadFromURL();
    
    // Context-specific initialization
    switch (this.context) {
      case 'collection':
        this.initCollection();
        break;
      case 'product':
        this.initProduct();
        break;
      case 'search':
        this.initSearch();
        break;
    }
  }

  /**
   * Initialize for Collection pages
   */
  async initCollection() {
    const collectionHandle = this.getCollectionHandle();
    
    try {
      // Fetch all products in collection (Shopify limits to 250 per page)
      const response = await fetch(`/collections/${collectionHandle}/products.json?limit=250`);
      const data = await response.json();
      
      this.products = data.products;
      this.buildDynamicFilters();
      this.applyFilters();
      
      // Check for smart redirect opportunity
      if (this.shouldRedirectToCollection()) {
        this.performSmartRedirect();
      }
      
    } catch (error) {
      console.error('Collection load error:', error);
      this.showEmpty();
    }
  }

  /**
   * Initialize for Product pages (related products sidebar)
   */
  async initProduct() {
    const productHandle = this.getProductHandle();
    
    try {
      // Get current product data
      const response = await fetch(`/products/${productHandle}.js`);
      const product = await response.json();
      
      // Fetch related products based on tags, vendor, or product_type
      await this.fetchRelatedProducts(product);
      
      this.buildDynamicFilters();
      this.applyFilters();
      
    } catch (error) {
      console.error('Product load error:', error);
    }
  }

  /**
   * Initialize for Search pages
   */
  async initSearch() {
    const query = new URLSearchParams(window.location.search).get('q') || '';
    
    if (this.resultQuery) {
      this.resultQuery.textContent = query ? `for "${query}"` : '';
    }
    
    try {
      // Check if query matches a collection
      if (this.config.enableSmartRedirect && await this.shouldRedirectToCollection(query)) {
        return; // Redirect will happen
      }
      
      // Perform search
      const response = await fetch(
        `/search/suggest.json?q=${encodeURIComponent(query)}&resources[type]=product&resources[limit]=250`
      );
      
      const data = await response.json();
      this.products = data.resources.results.products || [];
      
      this.buildDynamicFilters();
      this.applyFilters();
      
    } catch (error) {
      console.error('Search error:', error);
      this.showEmpty();
    }
  }

  /**
   * Fetch related products for product page sidebar
   */
  async fetchRelatedProducts(product) {
    // Strategy: Match by vendor, tags, or product_type
    const queries = [
      `vendor:${product.vendor}`,
      product.tags?.slice(0, 3).join(' OR ') || '',
      `product_type:${product.product_type}`
    ];
    
    const allProducts = new Set();
    
    for (const query of queries) {
      if (!query) continue;
      
      try {
        const response = await fetch(
          `/search/suggest.json?q=${encodeURIComponent(query)}&resources[type]=product&resources[limit]=50`
        );
        const data = await response.json();
        
        data.resources.results.products?.forEach(p => {
          if (p.id !== product.id) { // Exclude current product
            allProducts.add(p);
          }
        });
      } catch (error) {
        console.error(`Related products query error: ${query}`, error);
      }
    }
    
    this.products = Array.from(allProducts).slice(0, 50); // Limit to 50 related
  }

  /**
   * Smart redirect: If search query closely matches a collection, redirect there
   */
  async shouldRedirectToCollection(query) {
    if (!query || this.context !== 'search') return false;
    
    try {
      // Fetch all collections
      const response = await fetch('/collections.json');
      const data = await response.json();
      
      const collections = data.collections || [];
      
      // Find exact or close match
      const match = collections.find(c => 
        c.handle === query.toLowerCase().replace(/\s+/g, '-') ||
        c.title.toLowerCase() === query.toLowerCase()
      );
      
      if (match) {
        // Preserve filters in redirect
        const params = new URLSearchParams(window.location.search);
        params.delete('q'); // Remove search query
        
        const filterParams = params.toString();
        const redirectUrl = `/collections/${match.handle}${filterParams ? '?' + filterParams : ''}`;
        
        window.location.href = redirectUrl;
        return true;
      }
      
    } catch (error) {
      console.error('Collection check error:', error);
    }
    
    return false;
  }

  /**
   * Build dynamic filters based on current products
   */
  buildDynamicFilters() {
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
      const price = product.price ? product.price / 100 : 0;
      minPrice = Math.min(minPrice, price);
      maxPrice = Math.max(maxPrice, price);

      // Extract from tags
      product.tags?.forEach(tag => {
        // Room tags (multilingual)
        if (tag.includes('room:') || tag.includes('ruimte:') || tag.includes('raum:') || 
            tag.includes('pièce:') || tag.includes('habitación:') || tag.includes('stanza:')) {
          rooms.add(tag.split(':')[1]);
        }
        // Characteristic tags
        if (tag.includes('feature:') || tag.includes('eigenschap:') || tag.includes('caratteristica:')) {
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

  /**
   * Render filter checkbox options
   */
  renderFilterOptions(filterType, options) {
    const container = document.querySelector(`[data-filter-content="${filterType}"]`);
    if (!container || options.length === 0) {
      // Hide filter group if no options
      const group = document.querySelector(`[data-filter-group="${filterType}"]`);
      if (group) group.style.display = 'none';
      return;
    }

    // Show filter group
    const group = document.querySelector(`[data-filter-group="${filterType}"]`);
    if (group) group.style.display = '';

    // Sort options alphabetically
    options.sort();

    const html = options.map(option => {
      const id = `filter-${filterType}-${option.replace(/\s+/g, '-').toLowerCase()}`;
      const count = this.products.filter(p => this.productMatchesFilter(p, filterType, option)).length;
      const isChecked = this.filters[filterType].includes(option);
      
      return `
        <label class="filter-option">
          <input 
            type="checkbox" 
            class="filter-option__checkbox" 
            id="${id}"
            data-filter-type="${filterType}"
            data-filter-value="${option}"
            ${isChecked ? 'checked' : ''}
          >
          <span class="filter-option__label">${option}</span>
          <span class="filter-option__count">(${count})</span>
        </label>
      `;
    }).join('');

    container.innerHTML = html;

    // Attach checkbox event listeners
    container.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
      checkbox.addEventListener('change', (e) => {
        this.handleFilterChange(
          e.target.dataset.filterType,
          e.target.dataset.filterValue,
          e.target.checked
        );
      });
    });
  }

  /**
   * Check if product matches a specific filter
   */
  productMatchesFilter(product, filterType, value) {
    switch (filterType) {
      case 'category':
        return product.product_type === value;
      
      case 'brand':
        return product.vendor === value;
      
      case 'room':
        return product.tags?.some(tag => 
          (tag.includes('room:') || tag.includes('ruimte:') || tag.includes('raum:')) &&
          tag.split(':')[1] === value
        );
      
      case 'characteristics':
        return product.tags?.some(tag => 
          (tag.includes('feature:') || tag.includes('eigenschap:')) &&
          tag.split(':')[1] === value
        );
      
      default:
        return false;
    }
  }

  /**
   * Set price range inputs
   */
  setPriceRange(min, max) {
    const priceMin = document.querySelector('[data-price-min]');
    const priceMax = document.querySelector('[data-price-max]');
    
    if (priceMin) {
      priceMin.placeholder = `€${Math.floor(min)}`;
      priceMin.min = Math.floor(min);
    }
    
    if (priceMax) {
      priceMax.placeholder = `€${Math.ceil(max)}`;
      priceMax.max = Math.ceil(max);
    }
  }

  /**
   * Handle filter checkbox change
   */
  handleFilterChange(filterType, value, checked) {
    if (checked) {
      if (!this.filters[filterType].includes(value)) {
        this.filters[filterType].push(value);
      }
    } else {
      this.filters[filterType] = this.filters[filterType].filter(v => v !== value);
    }
    
    this.applyFilters();
  }

  /**
   * Apply all active filters
   */
  applyFilters() {
    this.filteredProducts = this.products.filter(product => {
      // Category filter (OR logic)
      if (this.filters.category.length > 0) {
        if (!this.filters.category.includes(product.product_type)) {
          return false;
        }
      }
      
      // Brand filter (OR logic)
      if (this.filters.brand.length > 0) {
        if (!this.filters.brand.includes(product.vendor)) {
          return false;
        }
      }
      
      // Room filter (OR logic)
      if (this.filters.room.length > 0) {
        const hasRoom = product.tags?.some(tag => 
          (tag.includes('room:') || tag.includes('ruimte:')) &&
          this.filters.room.includes(tag.split(':')[1])
        );
        if (!hasRoom) return false;
      }
      
      // Characteristics filter (AND logic - must have all selected)
      if (this.filters.characteristics.length > 0) {
        const hasAllCharacteristics = this.filters.characteristics.every(char =>
          product.tags?.some(tag => 
            (tag.includes('feature:') || tag.includes('eigenschap:')) &&
            tag.split(':')[1] === char
          )
        );
        if (!hasAllCharacteristics) return false;
      }
      
      // Price filter
      const price = product.price / 100;
      
      if (this.filters.priceMin !== null && price < this.filters.priceMin) {
        return false;
      }
      
      if (this.filters.priceMax !== null && price > this.filters.priceMax) {
        return false;
      }
      
      return true;
    });

    // Sort products
    this.sortProducts();
    
    // Update UI
    this.updateActiveFilters();
    this.updateResultCount();
    this.renderProducts();
    this.updateURL();
  }

  /**
   * Sort filtered products
   */
  sortProducts() {
    switch (this.sortBy) {
      case 'price-asc':
        this.filteredProducts.sort((a, b) => a.price - b.price);
        break;
      
      case 'price-desc':
        this.filteredProducts.sort((a, b) => b.price - a.price);
        break;
      
      case 'newest':
        this.filteredProducts.sort((a, b) => 
          new Date(b.created_at) - new Date(a.created_at)
        );
        break;
      
      case 'best-selling':
        // Would need sales data from metafields or API
        break;
      
      case 'relevance':
      default:
        // Keep original order (search relevance or collection order)
        break;
    }
  }

  /**
   * Render products in grid/list
   */
  renderProducts() {
    if (!this.productGrid) return;
    
    if (this.filteredProducts.length === 0) {
      this.showEmpty();
      return;
    }

    this.hideLoading();
    this.hideEmpty();

    // Calculate pagination
    const start = (this.currentPage - 1) * this.config.productsPerPage;
    const end = start + this.config.productsPerPage;
    const productsToShow = this.filteredProducts.slice(start, end);

    // Render based on context
    const html = productsToShow.map(product => this.renderProductCard(product)).join('');
    
    if (this.currentPage === 1) {
      this.productGrid.innerHTML = html;
    } else {
      this.productGrid.insertAdjacentHTML('beforeend', html);
    }

    // Update load more button
    this.updateLoadMore(end < this.filteredProducts.length);
  }

  /**
   * Render a single product card
   */
  renderProductCard(product) {
    const price = product.price / 100;
    const inStock = product.available !== false;
    
    // Context-specific card rendering
    const cardClass = this.context === 'product' ? 'related-product-card' : 'product-card';
    const imageSize = this.context === 'product' ? 200 : (this.viewMode === 'list' ? 200 : 400);
    
    return `
      <article class="${cardClass} ${cardClass}--${this.viewMode}" data-product-id="${product.id}">
        <a href="${product.url}" class="${cardClass}__link">
          <div class="${cardClass}__image-wrapper">
            <img 
              src="${product.featured_image || '/assets/placeholder.svg'}" 
              alt="${product.title}"
              loading="lazy"
              width="${imageSize}"
              height="${imageSize}"
              class="${cardClass}__image"
            >
          </div>
          
          <div class="${cardClass}__content">
            <p class="${cardClass}__vendor">${product.vendor}</p>
            <h3 class="${cardClass}__title">${product.title}</h3>
            
            <div class="${cardClass}__price-wrapper">
              <span class="${cardClass}__price">€${price.toFixed(2)}</span>
            </div>
            
            <span class="${cardClass}__availability ${inStock ? 'in-stock' : 'out-of-stock'}">
              ${inStock ? 'In Stock' : 'Out of Stock'}
            </span>
          </div>
        </a>
        
        ${this.config.enableComparison ? `
          <label class="${cardClass}__compare">
            <input type="checkbox" data-compare-product="${product.id}">
            <span>Compare</span>
          </label>
        ` : ''}
      </article>
    `;
  }

  /**
   * Update active filter chips
   */
  updateActiveFilters() {
    if (!this.filterChipsContainer) return;

    const activeFilters = [];

    // Category chips
    this.filters.category.forEach(value => {
      activeFilters.push({ type: 'category', value });
    });

    // Brand chips
    this.filters.brand.forEach(value => {
      activeFilters.push({ type: 'brand', value });
    });

    // Room chips
    this.filters.room.forEach(value => {
      activeFilters.push({ type: 'room', value });
    });

    // Characteristics chips
    this.filters.characteristics.forEach(value => {
      activeFilters.push({ type: 'characteristics', value });
    });

    // Price chip
    if (this.filters.priceMin !== null || this.filters.priceMax !== null) {
      const min = this.filters.priceMin !== null ? `€${this.filters.priceMin}` : '';
      const max = this.filters.priceMax !== null ? `€${this.filters.priceMax}` : '';
      const label = min && max ? `${min} - ${max}` : (min || `up to ${max}`);
      activeFilters.push({ type: 'price', value: label, isPriceFilter: true });
    }

    // Render chips
    if (activeFilters.length === 0) {
      this.activeFiltersContainer?.classList.add('hidden');
      this.filterChipsContainer.innerHTML = '';
      return;
    }

    this.activeFiltersContainer?.classList.remove('hidden');

    const html = activeFilters.map(filter => `
      <button 
        class="filter-chip" 
        data-remove-filter="${filter.type}"
        ${filter.isPriceFilter ? '' : `data-filter-value="${filter.value}"`}
      >
        ${filter.value}
        <svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor">
          <path d="M11 1L1 11M1 1L11 11" stroke="currentColor" stroke-width="2"/>
        </svg>
      </button>
    `).join('');

    this.filterChipsContainer.innerHTML = html;

    // Attach remove listeners
    this.filterChipsContainer.querySelectorAll('[data-remove-filter]').forEach(chip => {
      chip.addEventListener('click', () => {
        if (chip.dataset.removeFilter === 'price') {
          this.filters.priceMin = null;
          this.filters.priceMax = null;
          const priceMin = document.querySelector('[data-price-min]');
          const priceMax = document.querySelector('[data-price-max]');
          if (priceMin) priceMin.value = '';
          if (priceMax) priceMax.value = '';
        } else {
          this.handleFilterChange(
            chip.dataset.removeFilter,
            chip.dataset.filterValue,
            false
          );
          
          // Uncheck checkbox
          const checkbox = document.querySelector(
            `input[data-filter-type="${chip.dataset.removeFilter}"][data-filter-value="${chip.dataset.filterValue}"]`
          );
          if (checkbox) checkbox.checked = false;
        }
        
        this.applyFilters();
      });
    });
  }

  /**
   * Update result count
   */
  updateResultCount() {
    if (!this.resultCount) return;
    this.resultCount.textContent = this.filteredProducts.length;
  }

  /**
   * Update URL with filter params (preserves history)
   */
  updateURL() {
    const params = new URLSearchParams();

    // Preserve search query if in search context
    if (this.context === 'search') {
      const query = new URLSearchParams(window.location.search).get('q');
      if (query) params.set('q', query);
    }

    // Add active filters
    if (this.filters.category.length > 0) {
      params.set('category', this.filters.category.join(','));
    }

    if (this.filters.brand.length > 0) {
      params.set('brand', this.filters.brand.join(','));
    }

    if (this.filters.room.length > 0) {
      params.set('room', this.filters.room.join(','));
    }

    if (this.filters.characteristics.length > 0) {
      params.set('characteristics', this.filters.characteristics.join(','));
    }

    if (this.filters.priceMin !== null) {
      params.set('priceMin', this.filters.priceMin);
    }

    if (this.filters.priceMax !== null) {
      params.set('priceMax', this.filters.priceMax);
    }

    if (this.sortBy !== 'relevance') {
      params.set('sort', this.sortBy);
    }

    // Update URL without reload
    const newUrl = `${window.location.pathname}${params.toString() ? '?' + params.toString() : ''}`;
    window.history.pushState({}, '', newUrl);
  }

  /**
   * Load filters from URL params
   */
  loadFromURL() {
    const params = new URLSearchParams(window.location.search);

    if (params.has('category')) {
      this.filters.category = params.get('category').split(',');
    }

    if (params.has('brand')) {
      this.filters.brand = params.get('brand').split(',');
    }

    if (params.has('room')) {
      this.filters.room = params.get('room').split(',');
    }

    if (params.has('characteristics')) {
      this.filters.characteristics = params.get('characteristics').split(',');
    }

    if (params.has('priceMin')) {
      this.filters.priceMin = parseFloat(params.get('priceMin'));
    }

    if (params.has('priceMax')) {
      this.filters.priceMax = parseFloat(params.get('priceMax'));
    }

    if (params.has('sort')) {
      this.sortBy = params.get('sort');
    }
  }

  /**
   * Clear all filters
   */
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
    document.querySelectorAll('.filter-option__checkbox').forEach(checkbox => {
      checkbox.checked = false;
    });

    // Clear price inputs
    const priceMin = document.querySelector('[data-price-min]');
    const priceMax = document.querySelector('[data-price-max]');
    if (priceMin) priceMin.value = '';
    if (priceMax) priceMax.value = '';

    this.applyFilters();
  }

  /**
   * Toggle view mode (grid/list)
   */
  toggleView(mode) {
    this.viewMode = mode;
    
    // Update toggle buttons
    this.viewToggles?.forEach(btn => {
      if (btn.dataset.view === mode) {
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });

    // Update grid class
    if (this.productGrid) {
      this.productGrid.className = `product-grid product-grid--${mode}`;
    }

    // Re-render products
    this.currentPage = 1;
    this.renderProducts();
  }

  /**
   * Load more products (pagination)
   */
  loadMore() {
    this.currentPage++;
    this.renderProducts();
  }

  /**
   * Infinite scroll handler
   */
  handleScroll() {
    if (!this.config.enableInfiniteScroll) return;
    if (!this.loadMoreContainer) return;

    const rect = this.loadMoreContainer.getBoundingClientRect();
    const isVisible = rect.top < window.innerHeight && rect.bottom >= 0;

    if (isVisible && this.currentPage * this.config.productsPerPage < this.filteredProducts.length) {
      this.loadMore();
    }
  }

  /**
   * Update load more button visibility
   */
  updateLoadMore(hasMore) {
    if (!this.loadMoreContainer) return;
    
    if (hasMore) {
      this.loadMoreContainer.classList.remove('hidden');
    } else {
      this.loadMoreContainer.classList.add('hidden');
    }
  }

  /**
   * Show loading state
   */
  showLoading() {
    if (this.loadingState) this.loadingState.classList.remove('hidden');
    if (this.productGrid) this.productGrid.classList.add('hidden');
    if (this.emptyState) this.emptyState.classList.add('hidden');
  }

  /**
   * Hide loading state
   */
  hideLoading() {
    if (this.loadingState) this.loadingState.classList.add('hidden');
    if (this.productGrid) this.productGrid.classList.remove('hidden');
  }

  /**
   * Show empty state
   */
  showEmpty() {
    if (this.emptyState) this.emptyState.classList.remove('hidden');
    if (this.productGrid) this.productGrid.classList.add('hidden');
    if (this.loadingState) this.loadingState.classList.add('hidden');
  }

  /**
   * Hide empty state
   */
  hideEmpty() {
    if (this.emptyState) this.emptyState.classList.add('hidden');
  }

  /**
   * Get collection handle from URL
   */
  getCollectionHandle() {
    const match = window.location.pathname.match(/\/collections\/([^\/]+)/);
    return match ? match[1] : null;
  }

  /**
   * Get product handle from URL
   */
  getProductHandle() {
    const match = window.location.pathname.match(/\/products\/([^\/]+)/);
    return match ? match[1] : null;
  }

  /**
   * Cache DOM elements
   */
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

  /**
   * Attach event listeners
   */
  attachEventListeners() {
    // Filter group toggles (accordion)
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
      this.currentPage = 1; // Reset to first page
      this.applyFilters();
    });

    // View toggles
    this.viewToggles.forEach(btn => {
      btn.addEventListener('click', () => this.toggleView(btn.dataset.view));
    });

    // Load more
    this.loadMoreBtn?.addEventListener('click', () => this.loadMore());

    // Infinite scroll
    if (this.config.enableInfiniteScroll) {
      window.addEventListener('scroll', () => this.handleScroll());
    }
  }

  /**
   * Toggle filter group (accordion)
   */
  toggleFilterGroup(group) {
    const toggle = group.querySelector('.filter-group__toggle');
    const content = group.querySelector('.filter-group__content');
    const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
    
    toggle.setAttribute('aria-expanded', !isExpanded);
    content.hidden = isExpanded;
  }
}

// Auto-initialize if on supported page
document.addEventListener('DOMContentLoaded', () => {
  const context = window.location.pathname;
  
  if (context.includes('/search') || 
      context.includes('/collections/') || 
      context.includes('/products/')) {
    
    // Configuration based on context
    let config = {};
    
    if (context.includes('/products/')) {
      // Compact mode for product page sidebar
      config = {
        mode: 'compact',
        productsPerPage: 12,
        enableComparison: false,
        enableSmartRedirect: false
      };
    } else if (context.includes('/collections/')) {
      // Full mode for collections
      config = {
        mode: 'full',
        productsPerPage: 24,
        enableComparison: true,
        enableInfiniteScroll: false,
        enableSmartRedirect: true
      };
    } else if (context.includes('/search')) {
      // Full mode for search with smart redirects
      config = {
        mode: 'full',
        productsPerPage: 24,
        enableComparison: true,
        enableInfiniteScroll: false,
        enableSmartRedirect: true
      };
    }
    
    window.unifiedFilters = new UnifiedFilters(config);
  }
});
