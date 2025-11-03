"""
Shopify & E-commerce Expert Knowledge Base
Centralized Shopify expertise for Alex (and other analysts who need Shopify knowledge)
"""

LIQUID_BEST_PRACTICES = """
Shopify Liquid Best Practices:

1. Performance:
   - Minimize Liquid logic in templates
   - Use section settings instead of hardcoded values
   - Limit nested loops
   - Use {% render %} for snippets (isolated scope)

2. Theme Architecture:
   - sections/ for modular components
   - snippets/ for reusable elements
   - templates/ for page types
   - layout/ for overall structure

3. Online Store 2.0:
   - JSON templates for flexibility
   - Section groups for header/footer
   - App blocks support
   - Metaobjects for custom data
"""

SHOPIFY_AJAX = """
Shopify AJAX Cart API:

1. Add to Cart:
   POST /cart/add.js
   Body: { items: [{ id: variant_id, quantity: 1 }] }

2. Update Cart:
   POST /cart/update.js
   Body: { updates: { variant_id: quantity } }

3. Get Cart:
   GET /cart.js
   Returns: Full cart object with items, total, etc.

4. Change Cart:
   POST /cart/change.js
   Body: { id: variant_id, quantity: new_quantity }
"""

SHOPIFY_SEO = """
Shopify SEO Best Practices:

1. Product SEO:
   - Unique product descriptions
   - Optimize product titles (include keywords)
   - Use alt text for product images
   - Add product metafields for rich data

2. Collection SEO:
   - Write unique collection descriptions
   - Use SEO-friendly URLs
   - Implement breadcrumbs
   - Add canonical tags

3. Structured Data:
   - Product schema (price, availability, reviews)
   - BreadcrumbList for navigation
   - Organization schema in footer
   - Use Shopify's built-in schema.org support
"""

CONVERSION_OPTIMIZATION = """
Shopify Conversion Best Practices:

1. Product Pages:
   - Clear Add to Cart buttons
   - High-quality product images
   - Customer reviews
   - Trust badges
   - Related products

2. Cart Experience:
   - AJAX cart (no page reload)
   - Upsells in cart
   - Free shipping threshold
   - Exit intent for abandoned carts

3. Checkout:
   - Guest checkout option
   - Multiple payment methods
   - Trust signals
   - Mobile-optimized
"""

def get_recommendation(topic, context):
    """
    Generate Shopify recommendation based on topic and context
    """
    recommendations = {
        'ajax_cart': [
            'Implement AJAX Add to Cart with /cart/add.js',
            'Show cart drawer instead of cart page redirect',
            'Update cart count badge in real-time',
            'Add visual feedback (loading states, success messages)'
        ],
        'product_seo': [
            'Write unique product descriptions (min 150 words)',
            'Add structured data for products',
            'Optimize product images (alt text, file names)',
            'Use descriptive product URLs'
        ],
        'performance': [
            'Minimize Liquid logic in templates',
            'Use section settings for flexibility',
            'Optimize images (AVIF/WebP formats)',
            'Lazy load below-fold content'
        ],
        'conversion': [
            'Add prominent Add to Cart buttons',
            'Show customer reviews',
            'Implement upsells in cart',
            'Add trust badges near checkout'
        ]
    }
    
    return recommendations.get(topic, [])
