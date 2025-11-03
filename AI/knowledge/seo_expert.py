"""
SEO Expert Knowledge Base - Complete Google Certification Knowledge
==================================================================
Everything needed to pass: Google SEO Certification, Google Analytics, 
Google Search Console, and perform professional SEO audits.

Based on: Google Search Central, Google Analytics Academy, Search Quality Guidelines
"""

# ============================================================================
# GOOGLE SEARCH ESSENTIALS (formerly Webmaster Guidelines)
# ============================================================================

GOOGLE_SEARCH_ESSENTIALS = """
Google's Core Ranking Factors (2025):

1. CONTENT QUALITY (Most Important):
   - Helpful, reliable, people-first content
   - E-E-A-T: Experience, Expertise, Authoritativeness, Trustworthiness
   - Original, comprehensive information
   - Answer user intent fully
   - Regular updates to keep content fresh

2. MOBILE-FIRST INDEXING:
   - Google uses MOBILE version for ranking
   - Responsive design required
   - Fast mobile page speed (<2.5s LCP)
   - Touch-friendly navigation (48px targets)
   - No intrusive interstitials

3. CORE WEB VITALS (Page Experience):
   - LCP (Largest Contentful Paint): <2.5s
   - INP (Interaction to Next Paint): <200ms  
   - CLS (Cumulative Layout Shift): <0.1
   - HTTPS required (security)
   - No intrusive popups

4. BACKLINK QUALITY:
   - Natural, editorial links
   - Relevant, authoritative sources
   - Diverse anchor text
   - Avoid link schemes/buying links

5. TECHNICAL SEO:
   - Crawlability (robots.txt, sitemap)
   - Indexability (no noindex on important pages)
   - Site structure (logical hierarchy)
   - Internal linking
   - Canonical URLs
"""

# ============================================================================
# CORE WEB VITALS - Complete Technical Guide
# ============================================================================

CORE_WEB_VITALS = """
Core Web Vitals - Official Google Ranking Signals:

1. LCP (Largest Contentful Paint):
   Definition: Time to render largest content element
   Thresholds:
   - Good: <2.5 seconds (GREEN)
   - Needs Improvement: 2.5-4 seconds (YELLOW)
   - Poor: >4 seconds (RED)
   
   How to Optimize:
   - Optimize server response time (TTFB <600ms)
   - Remove render-blocking resources
   - Optimize images (modern formats, compression, CDN)
   - Preload critical resources
   - Use content delivery network (CDN)
   
   Measurement:
   - Chrome User Experience Report (CrUX)
   - PageSpeed Insights
   - Google Search Console (Core Web Vitals report)

2. INP (Interaction to Next Paint):
   Definition: Response time to user interactions
   Thresholds:
   - Good: <200 milliseconds
   - Needs Improvement: 200-500ms
   - Poor: >500ms
   
   How to Optimize:
   - Break up long JavaScript tasks (>50ms)
   - Defer unused JavaScript
   - Use web workers for heavy computation
   - Optimize event handlers
   - Reduce third-party script impact

3. CLS (Cumulative Layout Shift):
   Definition: Visual stability, unexpected layout shifts
   Thresholds:
   - Good: <0.1
   - Needs Improvement: 0.1-0.25
   - Poor: >0.25
   
   How to Optimize:
   - Set explicit width/height on images and videos
   - Reserve space for ads/embeds
   - Don't insert content above existing content
   - Use transform animations (not top/left/width/height)
   - Preload fonts to avoid FOIT/FOUT

Field Data vs Lab Data:
- Field Data (Real users): Chrome User Experience Report (CrUX)
- Lab Data (Simulated): Lighthouse, PageSpeed Insights
- Both matter: Field data for ranking, Lab data for debugging
"""

# ============================================================================
# GOOGLE SEARCH CONSOLE - Complete Guide
# ============================================================================

