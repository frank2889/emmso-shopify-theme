"""
Performance Expert Knowledge Base - Complete Web Performance Certification
=========================================================================
Everything needed to pass: Google PageSpeed Insights, Web.dev, Lighthouse,
Core Web Vitals certification, and perform professional performance audits.

Based on: Web.dev, Chrome DevTools, Lighthouse, HTTP/2, Modern Web Standards
"""

# ============================================================================
# LIGHTHOUSE SCORING - Complete Algorithm Understanding
# ============================================================================

LIGHTHOUSE_SCORING = """
Lighthouse Performance Score - Complete Breakdown (2025):

WEIGHTED METRICS (Total = 100 points):
1. LCP (Largest Contentful Paint): 25% weight
2. TBT (Total Blocking Time): 30% weight  
3. CLS (Cumulative Layout Shift): 25% weight
4. SI (Speed Index): 10% weight
5. FCP (First Contentful Paint): 10% weight

SCORING THRESHOLDS:
Each metric gets 0-100 score based on these curves:

LCP (Largest Contentful Paint):
- 0-1200ms: 100 points (excellent)
- 1200-2400ms: Linear decline to 90 points
- 2400-3600ms: Linear decline to 50 points
- 3600-4800ms: Linear decline to 0 points
- >4800ms: 0 points (fail)

TBT (Total Blocking Time):
- 0-150ms: 100 points
- 150-350ms: Linear decline to 90 points
- 350-750ms: Linear decline to 50 points
- 750-1500ms: Linear decline to 0 points
- >1500ms: 0 points

CLS (Cumulative Layout Shift):
- 0-0.1: 100 points
- 0.1-0.25: Linear decline to 50 points
- >0.25: 0 points

FCP (First Contentful Paint):
- 0-900ms: 100 points
- 900-1600ms: Linear decline to 90 points
- 1600-3000ms: Linear decline to 50 points
- >3000ms: 0 points

Speed Index:
- 0-1300ms: 100 points
- 1300-2300ms: Linear decline to 90 points
- 2300-4200ms: Linear decline to 50 points
- >4200ms: 0 points

FINAL SCORE CALCULATION:
Performance Score = (LCP_score × 0.25) + (TBT_score × 0.30) + 
                   (CLS_score × 0.25) + (SI_score × 0.10) + 
                   (FCP_score × 0.10)

COLOR CODING:
- 90-100: Green (Good)
- 50-89: Orange (Needs Improvement)
- 0-49: Red (Poor)

LAB DATA vs FIELD DATA:
- Lab Data: Lighthouse simulated tests (controlled environment)
- Field Data: Real user data from Chrome UX Report (CrUX)
- Rankings use Field Data, debugging uses Lab Data
"""

# ============================================================================
# CORE WEB VITALS - Deep Technical Implementation
# ============================================================================

