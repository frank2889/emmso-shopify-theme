"""
Marcus - Performance Analyst for EMMSO AI System
================================================

🎓 CERTIFICATIONS & EXPERTISE:
- Google PageSpeed Insights Certified
- Web.dev Performance Expert
- Lighthouse Performance Specialist
- Core Web Vitals Authority
- HTTP/2 & HTTP/3 Optimization Expert

Specializes in:
- Site speed optimization
- Core Web Vitals analysis
- Lighthouse performance audits
- Resource optimization
- Caching strategies
- Mobile performance
+ GPT-4 Vision voor Performance-focused screenshot analyse

════════════════════════════════════════════════════════════════════════════════
EXPERT KNOWLEDGE BASE - Web Performance Optimization (Complete 2025)
════════════════════════════════════════════════════════════════════════════════
Based on: Web.dev Learn Performance + Google PageSpeed + Lighthouse + HTTP Archive
Total Knowledge: ~20,000 tokens of expert performance optimization

CORE WEB VITALS (Google Ranking Factors 2025):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. LCP (Largest Contentful Paint) - Main Content Load Speed:
   ✅ GOOD: <2.5s | ⚠️ NEEDS IMPROVEMENT: 2.5-4s | ❌ POOR: >4s
   
   Optimization Strategies:
   - Server-side: Fast TTFB (<600ms), CDN, edge caching, HTTP/2 push
   - Images: fetchpriority="high" + preload for hero, AVIF/WebP formats
   - Fonts: Preload critical fonts, font-display: swap, subset fonts
   - CSS: Inline critical CSS (<14KB), defer non-critical, remove unused
   - JavaScript: Defer/async non-critical JS, code splitting, tree shaking
   
   Common LCP Elements:
   - Hero images (most common)
   - Hero text blocks with background
   - Video thumbnails
   - Full-width banners
   
   Measurement:
   ```javascript
   new PerformanceObserver((list) => {
     const entries = list.getEntries();
     const lastEntry = entries[entries.length - 1];
     console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
   }).observe({entryTypes: ['largest-contentful-paint']});
   ```

2. CLS (Cumulative Layout Shift) - Visual Stability:
   ✅ GOOD: <0.1 | ⚠️ NEEDS IMPROVEMENT: 0.1-0.25 | ❌ POOR: >0.25
   
   Prevention Strategies:
   - Images/Video: ALWAYS set width + height attributes
   - Fonts: Use font-display: optional or swap, preload fonts
   - Ads: Reserve space with min-height, avoid inserting above content
   - Dynamic content: Reserve space before injection
   - Animations: Use transform/opacity only (GPU-accelerated)
   - CSS: Avoid layout-shifting properties (top, left, width, height)
   
   Measurement:
   ```javascript
   let cls = 0;
   new PerformanceObserver((list) => {
     for (const entry of list.getEntries()) {
       if (!entry.hadRecentInput) {
         cls += entry.value;
         console.log('Current CLS:', cls);
       }
     }
   }).observe({entryTypes: ['layout-shift']});
   ```

3. INP (Interaction to Next Paint) - Replaces FID in 2024+:
   ✅ GOOD: <200ms | ⚠️ NEEDS IMPROVEMENT: 200-500ms | ❌ POOR: >500ms
   
   Optimization Strategies:
   - Long tasks: Break up tasks >50ms with setTimeout/requestIdleCallback
   - Input delay: Minimize event handler execution time
   - Web Workers: Offload heavy computation to workers
   - debounce/throttle: For scroll, resize, input events
   - Passive listeners: Use {passive: true} for touch/wheel
   
   Measurement:
   ```javascript
   new PerformanceObserver((list) => {
     for (const entry of list.getEntries()) {
       console.log('INP:', entry.duration, entry.name);
     }
   }).observe({type: 'event', buffered: true, durationThreshold: 16});
   ```

LIGHTHOUSE PERFORMANCE SCORING (100-point scale):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Weighted Metrics:
- FCP (First Contentful Paint): 10% weight - Target <1.8s
- SI (Speed Index): 10% weight - Target <3.4s
- LCP (Largest Contentful Paint): 25% weight - Target <2.5s
- TTI (Time to Interactive): 10% weight - Target <3.8s
- TBT (Total Blocking Time): 30% weight - Target <200ms
- CLS (Cumulative Layout Shift): 15% weight - Target <0.1

Performance Budget Guidelines:
- HTML: <50KB compressed
- CSS: <100KB total, <14KB critical inline
- JavaScript: <200KB total, <50KB initial bundle
- Images: Properly sized, next-gen formats (AVIF/WebP)
- Fonts: <100KB total, 1-2 font families max

RESOURCE LOADING OPTIMIZATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Critical Rendering Path:
   HTML → Parse → DOM → CSSOM → Render Tree → Layout → Paint
   
   Optimize by:
   - Minimize critical resources (HTML, CSS, fonts)
   - Inline critical CSS (<14KB)
   - Defer non-critical CSS: <link rel="preload" as="style" onload="this.rel='stylesheet'">
   - Defer JavaScript: <script defer src="app.js">
   - Remove render-blocking resources

2. Resource Hints (Preconnect, Prefetch, Preload):
   ```html
   <!-- Critical: Connect to required origins early -->
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="dns-prefetch" href="https://analytics.google.com">
   
   <!-- High Priority: Load critical resources ASAP -->
   <link rel="preload" as="image" href="hero.jpg" fetchpriority="high">
   <link rel="preload" as="font" href="font.woff2" type="font/woff2" crossorigin>
   <link rel="preload" as="style" href="critical.css">
   
   <!-- Low Priority: Prefetch future navigation resources -->
   <link rel="prefetch" href="/next-page.html">
   <link rel="modulepreload" href="module.js">
   ```

3. HTTP/2 & HTTP/3 Optimization:
   ✅ DO: Multiple small files (parallel multiplexing)
   ✅ DO: Server Push for critical resources
   ✅ DO: Enable compression (Brotli > Gzip)
   ❌ DON'T: Bundle everything into 1 file (kills caching)
   ❌ DON'T: Domain sharding (HTTP/1.1 technique)

IMAGE OPTIMIZATION (Complete Guide):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Modern Formats (Compression Comparison):
   - AVIF: 50% smaller than JPEG, excellent quality (NEW - best choice 2025)
   - WebP: 30% smaller than JPEG, great browser support
   - JPEG XL: Emerging format, not yet widely supported
   - JPEG: Universal fallback
   - PNG: Use only for transparency/logos
   
2. Responsive Images (Modern <picture> Syntax):
   ```html
   <picture>
     <!-- AVIF - Best compression -->
     <source type="image/avif" 
             srcset="hero-400.avif 400w,
                     hero-800.avif 800w,
                     hero-1200.avif 1200w"
             sizes="(min-width: 768px) 50vw, 100vw">
     
     <!-- WebP - Good fallback -->
     <source type="image/webp"
             srcset="hero-400.webp 400w,
                     hero-800.webp 800w,
                     hero-1200.webp 1200w"
             sizes="(min-width: 768px) 50vw, 100vw">
     
     <!-- JPEG - Universal fallback -->
     <img src="hero-800.jpg"
          srcset="hero-400.jpg 400w,
                  hero-800.jpg 800w,
                  hero-1200.jpg 1200w"
          sizes="(min-width: 768px) 50vw, 100vw"
          alt="Hero image"
          width="1200"
          height="600"
          loading="lazy"
          fetchpriority="high">
   </picture>
   ```

3. Loading Strategies:
   - Above fold (LCP): fetchpriority="high" + loading="eager" + preload
   - Below fold: loading="lazy" (saves ~50% bandwidth)
   - Carousels: Load first visible, lazy load rest
   - Thumbnails: Smaller sizes with proper srcset
   
4. Image CDN & Transformations:
   - Use image CDN (Cloudinary, Imgix, Shopify CDN)
   - Auto-format: Serve AVIF/WebP based on browser support
   - Auto-quality: Optimize quality based on viewport
   - Auto-resize: Generate responsive sizes on-the-fly

JAVASCRIPT OPTIMIZATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Loading Strategies:
   ```html
   <!-- Critical scripts (rare): Inline or sync -->
   <script>/* Critical JS */</script>
   
   <!-- Normal scripts: Use defer (maintains order) -->
   <script defer src="app.js"></script>
   
   <!-- Independent scripts: Use async (analytics, ads) -->
   <script async src="analytics.js"></script>
   
   <!-- Module scripts: Native ES6 modules -->
   <script type="module" src="app.mjs"></script>
   ```

2. Code Splitting:
   ```javascript
   // Dynamic import - only load when needed
   button.addEventListener('click', async () => {
     const module = await import('./heavy-feature.js');
     module.init();
   });
   
   // Route-based splitting
   const routes = {
     '/products': () => import('./pages/products.js'),
     '/cart': () => import('./pages/cart.js')
   };
   ```

3. Tree Shaking & Dead Code Elimination:
   - Use ES6 modules (import/export)
   - Avoid CommonJS (require/module.exports)
   - Use production builds: webpack -p, Rollup, esbuild
   - Remove console.log in production

4. Long Task Breaking:
   ```javascript
   // BAD: Blocks main thread
   for (let i = 0; i < 10000; i++) {
     processItem(i);
   }
   
   // GOOD: Yields to browser
   async function processAll() {
     for (let i = 0; i < 10000; i++) {
       processItem(i);
       if (i % 100 === 0) {
         await new Promise(r => setTimeout(r, 0));
       }
     }
   }
   ```

CSS OPTIMIZATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Critical CSS Strategy:
   - Inline critical CSS in <head> (<14KB gzipped)
   - Critical = Above-the-fold styles for first paint
   - Tools: critical, penthouse, critters
   - Defer non-critical: <link rel="preload" as="style">

2. CSS Performance Best Practices:
   - Avoid @import (blocks parallel downloads)
   - Minimize specificity (faster selector matching)
   - Use CSS containment: contain: layout paint
   - Avoid expensive properties: box-shadow, filter, opacity transitions
   - Use will-change sparingly (creates compositing layer)

3. Modern CSS Features:
   - CSS Grid/Flexbox over floats
   - CSS Custom Properties for theming
   - content-visibility: auto for lazy rendering
   - CSS containment for performance isolation

CACHING & CDN STRATEGIES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. HTTP Caching Headers:
   ```
   # Immutable assets (versioned files)
   Cache-Control: public, max-age=31536000, immutable
   
   # HTML (always revalidate)
   Cache-Control: no-cache
   
   # API responses
   Cache-Control: private, max-age=3600, must-revalidate
   ```

2. Service Worker Strategies:
   ```javascript
   // Cache First (for static assets)
   self.addEventListener('fetch', event => {
     event.respondWith(
       caches.match(event.request)
         .then(response => response || fetch(event.request))
     );
   });
   
   // Network First (for dynamic content)
   event.respondWith(
     fetch(event.request)
       .catch(() => caches.match(event.request))
   );
   
   // Stale-While-Revalidate (best of both)
   event.respondWith(
     caches.open('dynamic').then(cache =>
       cache.match(event.request).then(response => {
         const fetchPromise = fetch(event.request).then(networkResponse => {
           cache.put(event.request, networkResponse.clone());
           return networkResponse;
         });
         return response || fetchPromise;
       })
     )
   );
   ```

3. CDN Best Practices:
   - Use for all static assets (CSS, JS, images, fonts)
   - Enable HTTP/2 on CDN
   - Enable Brotli compression
   - Set proper cache headers
   - Use versioned URLs for cache busting

PERFORMANCE MONITORING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Real User Monitoring (RUM):
   ```javascript
   // Web Vitals library
   import {getCLS, getFID, getFCP, getLCP, getTTFB} from 'web-vitals';
   
   function sendToAnalytics({name, value, id}) {
     gtag('event', name, {
       event_category: 'Web Vitals',
       value: Math.round(name === 'CLS' ? value * 1000 : value),
       event_label: id,
       non_interaction: true
     });
   }
   
   getCLS(sendToAnalytics);
   getFID(sendToAnalytics);
   getLCP(sendToAnalytics);
   ```

2. Performance API:
   ```javascript
   // Navigation Timing
   const perfData = performance.getEntriesByType('navigation')[0];
   console.log('DNS:', perfData.domainLookupEnd - perfData.domainLookupStart);
   console.log('TCP:', perfData.connectEnd - perfData.connectStart);
   console.log('TTFB:', perfData.responseStart - perfData.requestStart);
   console.log('Download:', perfData.responseEnd - perfData.responseStart);
   console.log('DOM:', perfData.domContentLoadedEventEnd - perfData.domContentLoadedEventStart);
   
   // Resource Timing
   performance.getEntriesByType('resource').forEach(resource => {
     console.log(resource.name, resource.duration);
   });
   ```

3. Performance Budgets:
   - Set budgets in Lighthouse CI
   - Fail builds if exceeded
   - Monitor trends over time
   - Alert on regressions

════════════════════════════════════════════════════════════════════════════════
END OF EXPERT KNOWLEDGE BASE
════════════════════════════════════════════════════════════════════════════════
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from analyzers.screenshot_analyzer import ScreenshotAnalyzer

class MarcusPerformanceAnalyst:
    """Performance optimization specialist with Core Web Vitals expertise."""
    
    def __init__(self):
        """Initialize Marcus Performance analyst with expert performance knowledge."""
        self.name = "Marcus"
        self.specialty = "Performance"
        self.screenshot_analyzer = ScreenshotAnalyzer()
        self.expertise_areas = [
            'site_speed',
            'core_web_vitals',
            'lighthouse_audits',
            'resource_optimization',
            'caching',
            'mobile_performance',
            'lcp_optimization',
            'cls_prevention',
            'image_performance',
            'code_splitting'
        ]
    
    def analyze(self, site_data: Dict[str, Any], previous_findings: Dict[str, Any] = None, iteration: int = 1) -> Dict[str, Any]:
        """Perform performance analysis of current website."""
        
        print(f"  ⚡ Marcus: Analyzing current website performance...")
        
        # Get project goals
        project_goals = site_data.get('project_goals', {})
        
        # Analyze theme files
        theme_analysis = self._analyze_theme_files(site_data.get('shopify_theme_path'))
        
        # Test preview URL performance
        preview_performance = self._test_preview_performance(site_data.get('shopify_preview_url'))
        
        # Get screenshot analysis from Vision AI (shared data) or analyze ourselves
        screenshot_analysis = None
        if 'vision_screenshot_analysis' in site_data:
            screenshot_analysis = self._process_vision_screenshots_for_performance(site_data['vision_screenshot_analysis'], project_goals)
            print("      📸 Using Vision AI screenshot data")
        else:
            screenshot_analysis = self._analyze_screenshots_performance(site_data, project_goals)
            print("      📸 Performance Analysis: analyzing screenshots independently")
        
        # Calculate score
        score = self._calculate_performance_score(theme_analysis, preview_performance, screenshot_analysis)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(theme_analysis, preview_performance, screenshot_analysis)
        
        analysis_result = {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'iteration': iteration,
            'score': score,
            'findings': {
                'theme_file_analysis': theme_analysis,
                'preview_performance': preview_performance,
                'screenshot_performance_analysis': screenshot_analysis
            },
            'recommendations': recommendations
        }
        
        print(f"    Score: {score}/100")
        return analysis_result
    
    def _analyze_theme_files(self, theme_path):
        """Analyze theme files (CSS, JS, etc) as they are"""
        if not theme_path:
            return {'error': 'No theme path provided'}
        
        import os
        
        try:
            assets_path = os.path.join(theme_path, 'assets')
            if not os.path.exists(assets_path):
                return {'error': 'Assets folder not found'}
            
            asset_files = [f for f in os.listdir(assets_path) if os.path.isfile(os.path.join(assets_path, f))]
            
            # Count CSS files
            css_files = [f for f in asset_files if f.endswith('.css')]
            total_css_size = sum(os.path.getsize(os.path.join(assets_path, f)) for f in css_files)
            
            # Count JS files  
            js_files = [f for f in asset_files if f.endswith('.js')]
            total_js_size = sum(os.path.getsize(os.path.join(assets_path, f)) for f in js_files)
            
            return {
                'css_count': len(css_files),
                'css_files': css_files,
                'total_css_size_kb': round(total_css_size / 1024, 1),
                'js_count': len(js_files),
                'js_files': js_files,
                'total_js_size_kb': round(total_js_size / 1024, 1)
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def _test_preview_performance(self, preview_url):
        """Test preview URL performance"""
        if not preview_url:
            return {'error': 'No preview URL provided'}
        
        import requests
        import time
        
        try:
            start_time = time.time()
            response = requests.get(preview_url, timeout=15, headers={
                'User-Agent': 'EMMSO-Performance-Analyzer/1.0'
            })
            end_time = time.time()
            
            return {
                'url': preview_url,
                'status_code': response.status_code,
                'response_time': round((end_time - start_time) * 1000, 2),  # milliseconds
                'page_size': len(response.content),
                'content_type': response.headers.get('content-type', 'unknown')
            }
        except Exception as e:
            return {'error': str(e), 'url': preview_url}
    
    def _calculate_performance_score(self, theme_analysis, preview_performance, screenshot_analysis=None):
        """Calculate performance score based on current state"""
        score = 100
        
        if 'error' not in theme_analysis:
            # Penalize if too many files (harder to manage)
            css_count = theme_analysis.get('css_count', 0)
            if css_count > 20:
                score -= 10
            elif css_count > 10:
                score -= 5
            
            js_count = theme_analysis.get('js_count', 0)
            if js_count > 15:
                score -= 10
            elif js_count > 10:
                score -= 5
            
            # Penalize for large total sizes
            total_css_kb = theme_analysis.get('total_css_size_kb', 0)
            if total_css_kb > 200:
                score -= 15
            elif total_css_kb > 150:
                score -= 10
            
            total_js_kb = theme_analysis.get('total_js_size_kb', 0)
            if total_js_kb > 300:
                score -= 15
            elif total_js_kb > 200:
                score -= 10
        
        if 'error' not in preview_performance:
            response_time = preview_performance.get('response_time', 5000)
            if response_time > 3000:
                score -= 20
            elif response_time > 2000:
                score -= 15
            elif response_time > 1000:
                score -= 10
        
        return max(0, score)
    
    def _generate_recommendations(self, theme_analysis, preview_performance, screenshot_analysis=None):
        """
        Generate modern 2025 performance recommendations
        
        NOTE: CSS/JS consolidation is DEPRECATED (2024+)
        - HTTP/2 parallel loading makes multiple files FASTER
        - Better caching: small file changes don't invalidate entire bundle
        - Better code splitting and lazy loading opportunities
        - Critical CSS strategy requires separation anyway
        """
        recommendations = []
        
        if 'error' not in theme_analysis:
            total_css_kb = theme_analysis.get('total_css_size_kb', 0)
            css_count = theme_analysis.get('css_count', 0)
            
            # Modern CSS optimization (NOT consolidation)
            if total_css_kb > 200:
                recommendations.append(f"Total CSS {total_css_kb}KB - minify and enable gzip/brotli compression")
            
            # Check for critical CSS separation
            has_critical_css = any('critical' in f for f in theme_analysis.get('css_files', []))
            if not has_critical_css and css_count > 10:
                recommendations.append("Implement critical CSS inline strategy for faster first paint")
            
            # JavaScript optimization
            js_count = theme_analysis.get('js_count', 0)
            total_js_kb = theme_analysis.get('total_js_size_kb', 0)
            
            if total_js_kb > 150:
                recommendations.append(f"Total JS {total_js_kb}KB - consider code splitting and lazy loading")
            
            # Check for proper defer/async usage
            if js_count > 15:
                recommendations.append("Ensure all non-critical JS uses defer attribute for better parsing performance")
        
        if 'error' not in preview_performance:
            response_time = preview_performance.get('response_time', 0)
            if response_time > 2000:
                recommendations.append(f"Page load time {response_time}ms - optimize TTFB with CDN and caching")
            elif response_time > 1000:
                recommendations.append(f"Page load time {response_time}ms - consider preconnect hints for external resources")
        
        if not recommendations:
            recommendations.append("Performance is well-optimized for modern HTTP/2 delivery")
        
        return recommendations
    
    def _process_vision_screenshots_for_performance(self, vision_data, project_goals):
        """
        Process Vision AI's screenshot analysis from Performance perspective
        
        Uses Vision's scores to detect:
        - Visual layout shifts (CLS indicators)
        - Loading UX quality
        - Image optimization hints
        - Performance-impacting design choices
        """
        if not vision_data:
            return {
                'screenshots_analyzed': 0,
                'performance_score': 0,
                'issues': ['No Vision AI data available']
            }
        
        print("      📸 Using Vision AI screenshot data")
        
        perf_issues = []
        perf_recommendations = []
        detailed_analyses = {}
        
        # Performance-related scores
        hierarchy_scores = []  # Stable hierarchy = low CLS
        mobile_scores = []     # Good mobile = optimized assets
        simplicity_scores = [] # Brutalist = less bloat
        
        for screenshot_name, vision_analysis in vision_data.items():
            if 'error' in vision_analysis:
                continue
            
            scores = vision_analysis.get('scores', {})
            visual_hierarchy = scores.get('visual_hierarchy', 0)
            mobile_first = scores.get('mobile_first', 0)
            brutalist_simplicity = scores.get('brutalist_simplicity', 0)
            
            if visual_hierarchy > 0:
                hierarchy_scores.append(visual_hierarchy)
            if mobile_first > 0:
                mobile_scores.append(mobile_first)
            if brutalist_simplicity > 0:
                simplicity_scores.append(brutalist_simplicity)
            
            screenshot_issues = []
            screenshot_recs = []
            
            # High hierarchy score = stable layout = low CLS risk
            if visual_hierarchy < 70:
                screenshot_issues.append(f"Layout stability concerns (hierarchy: {visual_hierarchy}/100)")
                screenshot_recs.append("Stabilize layout to prevent Cumulative Layout Shift")
            
            # Low simplicity = potential bloat
            if brutalist_simplicity < 60:
                screenshot_issues.append(f"Visual complexity may impact performance (simplicity: {brutalist_simplicity}/100)")
                screenshot_recs.append("Reduce visual elements to improve loading speed")
            
            # Filter Vision's issues for performance-relevance
            if 'issues' in vision_analysis:
                for issue in vision_analysis['issues']:
                    if any(kw in issue.lower() for kw in ['layout', 'shift', 'loading', 'image', 'optimization', 'speed', 'cls', 'lcp', 'large', 'heavy']):
                        screenshot_issues.append(issue)
            
            if 'recommendations' in vision_analysis:
                for rec in vision_analysis['recommendations']:
                    if any(kw in rec.lower() for kw in ['performance', 'optimize', 'loading', 'image', 'compress', 'lazy', 'speed', 'fast']):
                        clean_rec = rec.replace(f"{screenshot_name}: ", "")
                        screenshot_recs.append(clean_rec)
            
            detailed_analyses[screenshot_name] = {
                'performance_indicators': {
                    'layout_stability': visual_hierarchy,
                    'asset_optimization': mobile_first,
                    'design_efficiency': brutalist_simplicity
                },
                'issues': screenshot_issues,
                'recommendations': screenshot_recs
            }
            
            for issue in screenshot_issues:
                perf_issues.append(f"{screenshot_name}: {issue}")
            for rec in screenshot_recs:
                perf_recommendations.append(f"{screenshot_name}: {rec}")
        
        # Performance score (Hierarchy=40%, Simplicity=35%, Mobile=25%)
        perf_score = 0
        if hierarchy_scores:
            perf_score += int(sum(hierarchy_scores) / len(hierarchy_scores) * 0.40)
        if simplicity_scores:
            perf_score += int(sum(simplicity_scores) / len(simplicity_scores) * 0.35)
        if mobile_scores:
            perf_score += int(sum(mobile_scores) / len(mobile_scores) * 0.25)
        
        return {
            'screenshots_analyzed': len(vision_data),
            'performance_score': perf_score,
            'source': 'vision_ai_processed_performance',
            'detailed_analyses': detailed_analyses,
            'avg_scores': {
                'layout_stability': int(sum(hierarchy_scores) / len(hierarchy_scores)) if hierarchy_scores else 0,
                'design_efficiency': int(sum(simplicity_scores) / len(simplicity_scores)) if simplicity_scores else 0,
                'asset_optimization': int(sum(mobile_scores) / len(mobile_scores)) if mobile_scores else 0
            },
            'issues': perf_issues,
            'recommendations': perf_recommendations
        }
    
    def _analyze_screenshots_performance(self, site_data, project_goals):
        """
        Analyze screenshots from Performance & UX perspective using GPT-4 Vision
        
        Focus on:
        - Visual layout shifts
        - Loading indicators present
        - Progressive enhancement visible
        - Image optimization (blur-up effects)
        - Core Web Vitals impact
        """
        screenshots = self.screenshot_analyzer.get_screenshots(site_data)
        
        if not screenshots:
            return {
                'screenshots_analyzed': 0,
                'performance_score': 0,
                'issues': ['No screenshots available for performance analysis']
            }
        
        # Performance-focused analysis prompt
        performance_prompt = """Analyze this website screenshot from a Performance & UX perspective.