GOOGLE_SEARCH_CONSOLE = """
Google Search Console - Essential SEO Tool:

1. PERFORMANCE REPORT:
   Metrics:
   - Total Clicks: Actual visits from Google
   - Total Impressions: Times shown in search results
   - Average CTR: Click-through rate (Clicks / Impressions)
   - Average Position: Where you rank on average
   
   Use Cases:
   - Find top performing pages
   - Identify keywords you rank for
   - Discover ranking opportunities (high impressions, low clicks)
   - Track ranking changes over time

2. COVERAGE REPORT (INDEX):
   Status Types:
   - Valid: Pages successfully indexed
   - Valid with warnings: Indexed but have issues
   - Error: Pages not indexed due to problems
   - Excluded: Intentionally not indexed
   
   Common Issues:
   - 404 errors (page not found)
   - Server errors (5xx)
   - Redirect errors
   - Noindex tag blocking indexing
   - Robots.txt blocking

3. CORE WEB VITALS REPORT:
   - Shows real user performance data (CrUX)
   - Mobile and Desktop data separate
   - Poor/Needs Improvement/Good URLs
   - Drill down by URL groups

4. MOBILE USABILITY:
   - Clickable elements too close
   - Text too small to read
   - Content wider than screen
   - Viewport not set

5. SITEMAPS:
   - Submit XML sitemap
   - Monitor indexing status
   - See which URLs Google discovered

6. URL INSPECTION TOOL:
   - Check if URL is indexed
   - Request indexing for new/updated pages
   - View rendered HTML
   - Check mobile vs desktop version
"""

# ============================================================================
# GOOGLE ANALYTICS 4 - Complete Certification Knowledge
# ============================================================================

GOOGLE_ANALYTICS_4 = """
Google Analytics 4 (GA4) - Complete Guide:

1. KEY CONCEPTS:
   Event-Based Model:
   - Everything is an event (pageviews, clicks, conversions)
   - No more sessions-based tracking
   - User-centric across devices
   
   Data Streams:
   - Web (website tracking)
   - iOS app
   - Android app
   - Combined cross-platform reporting

2. IMPORTANT METRICS:
   Engagement Metrics:
   - Engaged sessions: >10s OR 2+ pages OR conversion
   - Engagement rate: Engaged sessions / Total sessions
   - Engaged sessions per user
   
   Acquisition Metrics:
   - Users by source/medium
   - First user source/medium (attribution)
   - Session source/medium
   
   Monetization:
   - Purchase revenue
   - E-commerce conversions
   - Average purchase revenue

3. E-COMMERCE TRACKING:
   Required Events:
   - view_item: Product page view
   - add_to_cart: Item added to cart
   - begin_checkout: Checkout started
   - purchase: Transaction completed
   
   Enhanced Measurement (auto-tracked):
   - Page views
   - Scrolls
   - Outbound clicks
   - Site search
   - Video engagement
   - File downloads

4. CONVERSIONS:
   - Any event can be marked as conversion
   - Common e-commerce conversions:
     * purchase
     * add_to_cart
     * begin_checkout
     * generate_lead
   - Tracked in real-time and historical reports

5. AUDIENCE BUILDING:
   - Predictive audiences (likely to purchase)
   - Create segments based on behavior
   - Export to Google Ads for remarketing
   - Use for personalization

6. REPORTS:
   Acquisition: Where users come from
   Engagement: What users do on site
   Monetization: Revenue and transactions
   Retention: User loyalty and lifetime value
"""


# ============================================================================
# STRUCTURED DATA (Schema.org) - Complete E-commerce Guide
# ============================================================================

STRUCTURED_DATA = """
Structured Data - Schema.org for E-commerce:

1. PRODUCT SCHEMA (Most Important for E-commerce):
   Required Properties:
   - name: Product name
   - image: Product image URL (1200x1200px recommended)
   - description: Product description
   
   Recommended Properties:
   - offers: Price, availability, currency
   - brand: Manufacturer/brand name
   - sku: Stock keeping unit
   - gtin: Global trade item number (UPC, EAN)
   - aggregateRating: Average customer rating
   - review: Customer reviews
   
   Implementation (JSON-LD):
   {
     "@context": "https://schema.org",
     "@type": "Product",
     "name": "Hardwax Oil Classic",
     "image": "https://emmso.com/products/oil.jpg",
     "description": "Premium hardwax oil for wood floors",
     "sku": "HWO-001",
     "brand": {
       "@type": "Brand",
       "name": "Floorservice"
     },
     "offers": {
       "@type": "Offer",
       "url": "https://emmso.com/products/hardwax-oil",
       "priceCurrency": "EUR",
       "price": "49.95",
       "availability": "https://schema.org/InStock",
       "priceValidUntil": "2025-12-31"
     },
     "aggregateRating": {
       "@type": "AggregateRating",
       "ratingValue": "4.8",
       "reviewCount": "127"
     }
   }

2. BREADCRUMBLIST SCHEMA:
   - Shows navigation path
   - Appears in search results
   - Helps users understand site structure
   
   {
     "@context": "https://schema.org",
     "@type": "BreadcrumbList",
     "itemListElement": [
       {
         "@type": "ListItem",
         "position": 1,
         "name": "Home",
         "item": "https://emmso.com"
       },
       {
         "@type": "ListItem",
         "position": 2,
         "name": "Floor Care",
         "item": "https://emmso.com/collections/floor-care"
       },
       {
         "@type": "ListItem",
         "position": 3,
         "name": "Oils",
         "item": "https://emmso.com/collections/oils"
       }
     ]
   }

3. ORGANIZATION SCHEMA (Site-wide):
   - Company information
   - Contact details
   - Social media profiles
   - Logo
   
   {
     "@context": "https://schema.org",
     "@type": "Organization",
     "name": "EMMSO",
     "url": "https://emmso.com",
     "logo": "https://emmso.com/logo.png",
     "contactPoint": {
       "@type": "ContactPoint",
       "telephone": "+31-XX-XXX-XXXX",
       "contactType": "Customer Service",
       "availableLanguage": ["nl", "en", "de"]
     },
     "sameAs": [
       "https://facebook.com/emmso",
       "https://instagram.com/emmso"
     ]
   }

4. WEBSITE SCHEMA (with Site Search):
   {
     "@context": "https://schema.org",
     "@type": "WebSite",
     "url": "https://emmso.com",
     "potentialAction": {
       "@type": "SearchAction",
       "target": {
         "@type": "EntryPoint",
         "urlTemplate": "https://emmso.com/search?q={search_term_string}"
       },
       "query-input": "required name=search_term_string"
     }
   }

5. REVIEW SCHEMA:
   {
     "@context": "https://schema.org",
     "@type": "Review",
     "itemReviewed": {
       "@type": "Product",
       "name": "Hardwax Oil Classic"
     },
     "author": {
       "@type": "Person",
       "name": "Jan de Vries"
     },
     "reviewRating": {
       "@type": "Rating",
       "ratingValue": "5",
       "bestRating": "5"
     },
     "reviewBody": "Excellent product, easy to apply and great finish"
   }

Testing:
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org
- Google Search Console: Enhancement reports
"""