CORE_WEB_VITALS_DEEP = """
Core Web Vitals - Complete Technical Guide (2025):

1. LCP (LARGEST CONTENTFUL PAINT):
   
   What It Measures:
   - Time to render the largest visible element
   - Usually: hero image, video, large text block
   
   Thresholds (75th percentile of page loads):
   - Good: <2.5 seconds
   - Needs Improvement: 2.5-4 seconds
   - Poor: >4 seconds
   
   Common LCP Elements:
   - <img> tags
   - <image> inside <svg>
   - <video> poster images
   - Background images with url()
   - Block-level text elements
   
   Optimization Strategies:
   
   A) Server Response Time (TTFB):
      - Target: <600ms
      - Use CDN for static assets
      - Enable HTTP/2 or HTTP/3
      - Optimize database queries
      - Server-side caching (Redis, Varnish)
      - Edge caching (Cloudflare, Fastly)
   
   B) Resource Loading:
      - Preload LCP image: <link rel="preload" as="image" href="hero.jpg">
      - Use modern formats: AVIF (best) > WebP > JPEG
      - Optimize image size: Match display size, compress properly
      - Use CDN: Faster delivery, automatic optimization
      - Lazy load below-fold images only (NOT LCP image!)
   
   C) Render Blocking:
      - Inline critical CSS (<style> in <head>)
      - Defer non-critical CSS
      - Defer JavaScript: <script defer src="app.js">
      - Minimize JavaScript execution before LCP
   
   D) Client-side Rendering:
      - Avoid heavy JavaScript before LCP renders
      - Use Server-Side Rendering (SSR) or Static Generation
      - Progressive enhancement approach
   
   Measurement Code:
   new PerformanceObserver((list) => {
     const entries = list.getEntries();
     const lastEntry = entries[entries.length - 1];
     console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
   }).observe({type: 'largest-contentful-paint', buffered: true});

2. INP (INTERACTION TO NEXT PAINT):
   
   What It Measures:
   - Latency of ALL user interactions (clicks, taps, keyboard)
   - Replaces FID (First Input Delay) in 2024
   
   Thresholds:
   - Good: <200 milliseconds
   - Needs Improvement: 200-500ms
   - Poor: >500ms
   
   Interaction Types:
   - Click events
   - Tap events (mobile)
   - Keyboard events
   
   Optimization Strategies:
   
   A) Break Up Long Tasks:
      Long Task = JavaScript execution >50ms
      
      Bad:
      function processData(data) {
        // 500ms of synchronous work
        for (let item of data) {
          processItem(item); // Heavy computation
        }
      }
      
      Good:
      async function processData(data) {
        for (let item of data) {
          await processItem(item);
          // Yield to main thread every iteration
          await new Promise(resolve => setTimeout(resolve, 0));
        }
      }
   
   B) Use Web Workers:
      // Main thread
      const worker = new Worker('heavy-work.js');
      worker.postMessage(data);
      worker.onmessage = (e) => {
        console.log('Result:', e.data);
      };
      
      // heavy-work.js
      onmessage = (e) => {
        const result = heavyComputation(e.data);
        postMessage(result);
      };
   
   C) Optimize Event Handlers:
      - Debounce scroll/resize handlers
      - Use passive event listeners
      - Minimize DOM manipulation
      
      // Passive listeners (better scrolling)
      element.addEventListener('touchstart', handler, {passive: true});
      
      // Debouncing
      let timeout;
      window.addEventListener('resize', () => {
        clearTimeout(timeout);
        timeout = setTimeout(handleResize, 100);
      });
   
   D) Code Splitting:
      - Load only needed code for current page
      - Dynamic imports for heavy features
      
      // Dynamic import
      button.addEventListener('click', async () => {
        const {heavyFeature} = await import('./heavy-feature.js');
        heavyFeature();
      });
   
   E) Defer Non-Critical JavaScript:
      <script defer src="analytics.js"></script>
      <script defer src="chatbot.js"></script>

3. CLS (CUMULATIVE LAYOUT SHIFT):
   
   What It Measures:
   - Visual stability - unexpected layout shifts
   - Sum of all unexpected shift scores
   
   Thresholds:
   - Good: <0.1
   - Needs Improvement: 0.1-0.25
   - Poor: >0.25
   
   Calculation:
   Layout Shift Score = Impact Fraction × Distance Fraction
   
   Common Causes:
   - Images without dimensions
   - Ads/embeds/iframes without reserved space
   - Fonts causing FOIT/FOUT
   - Dynamically injected content
   - Animations using top/left/width/height
   
   Optimization Strategies:
   
   A) Set Explicit Dimensions:
      Bad:
      <img src="hero.jpg" alt="Hero">
      
      Good:
      <img src="hero.jpg" alt="Hero" width="1200" height="600">
      
      Or with CSS:
      img {
        aspect-ratio: 16 / 9;
        width: 100%;
        height: auto;
      }
   
   B) Reserve Space for Ads/Embeds:
      .ad-container {
        min-height: 250px; /* Reserve space */
      }
   
   C) Font Loading Strategy:
      /* Preload critical fonts */
      <link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
      
      /* Use font-display */
      @font-face {
        font-family: 'MyFont';
        src: url('font.woff2') format('woff2');
        font-display: swap; /* or optional */
      }
   
   D) Avoid Inserting Content Above Existing:
      Bad:
      header.innerHTML = newContent + header.innerHTML;
      
      Good:
      header.insertAdjacentHTML('beforeend', newContent);
   
   E) Use Transform for Animations:
      Bad:
      .element {
        animation: slide 1s;
      }
      @keyframes slide {
        from { top: 0; }
        to { top: 100px; }
      }
      
      Good:
      .element {
        animation: slide 1s;
      }
      @keyframes slide {
        from { transform: translateY(0); }
        to { transform: translateY(100px); }
      }
   
   Measurement Code:
   let clsScore = 0;
   new PerformanceObserver((list) => {
     for (const entry of list.getEntries()) {
       if (!entry.hadRecentInput) {
         clsScore += entry.value;
         console.log('Current CLS:', clsScore);
       }
     }
   }).observe({type: 'layout-shift', buffered: true});

ADDITIONAL METRICS:

4. TTFB (Time to First Byte):
   - Good: <600ms
   - Measure server response time
   - Optimize with CDN, caching, faster hosting

5. FCP (First Contentful Paint):
   - Good: <1.8s
   - First text/image rendered
   - Eliminate render-blocking resources

6. TTI (Time to Interactive):
   - Good: <3.8s
   - Page fully interactive
   - Minimize JavaScript execution time
"""


