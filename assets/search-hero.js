/**
 * Search Hero JavaScript
 * Handles search functionality and clears old cached searches
 * Includes CRO/UI testing helpers
 */

(function() {
  'use strict';

  // CRO/UI Testing Helper - Check for debug mode
  const isDebugMode = window.location.search.includes('debug=true') || 
                      localStorage.getItem('emmso_debug') === 'true';

  function debugLog(message, data) {
    if (isDebugMode) {
      console.log(`[EMMSO Search Hero] ${message}`, data || '');
    }
  }

  // Clear old flooring-specific searches from localStorage
  function clearOldSearches() {
    const oldSearchTerms = [
      'laminate flooring',
      'vinyl planks', 
      'wood care',
      'tile adhesive',
      'stone sealer',
      'lithofin',
      'lithof',
      'asdf',
      'asd',
      'laminate',
      'vinyl',
      'lithofinin', // typos
      'laminaat'
    ];

    try {
      // AGGRESSIVE CLEAR - Just remove all searches for now
      localStorage.removeItem('recentSearches');
      localStorage.removeItem('recent_searches');
      localStorage.removeItem('searchHistory');
      localStorage.removeItem('search_history');
      
      debugLog('Aggressively cleared all search history');
      
      // Hide recent searches section
      setTimeout(() => {
        const recentSection = document.querySelector('[data-recent-searches]');
        if (recentSection) {
          recentSection.setAttribute('hidden', '');
          recentSection.style.display = 'none';
        }
        
        // Also hide the chips
        const recentChips = document.querySelectorAll('.search-suggestions__recent');
        recentChips.forEach(chip => {
          chip.setAttribute('hidden', '');
          chip.style.display = 'none';
        });
      }, 100);
      
    } catch (e) {
      console.error('[EMMSO] Error clearing old searches:', e);
    }
  }

  // CRO Testing: Add data attributes for tracking
  function initCROTracking() {
    // Add data attributes to trackable elements
    const heroSection = document.querySelector('.search-hero');
    const categoryPills = document.querySelectorAll('.category-pill');
    const searchInput = document.querySelector('.search-input');
    const trendingChips = document.querySelectorAll('.search-suggestion-chip');

    if (heroSection) {
      heroSection.setAttribute('data-cro-element', 'search-hero');
      debugLog('CRO tracking initialized on hero section');
    }

    categoryPills.forEach((pill, index) => {
      pill.setAttribute('data-cro-element', 'category-pill');
      pill.setAttribute('data-cro-category', pill.getAttribute('data-category'));
      pill.setAttribute('data-cro-index', index);
    });

    if (searchInput) {
      searchInput.setAttribute('data-cro-element', 'search-input');
    }

    trendingChips.forEach((chip, index) => {
      chip.setAttribute('data-cro-element', 'trending-chip');
      chip.setAttribute('data-cro-index', index);
    });

    debugLog(`CRO tracking: ${categoryPills.length} category pills, ${trendingChips.length} trending chips`);
  }

  // Run on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      clearOldSearches();
      initCROTracking();
    });
  } else {
    clearOldSearches();
    initCROTracking();
  }

  // Category pill click handlers
  document.addEventListener('DOMContentLoaded', function() {
    const categoryPills = document.querySelectorAll('.category-pill');
    const searchInput = document.querySelector('.search-input');

    categoryPills.forEach(pill => {
      pill.addEventListener('click', function() {
        const category = this.getAttribute('data-category');
        
        // CRO Tracking
        debugLog('Category pill clicked:', category);
        
        // Remove active class from all pills
        categoryPills.forEach(p => p.classList.remove('is-active'));
        
        // Add active class to clicked pill
        this.classList.add('is-active');
        
        // Optionally populate search input
        if (searchInput && category) {
          searchInput.value = this.textContent.trim();
          searchInput.focus();
        }

        // Fire custom event for external tracking (GTM, analytics, etc.)
        window.dispatchEvent(new CustomEvent('emmso:category-selected', {
          detail: { category, element: this }
        }));
      });
    });

    // Suggestion chip click handlers
    const suggestionChips = document.querySelectorAll('.search-suggestion-chip');
    suggestionChips.forEach(chip => {
      chip.addEventListener('click', function(e) {
        e.preventDefault();
        const suggestion = this.getAttribute('data-suggestion');
        
        debugLog('Suggestion chip clicked:', suggestion);
        
        if (searchInput && suggestion) {
          searchInput.value = suggestion;
          searchInput.focus();
          
          // Fire custom event
          window.dispatchEvent(new CustomEvent('emmso:suggestion-selected', {
            detail: { suggestion, element: this }
          }));
          
          // Optionally trigger search
          const searchForm = searchInput.closest('form');
          if (searchForm) {
            searchForm.submit();
          }
        }
      });
    });

    // Search input tracking
    if (searchInput) {
      searchInput.addEventListener('focus', function() {
        debugLog('Search input focused');
        window.dispatchEvent(new CustomEvent('emmso:search-focused'));
      });
    }
  });

  // Expose debug helper globally
  window.EMMSO = window.EMMSO || {};
  window.EMMSO.enableDebug = function() {
    localStorage.setItem('emmso_debug', 'true');
    location.reload();
  };
  window.EMMSO.disableDebug = function() {
    localStorage.removeItem('emmso_debug');
    location.reload();
  };
  window.EMMSO.clearAllSearches = function() {
    localStorage.removeItem('recentSearches');
    debugLog('All searches cleared manually');
    location.reload();
  };

  if (isDebugMode) {
    console.log('[EMMSO] Debug mode enabled. Available commands:');
    console.log('  EMMSO.disableDebug() - Turn off debug mode');
    console.log('  EMMSO.clearAllSearches() - Clear all search history');
  } else {
    console.log('[EMMSO] Run EMMSO.enableDebug() to see detailed logs');
  }

})();
