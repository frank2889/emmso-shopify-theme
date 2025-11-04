"""
Shopify Expert Knowledge Base - Complete Shopify.dev Certification
================================================================
Everything needed to build professional Shopify themes (2025).
Based on official Shopify.dev documentation.
"""

LIQUID_COMPLETE = """
Shopify Liquid - Complete Template Language (2025):

OBJECTS:
{{ product.title }} {{ product.price | money }} {{ product.available }}
{{ collection.products }} {{ cart.items }} {{ cart.total_price }}
{{ customer.email }} {{ shop.name }} {{ settings.color_primary }}

TAGS:
{% if product.available %}...{% endif %}
{% for item in cart.items %}...{% endfor %}
{% assign price = product.price | divided_by: 100.0 %}
{% render 'snippet', product: product %}

FILTERS:
{{ 'text' | upcase | truncate: 10 }}
{{ 1999 | money }} → $19.99
{{ product.images | first | image_url: width: 600 }}
{{ array | where: 'available' | sort: 'price' }}

LIQUID VALIDATION RULES (CRITICAL):
================================

1. COMMENT TAG SYNTAX:
   ❌ WRONG: comment text endcomment (missing {% %})
   ✅ CORRECT: {% comment %}text{% endcomment %}
   ✅ CORRECT: {%- comment -%}text{%- endcomment -%}
   
2. LIQUID TAG SYNTAX:
   ❌ WRONG: {% liquid assign x = 5 endliquid %}
   ✅ CORRECT: {% liquid
                 assign x = 5
               %}
   - Inside {% liquid %} blocks, use # for comments (NOT comment tag)
   - Example: {% liquid
                # This is a comment
                assign price = 100
              %}

3. ALL TAGS MUST BE PROPERLY CLOSED:
   - {% if %} requires {% endif %}
   - {% for %} requires {% endfor %}
   - {% comment %} requires {% endcomment %}
   - {% liquid %} requires %} (on separate line)
   - {% schema %} requires {% endschema %}
   
4. WHITESPACE CONTROL:
   - Use {%- -%} to strip whitespace
   - Example: {%- if condition -%}...{%- endif -%}
   
5. COMMON VALIDATION ERRORS:
   - Missing endcomment, endif, endfor, endschema
   - Using 'comment' without {% %} tags inside {% liquid %} blocks
   - Unclosed quotes in strings
   - Missing | pipe before filters
   - Wrong filter syntax

6. SHOPIFY THEME CHECK:
   - Run 'shopify theme check' before deploying
   - Fix all syntax errors (line number shown in error)
   - All templates must pass validation
"""

ONLINE_STORE_2_0 = """
Online Store 2.0 Architecture:

JSON TEMPLATES:
{
  "sections": {
    "main": { "type": "main-product" }
  },
  "order": ["main"]
}

SECTION SCHEMA:
{% schema %}
{
  "name": "Product Section",
  "settings": [
    { "type": "text", "id": "title", "label": "Title" },
    { "type": "color", "id": "bg_color", "label": "Background" }
  ],
  "blocks": [
    { "type": "text", "name": "Text Block" }
  ]
}
{% endschema %}

APP BLOCKS: Enable app integrations in theme editor
"""

SHOPIFY_AJAX = """
Shopify AJAX Cart API:

ADD TO CART:
fetch('/cart/add.js', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ items: [{ id: variantId, quantity: 1 }] })
})

GET CART:
fetch('/cart.js').then(r => r.json())

UPDATE:
fetch('/cart/update.js', {
  method: 'POST',
  body: JSON.stringify({ updates: { [variantId]: quantity } })
})
"""

THEME_ARCHITECTURE = """
Shopify Theme Structure:

/sections/ - Modular components (header, product, collection)
/snippets/ - Reusable elements (product-card, icon)
/templates/ - Page types (product.json, collection.json)
/layout/ - Overall structure (theme.liquid)
/assets/ - CSS, JS, images
/config/ - Theme settings (settings_schema.json)
/locales/ - Translations (en.default.json)

BEST PRACTICES:
- Use {% render %} for snippets (isolated scope)
- Section settings > hardcoded values
- Minimize Liquid logic
- Lazy load images
"""