# ============================================================================
# HTTP/2 & HTTP/3 - Modern Protocol Optimization
# ============================================================================

HTTP2_HTTP3_COMPLETE = """
HTTP/2 & HTTP/3 - Complete Modern Web Performance:

CRITICAL: The old advice to "concatenate CSS/JS files" is OUTDATED (2015 era)

HTTP/1.1 LIMITATIONS (Old):
- Only 6 parallel connections per domain
- Head-of-line blocking
- No multiplexing
- Solution was: Concatenate all CSS/JS into single files

HTTP/2 ADVANTAGES (Current - 2015+):
✓ Multiplexing: Multiple requests over single connection
✓ Header compression: Smaller request/response headers
✓ Server Push: Proactive resource delivery
✓ Binary protocol: Faster parsing
✓ Stream prioritization: Critical resources first

HTTP/3 ADVANTAGES (Latest - 2020+):
✓ QUIC protocol: UDP instead of TCP
✓ Faster connection establishment
✓ Better packet loss recovery
✓ Built-in encryption
✓ Zero round-trip time (0-RTT) resumption

MODERN BEST PRACTICES (2025):

1. MULTIPLE SMALL FILES ARE GOOD:
   
   Why:
   - Better browser caching (change 1 file, cache rest)
   - Parallel loading via HTTP/2 multiplexing
   - Selective loading (only load what's needed)
   - Easier code splitting
   
   Example:
   Good (HTTP/2):
   <link rel="stylesheet" href="base.css">
   <link rel="stylesheet" href="header.css">
   <link rel="stylesheet" href="footer.css">
   <script src="utils.js"></script>
   <script src="components.js"></script>
   
   Bad (HTTP/1.1 thinking):
   <link rel="stylesheet" href="all-styles.min.css"> // 500KB monolith
   <script src="all-scripts.min.js"></script> // 2MB monolith

2. RESOURCE LOADING STRATEGIES:
   
   A) Critical CSS:
      Inline above-the-fold styles in <head>:
      <style>
        /* Critical styles for immediate render */
        .header { ... }
        .hero { ... }
      </style>
      
      Load rest async:
      <link rel="preload" href="non-critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
   
   B) JavaScript Loading:
      - defer: Execute after HTML parsing (maintains order)
      - async: Execute ASAP (no order guarantee)
      - type="module": Automatic defer + modern syntax
      
      <script defer src="app.js"></script>
      <script async src="analytics.js"></script>
      <script type="module" src="modern-app.js"></script>
   
   C) Resource Hints:
      dns-prefetch: Resolve DNS early
      <link rel="dns-prefetch" href="//cdn.example.com">
      
      preconnect: Establish connection early
      <link rel="preconnect" href="https://api.example.com">
      
      prefetch: Load for next navigation
      <link rel="prefetch" href="next-page.html">
      
      preload: Load critical resource now
      <link rel="preload" href="hero.jpg" as="image">

3. CODE SPLITTING:
   
   Route-based splitting:
   // Load different code per page
   if (page === 'product') {
     import('./product-page.js');
   } else if (page === 'cart') {
     import('./cart.js');
   }
   
   Feature-based splitting:
   // Load features on-demand
   button.addEventListener('click', async () => {
     const {Modal} = await import('./modal.js');
     new Modal().show();
   });
   
   Vendor splitting:
   // Separate vendor code (better caching)
   vendors.js  // React, libraries (changes rarely)
   app.js      // Your code (changes often)

4. CACHING STRATEGY:
   
   File-level cache invalidation:
   style.abc123.css  // Hash in filename
   app.xyz789.js
   
   When file changes, hash changes, new file downloaded
   Unchanged files stay cached
   
   Cache-Control Headers:
   # Static assets (1 year)
   Cache-Control: public, max-age=31536000, immutable
   
   # HTML (validate every time)
   Cache-Control: no-cache
   
   # API responses (5 minutes)
   Cache-Control: public, max-age=300

5. COMPRESSION:
   
   Enable Brotli (better than gzip):
   - 15-25% better compression than gzip
   - Support: All modern browsers
   - Server: Enable brotli compression
   
   Fallback to gzip for older browsers
   
   Accept-Encoding: br, gzip, deflate
"""