# ============================================================================
# ON-PAGE SEO - Complete Optimization Guide
# ============================================================================

ON_PAGE_SEO = """
On-Page SEO - Complete Optimization Checklist:

1. TITLE TAG (Most Important):
   Rules:
   - 50-60 characters (512px width)
   - Primary keyword near beginning
   - Include brand name at end
   - Unique for every page
   - Match search intent
   
   Examples:
   Good: "Hardwax Oil for Wood Floors | Premium Quality | EMMSO"
   Bad: "Buy Our Products | EMMSO | Shop Now | Free Shipping"
   
   Formula: [Primary Keyword] | [Modifier] | [Brand]

2. META DESCRIPTION:
   Rules:
   - 150-160 characters
   - Compelling call-to-action
   - Include primary keyword naturally
   - Unique for every page
   - Benefits-focused
   
   Example: "Premium hardwax oil for wood floors. Easy application, 
   durable protection. Free shipping Netherlands & Belgium. Order today!"

3. HEADING STRUCTURE (H1-H6):
   Rules:
   - ONE H1 per page (main topic)
   - H2 for main sections
   - H3-H6 for subsections
   - Logical hierarchy (don't skip levels)
   - Include keywords naturally
   
   Structure:
   H1: Hardwax Oil Classic - Premium Floor Protection
     H2: Product Features
       H3: Easy Application
       H3: Long-lasting Protection
     H2: How to Use
       H3: Surface Preparation
       H3: Application Steps
     H2: Customer Reviews

4. URL STRUCTURE:
   Best Practices:
   - Short and descriptive (3-5 words ideal)
   - Use hyphens (not underscores)
   - Lowercase only
   - Include target keyword
   - Remove stop words (a, the, and, or)
   - No special characters
   
   Good: /hardwax-oil-classic
   Bad: /product_123456?cat=oils&sort=price

5. IMAGE OPTIMIZATION:
   Alt Text:
   - Describe image content
   - Include keyword naturally
   - Help screen readers
   - 125 characters max
   
   File Names:
   - Descriptive, not DSC_1234.jpg
   - Use hyphens between words
   - Example: hardwax-oil-application.jpg
   
   Technical:
   - Modern formats (AVIF > WebP > JPEG)
   - Compress images (<200KB)
   - Lazy load below fold
   - Responsive images (srcset)

6. INTERNAL LINKING:
   Strategy:
   - Link related products/content
   - Use descriptive anchor text
   - Build topic clusters
   - Link high-value pages from homepage
   - Breadcrumb navigation
   - Related products section
   
   Anchor Text Best Practices:
   Good: "See our complete guide to floor oil application"
   Bad: "Click here" or "Read more"

7. CONTENT QUALITY:
   E-E-A-T Principles:
   - Experience: First-hand experience with product/topic
   - Expertise: Demonstrate knowledge
   - Authoritativeness: Recognized in industry
   - Trustworthiness: Accurate, transparent, secure
   
   Length Guidelines:
   - Product pages: 300+ words minimum
   - Category pages: 500+ words
   - Blog posts: 1500+ words
   - Comprehensive guides: 3000+ words
   
   Content Checklist:
   - Answer user questions completely
   - Include relevant keywords (2-3% density)
   - Add images/videos
   - Update regularly
   - Cite sources for facts
   - Add FAQ section
"""

