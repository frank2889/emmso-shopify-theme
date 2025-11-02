/**
 * Search Engine - Ultra-fast predictive search
 * Performance optimized with debouncing, caching, and progressive enhancement
 */

class SearchEngine {
  constructor() {
    this.input = document.querySelector('[data-predictive-search-input]');
    this.results = document.querySelector('[data-predictive-search-results]');
    this.resultsContainer = document.querySelector('[data-search-results-container]');
    this.loading = document.querySelector('[data-search-loading]');
    this.footer = document.querySelector('[data-search-footer]');
    this.clearBtn = document.querySelector('[data-search-clear]');
    this.voiceBtn = document.querySelector('[data-voice-search-button]');
    this.viewAllLink = document.querySelector('[data-search-view-all]');
    
    this.cache = new Map();
    this.recentSearches = this.loadRecentSearches();
    this.debounceTimer = null;
    this.abortController = null;
    
    // Initialize search intelligence
    this.intelligence = window.SearchIntelligence ? new window.SearchIntelligence() : null;
    
    this.init();
  }

  init() {
    if (!this.input) return;

    // Input events
    this.input.addEventListener('input', this.handleInput.bind(this));
    this.input.addEventListener('focus', this.handleFocus.bind(this));
    this.input.addEventListener('keydown', this.handleKeydown.bind(this));
    
    // Clear button
    if (this.clearBtn) {
      this.clearBtn.addEventListener('click', this.clearSearch.bind(this));
    }

    // Voice search
    if (this.voiceBtn && 'webkitSpeechRecognition' in window) {
      this.voiceBtn.addEventListener('click', this.handleVoiceSearch.bind(this));
    } else if (this.voiceBtn) {
      this.voiceBtn.style.display = 'none';
    }

    // Suggestion chips
    document.querySelectorAll('[data-suggestion]').forEach(chip => {
      chip.addEventListener('click', () => {
        this.input.value = chip.dataset.suggestion;
        this.performSearch(chip.dataset.suggestion);
      });
    });

    // Close results on outside click
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-form')) {
        this.hideResults();
      }
    });

    // Show recent searches on focus
    this.showRecentSearches();
  }

  handleInput(e) {
    const query = e.target.value.trim();
    
    // Toggle clear button
    if (this.clearBtn) {
      this.clearBtn.hidden = query.length === 0;
    }

    // Debounce search
    clearTimeout(this.debounceTimer);
    
    if (query.length < 2) {
      this.hideResults();
      this.showRecentSearches();
      return;
    }

    this.debounceTimer = setTimeout(() => {
      this.performSearch(query);
    }, 150); // 150ms debounce for optimal UX
  }

  handleFocus() {
    if (this.input.value.trim().length === 0) {
      this.showRecentSearches();
    }
  }

  handleKeydown(e) {
    // Escape key closes results
    if (e.key === 'Escape') {
      this.hideResults();
      this.input.blur();
    }
  }

  async performSearch(query) {
    // Analyze query with intelligence module
    const analysis = this.intelligence ? this.intelligence.analyzeQuery(query) : null;
    
    if (analysis) {
      console.log('Search Analysis:', analysis);
      
      // Log insights
      if (analysis.intent !== 'search') {
        console.log(`Detected intent: ${analysis.intent}`);
      }
      if (analysis.room) {
        console.log(`Room context: ${analysis.room}`);
      }
      if (analysis.characteristics.length > 0) {
        console.log(`Characteristics: ${analysis.characteristics.join(', ')}`);
      }
      if (analysis.synonyms.length > 1) {
        console.log(`Expanded to ${analysis.synonyms.length} synonym variations (multilingual)`);
      }
    }

    // Check cache first
    if (this.cache.has(query)) {
      this.displayResults(this.cache.get(query), query, analysis);
      return;
    }

    // Cancel previous request
    if (this.abortController) {
      this.abortController.abort();
    }
    this.abortController = new AbortController();

    // Show loading state
    this.showLoading();

    try {
      const startTime = performance.now();
      
      // Get all query variations for multilingual search
      const queryVariations = this.intelligence ? 
        this.intelligence.getQueryVariations(query) : 
        [query];
      
      console.log(`Searching with ${queryVariations.length} variations:`, queryVariations);
      
      // Perform searches for all variations (multilingual support)
      const searchPromises = queryVariations.slice(0, 3).map(searchQuery => 
        fetch(
          `/search/suggest.json?q=${encodeURIComponent(searchQuery)}&resources[type]=product&resources[limit]=12&resources[options][unavailable_products]=last&resources[options][fields]=title,vendor,product_type,tag,variants.title`,
          { signal: this.abortController.signal }
        ).then(res => res.ok ? res.json() : null)
      );

      // Wait for all searches to complete
      const results = await Promise.all(searchPromises);
      
      // Merge and deduplicate results
      const allProducts = new Map();
      results.forEach(data => {
        if (data?.resources?.results?.products) {
          data.resources.results.products.forEach(product => {
            // Deduplicate by product ID or handle
            const key = product.id || product.handle;
            if (!allProducts.has(key)) {
              allProducts.set(key, product);
            }
          });
        }
      });

      // Convert back to array
      const mergedProducts = Array.from(allProducts.values());
      
      const endTime = performance.now();
      console.log(`Multilingual search completed in ${(endTime - startTime).toFixed(2)}ms - Found ${mergedProducts.length} unique products`);

      // Create merged response
      const data = {
        resources: {
          results: {
            products: mergedProducts
          }
        }
      };

      // Enhance results with intelligence ranking
      if (this.intelligence && data.resources?.results?.products) {
        data.resources.results.products = this.intelligence.rankResults(
          data.resources.results.products,
          query,
          analysis
        );
      }

      // Cache results
      this.cache.set(query, data);
      
      // Limit cache size
      if (this.cache.size > 50) {
        const firstKey = this.cache.keys().next().value;
        this.cache.delete(firstKey);
      }

      this.displayResults(data, query, analysis);
      this.saveRecentSearch(query);

    } catch (error) {
      if (error.name === 'AbortError') return;
      console.error('Search error:', error);
      this.showError();
    } finally {
      this.hideLoading();
    }
  }

  displayResults(data, query, analysis = null) {
    const products = data.resources.results.products || [];
    
    if (products.length === 0) {
      this.showNoResults(query, analysis);
      return;
    }

    let html = '';

    // Show smart insights banner if available
    if (analysis && this.intelligence) {
      const suggestions = this.intelligence.generateSmartSuggestions(query, analysis);
      if (suggestions.length > 0) {
        html += '<div class="search-insights">';
        suggestions.slice(0, 2).forEach(suggestion => {
          html += `
            <a href="${suggestion.action}" class="search-insight-chip">
              <span class="search-insight-icon">💡</span>
              ${this.escapeHtml(suggestion.text)}
            </a>
          `;
        });
        html += '</div>';
      }

      // Show detected context
      if (analysis.room || analysis.characteristics.length > 0 || analysis.brands.length > 0) {
        html += '<div class="search-context">';
        html += '<p class="search-context__label">Searching for:</p>';
        html += '<div class="search-context__tags">';
        
        if (analysis.room) {
          html += `<span class="context-tag">${analysis.room} flooring</span>`;
        }
        if (analysis.brands.length > 0) {
          analysis.brands.forEach(brand => {
            html += `<span class="context-tag">${this.escapeHtml(brand)}</span>`;
          });
        }
        if (analysis.characteristics.length > 0) {
          analysis.characteristics.forEach(char => {
            html += `<span class="context-tag">${char.replace(/-/g, ' ')}</span>`;
          });
        }
        
        html += '</div></div>';
      }
    }

    html += '<div class="search-results__products">';
    
    products.slice(0, 6).forEach(product => {
      const image = product.image || product.featured_image;
      const price = this.formatPrice(product.price);
      const comparePrice = product.compare_at_price ? this.formatPrice(product.compare_at_price) : null;
      const available = product.available;
      const relevanceScore = product.relevanceScore || 0;

      html += `
        <a href="${product.url}" class="search-result-item" ${relevanceScore > 0 ? `data-score="${relevanceScore}"` : ''}>
          <div class="search-result-item__image">
            ${image ? `
              <img 
                src="${image}" 
                alt="${this.escapeHtml(product.title)}"
                loading="lazy"
                width="80"
                height="80"
              >
            ` : `
              <div class="search-result-item__placeholder"></div>
            `}
            ${relevanceScore >= 100 ? '<span class="search-result-item__match-badge">Best Match</span>' : ''}
          </div>
          <div class="search-result-item__details">
            <h3 class="search-result-item__title">${this.highlightQuery(product.title, query)}</h3>
            ${product.vendor ? `<p class="search-result-item__vendor">${this.escapeHtml(product.vendor)}</p>` : ''}
            <div class="search-result-item__price">
              ${comparePrice ? `<span class="search-result-item__compare-price">${comparePrice}</span>` : ''}
              <span class="search-result-item__final-price ${comparePrice ? 'on-sale' : ''}">${price}</span>
            </div>
            ${!available ? '<span class="search-result-item__badge badge-out-of-stock">Out of Stock</span>' : ''}
          </div>
        </a>
      `;
    });

    html += '</div>';

    this.resultsContainer.innerHTML = html;
    this.showResults();
    
    // Update view all link
    if (this.viewAllLink) {
      this.viewAllLink.href = `/search?q=${encodeURIComponent(query)}`;
      this.viewAllLink.textContent = `View all ${products.length} results`;
      this.footer.hidden = false;
    }
  }

  showNoResults(query, analysis = null) {
    const suggestions = this.generateSuggestions(query);
    let smartSuggestions = [];
    
    if (analysis && this.intelligence) {
      smartSuggestions = this.intelligence.generateSmartSuggestions(query, analysis);
    }
    
    this.resultsContainer.innerHTML = `
      <div class="search-no-results">
        <h3>No results found for "${this.escapeHtml(query)}"</h3>
        
        ${suggestions.length > 0 ? `
          <p>Did you mean:</p>
          <ul class="search-suggestions-list">
            ${suggestions.map(s => `
              <li>
                <button type="button" class="search-suggestion-link" data-suggestion="${s}">
                  ${this.escapeHtml(s)}
                </button>
              </li>
            `).join('')}
          </ul>
        ` : ''}
        
        ${smartSuggestions.length > 0 ? `
          <div class="search-alternatives">
            <p>Try these instead:</p>
            ${smartSuggestions.map(s => `
              <a href="${s.action}" class="search-alternative-link">
                ${this.escapeHtml(s.text)}
              </a>
            `).join('')}
          </div>
        ` : `
          <p>Try different keywords or <a href="/collections/all">browse all products</a></p>
        `}
        
        ${analysis && analysis.isQuestion ? `
          <div class="search-help-tip">
            <p>💡 Looking for help? Visit our <a href="/pages/learning-center">Learning Center</a> for guides and tutorials</p>
          </div>
        ` : ''}
      </div>
    `;

    // Add event listeners to suggestion links
    this.resultsContainer.querySelectorAll('[data-suggestion]').forEach(link => {
      link.addEventListener('click', () => {
        this.input.value = link.dataset.suggestion;
        this.performSearch(link.dataset.suggestion);
      });
    });

    this.showResults();
  }

  showLoading() {
    if (this.loading) {
      this.loading.hidden = false;
    }
  }

  hideLoading() {
    if (this.loading) {
      this.loading.hidden = true;
    }
  }

  showResults() {
    if (this.results) {
      this.results.hidden = false;
    }
  }

  hideResults() {
    if (this.results) {
      this.results.hidden = true;
    }
    if (this.footer) {
      this.footer.hidden = true;
    }
  }

  showError() {
    this.resultsContainer.innerHTML = `
      <div class="search-error">
        <p>Something went wrong. Please try again.</p>
      </div>
    `;
    this.showResults();
  }

  clearSearch() {
    this.input.value = '';
    this.input.focus();
    this.hideResults();
    this.showRecentSearches();
    if (this.clearBtn) {
      this.clearBtn.hidden = true;
    }
  }

  handleVoiceSearch() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = document.documentElement.lang || 'en-US';
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      this.input.value = transcript;
      this.performSearch(transcript);
    };

    recognition.onerror = (event) => {
      console.error('Voice search error:', event.error);
    };

    recognition.start();
  }

  // Recent searches management
  loadRecentSearches() {
    try {
      const stored = localStorage.getItem('emmso_recent_searches');
      return stored ? JSON.parse(stored) : [];
    } catch (e) {
      return [];
    }
  }

  saveRecentSearch(query) {
    if (!query || query.length < 2) return;
    
    // Remove if already exists
    this.recentSearches = this.recentSearches.filter(s => s !== query);
    
    // Add to beginning
    this.recentSearches.unshift(query);
    
    // Keep only last 5
    this.recentSearches = this.recentSearches.slice(0, 5);
    
    try {
      localStorage.setItem('emmso_recent_searches', JSON.stringify(this.recentSearches));
    } catch (e) {
      console.warn('Could not save recent searches');
    }
  }

  showRecentSearches() {
    const container = document.querySelector('[data-recent-searches]');
    const list = document.querySelector('[data-recent-list]');
    
    if (!container || !list || this.recentSearches.length === 0) return;

    list.innerHTML = this.recentSearches.map(search => `
      <li>
        <button type="button" class="search-suggestion-chip" data-suggestion="${search}">
          ${this.escapeHtml(search)}
        </button>
      </li>
    `).join('');

    // Add click handlers
    list.querySelectorAll('[data-suggestion]').forEach(chip => {
      chip.addEventListener('click', () => {
        this.input.value = chip.dataset.suggestion;
        this.performSearch(chip.dataset.suggestion);
      });
    });

    container.hidden = false;
  }

  // Utility functions
  formatPrice(cents) {
    const amount = cents / 100;
    return new Intl.NumberFormat(document.documentElement.lang || 'en-US', {
      style: 'currency',
      currency: window.Shopify?.currency?.active || 'EUR'
    }).format(amount);
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  highlightQuery(text, query) {
    const regex = new RegExp(`(${query})`, 'gi');
    return this.escapeHtml(text).replace(regex, '<mark>$1</mark>');
  }

  generateSuggestions(query) {
    // Enhanced with Levenshtein distance
    const commonTerms = [
      'laminate', 'vinyl', 'wood', 'floor', 'flooring', 'care', 'adhesive', 
      'sealer', 'cleaner', 'maintenance', 'parquet', 'tile', 'stone', 'oak',
      'walnut', 'herringbone', 'planks', 'protection', 'finish', 'oil'
    ];
    
    return commonTerms
      .map(term => ({
        term,
        distance: this.levenshteinDistance(query.toLowerCase(), term.toLowerCase())
      }))
      .filter(item => item.distance <= 3) // Max 3 character difference
      .sort((a, b) => a.distance - b.distance)
      .slice(0, 3)
      .map(item => item.term);
  }

  // Levenshtein distance for fuzzy matching
  levenshteinDistance(str1, str2) {
    const matrix = [];

    for (let i = 0; i <= str2.length; i++) {
      matrix[i] = [i];
    }

    for (let j = 0; j <= str1.length; j++) {
      matrix[0][j] = j;
    }

    for (let i = 1; i <= str2.length; i++) {
      for (let j = 1; j <= str1.length; j++) {
        if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
          matrix[i][j] = matrix[i - 1][j - 1];
        } else {
          matrix[i][j] = Math.min(
            matrix[i - 1][j - 1] + 1, // substitution
            matrix[i][j - 1] + 1,     // insertion
            matrix[i - 1][j] + 1      // deletion
          );
        }
      }
    }

    return matrix[str2.length][str1.length];
  }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new SearchEngine();
  });
} else {
  new SearchEngine();
}

// Performance monitoring
if (window.PerformanceObserver) {
  const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
      if (entry.name.includes('search/suggest')) {
        console.log(`Search API: ${entry.duration.toFixed(2)}ms`);
      }
    }
  });
  observer.observe({ entryTypes: ['resource'] });
}