# ============================================================================
# IMAGE OPTIMIZATION - Complete Modern Guide
# ============================================================================

IMAGE_OPTIMIZATION_COMPLETE = """
Modern Image Optimization (2025) - Complete Guide:

1. FORMAT SELECTION:
   
   AVIF (AV1 Image Format) - BEST:
   - 50% smaller than JPEG at same quality
   - Better than WebP for most images
   - Support: Chrome 85+, Firefox 93+, Safari 16+
   
   WebP - GOOD FALLBACK:
   - 25-35% smaller than JPEG
   - Wide browser support
   - Support: All modern browsers
   
   JPEG - LEGACY FALLBACK:
   - Universal support
   - Use for old browsers only
   
   PNG - For transparency/graphics:
   - Lossless compression
   - Use for logos, icons with transparency
   
   SVG - For vector graphics:
   - Infinitely scalable
   - Small file size
   - Use for icons, logos, illustrations

2. RESPONSIVE IMAGES:
   
   Picture Element (best):
   <picture>
     <source 
       srcset="hero.avif" 
       type="image/avif">
     <source 
       srcset="hero.webp" 
       type="image/webp">
     <img 
       src="hero.jpg" 
       alt="Hero image"
       width="1200" 
       height="600"
       loading="lazy">
   </picture>
   
   Srcset for Different Sizes:
   <img 
     srcset="small.jpg 400w,
             medium.jpg 800w,
             large.jpg 1200w"
     sizes="(max-width: 640px) 400px,
            (max-width: 1024px) 800px,
            1200px"
     src="large.jpg"
     alt="Responsive image">
   
   Browser picks appropriate size based on:
   - Screen width
   - Device pixel ratio (Retina displays)
   - Network conditions

3. LAZY LOADING:
   
   Native Lazy Loading:
   <img src="image.jpg" loading="lazy" alt="...">
   
   Rules:
   - Use for below-the-fold images only
   - DO NOT lazy load LCP image (hurts performance)
   - DO NOT lazy load above-the-fold images
   
   Intersection Observer (advanced):
   const observer = new IntersectionObserver((entries) => {
     entries.forEach(entry => {
       if (entry.isIntersecting) {
         const img = entry.target;
         img.src = img.dataset.src;
         observer.unobserve(img);
       }
     });
   });
   
   document.querySelectorAll('img[data-src]').forEach(img => {
     observer.observe(img);
   });

4. OPTIMIZATION TECHNIQUES:
   
   A) Compression:
      - JPEG: 80-85% quality (sweet spot)
      - WebP: 75-80% quality
      - AVIF: 50-60% quality (better algorithm)
      - Use tools: ImageOptim, Squoosh, Sharp
   
   B) Proper Sizing:
      - Don't serve 3000x2000px for 400x300px display
      - Generate multiple sizes (thumbnails, medium, large)
      - Use srcset to serve appropriate size
   
   C) CDN with Auto-Optimization:
      - Cloudinary: Automatic format selection
      - Cloudflare Images: On-the-fly optimization
      - Imgix: Real-time image processing
      - Shopify CDN: Automatic resizing/format
   
   D) Dimensions:
      Always set width/height to prevent CLS:
      <img src="image.jpg" width="800" height="600" alt="...">
      
      Or use aspect-ratio:
      img {
        aspect-ratio: 16 / 9;
        width: 100%;
        height: auto;
      }

5. SHOPIFY-SPECIFIC:
   
   Shopify Image Filters:
   {{ product.featured_image | image_url: width: 800 }}
   
   Multiple sizes:
   <img 
     srcset="{{ product.featured_image | image_url: width: 400 }} 400w,
             {{ product.featured_image | image_url: width: 800 }} 800w,
             {{ product.featured_image | image_url: width: 1200 }} 1200w"
     sizes="(max-width: 640px) 400px, 800px"
     src="{{ product.featured_image | image_url: width: 800 }}"
     alt="{{ product.title }}">
   
   Shopify automatically serves WebP to supporting browsers!
"""