FOCUS AREAS:
1. **Visual Stability** (0-100): Are there signs of layout shifts (CLS)? Is content stable?
2. **Loading UX** (0-100): Are loading indicators present? Is progressive enhancement visible?
3. **Image Optimization** (0-100): Do images appear optimized? Any blur-up effects?
4. **Content Prioritization** (0-100): Is above-the-fold content prioritized?
5. **Performance Indicators** (0-100): Any visible performance issues (render blocking, etc)?

PROVIDE:
**SCORES:**
- Visual Stability: X/100
- Loading UX: X/100
- Image Optimization: X/100
- Content Prioritization: X/100
- Performance Indicators: X/100
- OVERALL: X/100

**ISSUES FOUND:**
- List specific performance or UX issues visible in the screenshot

**RECOMMENDATIONS:**
- Provide actionable recommendations to improve performance

**HIGHLIGHTS:**
- What performance best practices are visible"""
        
        # Analyze screenshots
        analyses = {}
        all_scores = []
        all_recommendations = []
        all_issues = []
        
        for screenshot_name, screenshot_path in screenshots.items():
            print(f"      📸 Performance Analysis: {screenshot_name}")
            
            analysis = self.screenshot_analyzer.analyze_screenshot(
                screenshot_path,
                screenshot_name,
                performance_prompt,
                project_goals
            )
            
            analyses[screenshot_name] = analysis
            
            if 'score' in analysis:
                all_scores.append(analysis['score'])
            
            if 'recommendations' in analysis:
                all_recommendations.extend(analysis['recommendations'])
            
            if 'issues' in analysis:
                all_issues.extend([f"{screenshot_name}: {issue}" for issue in analysis['issues']])
        
        # Calculate overall Performance screenshot score
        avg_score = int(sum(all_scores) / len(all_scores)) if all_scores else 0
        
        return {
            'screenshots_analyzed': len(screenshots),
            'performance_score': avg_score,
            'analyses': analyses,
            'recommendations': all_recommendations,
            'issues': all_issues
        }
