/**
 * Cart JavaScript - AJAX cart updates and interactions
 * 
 * Features:
 * - AJAX cart quantity updates
 * - Add/remove items without page reload
 * - Free shipping progress bar updates
 * - Debounced quantity inputs
 * - Error handling with user feedback
 * 
 * Dependencies:
 * - Shopify Cart API
 * - debounce utility (inline)
 */

class Cart {
  constructor() {
    this.cartWrapper = document.querySelector('[data-cart-wrapper]');
    this.cartForm = document.querySelector('[data-cart-form]');
    this.cartItems = document.querySelector('[data-cart-items]');
    this.shippingBar = document.querySelector('[data-shipping-bar]');
    this.checkoutButton = document.querySelector('[data-checkout-button]');
    
    if (!this.cartWrapper) return;
    
    this.init();
  }

  init() {
    this.bindEvents();
    this.updateShippingProgress();
  }

  bindEvents() {
    // Quantity increase buttons
    const increaseButtons = this.cartWrapper.querySelectorAll('[data-qty-increase]');
    increaseButtons.forEach(button => {
      button.addEventListener('click', (e) => this.handleQuantityChange(e, 'increase'));
    });

    // Quantity decrease buttons
    const decreaseButtons = this.cartWrapper.querySelectorAll('[data-qty-decrease]');
    decreaseButtons.forEach(button => {
      button.addEventListener('click', (e) => this.handleQuantityChange(e, 'decrease'));
    });

    // Quantity inputs (with debounce)
    const qtyInputs = this.cartWrapper.querySelectorAll('[data-qty-input]');
    qtyInputs.forEach(input => {
      input.addEventListener('change', this.debounce((e) => {
        this.handleQuantityInput(e);
      }, 500));
    });

    // Remove buttons
    const removeButtons = this.cartWrapper.querySelectorAll('[data-remove-item]');
    removeButtons.forEach(button => {
      button.addEventListener('click', (e) => this.handleRemoveItem(e));
    });

    // Prevent default form submission
    if (this.cartForm) {
      this.cartForm.addEventListener('submit', (e) => {
        if (!e.submitter || e.submitter.name !== 'checkout') {
          e.preventDefault();
        }
      });
    }
  }

  /**
   * Handle quantity button clicks (+/-)
   */
  async handleQuantityChange(e, action) {
    const button = e.currentTarget;
    const index = button.dataset.index;
    const input = this.cartWrapper.querySelector(`[data-qty-input][data-index="${index}"]`);
    
    if (!input) return;

    const currentQty = parseInt(input.value);
    const newQty = action === 'increase' ? currentQty + 1 : Math.max(0, currentQty - 1);

    input.value = newQty;
    await this.updateCart(index, newQty);
  }

  /**
   * Handle manual quantity input changes
   */
  async handleQuantityInput(e) {
    const input = e.currentTarget;
    const index = input.dataset.index;
    const newQty = parseInt(input.value) || 0;

    await this.updateCart(index, newQty);
  }

  /**
   * Handle remove item button
   */
  async handleRemoveItem(e) {
    e.preventDefault();
    const button = e.currentTarget;
    const index = button.dataset.index;

    if (confirm(window.theme?.translations?.cart?.confirmRemove || 'Remove this item?')) {
      await this.updateCart(index, 0);
    }
  }