# ============================================================================
# JAVASCRIPT OPTIMIZATION - Complete Guide
# ============================================================================

JAVASCRIPT_OPTIMIZATION_COMPLETE = """
JavaScript Performance Optimization - Complete Guide:

1. CODE SPLITTING:
   
   Why Split Code:
   - Reduce initial bundle size
   - Load only what's needed for current page
   - Faster Time to Interactive (TTI)
   - Better caching (change one module, rest stay cached)
   
   Route-Based Splitting:
   // React example
   const ProductPage = lazy(() => import('./ProductPage'));
   const CartPage = lazy(() => import('./CartPage'));
   
   <Suspense fallback={<Loading />}>
     <Route path="/product" component={ProductPage} />
     <Route path="/cart" component={CartPage} />
   </Suspense>
   
   Feature-Based Splitting:
   // Load feature on-demand
   button.addEventListener('click', async () => {
     const {VideoPlayer} = await import('./video-player.js');
     new VideoPlayer().play();
   });

2. TREE SHAKING:
   
   What It Is:
   - Remove unused code from bundles
   - Dead code elimination
   - Requires ES6 modules (import/export)
   
   Bad (CommonJS - can't tree shake):
   const utils = require('./utils');
   
   Good (ES6 - tree shakeable):
   import {neededFunction} from './utils';
   
   Package.json:
   {
     "sideEffects": false  // Tells bundler: safe to remove unused exports
   }

3. DEFER & ASYNC:
   
   Normal (blocking):
   <script src="app.js"></script>
   - Stops HTML parsing
   - Downloads script
   - Executes immediately
   - Then continues parsing
   
   Defer (non-blocking, ordered):
   <script defer src="app.js"></script>
   - Downloads in parallel with HTML parsing
   - Executes after HTML parsing complete
   - Maintains script order
   - Best for: Scripts that need DOM or other scripts
   
   Async (non-blocking, unordered):
   <script async src="analytics.js"></script>
   - Downloads in parallel
   - Executes as soon as downloaded (pauses parsing)
   - No order guarantee
   - Best for: Independent scripts (analytics, ads)
   
   Module (auto-defer):
   <script type="module" src="app.js"></script>
   - Automatically deferred
   - Modern syntax (import/export)
   - Strict mode by default

4. MINIMIZE MAIN THREAD WORK:
   
   Long Tasks (>50ms):
   Bad:
   function processAllData(data) {
     for (let item of data) {  // 1000 items = 500ms
       heavyProcessing(item);
     }
   }
   
   Good (chunked):
   async function processAllData(data) {
     for (let i = 0; i < data.length; i += 10) {
       const chunk = data.slice(i, i + 10);
       chunk.forEach(item => heavyProcessing(item));
       await new Promise(r => setTimeout(r, 0)); // Yield to browser
     }
   }
   
   Good (requestIdleCallback):
   function processInIdle(data) {
     requestIdleCallback(deadline => {
       while (deadline.timeRemaining() > 0 && data.length > 0) {
         const item = data.shift();
         heavyProcessing(item);
       }
       if (data.length > 0) {
         processInIdle(data); // Continue when idle
       }
     });
   }

5. WEB WORKERS:
   
   Offload Heavy Computation:
   // main.js
   const worker = new Worker('worker.js');
   worker.postMessage({data: largeDataset});
   worker.onmessage = (e) => {
     console.log('Result:', e.data);
   };
   
   // worker.js
   onmessage = (e) => {
     const result = heavyCalculation(e.data);
     postMessage(result);
   };
   
   Use Cases:
   - Data processing
   - Image manipulation
   - Cryptography
   - Complex calculations
   - JSON parsing (large files)

6. PERFORMANCE API:
   
   Measure Performance:
   // Mark start
   performance.mark('function-start');
   
   expensiveFunction();
   
   // Mark end
   performance.mark('function-end');
   
   // Measure
   performance.measure('function-duration', 'function-start', 'function-end');
   
   // Get results
   const measures = performance.getEntriesByType('measure');
   console.log(measures[0].duration);
   
   Monitor Long Tasks:
   new PerformanceObserver((list) => {
     for (const entry of list.getEntries()) {
       console.log('Long task detected:', entry.duration);
     }
   }).observe({entryTypes: ['longtask']});
"""