PERFORMANCE_OPTIMIZATION = """
Shopify Performance Best Practices:

IMAGES:
- Modern formats: AVIF > WebP > JPEG
- Responsive: {{ image | image_url: width: 600 }}
- Lazy loading: loading="lazy"
- CDN: Shopify serves from global CDN

JAVASCRIPT:
- Defer non-critical JS
- Code splitting
- Minimize Liquid in JS
- Use Shopify AJAX API

CSS:
- Critical CSS inline
- Defer non-critical
- Remove unused CSS
- Use CSS custom properties

LIQUID:
- Limit nested loops
- Use {% render %} not {% include %}
- Cache expensive operations
- Avoid in templates
"""

SHOPIFY_SEO = """
Shopify SEO Essentials:

PRODUCT SEO:
- Unique descriptions (150+ words)
- Structured data (automatic)
- Alt text for images
- Clean URLs (/products/handle)

STRUCTURED DATA:
Shopify auto-generates:
- Product schema (price, availability)
- BreadcrumbList
- Organization

Manual additions:
{% schema %}
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{ product.title }}",
  "offers": {
    "@type": "Offer",
    "price": "{{ product.price | divided_by: 100.0 }}",
    "priceCurrency": "{{ shop.currency }}"
  }
}
{% endschema %}

CANONICALS:
{{ canonical_url }} - Auto-generated
"""

METAFIELDS = """
Shopify Metafields (Custom Data):

ACCESS IN LIQUID:
{{ product.metafields.custom.field_name }}
{{ product.metafields.namespace.key }}

DEFINITION (Admin):
- Name: "Special Instructions"
- Namespace: "custom"
- Key: "instructions"
- Type: single_line_text, number, color, etc.

EXAMPLE:
{% if product.metafields.custom.care_instructions %}
  <p>{{ product.metafields.custom.care_instructions }}</p>
{% endif %}
"""

SHOPIFY_CLI = """
Shopify CLI - Theme Development:

SETUP:
npm install -g @shopify/cli @shopify/theme

COMMANDS:
shopify theme dev - Local development server
shopify theme push - Deploy to store
shopify theme pull - Download from store
shopify theme check - Lint theme files

WORKFLOW:
1. shopify theme dev
2. Make changes locally
3. Preview at localhost
4. shopify theme push
"""

CONVERSION_BEST_PRACTICES = """
Shopify Conversion Optimization:

PRODUCT PAGES:
✓ Clear Add to Cart (48px touch targets)
✓ High-quality images (zoom, multiple angles)
✓ Customer reviews
✓ Trust badges
✓ Related products
✓ Clear pricing (compare_at_price for sales)

CART:
✓ AJAX cart (no page reload)
✓ Cart drawer (quick view)
✓ Upsells
✓ Free shipping threshold
✓ Easy to edit quantities

CHECKOUT:
✓ Guest checkout
✓ Multiple payment methods (Shop Pay, Apple Pay)
✓ Trust signals
✓ Mobile-optimized (80%+ mobile traffic)

COLLECTION PAGES:
✓ Add to Cart on collection pages
✓ Quick view modals
✓ Filters (price, size, color)
✓ Sort options
"""


def get_recommendation(topic, context=None):
    """Generate Shopify recommendations"""
    recs = {
        'ajax_cart': [
            'Implement AJAX Add to Cart with /cart/add.js',
            'Show cart drawer instead of page redirect',
            'Update cart count in real-time',
            'Add loading states and success feedback'
        ],
        'performance': [
            'Use modern image formats (AVIF/WebP)',
            'Lazy load below-fold images',
            'Defer non-critical JavaScript',
            'Minimize Liquid logic in templates'
        ],
        'seo': [
            'Write unique product descriptions (150+ words)',
            'Optimize product images (alt text, file names)',
            'Use Shopify auto-generated structured data',
            'Add metafields for rich product data'
        ],
        'conversion': [
            'Add prominent Add to Cart buttons (48px)',
            'Show customer reviews on product pages',
            'Implement cart upsells',
            'Add trust badges near checkout'
        ]
    }
    return recs.get(topic, [])


def get_expert_knowledge():
    """Returns complete Shopify expert knowledge"""
    return "\n\n".join([
        "SHOPIFY EXPERT KNOWLEDGE BASE - SHOPIFY.DEV CERTIFICATION",
        "=" * 80,
        LIQUID_COMPLETE,
        ONLINE_STORE_2_0,
        SHOPIFY_AJAX,
        THEME_ARCHITECTURE,
        PERFORMANCE_OPTIMIZATION,
        SHOPIFY_SEO,
        METAFIELDS,
        SHOPIFY_CLI,
        CONVERSION_BEST_PRACTICES
    ])