# ============================================================================
# TECHNICAL SEO - Complete Implementation Guide
# ============================================================================

TECHNICAL_SEO_COMPLETE = """
Technical SEO - Complete Implementation:

1. ROBOTS.TXT:
   Purpose: Control crawler access
   
   Best Practice Example:
   User-agent: *
   Disallow: /admin/
   Disallow: /cart/
   Disallow: /checkout/
   Disallow: /account/
   Disallow: /search?
   Allow: /
   
   Sitemap: https://emmso.com/sitemap.xml
   
   Testing: Google Search Console > robots.txt Tester

2. XML SITEMAP:
   Purpose: Help Google discover all pages
   
   Include:
   - All product pages
   - All category/collection pages
   - Blog posts/articles
   - Important static pages
   
   Exclude:
   - Admin pages
   - Duplicate content
   - Low-value pages (tags, search results)
   - NoIndex pages
   
   Best Practices:
   - Submit to Google Search Console
   - Update automatically when content changes
   - Split into multiple sitemaps if >50,000 URLs
   - Include lastmod dates
   - Priority: 0.1-1.0 (homepage = 1.0)

3. CANONICAL URLS:
   Purpose: Prevent duplicate content issues
   
   <link rel="canonical" href="https://emmso.com/products/hardwax-oil">
   
   Common Scenarios:
   - Product available in multiple categories
   - Filter/sort parameters create duplicate URLs
   - HTTP vs HTTPS versions
   - www vs non-www
   - Paginated content
   
   Self-referencing: Even unique pages should have canonical tag

4. HREFLANG (Multi-language/Multi-region):
   Purpose: Tell Google which language version to show
   
   <link rel="alternate" hreflang="nl-nl" href="https://emmso.com/nl/products/hardwax-oil">
   <link rel="alternate" hreflang="de-de" href="https://emmso.com/de/products/hartewachsol">
   <link rel="alternate" hreflang="en-gb" href="https://emmso.com/en/products/hardwax-oil">
   <link rel="alternate" hreflang="x-default" href="https://emmso.com/products/hardwax-oil">
   
   Rules:
   - Self-referencing required
   - Return links (bidirectional)
   - Use x-default for catchall
   - ISO 639-1 language codes
   - ISO 3166-1 Alpha 2 country codes

5. HTTPS / SSL:
   Requirements:
   - Valid SSL certificate
   - All resources loaded via HTTPS
   - Redirect HTTP to HTTPS (301)
   - Update internal links to HTTPS
   - Update canonical tags to HTTPS
   
   Ranking Signal: Yes (minor factor)
   Trust Signal: Yes (major for e-commerce)

6. MOBILE-FIRST:
   Google uses mobile version for ranking
   
   Requirements:
   - Responsive design (not separate m. subdomain)
   - Same content on mobile and desktop
   - Fast mobile loading (<2.5s LCP)
   - Touch-friendly (48px targets)
   - No intrusive interstitials
   - Readable without zooming (16px+ font)
   - Viewport meta tag
   
   <meta name="viewport" content="width=device-width, initial-scale=1">

7. SITE SPEED:
   Core Web Vitals (covered separately)
   
   Additional Speed Factors:
   - Server response time (TTFB <600ms)
   - Minimize redirects
   - Enable compression (gzip/brotli)
   - Browser caching
   - CDN for static assets
   - Minify CSS/JS
   - Remove unused code

8. CRAWL BUDGET OPTIMIZATION:
   For Large Sites (10,000+ pages):
   - Fix broken links (404s)
   - Remove low-quality pages
   - Consolidate thin content
   - Use noindex for admin/filter pages
   - Optimize internal linking
   - Fast server response times
"""

# ============================================================================
# E-COMMERCE SEO - Shopify Specific
# ============================================================================