# ============================================================================
# CACHING STRATEGIES - Complete Implementation
# ============================================================================

CACHING_COMPLETE = """
Caching Strategies - Complete Performance Guide:

1. BROWSER CACHING (HTTP Headers):
   
   Cache-Control Header:
   
   Immutable Static Assets (CSS, JS, Images with hash):
   Cache-Control: public, max-age=31536000, immutable
   - Cache for 1 year
   - "immutable" tells browser: never revalidate
   - Use with versioned filenames: app.abc123.js
   
   HTML Pages:
   Cache-Control: no-cache
   - Validate with server every time
   - Can still use cached version if 304 Not Modified
   
   API Responses (short-lived):
   Cache-Control: public, max-age=300
   - Cache for 5 minutes
   - Good for: Product data, prices
   
   Private Data:
   Cache-Control: private, max-age=3600
   - Cache only in user's browser (not CDN)
   - Good for: User-specific data
   
   No Caching:
   Cache-Control: no-store
   - Never cache (sensitive data)
   - Good for: Checkout, account pages

2. SERVICE WORKERS:
   
   Cache-First Strategy (static assets):
   self.addEventListener('fetch', (event) => {
     event.respondWith(
       caches.match(event.request)
         .then(response => response || fetch(event.request))
     );
   });
   
   Network-First Strategy (dynamic content):
   self.addEventListener('fetch', (event) => {
     event.respondWith(
       fetch(event.request)
         .catch(() => caches.match(event.request))
     );
   });
   
   Stale-While-Revalidate (best UX):
   self.addEventListener('fetch', (event) => {
     event.respondWith(
       caches.open('my-cache').then(cache => {
         return cache.match(event.request).then(response => {
           const fetchPromise = fetch(event.request).then(networkResponse => {
             cache.put(event.request, networkResponse.clone());
             return networkResponse;
           });
           return response || fetchPromise;
         });
       })
     );
   });

3. CDN CACHING:
   
   Edge Caching:
   - Content served from nearest location
   - Reduces TTFB (Time to First Byte)
   - Geographic distribution
   
   Popular CDNs:
   - Cloudflare (fastest, best DDoS protection)
   - Fastly (programmable edge)
   - Amazon CloudFront (AWS integration)
   - Shopify CDN (automatic for Shopify stores)
   
   Cache-Control for CDN:
   Cache-Control: public, s-maxage=86400, max-age=3600
   - s-maxage: CDN caches for 24 hours
   - max-age: Browser caches for 1 hour

4. VERSIONED FILENAMES:
   
   Content-Based Hashing:
   app.js → app.abc123.js (hash changes when content changes)
   
   Benefits:
   - Aggressive caching (1 year+)
   - Instant invalidation when file changes
   - No cache busting query strings (?v=123)
   
   Webpack/Vite Configuration:
   output: {
     filename: '[name].[contenthash].js'
   }

5. RESOURCE HINTS:
   
   DNS Prefetch:
   <link rel="dns-prefetch" href="//cdn.example.com">
   - Resolve DNS before resource needed
   - Save ~20-120ms per domain
   
   Preconnect:
   <link rel="preconnect" href="https://fonts.googleapis.com">
   - DNS + TCP + TLS handshake
   - Save ~100-500ms per connection
   
   Prefetch (next page):
   <link rel="prefetch" href="/next-page.html">
   - Load during idle time
   - Ready for next navigation
   
   Preload (current page):
   <link rel="preload" href="critical.css" as="style">
   - High priority loading
   - Use for critical resources
"""

# ============================================================================
# PERFORMANCE MONITORING - Complete Toolkit
# ============================================================================

