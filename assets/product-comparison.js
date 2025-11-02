/**
 * Product Comparison Tool
 * Side-by-side comparison of up to 4 products
 * 
 * Features:
 * - Add/remove products from search or collection results
 * - Persistent comparison (localStorage)
 * - Modal comparison view
 * - Spec-by-spec comparison
 * - Price comparison
 * - Feature highlighting (better/worse/equal)
 * - Multilingual support
 * - Mobile responsive
 */

class ProductComparison {
  constructor(config = {}) {
    this.config = {
      maxProducts: config.maxProducts || 4,
      storageKey: config.storageKey || 'product-comparison',
      locale: config.locale || document.documentElement.lang || 'en',
      ...config
    };

    this.comparedProducts = [];
    this.loadFromStorage();
    this.init();
  }

  /**
   * Initialize comparison tool
   */
  init() {
    this.cacheElements();
    this.attachEventListeners();
    this.updateUI();
    this.createComparisonModal();
  }

  /**
   * Cache DOM elements
   */
  cacheElements() {
    this.compareBar = document.querySelector('[data-compare-bar]');
    this.compareCount = document.querySelector('[data-compare-count]');
    this.compareButton = document.querySelector('[data-compare-button]');
    this.clearCompareButton = document.querySelector('[data-clear-compare]');
    this.compareCheckboxes = document.querySelectorAll('[data-compare-product]');
  }

  /**
   * Attach event listeners
   */
  attachEventListeners() {
    // Compare button (open modal)
    this.compareButton?.addEventListener('click', () => this.showComparison());

    // Clear all
    this.clearCompareButton?.addEventListener('click', () => this.clearAll());

    // Product checkboxes (delegate for dynamic content)
    document.addEventListener('change', (e) => {
      if (e.target.matches('[data-compare-product]')) {
        const productId = e.target.dataset.compareProduct;
        const isChecked = e.target.checked;

        if (isChecked) {
          this.addProduct(productId);
        } else {
          this.removeProduct(productId);
        }
      }
    });

    // Keyboard shortcut: Press 'C' to open comparison
    document.addEventListener('keydown', (e) => {
      if (e.key === 'c' && !e.ctrlKey && !e.metaKey && this.comparedProducts.length >= 2) {
        const target = e.target;
        // Don't trigger if typing in input/textarea
        if (target.tagName !== 'INPUT' && target.tagName !== 'TEXTAREA') {
          this.showComparison();
        }
      }
    });
  }

  /**
   * Add product to comparison
   */
  async addProduct(productId) {
    // Check max limit
    if (this.comparedProducts.length >= this.config.maxProducts) {
      this.showNotification(
        this.translate('comparison.max_reached', { max: this.config.maxProducts }),
        'warning'
      );
      
      // Uncheck the checkbox
      const checkbox = document.querySelector(`[data-compare-product="${productId}"]`);
      if (checkbox) checkbox.checked = false;
      
      return;
    }

    // Check if already added
    if (this.comparedProducts.find(p => p.id === productId)) {
      return;
    }

    // Fetch product data
    const product = await this.fetchProductData(productId);
    
    if (!product) {
      this.showNotification(this.translate('comparison.error_loading'), 'error');
      return;
    }

    this.comparedProducts.push(product);
    this.saveToStorage();
    this.updateUI();
    this.showNotification(
      this.translate('comparison.added', { product: product.title }),
      'success'
    );
  }

  /**
   * Remove product from comparison
   */
  removeProduct(productId) {
    this.comparedProducts = this.comparedProducts.filter(p => p.id !== productId);
    this.saveToStorage();
    this.updateUI();

    // Uncheck checkbox if exists
    const checkbox = document.querySelector(`[data-compare-product="${productId}"]`);
    if (checkbox) checkbox.checked = false;
  }

  /**
   * Clear all products
   */
  clearAll() {
    this.comparedProducts = [];
    this.saveToStorage();
    this.updateUI();

    // Uncheck all checkboxes
    document.querySelectorAll('[data-compare-product]:checked').forEach(cb => {
      cb.checked = false;
    });

    this.showNotification(this.translate('comparison.cleared'), 'info');
  }

  /**
   * Fetch product data from Shopify
   */
  async fetchProductData(productId) {
    try {
      // Try to get from DOM first (faster)
      const productCard = document.querySelector(`[data-product-id="${productId}"]`);
      
      if (productCard) {
        return this.extractProductFromCard(productCard, productId);
      }

      // Fallback: Fetch from API
      const response = await fetch(`/products/${productId}.js`);
      const product = await response.json();
      
      return {
        id: product.id,
        handle: product.handle,
        title: product.title,
        vendor: product.vendor,
        type: product.product_type,
        price: product.price / 100,
        compareAtPrice: product.compare_at_price ? product.compare_at_price / 100 : null,
        available: product.available,
        url: `/products/${product.handle}`,
        image: product.featured_image,
        description: product.description,
        tags: product.tags || [],
        variants: product.variants || [],
        options: product.options || [],
        metafields: product.metafields || {}
      };
    } catch (error) {
      console.error('Error fetching product:', error);
      return null;
    }
  }

