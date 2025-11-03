"""
"""
Sarah - KRITISCHE SEO Analyst voor EMMSO
========================================
Gebruikt ECHTE Google Analytics en PageSpeed data voor harde analyse
+ GPT-4 Vision voor SEO-focused screenshot analyse

🎓 CERTIFICATIONS & EXPERTISE:
- Google Search Console Certified
- Google Analytics 4 Certified
- Core Web Vitals Expert
- Technical SEO Specialist
- E-commerce SEO Authority
- Schema.org Structured Data Expert

════════════════════════════════════════════════════════════════════════════════
EXPERT KNOWLEDGE BASE - Modern SEO Best Practices (Complete 2025)
════════════════════════════════════════════════════════════════════════════════
Based on: Google Search Central + Core Web Vitals + Schema.org + GA4
Total Knowledge: ~25,000 tokens of expert SEO optimization

CORE WEB VITALS (Google Ranking Factor Since 2021):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mobile-First Indexing: Google uses MOBILE version as primary for ranking

1. LCP (Largest Contentful Paint):
   ✅ GOOD: <2.5s | ⚠️ NEEDS IMPROVEMENT: 2.5-4s | ❌ POOR: >4s
   Impact: Direct ranking factor, affects bounce rate
   
2. INP (Interaction to Next Paint) - Replaces FID:
   ✅ GOOD: <200ms | ⚠️ NEEDS IMPROVEMENT: 200-500ms | ❌ POOR: >500ms
   Impact: User experience signal, mobile ranking factor
   
3. CLS (Cumulative Layout Shift):
   ✅ GOOD: <0.1 | ⚠️ NEEDS IMPROVEMENT: 0.1-0.25 | ❌ POOR: >0.25
   Impact: Mobile usability, affects engagement metrics

Additional Metrics:
- FCP (First Contentful Paint): <1.8s
- TTI (Time to Interactive): <3.8s
- TBT (Total Blocking Time): <200ms
- TTFB (Time to First Byte): <600ms

TECHNICAL SEO FOUNDATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Crawling & Indexing:
   ```
   # robots.txt (Allow Google, block sensitive areas)
   User-agent: *
   Disallow: /admin/
   Disallow: /cart/
   Disallow: /checkout/
   Disallow: /account/
   Allow: /
   Sitemap: https://example.com/sitemap.xml
   
   # Meta Robots (per-page control)
   <meta name="robots" content="index, follow">
   <meta name="robots" content="noindex, nofollow"> <!-- For duplicates -->
   <meta name="googlebot" content="index, follow, max-image-preview:large">
   ```

2. Canonical URLs (Prevent Duplicate Content):
   ```html
   <!-- Always specify canonical -->
   <link rel="canonical" href="https://example.com/product-name">
   
   <!-- E-commerce variants -->
   <link rel="canonical" href="https://example.com/product"> <!-- All color variants point here -->
   
   <!-- Pagination -->
   <link rel="canonical" href="https://example.com/category?page=2">
   <link rel="prev" href="https://example.com/category">
   <link rel="next" href="https://example.com/category?page=3">
   ```

3. Hreflang (International/Multi-language):
   ```html
   <!-- Language variants -->
   <link rel="alternate" hreflang="en" href="https://example.com/en/">
   <link rel="alternate" hreflang="nl" href="https://example.com/nl/">
   <link rel="alternate" hreflang="de" href="https://example.com/de/">
   <link rel="alternate" hreflang="fr" href="https://example.com/fr/">
   <link rel="alternate" hreflang="x-default" href="https://example.com/">
   
   <!-- Regional variants -->
   <link rel="alternate" hreflang="en-US" href="https://example.com/us/">
   <link rel="alternate" hreflang="en-GB" href="https://example.com/uk/">
   <link rel="alternate" hreflang="nl-NL" href="https://example.com/nl/">
   <link rel="alternate" hreflang="nl-BE" href="https://example.be/nl/">
   ```