PERFORMANCE_MONITORING = """
Performance Monitoring - Complete Real User Monitoring (RUM):

1. CHROME USER EXPERIENCE REPORT (CrUX):
   
   What It Is:
   - Real user data from Chrome browsers
   - 28-day rolling average
   - Used for Google Search rankings
   - Available in PageSpeed Insights
   
   Accessing CrUX Data:
   - PageSpeed Insights API
   - BigQuery (raw data)
   - Chrome UX Report Dashboard
   - Google Search Console (Core Web Vitals report)
   
   Metrics Included:
   - LCP, INP, CLS (Core Web Vitals)
   - FCP, TTFB
   - By connection type (4G, 3G, etc.)
   - By device type (phone, desktop, tablet)

2. PERFORMANCE API (Rum Implementation):
   
   Complete RUM Script:
   // Core Web Vitals
   import {onCLS, onINP, onLCP} from 'web-vitals';
   
   function sendToAnalytics(metric) {
     const body = JSON.stringify({
       name: metric.name,
       value: metric.value,
       id: metric.id,
       rating: metric.rating
     });
     
     // Use sendBeacon (guaranteed delivery)
     navigator.sendBeacon('/analytics', body);
   }
   
   onCLS(sendToAnalytics);
   onINP(sendToAnalytics);
   onLCP(sendToAnalytics);
   
   // Navigation Timing
   window.addEventListener('load', () => {
     const nav = performance.getEntriesByType('navigation')[0];
     console.log('TTFB:', nav.responseStart - nav.requestStart);
     console.log('DOM Ready:', nav.domContentLoadedEventEnd - nav.requestStart);
     console.log('Page Load:', nav.loadEventEnd - nav.requestStart);
   });
   
   // Resource Timing
   const resources = performance.getEntriesByType('resource');
   resources.forEach(resource => {
     if (resource.duration > 1000) {
       console.log('Slow resource:', resource.name, resource.duration);
     }
   });

3. PERFORMANCE BUDGETS:
   
   Set Limits:
   {
     "budgets": [
       {
         "path": "/*",
         "timings": [
           {"metric": "interactive", "budget": 3800},
           {"metric": "first-contentful-paint", "budget": 1800}
         ],
         "resourceSizes": [
           {"resourceType": "script", "budget": 300},
           {"resourceType": "stylesheet", "budget": 100},
           {"resourceType": "image", "budget": 500}
         ]
       }
     ]
   }
   
   Enforcement:
   - Lighthouse CI (fail builds if over budget)
   - Webpack Performance Hints
   - Bundle analyzers
   
   webpack.config.js:
   performance: {
     maxAssetSize: 300000,  // 300KB
     maxEntrypointSize: 500000,  // 500KB
     hints: 'error'  // Fail build if exceeded
   }

4. MONITORING TOOLS:
   
   Synthetic Monitoring (Lab):
   - Lighthouse CI (automated testing)
   - WebPageTest (detailed waterfall)
   - SpeedCurve (continuous monitoring)
   - Chrome DevTools (local debugging)
   
   Real User Monitoring (Field):
   - Google Analytics 4 (web vitals integration)
   - Sentry Performance
   - New Relic Browser
   - Datadog RUM
   - Custom RUM (Performance API)
   
   Shopify-Specific:
   - Shopify Speed Report (admin dashboard)
   - Online Store Speed score
   - PageSpeed Insights integration
"""

# ============================================================================
# HELPER FUNCTION - Smart Recommendations
# ============================================================================