  /**
   * Extract product data from card in DOM
   */
  extractProductFromCard(card, productId) {
    return {
      id: productId,
      title: card.querySelector('.product-card__title')?.textContent.trim() || '',
      vendor: card.querySelector('.product-card__vendor')?.textContent.trim() || '',
      price: parseFloat(card.querySelector('.product-card__price')?.textContent.replace(/[^0-9.]/g, '') || 0),
      available: !card.querySelector('.product-card__availability')?.classList.contains('out-of-stock'),
      url: card.querySelector('.product-card__link')?.href || '',
      image: card.querySelector('.product-card__image')?.src || '',
      tags: [],
      variants: []
    };
  }

  /**
   * Update UI (compare bar, checkboxes)
   */
  updateUI() {
    const count = this.comparedProducts.length;

    // Update count
    if (this.compareCount) {
      this.compareCount.textContent = count;
    }

    // Show/hide compare bar
    if (this.compareBar) {
      if (count > 0) {
        this.compareBar.classList.remove('hidden');
      } else {
        this.compareBar.classList.add('hidden');
      }
    }

    // Enable/disable compare button
    if (this.compareButton) {
      this.compareButton.disabled = count < 2;
    }

    // Sync checkboxes with stored products
    this.comparedProducts.forEach(product => {
      const checkbox = document.querySelector(`[data-compare-product="${product.id}"]`);
      if (checkbox && !checkbox.checked) {
        checkbox.checked = true;
      }
    });
  }