ECOMMERCE_SEO_SHOPIFY = """
E-commerce SEO - Shopify Best Practices:

1. PRODUCT PAGE OPTIMIZATION:
   Unique Descriptions:
   - NEVER use manufacturer descriptions
   - Write 300+ words unique content
   - Include target keywords naturally
   - Answer common questions
   - Highlight benefits, not just features
   
   Product Images:
   - 1200x1200px minimum (Shopify requirement)
   - Multiple angles (6-8 images)
   - Lifestyle images showing use
   - Alt text for every image
   - File names: product-name-angle.jpg
   - Modern formats (AVIF/WebP with fallback)
   
   Product Titles:
   Format: [Brand] [Product Name] - [Key Feature]
   Example: "Floorservice Hardwax Oil Classic - Natural Finish"
   
   Product URLs:
   Shopify format: /products/handle
   Optimize handle: short, keyword-rich, descriptive

2. COLLECTION/CATEGORY PAGES:
   SEO Content:
   - 500+ words unique intro text
   - Explain category/collection
   - Internal links to products
   - Related collections links
   - FAQ section
   
   Pagination:
   - Use rel="next" and rel="prev" (Shopify handles this)
   - Canonical on page 1
   - Load more vs pagination (UX decision)
   
   Filtering (Faceted Navigation):
   - Use AJAX to prevent duplicate content
   - Canonical to main category URL
   - NoIndex filter combinations
   - Test in Google Search Console

3. OUT-OF-STOCK PRODUCTS:
   DO NOT DELETE OR 404!
   
   Instead:
   - Keep page live with "Out of Stock" status
   - Update Product schema availability to "OutOfStock"
   - Add "Notify me when back in stock" form
   - Show alternative/similar products
   - Explain when item will be back (if known)
   
   Reason: You don't lose rankings, backlinks, or indexed status

4. DUPLICATE CONTENT:
   Common Issues:
   - Product in multiple collections
   - Variant URLs (color, size)
   - Print/mobile versions
   - Session IDs in URLs
   
   Solutions:
   - Canonical tags (Shopify handles product canonicals)
   - Parameter handling in Google Search Console
   - Avoid creating separate variant URLs

5. REVIEWS & RATINGS:
   SEO Benefits:
   - User-generated content (fresh content signal)
   - Rich snippets in search (star ratings)
   - Social proof for conversions
   - Long-tail keyword coverage
   
   Implementation:
   - Add review schema (aggregateRating)
   - Respond to reviews (shows engagement)
   - Display reviews on product pages
   - Allow filtering by rating

6. SHOPIFY-SPECIFIC SEO:
   Theme.liquid Additions:
   - Structured data snippets
   - Open Graph tags
   - Twitter Cards
   - Canonical tags
   - Hreflang tags (if multi-market)
   
   Apps to Consider:
   - SEO Manager (structured data)
   - Plug in SEO (SEO checker)
   - Smart SEO (bulk optimization)
   - JSON-LD for SEO (schema)
   
   URL Structure:
   Shopify defaults:
   - /products/handle (products)
   - /collections/handle (collections)
   - /pages/handle (pages)
   - /blogs/handle/article-handle (blog)
   
   Cannot change /products/ prefix without app/workaround
"""

def get_recommendation(topic, current_score):
    """
    Generate SEO recommendation based on topic and score
    """
    recommendations = {
        'core_web_vitals': [
            'Optimize images with modern formats (AVIF/WebP)',
            'Implement lazy loading for below-fold content',
            'Minimize JavaScript execution time',
            'Use CDN for faster content delivery'
        ],
        'technical_seo': [
            'Add structured data for products',
            'Implement proper heading hierarchy (H1-H6)',
            'Optimize meta descriptions for CTR',
            'Fix broken internal links'
        ],
        'mobile': [
            'Increase touch target sizes to 48px minimum',
            'Improve mobile page speed (target <2.5s LCP)',
            'Remove intrusive interstitials',
            'Test mobile usability in Google Search Console'
        ]
    }
    
    return recommendations.get(topic, [])


def get_expert_knowledge():
    """
    Returns complete SEO expert knowledge as single string
    
    Use this for AI/LLM context when generating SEO recommendations.
    Contains complete Google certification-level knowledge covering:
    - Google Search Essentials
    - Core Web Vitals
    - Google Search Console
    - Structured Data
    - On-Page SEO
    - Technical SEO
    - E-commerce SEO (Shopify)
    
    Returns:
        str: Complete knowledge base
    """
    return "\n\n".join([
        "SEO EXPERT KNOWLEDGE BASE - GOOGLE CERTIFICATION",
        "=" * 80,
        GOOGLE_SEARCH_ESSENTIALS,
        CORE_WEB_VITALS,
        GOOGLE_SEARCH_CONSOLE,
        STRUCTURED_DATA,
        ON_PAGE_SEO,
        TECHNICAL_SEO_COMPLETE,
        ECOMMERCE_SEO_SHOPIFY
    ])