def get_recommendation(metric, current_value):
    """
    Generate performance recommendation based on metric and current value
    
    Args:
        metric (str): Performance metric (lcp, inp, cls, ttfb, etc.)
        current_value (float): Current measured value
    
    Returns:
        list: Prioritized recommendations for improvement
    """
    recommendations = {
        'lcp': {
            'critical': [
                'CRITICAL: Preload LCP image with <link rel="preload" as="image" href="hero.jpg">',
                'Use modern image format (AVIF > WebP > JPEG) for LCP image',
                'Enable CDN for faster image delivery',
                'Optimize server response time (TTFB < 600ms)'
            ],
            'high': [
                'Implement lazy loading for below-fold images only',
                'Use responsive images with srcset for proper sizing',
                'Inline critical CSS to eliminate render-blocking',
                'Defer non-critical JavaScript'
            ],
            'medium': [
                'Enable HTTP/2 or HTTP/3 on server',
                'Compress images (target <200KB for LCP image)',
                'Use Service Worker for caching strategy',
                'Implement resource hints (dns-prefetch, preconnect)'
            ]
        },
        'inp': {
            'critical': [
                'CRITICAL: Break up long JavaScript tasks (>50ms)',
                'Defer heavy JavaScript execution until after page load',
                'Use Web Workers for heavy computation',
                'Optimize event handlers (debounce, passive listeners)'
            ],
            'high': [
                'Implement code splitting (load only needed JavaScript)',
                'Use requestIdleCallback for low-priority work',
                'Remove or defer third-party scripts',
                'Minimize DOM manipulation in event handlers'
            ],
            'medium': [
                'Enable JavaScript tree shaking',
                'Use modern build tools (Vite, esbuild)',
                'Implement dynamic imports for features',
                'Profile with Chrome DevTools Performance tab'
            ]
        },
        'cls': {
            'critical': [
                'CRITICAL: Set explicit width/height on all images',
                'Reserve space for ads/embeds with min-height',
                'Preload fonts to prevent FOIT/FOUT',
                'Avoid inserting content above existing content'
            ],
            'high': [
                'Use CSS aspect-ratio for responsive images',
                'Set font-display: swap for web fonts',
                'Add skeleton screens for dynamic content',
                'Use CSS transform for animations (not top/left)'
            ],
            'medium': [
                'Measure CLS with Performance Observer',
                'Test on real devices (mobile has higher CLS)',
                'Use Lighthouse to identify shifting elements',
                'Implement proper loading states'
            ]
        },
        'ttfb': {
            'critical': [
                'CRITICAL: Enable CDN for edge caching',
                'Optimize database queries',
                'Enable server-side caching (Redis, Varnish)',
                'Upgrade to HTTP/2 or HTTP/3'
            ],
            'high': [
                'Reduce server processing time',
                'Enable compression (Brotli > gzip)',
                'Optimize third-party API calls',
                'Use faster hosting/upgrade server'
            ],
            'medium': [
                'Implement edge computing (Cloudflare Workers)',
                'Use static site generation where possible',
                'Monitor server performance metrics',
                'Optimize backend code efficiency'
            ]
        },
        'fcp': {
            'critical': [
                'Eliminate render-blocking CSS/JavaScript',
                'Inline critical CSS in <head>',
                'Use font-display: swap for web fonts',
                'Preload critical resources'
            ],
            'high': [
                'Defer non-critical CSS loading',
                'Minimize CSS file size (remove unused)',
                'Use modern CSS (avoid @import)',
                'Optimize web font loading'
            ],
            'medium': [
                'Enable HTTP/2 server push for critical assets',
                'Use resource hints (preconnect, dns-prefetch)',
                'Implement Service Worker caching',
                'Monitor with Lighthouse CI'
            ]
        },
        'tbt': {
            'critical': [
                'Break up long tasks into smaller chunks',
                'Defer JavaScript execution with defer/async',
                'Remove unused JavaScript (tree shaking)',
                'Use code splitting for large bundles'
            ],
            'high': [
                'Implement lazy loading for features',
                'Use Web Workers for heavy processing',
                'Optimize third-party scripts',
                'Profile with Chrome DevTools Performance'
            ],
            'medium': [
                'Use requestIdleCallback for non-critical work',
                'Implement performance budgets',
                'Monitor with Lighthouse CI',
                'Use modern JavaScript syntax (smaller bundles)'
            ]
        }
    }
    
    metric_lower = metric.lower()
    
    if metric_lower not in recommendations:
        return [f'Monitor {metric} performance and consult Web.dev documentation']
    
    # Determine severity based on value (simplified logic)
    # You can make this more sophisticated based on actual thresholds
    if current_value is None:
        return recommendations[metric_lower].get('high', [])
    
    # Return all recommendations for the metric, prioritized
    all_recs = []
    all_recs.extend(recommendations[metric_lower].get('critical', []))
    all_recs.extend(recommendations[metric_lower].get('high', []))
    all_recs.extend(recommendations[metric_lower].get('medium', []))
    
    return all_recs[:5]  # Return top 5 recommendations

