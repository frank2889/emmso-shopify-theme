/**
 * Search Hero JavaScript
 * Handles search functionality and clears old cached searches
 */

(function() {
  'use strict';

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
      'asd'
    ];

    try {
      // Get existing recent searches
      const recentSearches = JSON.parse(localStorage.getItem('recentSearches') || '[]');
      
      // Filter out old flooring-specific terms
      const filteredSearches = recentSearches.filter(term => {
        const lowerTerm = term.toLowerCase();
        return !oldSearchTerms.some(oldTerm => lowerTerm.includes(oldTerm.toLowerCase()));
      });

      // Save cleaned searches back
      if (filteredSearches.length !== recentSearches.length) {
        localStorage.setItem('recentSearches', JSON.stringify(filteredSearches));
        console.log('Cleared old flooring-specific searches');
      }
    } catch (e) {
      console.error('Error clearing old searches:', e);
    }
  }

  // Run on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', clearOldSearches);
  } else {
    clearOldSearches();
  }

  // Category pill click handlers
  document.addEventListener('DOMContentLoaded', function() {
    const categoryPills = document.querySelectorAll('.category-pill');
    const searchInput = document.querySelector('.search-input');

    categoryPills.forEach(pill => {
      pill.addEventListener('click', function() {
        const category = this.getAttribute('data-category');
        
        // Remove active class from all pills
        categoryPills.forEach(p => p.classList.remove('is-active'));
        
        // Add active class to clicked pill
        this.classList.add('is-active');
        
        // Optionally populate search input
        if (searchInput && category) {
          searchInput.value = this.textContent.trim();
          searchInput.focus();
        }
      });
    });

    // Suggestion chip click handlers
    const suggestionChips = document.querySelectorAll('.search-suggestion-chip');
    suggestionChips.forEach(chip => {
      chip.addEventListener('click', function(e) {
        e.preventDefault();
        const suggestion = this.getAttribute('data-suggestion');
        
        if (searchInput && suggestion) {
          searchInput.value = suggestion;
          searchInput.focus();
          
          // Optionally trigger search
          const searchForm = searchInput.closest('form');
          if (searchForm) {
            searchForm.submit();
          }
        }
      });
    });
  });

})();