  /**
   * Create comparison modal
   */
  createComparisonModal() {
    if (document.getElementById('product-comparison-modal')) {
      return; // Already exists
    }

    const modal = document.createElement('div');
    modal.id = 'product-comparison-modal';
    modal.className = 'comparison-modal';
    modal.innerHTML = `
      <div class="comparison-modal__overlay" data-close-modal></div>
      <div class="comparison-modal__content">
        <div class="comparison-modal__header">
          <h2 class="comparison-modal__title">${this.translate('comparison.title')}</h2>
          <button class="comparison-modal__close" data-close-modal>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
        <div class="comparison-modal__body" data-comparison-table></div>
      </div>
    `;

    document.body.appendChild(modal);

    // Close handlers
    modal.querySelectorAll('[data-close-modal]').forEach(el => {
      el.addEventListener('click', () => this.hideComparison());
    });

    // ESC key to close
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        this.hideComparison();
      }
    });
  }

  /**
   * Show comparison modal
   */
  showComparison() {
    if (this.comparedProducts.length < 2) {
      this.showNotification(this.translate('comparison.min_required'), 'warning');
      return;
    }

    const modal = document.getElementById('product-comparison-modal');
    const tableContainer = modal.querySelector('[data-comparison-table]');

    // Build comparison table
    tableContainer.innerHTML = this.buildComparisonTable();

    // Show modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  /**
   * Hide comparison modal
   */
  hideComparison() {
    const modal = document.getElementById('product-comparison-modal');
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  /**
   * Build comparison table HTML
   */
  buildComparisonTable() {
    const products = this.comparedProducts;
    
    // Extract all unique attributes
    const attributes = this.extractAttributes(products);

    let html = '<div class="comparison-table">';

    // Header row (product images & titles)
    html += '<div class="comparison-row comparison-row--header">';
    html += '<div class="comparison-cell comparison-cell--label"></div>';
    
    products.forEach(product => {
      html += `
        <div class="comparison-cell comparison-cell--product">
          <button class="comparison-remove" data-remove-product="${product.id}" title="${this.translate('comparison.remove')}">
            <svg width="16" height="16" viewBox="0 0 16 16">
              <path d="M12 4L4 12M4 4L12 12" stroke="currentColor" stroke-width="2"/>
            </svg>
          </button>
          <img src="${product.image}" alt="${product.title}" class="comparison-product-image">
          <h3 class="comparison-product-title">${product.title}</h3>
          <p class="comparison-product-vendor">${product.vendor}</p>
          <a href="${product.url}" class="comparison-view-link">${this.translate('comparison.view_product')}</a>
        </div>
      `;
    });
    
    html += '</div>';

    // Price row
    html += this.buildAttributeRow(
      this.translate('comparison.price'),
      products,
      (p) => this.formatPrice(p.price),
      'price'
    );

    // Availability row
    html += this.buildAttributeRow(
      this.translate('comparison.availability'),
      products,
      (p) => p.available ? 
        `<span class="comparison-badge comparison-badge--success">${this.translate('comparison.in_stock')}</span>` : 
        `<span class="comparison-badge comparison-badge--danger">${this.translate('comparison.out_of_stock')}</span>`,
      'availability'
    );

    // Type row
    if (attributes.type.size > 1) {
      html += this.buildAttributeRow(
        this.translate('comparison.type'),
        products,
        (p) => p.type || '-',
        'type'
      );
    }

    // Variants row
    html += this.buildAttributeRow(
      this.translate('comparison.variants'),
      products,
      (p) => p.variants?.length || 0,
      'variants'
    );

    // Tags comparison (features)
    const allTags = new Set();
    products.forEach(p => p.tags?.forEach(tag => {
      // Only show feature tags
      if (tag.includes('feature:') || tag.includes('eigenschap:')) {
        allTags.add(tag.split(':')[1]);
      }
    }));

    if (allTags.size > 0) {
      html += '<div class="comparison-section">';
      html += `<div class="comparison-section-title">${this.translate('comparison.features')}</div>`;
      
      Array.from(allTags).forEach(feature => {
        html += this.buildAttributeRow(
          feature,
          products,
          (p) => {
            const hasFeature = p.tags?.some(tag => tag.includes(feature));
            return hasFeature ? 
              `<span class="comparison-check">✓</span>` : 
              `<span class="comparison-cross">✗</span>`;
          },
          'feature'
        );
      });
      
      html += '</div>';
    }

    // Add remove buttons to modal
    setTimeout(() => {
      document.querySelectorAll('[data-remove-product]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          const productId = e.currentTarget.dataset.removeProduct;
          this.removeProduct(productId);
          
          // Rebuild table
          const tableContainer = document.querySelector('[data-comparison-table]');
          tableContainer.innerHTML = this.buildComparisonTable();
          
          // Close modal if less than 2 products
          if (this.comparedProducts.length < 2) {
            this.hideComparison();
          }
        });
      });
    }, 0);

    html += '</div>';

    return html;
  }

  /**
   * Build single attribute row
   */
  buildAttributeRow(label, products, getValue, type = 'default') {
    const values = products.map(p => getValue(p));
    
    // Determine if we should highlight best/worst
    let highlightMode = null;
    if (type === 'price') {
      highlightMode = 'lower-better';
    } else if (type === 'variants') {
      highlightMode = 'higher-better';
    }

    let html = '<div class="comparison-row">';
    html += `<div class="comparison-cell comparison-cell--label">${label}</div>`;
    
    products.forEach((product, index) => {
      const value = values[index];
      let cellClass = 'comparison-cell';
      
      // Add highlight class
      if (highlightMode && type !== 'availability') {
        const numericValues = values.map(v => parseFloat(String(v).replace(/[^0-9.]/g, '')) || 0);
        const currentValue = numericValues[index];
        
        if (highlightMode === 'lower-better') {
          const min = Math.min(...numericValues.filter(v => v > 0));
          if (currentValue === min && currentValue > 0) {
            cellClass += ' comparison-cell--best';
          }
        } else if (highlightMode === 'higher-better') {
          const max = Math.max(...numericValues);
          if (currentValue === max && currentValue > 0) {
            cellClass += ' comparison-cell--best';
          }
        }
      }
      
      html += `<div class="${cellClass}">${value}</div>`;
    });
    
    html += '</div>';
    return html;
  }

  /**
   * Extract all unique attributes from products
   */
  extractAttributes(products) {
    const attributes = {
      type: new Set(),
      tags: new Set(),
      features: new Set()
    };

    products.forEach(product => {
      if (product.type) attributes.type.add(product.type);
      
      product.tags?.forEach(tag => {
        attributes.tags.add(tag);
        
        if (tag.includes('feature:') || tag.includes('eigenschap:')) {
          attributes.features.add(tag.split(':')[1]);
        }
      });
    });

    return attributes;
  }

  /**
   * Format price with currency
   */
  formatPrice(price) {
    return new Intl.NumberFormat(this.config.locale, {
      style: 'currency',
      currency: 'EUR'
    }).format(price);
  }

  /**
   * Save to localStorage
   */
  saveToStorage() {
    try {
      localStorage.setItem(
        this.config.storageKey,
        JSON.stringify(this.comparedProducts.map(p => ({
          id: p.id,
          title: p.title,
          vendor: p.vendor,
          price: p.price,
          url: p.url,
          image: p.image,
          available: p.available,
          tags: p.tags,
          type: p.type,
          variants: p.variants
        })))
      );
    } catch (error) {
      console.error('Failed to save comparison:', error);
    }
  }

  /**
   * Load from localStorage
   */
  loadFromStorage() {
    try {
      const stored = localStorage.getItem(this.config.storageKey);
      if (stored) {
        this.comparedProducts = JSON.parse(stored);
      }
    } catch (error) {
      console.error('Failed to load comparison:', error);
      this.comparedProducts = [];
    }
  }

  /**
   * Show notification
   */
  showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `comparison-notification comparison-notification--${type}`;
    notification.textContent = message;

    document.body.appendChild(notification);

    // Trigger animation
    setTimeout(() => notification.classList.add('active'), 10);

    // Remove after 3s
    setTimeout(() => {
      notification.classList.remove('active');
      setTimeout(() => notification.remove(), 300);
    }, 3000);
  }

  /**
   * Translate text (multilingual support)
   */
  translate(key, params = {}) {
    const lang = this.config.locale.split('-')[0];
    
    const translations = {
      en: {
        'comparison.title': 'Product Comparison',
        'comparison.added': 'Added {product} to comparison',
        'comparison.removed': 'Removed from comparison',
        'comparison.cleared': 'Comparison cleared',
        'comparison.max_reached': 'Maximum {max} products can be compared',
        'comparison.min_required': 'Select at least 2 products to compare',
        'comparison.error_loading': 'Error loading product',
        'comparison.price': 'Price',
        'comparison.availability': 'Availability',
        'comparison.type': 'Product Type',
        'comparison.variants': 'Variants',
        'comparison.features': 'Features',
        'comparison.in_stock': 'In Stock',
        'comparison.out_of_stock': 'Out of Stock',
        'comparison.view_product': 'View Product',
        'comparison.remove': 'Remove'
      },
      nl: {
        'comparison.title': 'Productvergelijking',
        'comparison.added': '{product} toegevoegd aan vergelijking',
        'comparison.removed': 'Verwijderd uit vergelijking',
        'comparison.cleared': 'Vergelijking gewist',
        'comparison.max_reached': 'Maximaal {max} producten kunnen worden vergeleken',
        'comparison.min_required': 'Selecteer minimaal 2 producten om te vergelijken',
        'comparison.error_loading': 'Fout bij laden product',
        'comparison.price': 'Prijs',
        'comparison.availability': 'Beschikbaarheid',
        'comparison.type': 'Producttype',
        'comparison.variants': 'Varianten',
        'comparison.features': 'Kenmerken',
        'comparison.in_stock': 'Op voorraad',
        'comparison.out_of_stock': 'Niet op voorraad',
        'comparison.view_product': 'Bekijk Product',
        'comparison.remove': 'Verwijderen'
      },
      de: {
        'comparison.title': 'Produktvergleich',
        'comparison.added': '{product} zum Vergleich hinzugefügt',
        'comparison.removed': 'Aus Vergleich entfernt',
        'comparison.cleared': 'Vergleich gelöscht',
        'comparison.max_reached': 'Maximal {max} Produkte können verglichen werden',
        'comparison.min_required': 'Wählen Sie mindestens 2 Produkte zum Vergleichen',
        'comparison.error_loading': 'Fehler beim Laden des Produkts',
        'comparison.price': 'Preis',
        'comparison.availability': 'Verfügbarkeit',
        'comparison.type': 'Produkttyp',
        'comparison.variants': 'Varianten',
        'comparison.features': 'Merkmale',
        'comparison.in_stock': 'Auf Lager',
        'comparison.out_of_stock': 'Nicht auf Lager',
        'comparison.view_product': 'Produkt ansehen',
        'comparison.remove': 'Entfernen'
      },
      fr: {
        'comparison.title': 'Comparaison de produits',
        'comparison.added': '{product} ajouté à la comparaison',
        'comparison.removed': 'Retiré de la comparaison',
        'comparison.cleared': 'Comparaison effacée',
        'comparison.max_reached': 'Maximum {max} produits peuvent être comparés',
        'comparison.min_required': 'Sélectionnez au moins 2 produits à comparer',
        'comparison.error_loading': 'Erreur de chargement du produit',
        'comparison.price': 'Prix',
        'comparison.availability': 'Disponibilité',
        'comparison.type': 'Type de produit',
        'comparison.variants': 'Variantes',
        'comparison.features': 'Caractéristiques',
        'comparison.in_stock': 'En stock',
        'comparison.out_of_stock': 'Rupture de stock',
        'comparison.view_product': 'Voir le produit',
        'comparison.remove': 'Retirer'
      }
    };

    let text = translations[lang]?.[key] || translations.en[key] || key;
    
    // Replace parameters
    Object.keys(params).forEach(param => {
      text = text.replace(`{${param}}`, params[param]);
    });

    return text;
  }
}

// Auto-initialize
document.addEventListener('DOMContentLoaded', () => {
  if (document.querySelector('[data-compare-bar]')) {
    window.productComparison = new ProductComparison();
  }
});