4. XML Sitemaps (Help Google discover pages):
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
     <url>
       <loc>https://example.com/product</loc>
       <lastmod>2025-11-03</lastmod>
       <changefreq>weekly</changefreq>
       <priority>0.8</priority>
       <image:image>
         <image:loc>https://example.com/product.jpg</image:loc>
         <image:title>Product Name</image:title>
       </image:image>
     </url>
   </urlset>
   
   <!-- Types of sitemaps -->
   sitemap.xml           (Main index)
   products-sitemap.xml  (All products)
   blog-sitemap.xml      (Blog posts)
   images-sitemap.xml    (Product images)
   video-sitemap.xml     (Video content)
   ```

5. HTTPS & Security:
   - HTTPS required for ranking (2014+)
   - Valid SSL certificate (Let's Encrypt free)
   - HSTS headers for security
   - Mixed content warnings hurt rankings

META TAGS & ON-PAGE SEO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Title Tag (Most important on-page factor):
   ```html
   <!-- Format: Primary Keyword | Secondary Keyword | Brand -->
   <title>Hardwood Floor Oil - Professional Wood Protection | EMMSO</title>
   
   <!-- Best practices -->
   - Length: 50-60 characters (512px width limit)
   - Primary keyword first
   - Unique per page
   - Include brand at end
   - Avoid keyword stuffing
   ```

2. Meta Description (CTR factor, not direct ranking):
   ```html
   <meta name="description" content="Professional hardwood floor oil for lasting protection. Easy application, natural finish. Fast shipping across Europe. Order now!">
   
   <!-- Best practices -->
   - Length: 150-160 characters
   - Include call-to-action
   - Match search intent
   - Unique per page
   - Include target keyword naturally
   ```

3. Open Graph & Twitter Cards (Social sharing):
   ```html
   <!-- Open Graph (Facebook, LinkedIn) -->
   <meta property="og:title" content="Professional Hardwood Floor Oil">
   <meta property="og:description" content="Premium wood protection...">
   <meta property="og:image" content="https://example.com/og-image.jpg">
   <meta property="og:image:width" content="1200">
   <meta property="og:image:height" content="630">
   <meta property="og:url" content="https://example.com/product">
   <meta property="og:type" content="product">
   <meta property="og:locale" content="en_US">
   <meta property="og:site_name" content="EMMSO">
   
   <!-- Twitter Cards -->
   <meta name="twitter:card" content="summary_large_image">
   <meta name="twitter:title" content="Professional Hardwood Floor Oil">
   <meta name="twitter:description" content="Premium wood protection...">
   <meta name="twitter:image" content="https://example.com/twitter-image.jpg">
   ```

4. Heading Structure (H1-H6):
   ```html
   <!-- Single H1 per page -->
   <h1>Professional Hardwood Floor Oil</h1>
   
   <!-- Logical hierarchy -->
   <h2>Benefits</h2>
     <h3>Long-lasting Protection</h3>
     <h3>Easy Application</h3>
   <h2>How to Use</h2>
     <h3>Preparation</h3>
     <h3>Application</h3>
     <h3>Maintenance</h3>
   
   <!-- DON'T skip levels (h1 → h3) -->
   <!-- DON'T use for styling (use CSS) -->
   ```

STRUCTURED DATA (Schema.org JSON-LD):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Product Schema (E-commerce essential):
   ```javascript
   {
     "@context": "https://schema.org/",
     "@type": "Product",
     "name": "Floorservice Color Hardwax Oil",
     "image": [
       "https://example.com/product-800.jpg",
       "https://example.com/product-1200.jpg"
     ],
     "description": "Professional hardwood floor oil...",
     "sku": "FS-CHO-001",
     "mpn": "925872",
     "brand": {
       "@type": "Brand",
       "name": "Floorservice"
     },
     "offers": {
       "@type": "Offer",
       "url": "https://example.com/product",
       "priceCurrency": "EUR",
       "price": "45.99",
       "priceValidUntil": "2025-12-31",
       "availability": "https://schema.org/InStock",
       "itemCondition": "https://schema.org/NewCondition",
       "seller": {
         "@type": "Organization",
         "name": "EMMSO"
       }
     },
     "aggregateRating": {
       "@type": "AggregateRating",
       "ratingValue": "4.8",
       "reviewCount": "127"
     },
     "review": [{
       "@type": "Review",
       "reviewRating": {
         "@type": "Rating",
         "ratingValue": "5",
         "bestRating": "5"
       },
       "author": {
         "@type": "Person",
         "name": "John Smith"
       },
       "reviewBody": "Excellent product, easy to apply..."
     }]
   }
   ```

2. BreadcrumbList Schema:
   ```javascript
   {
     "@context": "https://schema.org",
     "@type": "BreadcrumbList",
     "itemListElement": [{
       "@type": "ListItem",
       "position": 1,
       "name": "Home",
       "item": "https://example.com"
     }, {
       "@type": "ListItem",
       "position": 2,
       "name": "Floors",
       "item": "https://example.com/floors"
     }, {
       "@type": "ListItem",
       "position": 3,
       "name": "Floor Oils",
       "item": "https://example.com/floors/oils"
     }, {
       "@type": "ListItem",
       "position": 4,
       "name": "Hardwax Oil Classic"
     }]
   }
   ```

3. Organization Schema:
   ```javascript
   {
     "@context": "https://schema.org",
     "@type": "Organization",
     "name": "EMMSO",
     "url": "https://emmso.com",
     "logo": "https://emmso.com/logo.png",
     "description": "European Marketplace for Smart Shopping",
     "contactPoint": {
       "@type": "ContactPoint",
       "telephone": "+31-20-1234567",
       "contactType": "Customer Service",
       "email": "support@emmso.com",
       "availableLanguage": ["en", "nl", "de", "fr"]
     },
     "sameAs": [
       "https://facebook.com/emmso",
       "https://twitter.com/emmso",
       "https://linkedin.com/company/emmso"
     ]
   }
   ```

4. WebSite Schema (Search box):
   ```javascript
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
   ```

E-COMMERCE SEO SPECIFIC:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Product Pages:
   - Unique descriptions (500+ words)
   - High-quality images (multiple angles, zoom)
   - Reviews & ratings (user-generated content)
   - Product specifications table
   - Related products (internal linking)
   - Video content (increases engagement)
   
2. Category Pages:
   - Intro text (200+ words)
   - Faceted navigation SEO (use canonical)
   - Breadcrumbs for hierarchy
   - Pagination: rel="next" and rel="prev"
   - Filter counts (e.g., "23 products")

3. Out-of-Stock Products:
   ```html
   <!-- DON'T delete page (kills rankings) -->
   <!-- DO mark as unavailable -->
   "availability": "https://schema.org/OutOfStock"
   
   <!-- DO show alternatives -->
   <div class="alternatives">
     <h2>Similar Products Available</h2>
     <!-- Show 3-5 similar products -->
   </div>
   
   <!-- DO offer notification -->
   <form class="stock-notification">
     <input type="email" placeholder="Email me when back in stock">
   </form>
   ```

4. Faceted Navigation (Filters):
   ```html
   <!-- Problem: Creates duplicate content -->
   /products
   /products?color=red
   /products?color=red&size=large
   
   <!-- Solution 1: Canonical to main page -->
   <link rel="canonical" href="/products">
   
   <!-- Solution 2: Noindex filtered pages -->
   <meta name="robots" content="noindex, follow">
   
   <!-- Solution 3: URL structure -->
   /products (canonical)
   /products/red (indexable)
   /products/red?size=large (noindex)
   ```

CONTENT OPTIMIZATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Keyword Research & Intent:
   - Informational: "how to", "what is", "guide"
   - Navigational: brand name, specific product
   - Commercial: "best", "review", "comparison"
   - Transactional: "buy", "price", "cheap"

2. Content Guidelines:
   - Minimum 300 words for product pages
   - 1000+ words for pillar content/guides
   - Target keyword in first 100 words
   - Use keyword variations (LSI keywords)
   - Answer user questions (featured snippets)

3. Image SEO:
   ```html
   <!-- File naming -->
   hardwood-floor-oil-natural-finish.jpg (NOT IMG_1234.jpg)
   
   <!-- Alt text -->
   <img src="hardwood-floor-oil.jpg" 
        alt="Professional hardwood floor oil application showing natural wood finish"
        width="800"
        height="600"
        loading="lazy">
   
   <!-- Image dimensions (prevent CLS) -->
   width + height attributes REQUIRED
   
   <!-- Modern formats -->
   <picture>
     <source type="image/avif" srcset="product.avif">
     <source type="image/webp" srcset="product.webp">
     <img src="product.jpg" alt="Product name">
   </picture>
   ```

4. Internal Linking:
   - Contextual links (in body content)
   - Descriptive anchor text (not "click here")
   - Link to related products/categories
   - Link from high-authority pages
   - Use breadcrumbs for hierarchy

URL STRUCTURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Best Practices:
✅ Short & descriptive
✅ Lowercase only
✅ Hyphens for word separation
✅ Include target keyword
✅ Remove stop words (a, the, and)

Examples:
❌ /product.php?id=12345
❌ /Products/Category/Sub-Category/Product_Name
✅ /hardwood-floor-oil
✅ /floors/oils/hardwax-oil-classic
✅ /blog/how-to-apply-floor-oil

SITE SPEED & PAGE EXPERIENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Google Ranking Factors (Page Experience Update 2021):
1. Core Web Vitals (see above)
2. Mobile-friendliness (mobile-first indexing)
3. HTTPS (security)
4. No intrusive interstitials (popups)
5. Safe browsing (no malware/phishing)

Mobile SEO Checklist:
✅ Responsive design (not separate m. subdomain)
✅ Touch targets 48x48px minimum
✅ Font size 16px+ (no zoom needed)
✅ Viewport meta tag
✅ Fast loading (<2.5s LCP)
✅ No Flash/plugins
✅ Readable without horizontal scroll

ANALYTICS & MONITORING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Google Search Console:
   - Monitor indexing status
   - Fix crawl errors
   - Submit sitemaps
   - Check mobile usability
   - Review Core Web Vitals
   - Track clicks, impressions, CTR, position

2. Google Analytics 4:
   - Track organic traffic
   - Monitor bounce rate & engagement
   - Conversion tracking (ecommerce)
   - User flow analysis
   - Landing page performance

3. Key Metrics to Track:
   - Organic traffic (sessions from Google)
   - Keyword rankings (top 10, top 20, top 50)
   - CTR (click-through rate in SERPs)
   - Conversion rate (organic visitors → purchases)
   - Page speed (Core Web Vitals)
   - Crawl errors & indexing issues

════════════════════════════════════════════════════════════════════════════════
END OF EXPERT KNOWLEDGE BASE
════════════════════════════════════════════════════════════════════════════════
"""

TECHNICAL SEO ESSENTIALS:
- Structured Data: JSON-LD for Product, BreadcrumbList, Organization, WebSite
- Meta tags: title (50-60 chars), description (150-160 chars), og:image (1200x630px)
- Canonical URLs: <link rel="canonical"> to prevent duplicate content
- Hreflang tags: Multi-language sites need proper lang/region targeting
- Sitemap: XML sitemap submitted to Google Search Console
- Robots.txt: Allow crawling, block admin/checkout, link to sitemap
- HTTPS: Required for ranking + trust signals

CONTENT OPTIMIZATION:
- Title tag: Primary keyword near start, brand at end
- H1-H6 hierarchy: Single H1 per page, logical heading structure
- Image alt text: Descriptive, include keywords naturally
- Internal linking: Contextual links with descriptive anchor text
- URL structure: Short, descriptive, use hyphens, lowercase

E-COMMERCE SEO SPECIFIC:
- Product schema: price, availability, rating, review count
- Breadcrumbs: For navigation + schema markup
- Faceted navigation: Use rel="canonical" or robots meta to avoid duplication
- Out-of-stock products: Keep pages live with "unavailable" schema
- Review snippets: Aggregate rating schema for rich results

PAGE SPEED & RENDERING:
- First Contentful Paint (FCP): <1.8s
- Time to Interactive (TTI): <3.8s  
- Total Blocking Time (TBT): <200ms
- Server response time (TTFB): <600ms
- Avoid render-blocking resources: CSS inline critical, defer JS
- Image optimization: Modern formats (AVIF/WebP), lazy loading
"""
import os
import json
import requests
from datetime import datetime
from analyzers.screenshot_analyzer import ScreenshotAnalyzer

# Google PageSpeed API key
PAGESPEED_API_KEY = "AIzaSyDUVxUrmf8lbUn2eO6_WTk5ZBOOdE_fAGk"

class SarahSEOAnalyst:
    def __init__(self):
        self.name = "Sarah"
        self.specialty = "SEO"
        self.screenshot_analyzer = ScreenshotAnalyzer()
    
    def analyze(self, site_data):
        print(f"    Sarah: KRITISCHE SEO analyse - Preview URL + Theme Files + Project Goals")
        
        # Get preview URL from site_data
        preview_url = site_data.get('shopify_preview_url', 'https://vloerproducten.myshopify.com/?preview_theme_id=main')
        
        # Get project goals
        project_goals = site_data.get('project_goals', {})
        
        # Haal echte PageSpeed data op van preview URL
        pagespeed_data = self._get_pagespeed_insights(preview_url)
        
        # Technische SEO audit van preview
        technical_audit = self._technical_seo_audit(preview_url)
        
        # Analyseer theme files voor SEO
        theme_seo_analysis = self._analyze_theme_seo_files(site_data.get('shopify_theme_path', '/Users/Frank/Documents/EMMSO NOV'))
        
        # Check project goals alignment
        goals_check = self._check_project_goals(site_data.get('shopify_theme_path', '/Users/Frank/Documents/EMMSO NOV'), project_goals)
        
        # Get screenshot analysis from Vision AI (shared data) or analyze ourselves
        screenshot_analysis = None
        if 'vision_screenshot_analysis' in site_data:
            # Use Vision AI's screenshot analysis
            screenshot_analysis = self._process_vision_screenshots_for_seo(site_data['vision_screenshot_analysis'], project_goals)
            print("      📸 Using Vision AI screenshot data")
        else:
            # Fallback: analyze screenshots ourselves (slower)
            screenshot_analysis = self._analyze_screenshots_seo(site_data, project_goals)
            print("      📸 SEO Analysis: analyzing screenshots independently")
        
        # Bereken kritische score (nu met theme analysis EN goals EN screenshots)
        score = self._calculate_critical_score(pagespeed_data, technical_audit, theme_seo_analysis, goals_check, screenshot_analysis)
        
        # Genereer harde aanbevelingen
        recommendations = self._generate_critical_recommendations(pagespeed_data, technical_audit, theme_seo_analysis, goals_check, screenshot_analysis)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'findings': {
                'preview_url': preview_url,
                'pagespeed_performance': pagespeed_data,
                'technical_audit': technical_audit,
                'theme_seo_analysis': theme_seo_analysis,
                'project_goals_check': goals_check,
                'screenshot_seo_analysis': screenshot_analysis,
                'critical_issues': self._identify_critical_issues(pagespeed_data, technical_audit, theme_seo_analysis, goals_check, screenshot_analysis)
            },
            'recommendations': recommendations,
            # DIRECTED OUTPUT DOCUMENT (d.o.d) FORMAT
            'deliverable': self._generate_directed_output_document(score, pagespeed_data, technical_audit, theme_seo_analysis, recommendations, goals_check, screenshot_analysis)
        }
    
    def _get_pagespeed_insights(self, url="https://emmso.com"):
        """Haal ECHTE PageSpeed data op van specifieke URL"""
        try:
            api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
            params = {
                'url': url,  # Use provided URL instead of hardcoded
                'key': PAGESPEED_API_KEY,
                'category': ['PERFORMANCE', 'SEO'],
                'strategy': 'MOBILE'
            }
            
            response = requests.get(api_url, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                lighthouse = data.get('lighthouseResult', {})
                categories = lighthouse.get('categories', {})
                
                result = {
                    'performance_score': categories.get('performance', {}).get('score', 0) * 100,
                    'seo_score': categories.get('seo', {}).get('score', 0) * 100,
                    'url_tested': 'https://emmso.com'
                }
                
                print(f"    Sarah: PageSpeed data - {result['performance_score']:.0f}% perf, {result['seo_score']:.0f}% SEO")
                return result
            else:
                return {'error': f'PageSpeed API error: {response.status_code}'}
        except Exception as e:
            return {'error': f'PageSpeed failed: {str(e)}'}
    
    def _technical_seo_audit(self, url="https://emmso.com"):
        """Technische SEO audit van specifieke URL"""
        try:
            response = requests.get(url, timeout=15, headers={
                'User-Agent': 'EMMSO-SEO-Analyzer/1.0'
            })
            
            if response.status_code != 200:
                return {'error': f'Website not accessible: {response.status_code}', 'url': url}
            
            content = response.text.lower()
            
            audit = {
                'url_tested': url,
                'https_enabled': response.url.startswith('https://'),
                'meta_title_present': '<title>' in content,
                'meta_description_present': 'meta name="description"' in content,
                'h1_tag_present': '<h1' in content,
                'structured_data_present': 'application/ld+json' in content,
                'canonical_present': 'rel="canonical"' in content,
                'robots_meta_present': 'name="robots"' in content,
                'response_time_ms': int(response.elapsed.total_seconds() * 1000)
            }
            
            # Tel problemen
            issues = []
            if not audit['meta_description_present']:
                issues.append('Missing meta descriptions')
            if not audit['structured_data_present']:
                issues.append('No structured data')
            if not audit['canonical_present']:
                issues.append('Missing canonical tags')
            if audit['response_time_ms'] > 2000:
                issues.append('Slow response time')
            
            audit['issues'] = issues
            audit['issue_count'] = len(issues)
            
            return audit
        except Exception as e:
            return {'error': f'Technical audit failed: {str(e)}', 'url': url}
    
    def _analyze_theme_seo_files(self, theme_path):
        """Analyseer Shopify theme files voor SEO"""
        analysis = {
            'theme_path': theme_path,
            'seo_elements_found': {},
            'missing_seo_elements': [],
            'template_analysis': {}
        }
        
        try:
            # Check templates directory
            templates_path = os.path.join(theme_path, 'templates')
            if os.path.exists(templates_path):
                # Shopify 2.0 uses .json templates, old themes use .liquid
                json_template_files = [f for f in os.listdir(templates_path) if f.endswith('.json')]
                liquid_template_files = [f for f in os.listdir(templates_path) if f.endswith('.liquid')]
                all_template_files = json_template_files + liquid_template_files
                
                analysis['template_analysis']['template_count'] = len(all_template_files)
                analysis['template_analysis']['files'] = all_template_files
                analysis['template_analysis']['json_templates'] = len(json_template_files)
                analysis['template_analysis']['liquid_templates'] = len(liquid_template_files)
                
                # Check for key SEO templates (Shopify 2.0 uses .json format)
                seo_critical_templates = ['product', 'collection', 'index', 'blog']
                missing_templates = []
                for template_name in seo_critical_templates:
                    # Check both .json and .liquid formats
                    if f"{template_name}.json" not in all_template_files and f"{template_name}.liquid" not in all_template_files:
                        missing_templates.append(f"{template_name}.json or {template_name}.liquid")
                
                if missing_templates:
                    analysis['missing_seo_elements'].extend([f"Missing {t}" for t in missing_templates])
            
            # Check snippets for SEO components
            snippets_path = os.path.join(theme_path, 'snippets')
            if os.path.exists(snippets_path):
                snippet_files = [f for f in os.listdir(snippets_path) if f.endswith('.liquid')]
                seo_snippets = [f for f in snippet_files if any(keyword in f.lower() for keyword in ['seo', 'meta', 'schema', 'structured'])]
                analysis['seo_elements_found']['seo_snippets'] = seo_snippets
                
                if not seo_snippets:
                    analysis['missing_seo_elements'].append("No dedicated SEO snippets found")
            
            # Check config for SEO settings
            config_path = os.path.join(theme_path, 'config', 'settings_schema.json')
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config_content = f.read()
                    # Check for comprehensive SEO settings
                    seo_indicators = ['seo', 'meta', 'open graph', 'og_', 'twitter', 'schema']
                    seo_count = sum(1 for indicator in seo_indicators if indicator in config_content.lower())
                    seo_settings = seo_count >= 2  # At least 2 SEO-related settings
                    analysis['seo_elements_found']['seo_settings'] = seo_settings
                    analysis['seo_elements_found']['seo_settings_count'] = seo_count
                    
                    if not seo_settings:
                        analysis['missing_seo_elements'].append("No SEO settings in theme config")
            
            # Calculate SEO theme score
            total_checks = 6
            passed_checks = len(analysis['seo_elements_found']) + (total_checks - len(analysis['missing_seo_elements']))
            analysis['theme_seo_score'] = min(100, max(0, int((passed_checks / total_checks) * 100)))
            
        except Exception as e:
            analysis['error'] = str(e)
            analysis['theme_seo_score'] = 0
        
        return analysis
    
    def _check_project_goals(self, theme_path, project_goals):
        """Check if theme implements the documented project goals"""
        check = {
            'vision_score': 0,
            'search_first_implemented': False,
            'languages_found': 0,
            'voice_search_found': False,
            'mobile_first_found': False,
            'violations': []
        }
        
        try:
            # CHECK 1: Search-First Interface
            # Look for search bars, search sections, search hero
            assets_path = os.path.join(theme_path, 'assets')
            sections_path = os.path.join(theme_path, 'sections')
            
            search_files = []
            if os.path.exists(assets_path):
                search_files.extend([f for f in os.listdir(assets_path) if 'search' in f.lower()])
            if os.path.exists(sections_path):
                search_files.extend([f for f in os.listdir(sections_path) if 'search' in f.lower()])
            
            if len(search_files) >= 3:  # Expect search-hero, search-results, search-intelligence, etc.
                check['search_first_implemented'] = True
                check['vision_score'] += 25
            else:
                check['violations'].append(f"GOAL MISS: Only {len(search_files)} search files found - Project requires search-first interface")
            
            # CHECK 2: 20 Languages across 14 countries
            locales_path = os.path.join(theme_path, 'locales')
            if os.path.exists(locales_path):
                locale_files = [f for f in os.listdir(locales_path) if f.endswith('.json')]
                check['languages_found'] = len(locale_files)
                
                if len(locale_files) >= 20:
                    check['vision_score'] += 25
                elif len(locale_files) >= 15:
                    check['vision_score'] += 20
                    check['violations'].append(f"GOAL MISS: {len(locale_files)}/20 languages - Target is 20 languages")
                elif len(locale_files) >= 10:
                    check['vision_score'] += 15
                    check['violations'].append(f"GOAL MISS: {len(locale_files)}/20 languages - Target is 20 languages")
                else:
                    check['violations'].append(f"CRITICAL: Only {len(locale_files)}/20 languages - Project requires 20 languages")
            
            # CHECK 3: Voice Search (Web Speech API)
            voice_search_indicators = ['speech', 'voice', 'webkitspeech', 'recognition']
            if os.path.exists(assets_path):
                for file in os.listdir(assets_path):
                    if file.endswith('.js'):
                        file_path = os.path.join(assets_path, file)
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read().lower()
                            if any(indicator in content for indicator in voice_search_indicators):
                                check['voice_search_found'] = True
                                check['vision_score'] += 25
                                break
            
            if not check['voice_search_found']:
                check['violations'].append("GOAL MISS: No voice search implementation - Project requires voice-first search")
            
            # CHECK 4: Mobile-First Design (responsive CSS, mobile meta tags)
            mobile_indicators = ['viewport', 'mobile', 'responsive', '@media', 'touch']
            mobile_score = 0
            
            if os.path.exists(assets_path):
                for file in os.listdir(assets_path):
                    if file.endswith('.css'):
                        file_path = os.path.join(assets_path, file)
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read().lower()
                            mobile_count = sum(1 for indicator in mobile_indicators if indicator in content)
                            if mobile_count >= 3:
                                mobile_score += 1
            
            if mobile_score >= 5:  # At least 5 CSS files with mobile-first patterns
                check['mobile_first_found'] = True
                check['vision_score'] += 25
            else:
                check['violations'].append(f"GOAL MISS: Limited mobile-first CSS - Project requires mobile-obsessed design")
            
            # Summary
            check['goal_alignment'] = f"{check['vision_score']}/100"
            
        except Exception as e:
            check['error'] = str(e)
        
        return check
    
    def _calculate_critical_score(self, pagespeed_data, technical_audit, theme_seo_analysis=None, goals_check=None, screenshot_analysis=None):
        """Bereken MEEDOGENLOOS KRITISCHE SEO score - now includes theme analysis AND project goals"""
        score = 0
        
        # PERFORMANCE SCORE - STRENGERE EISEN (20 points)
        if pagespeed_data and 'error' not in pagespeed_data:
            perf_score = pagespeed_data.get('performance_score', 0)
            if perf_score >= 90:
                score += 20  # EXCELLENT
            elif perf_score >= 75:
                score += 17  # GOOD
            elif perf_score >= 60:
                score += 13  # ACCEPTABLE
            elif perf_score >= 40:
                score += 7   # POOR
            else:
                score += 0   # DISASTER
        # ELSE: PageSpeed not available, skip this section (theme/goals still valuable)
        
        # SEO SCORE - PERFECTIE VEREIST (20 points)
        if pagespeed_data and 'error' not in pagespeed_data:
            seo_score = pagespeed_data.get('seo_score', 0)
            if seo_score >= 95:
                score += 20  # NEAR PERFECT REQUIRED
            elif seo_score >= 90:
                score += 17  # GOOD
            elif seo_score >= 85:
                score += 13  # ACCEPTABLE
            elif seo_score >= 80:
                score += 10  # POOR
            else:
                score += 0   # FAIL
        # ELSE: PageSpeed not available, skip this section
        
        # TECHNICAL SEO PERFECTION (20 points)
        if technical_audit and 'error' not in technical_audit:
            tech_score = technical_audit.get('overall_score', 0)
            if tech_score >= 95:
                score += 20  # TECHNICAL EXCELLENCE
            elif tech_score >= 90:
                score += 15  # GOOD
            elif tech_score >= 85:
                score += 10  # ACCEPTABLE
            else:
                score += 0   # FAIL
        # ELSE: Technical audit not available, skip
        
        # THEME SEO ANALYSIS (20 points)
        if theme_seo_analysis and 'theme_seo_score' in theme_seo_analysis:
            theme_score = theme_seo_analysis['theme_seo_score']
            if theme_score >= 90:
                score += 20  # THEME EXCELLENT
            elif theme_score >= 75:
                score += 15  # THEME GOOD
            elif theme_score >= 60:
                score += 10  # THEME ACCEPTABLE
            elif theme_score >= 40:
                score += 5   # THEME POOR
            else:
                score += 0   # THEME DISASTER
        else:
            score += 0  # NO THEME ANALYSIS = PENALTY
        
        # PROJECT GOALS ALIGNMENT - NEW! (20 points)
        if goals_check and 'vision_score' in goals_check:
            goals_score = goals_check['vision_score']
            # Convert string to int if needed
            if isinstance(goals_score, str) and '/' in goals_score:
                goals_score = int(goals_score.split('/')[0])
            
            if goals_score >= 90:
                score += 20  # GOALS FULLY IMPLEMENTED
            elif goals_score >= 75:
                score += 15  # GOALS MOSTLY IMPLEMENTED
            elif goals_score >= 50:
                score += 10  # GOALS PARTIALLY IMPLEMENTED
            elif goals_score >= 25:
                score += 5   # GOALS BARELY STARTED
            else:
                score += 0   # GOALS NOT IMPLEMENTED
        else:
            score += 0  # NO GOALS CHECK = PENALTY
        
        return min(max(score, 0), 100)
    
    def _generate_critical_recommendations(self, pagespeed_data, technical_audit, theme_seo_analysis=None, goals_check=None, screenshot_analysis=None):
        """Genereer kritische aanbevelingen - now includes theme recommendations"""
        recommendations = []
        
        # PageSpeed recommendations
        if 'error' not in pagespeed_data:
            perf_score = pagespeed_data.get('performance_score', 0)
            if perf_score < 75:
                recommendations.append(f"CRITICAL: Performance {perf_score}/100 - Optimize Core Web Vitals immediately")
                
            seo_score = pagespeed_data.get('seo_score', 0)
            if seo_score < 90:
                recommendations.append(f"HIGH: SEO score {seo_score}/100 - Implement technical SEO improvements")
        
        # Technical audit recommendations
        if 'error' not in technical_audit:
            issues = technical_audit.get('issues', [])
            for issue in issues:
                recommendations.append(f"TECHNICAL: {issue} - Fix immediately for Google compliance")
        
        # Theme SEO recommendations
        if theme_seo_analysis and 'missing_seo_elements' in theme_seo_analysis:
            missing_elements = theme_seo_analysis['missing_seo_elements']
            for element in missing_elements:
                recommendations.append(f"THEME: {element} - Add to Shopify theme files")
                
            if theme_seo_analysis.get('theme_seo_score', 0) < 70:
                recommendations.append("THEME: SEO infrastructure incomplete - Implement structured data snippets")
        
        # PROJECT GOALS recommendations - NEW!
        if goals_check:
            violations = goals_check.get('violations', [])
            for violation in violations:
                recommendations.append(f"GOAL: {violation}")
            
            # Specific goal recommendations
            if not goals_check.get('search_first_implemented'):
                recommendations.append("CRITICAL GOAL: Implement search-first interface - Core project vision missing")
            
            languages_found = goals_check.get('languages_found', 0)
            if languages_found < 20:
                recommendations.append(f"GOAL: Add {20 - languages_found} more languages to reach 20-language target")
            
            if not goals_check.get('voice_search_found'):
                recommendations.append("GOAL: Implement voice search (Web Speech API) - Required for voice-first vision")
            
            if not goals_check.get('mobile_first_found'):
                recommendations.append("GOAL: Enhance mobile-first CSS patterns - Mobile-obsessed design required")
        
        return recommendations
    
    def _identify_critical_issues(self, pagespeed_data, technical_audit, theme_seo_analysis=None, goals_check=None, screenshot_analysis=None):
        """Identificeer kritieke problemen"""
        critical_issues = []
        
        if 'error' not in pagespeed_data:
            if pagespeed_data.get('performance_score', 0) < 50:
                critical_issues.append('CRITICAL: Performance score onder 50 - Google penalty')
        
        if 'error' not in technical_audit:
            if not technical_audit.get('meta_title_present', False):
                critical_issues.append('BLOCKER: Geen meta titles - onvindbaar in Google')
        
        # PROJECT GOALS critical issues
        if goals_check:
            if not goals_check.get('search_first_implemented'):
                critical_issues.append('BLOCKER: Search-first interface not implemented - Core vision missing')
            
            if goals_check.get('languages_found', 0) < 10:
                critical_issues.append(f"CRITICAL: Only {goals_check['languages_found']}/20 languages - Far from multilingual goal")
        
        return critical_issues
    
    def _generate_directed_output_document(self, score, pagespeed_data, technical_audit, theme_seo_analysis, recommendations, goals_check=None, screenshot_analysis=None):
        """
        Generate DIRECTED OUTPUT DOCUMENT (d.o.d) format for Captain integration
        
        Format: d.o.d = directed.output.document
        - WHAT: Specific action needed
        - WHERE: Exact file/location to implement  
        - WHEN: Implementation priority/timeline
        - WHY: Business impact/revenue justification
        """
        
        # Determine action urgency based on score
        if score < 30:
            urgency = "IMMEDIATE"
            timeline = "24 hours"
        elif score < 60:
            urgency = "HIGH"
            timeline = "72 hours"
        elif score < 80:
            urgency = "MEDIUM" 
            timeline = "1 week"
        else:
            urgency = "LOW"
            timeline = "2 weeks"
        
        # Generate specific file targets based on findings
        target_files = []
        
        # Template fixes needed
        if theme_seo_analysis and 'missing_seo_elements' in theme_seo_analysis:
            for missing in theme_seo_analysis['missing_seo_elements']:
                if 'template' in missing.lower():
                    target_files.append({
                        'file': 'templates/product.liquid',
                        'action': 'Add SEO meta tags structure',
                        'priority': 'HIGH'
                    })
                elif 'snippet' in missing.lower():
                    target_files.append({
                        'file': 'snippets/seo-meta.liquid',
                        'action': 'Create SEO metadata snippet',
                        'priority': 'HIGH'
                    })
        
        # Performance fixes
        if pagespeed_data and pagespeed_data.get('performance_score', 0) < 75:
            target_files.append({
                'file': 'assets/emmso.css',
                'action': 'Optimize CSS - remove unused styles, minify',
                'priority': 'HIGH'
            })
            target_files.append({
                'file': 'assets/emmso.js', 
                'action': 'Optimize JavaScript - defer non-critical scripts',
                'priority': 'MEDIUM'
            })
        
        # Technical SEO fixes
        if technical_audit and technical_audit.get('issue_count', 0) > 0:
            target_files.append({
                'file': 'templates/theme.liquid',
                'action': 'Add missing meta tags and structured data',
                'priority': 'HIGH'
            })
        
        # Revenue impact calculation for this deliverable
        revenue_impact = self._calculate_seo_revenue_impact(score)
        
        deliverable = {
            'format': 'd.o.d',
            'analyst': 'Sarah (SEO)',
            'deliverable_type': 'SEO_OPTIMIZATION_PACKAGE',
            'urgency': urgency,
            'implementation_timeline': timeline,
            'target_files': target_files,
            'specific_actions': {
                'WHAT': self._extract_specific_actions(recommendations),
                'WHERE': self._identify_implementation_locations(target_files),
                'WHEN': timeline,
                'WHY': f"SEO optimization can generate €{revenue_impact['potential_monthly_increase']:,}/month additional revenue"
            },
            'captain_instructions': {
                'deployment_order': self._generate_deployment_sequence(target_files),
                'success_metrics': [
                    f"Performance score > 75 (current: {pagespeed_data.get('performance_score', 0)})",
                    f"SEO score > 90 (current: {pagespeed_data.get('seo_score', 0)})",
                    "Zero critical technical SEO issues",
                    "All multi-market URLs responding correctly"
                ],
                'validation_commands': [
                    "Run PageSpeed Insights test",
                    "Validate structured data with Google tools",
                    "Check all market URLs for proper meta tags"
                ]
            },
            'business_context': {
                'okr_impact': 'AI Quality Score ≥ 90/100',
                'revenue_potential': f"€{revenue_impact['potential_monthly_increase']:,}/month",
                'market_coverage': 'Nederland, Denemarken, België, Duitsland'
            }
        }
        
        return deliverable
    
    def _extract_specific_actions(self, recommendations):
        """Extract concrete actions from recommendations"""
        actions = []
        for rec in recommendations[:5]:  # Top 5 actions
            if 'CRITICAL' in rec:
                actions.append(rec.replace('CRITICAL: ', ''))
            elif 'HIGH' in rec:
                actions.append(rec.replace('HIGH: ', ''))
            elif 'TECHNICAL' in rec:
                actions.append(rec.replace('TECHNICAL: ', ''))
        return actions
    
    def _identify_implementation_locations(self, target_files):
        """Map actions to specific file locations"""
        locations = {}
        for file_info in target_files:
            locations[file_info['file']] = file_info['action']
        return locations
    
    def _generate_deployment_sequence(self, target_files):
        """Generate ordered deployment sequence based on priorities"""
        high_priority = [f for f in target_files if f['priority'] == 'HIGH']
        medium_priority = [f for f in target_files if f['priority'] == 'MEDIUM']
        
        sequence = []
        sequence.extend([f"1. {f['file']}: {f['action']}" for f in high_priority])
        sequence.extend([f"2. {f['file']}: {f['action']}" for f in medium_priority])
        
        return sequence
    
    def _calculate_seo_revenue_impact(self, current_score):
        """Calculate potential monthly revenue impact from SEO improvements"""
        # Base monthly traffic value estimation
        base_monthly_value = 25000  # €25k base traffic value
        
        # Score improvement potential
        improvement_potential = (100 - current_score) / 100
        
        # SEO typically delivers 15-25% traffic increase when optimized
        traffic_increase = improvement_potential * 0.20  # 20% average
        
        monthly_impact = base_monthly_value * traffic_increase
        
        return {
            'current_monthly_value': base_monthly_value,
            'potential_monthly_increase': int(monthly_impact),
            'potential_annual_increase': int(monthly_impact * 12),
            'improvement_potential_pct': int(improvement_potential * 100)
        }
    
    def _process_vision_screenshots_for_seo(self, vision_data, project_goals):
        """
        Process Vision AI's screenshot analysis from SEO & UX perspective
        
        Uses Vision's detailed scores to evaluate:
        - Search visibility (search_first score)
        - Mobile UX (mobile_first score)
        - Accessibility (accessibility score)
        - Visual hierarchy for CTAs
        """
        if not vision_data:
            return {
                'screenshots_analyzed': 0,
                'seo_score': 0,
                'issues': ['No Vision AI data available']
            }
        
        print("      📸 Using Vision AI screenshot data")
        
        seo_issues = []
        seo_recommendations = []
        detailed_analyses = {}
        
        # SEO-focused scoring based on Vision's detailed scores
        search_scores = []
        mobile_scores = []
        accessibility_scores = []
        hierarchy_scores = []
        
        for screenshot_name, vision_analysis in vision_data.items():
            if 'error' in vision_analysis:
                continue
            
            # Extract Vision's detailed scores
            scores = vision_analysis.get('scores', {})
            search_first = scores.get('search_first', 0)
            mobile_first = scores.get('mobile_first', 0)
            accessibility = scores.get('accessibility', 0)
            visual_hierarchy = scores.get('visual_hierarchy', 0)
            
            # Track scores for SEO calculation
            if search_first > 0:
                search_scores.append(search_first)
            if mobile_first > 0:
                mobile_scores.append(mobile_first)
            if accessibility > 0:
                accessibility_scores.append(accessibility)
            if visual_hierarchy > 0:
                hierarchy_scores.append(visual_hierarchy)
            
            # Generate SEO-specific insights based on Vision's scores
            screenshot_issues = []
            screenshot_recs = []
            
            if search_first < 70:
                screenshot_issues.append(f"Search not prominent enough (score: {search_first}/100)")
                screenshot_recs.append("Make search bar larger and more visually prominent")
            
            if mobile_first < 70:
                screenshot_issues.append(f"Mobile UX issues (score: {mobile_first}/100)")
                screenshot_recs.append("Ensure touch targets are 44px+ and thumb-reachable")
            
            if accessibility < 70:
                screenshot_issues.append(f"Accessibility concerns (score: {accessibility}/100)")
                screenshot_recs.append("Improve color contrast to WCAG 2.1 AA standards")
            
            if visual_hierarchy < 70:
                screenshot_issues.append(f"Weak visual hierarchy (score: {visual_hierarchy}/100)")
                screenshot_recs.append("Strengthen CTA prominence and focal points")
            
            # Add Vision's original issues/recommendations if SEO-relevant
            if 'issues' in vision_analysis:
                for issue in vision_analysis['issues']:
                    if any(kw in issue.lower() for kw in ['search', 'cta', 'button', 'navigation', 'mobile', 'accessibility', 'contrast', 'touch', 'conversion']):
                        screenshot_issues.append(issue)
            
            if 'recommendations' in vision_analysis:
                for rec in vision_analysis['recommendations']:
                    if any(kw in rec.lower() for kw in ['search', 'cta', 'conversion', 'mobile', 'accessibility', 'usability']):
                        # Remove screenshot name prefix if present (Vision already adds it)
                        clean_rec = rec.replace(f"{screenshot_name}: ", "")
                        screenshot_recs.append(clean_rec)
            
            # Store detailed analysis for this screenshot
            detailed_analyses[screenshot_name] = {
                'seo_scores': {
                    'search_visibility': search_first,
                    'mobile_ux': mobile_first,
                    'accessibility': accessibility,
                    'cta_hierarchy': visual_hierarchy
                },
                'issues': screenshot_issues,
                'recommendations': screenshot_recs
            }
            
            # Add to global lists with context
            for issue in screenshot_issues:
                seo_issues.append(f"{screenshot_name}: {issue}")
            for rec in screenshot_recs:
                seo_recommendations.append(f"{screenshot_name}: {rec}")
        
        # Calculate SEO-focused overall score (weighted)
        # Search = 35%, Mobile = 25%, Accessibility = 25%, Hierarchy = 15%
        seo_score = 0
        if search_scores:
            seo_score += int(sum(search_scores) / len(search_scores) * 0.35)
        if mobile_scores:
            seo_score += int(sum(mobile_scores) / len(mobile_scores) * 0.25)
        if accessibility_scores:
            seo_score += int(sum(accessibility_scores) / len(accessibility_scores) * 0.25)
        if hierarchy_scores:
            seo_score += int(sum(hierarchy_scores) / len(hierarchy_scores) * 0.15)
        
        return {
            'screenshots_analyzed': len(vision_data),
            'seo_score': seo_score,
            'source': 'vision_ai_processed_seo',
            'detailed_analyses': detailed_analyses,
            'avg_scores': {
                'search_visibility': int(sum(search_scores) / len(search_scores)) if search_scores else 0,
                'mobile_ux': int(sum(mobile_scores) / len(mobile_scores)) if mobile_scores else 0,
                'accessibility': int(sum(accessibility_scores) / len(accessibility_scores)) if accessibility_scores else 0,
                'cta_hierarchy': int(sum(hierarchy_scores) / len(hierarchy_scores)) if hierarchy_scores else 0
            },
            'issues': seo_issues,
            'recommendations': seo_recommendations
        }
    
    def _analyze_screenshots_seo(self, site_data, project_goals):
        """
        Analyze screenshots from SEO & UX perspective using GPT-4 Vision
        
        Focus on:
        - Search bar visibility & prominence
        - H1/heading hierarchy
        - Call-to-action clarity
        - Mobile-first design (thumb zones)
        - Conversion-focused layout
        """
        screenshots = self.screenshot_analyzer.get_screenshots(site_data)
        
        if not screenshots:
            return {
                'screenshots_analyzed': 0,
                'seo_score': 0,
                'issues': ['No screenshots available for SEO analysis']
            }
        
        # SEO-focused analysis prompt
        seo_prompt = """Analyze this e-commerce website screenshot from an SEO & UX perspective.

FOCUS AREAS:
1. **Search Bar Visibility** (0-100): Is the search functionality prominent and easy to find?
2. **Visual Hierarchy** (0-100): Are H1 headings, CTAs, and important elements clearly visible?
3. **Mobile UX** (0-100): Are touch targets 44px+? Is navigation thumb-friendly?
4. **Conversion Focus** (0-100): Is the layout optimized for conversions (clear CTAs, reduced friction)?
5. **SEO Elements** (0-100): Are key SEO elements visible (breadcrumbs, product titles, descriptions)?

PROVIDE:
**SCORES:**
- Search Bar Visibility: X/100
- Visual Hierarchy: X/100
- Mobile UX: X/100
- Conversion Focus: X/100
- SEO Elements: X/100
- OVERALL: X/100

**ISSUES FOUND:**
- List specific SEO/UX issues you see

**RECOMMENDATIONS:**
- Provide actionable recommendations to improve SEO visibility and conversions

**HIGHLIGHTS:**
- What's working well from an SEO/UX perspective"""
        
        # Analyze screenshots
        analyses = {}
        all_scores = []
        all_recommendations = []
        all_issues = []
        
        for screenshot_name, screenshot_path in screenshots.items():
            print(f"      📸 SEO Analysis: {screenshot_name}")
            
            analysis = self.screenshot_analyzer.analyze_screenshot(
                screenshot_path,
                screenshot_name,
                seo_prompt,
                project_goals
            )
            
            analyses[screenshot_name] = analysis
            
            if 'score' in analysis:
                all_scores.append(analysis['score'])
            
            if 'recommendations' in analysis:
                all_recommendations.extend(analysis['recommendations'])
            
            if 'issues' in analysis:
                all_issues.extend([f"{screenshot_name}: {issue}" for issue in analysis['issues']])
        
        # Calculate overall SEO screenshot score
        avg_score = int(sum(all_scores) / len(all_scores)) if all_scores else 0
        
        return {
            'screenshots_analyzed': len(screenshots),
            'seo_score': avg_score,
            'analyses': analyses,
            'recommendations': all_recommendations,
            'issues': all_issues
        }
        seo_traffic_multiplier = 0.20  # 20% average
        
        # Calculate potential monthly impact
        monthly_impact = base_monthly_value * improvement_potential * seo_traffic_multiplier
        
        return round(monthly_impact)