  /**
   * Update cart via AJAX
   */
  async updateCart(lineIndex, quantity) {
    try {
      this.setLoadingState(true, lineIndex);

      // Shopify Cart API update
      const response = await fetch('/cart/change.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          line: lineIndex,
          quantity: quantity
        })
      });

      if (!response.ok) {
        throw new Error('Failed to update cart');
      }

      const cart = await response.json();

      // If quantity is 0, remove the item from DOM
      if (quantity === 0) {
        this.removeItemFromDOM(lineIndex);
      }

      // Update cart totals
      this.updateCartTotals(cart);

      // Update shipping progress
      this.updateShippingProgress(cart);

      // If cart is now empty, reload page to show empty state
      if (cart.item_count === 0) {
        window.location.reload();
      }

    } catch (error) {
      console.error('Cart update error:', error);
      this.showError('Failed to update cart. Please try again.');
      
      // Reload page as fallback
      setTimeout(() => window.location.reload(), 2000);
    } finally {
      this.setLoadingState(false, lineIndex);
    }
  }

  /**
   * Remove item from DOM
   */
  removeItemFromDOM(lineIndex) {
    const item = this.cartWrapper.querySelector(`[data-cart-item][data-line-index="${lineIndex}"]`);
    if (item) {
      item.style.opacity = '0';
      item.style.transform = 'translateX(-20px)';
      setTimeout(() => item.remove(), 300);
    }
  }

  /**
   * Update cart totals in UI
   */
  updateCartTotals(cart) {
    const subtotalElement = document.querySelector('[data-cart-subtotal]');
    if (subtotalElement) {
      subtotalElement.textContent = this.formatMoney(cart.total_price);
    }

    // Update item count in header (if exists)
    const cartCountElements = document.querySelectorAll('[data-cart-count]');
    cartCountElements.forEach(el => {
      el.textContent = cart.item_count;
    });
  }

  /**
   * Update free shipping progress bar
   */
  updateShippingProgress(cart = null) {
    if (!this.shippingBar) return;

    const threshold = parseInt(this.shippingBar.dataset.threshold || 5000); // in cents
    const currentTotal = cart ? cart.total_price : this.getCurrentCartTotal();
    const remaining = Math.max(0, threshold - currentTotal);
    const progress = Math.min(100, (currentTotal / threshold) * 100);

    // Update progress bar
    const progressFill = this.shippingBar.querySelector('.cart__shipping-fill');
    if (progressFill) {
      progressFill.style.width = `${progress}%`;
    }

    // Update message
    const message = this.shippingBar.querySelector('.cart__shipping-message');
    if (message) {
      if (remaining > 0) {
        message.textContent = `Add ${this.formatMoney(remaining)} more for free shipping`;
        message.classList.remove('cart__shipping-message--success');
      } else {
        message.textContent = '🎉 You qualify for free shipping!';
        message.classList.add('cart__shipping-message--success');
      }
    }
  }

  /**
   * Get current cart total from DOM
   */
  getCurrentCartTotal() {
    const subtotalElement = document.querySelector('[data-cart-subtotal]');
    if (!subtotalElement) return 0;
    
    // Extract number from money string (e.g., "€123.45" -> 12345)
    const text = subtotalElement.textContent;
    const number = parseFloat(text.replace(/[^0-9,.]/g, '').replace(',', '.'));
    return Math.round(number * 100); // Convert to cents
  }

  /**
   * Set loading state on cart items
   */
  setLoadingState(isLoading, lineIndex = null) {
    if (lineIndex) {
      const item = this.cartWrapper.querySelector(`[data-cart-item][data-line-index="${lineIndex}"]`);
      if (item) {
        item.classList.toggle('cart-item--loading', isLoading);
      }
    }

    if (this.checkoutButton) {
      this.checkoutButton.classList.toggle('cart__checkout-button--loading', isLoading);
      this.checkoutButton.disabled = isLoading;
    }
  }

  /**
   * Show error message to user
   */
  showError(message) {
    // Simple alert for now - could be replaced with toast notification
    alert(message);
  }

  /**
   * Format money (simple version - Shopify's money filter is better)
   */
  formatMoney(cents) {
    const amount = (cents / 100).toFixed(2);
    return `€${amount}`;
  }

  /**
   * Debounce utility
   */
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }
}

// Initialize cart when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new Cart());
} else {
  new Cart();
}

/**
 * Export for use in other modules
 */
window.Cart = Cart;
