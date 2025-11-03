"""
Performance Expert Knowledge Base
Centralized performance expertise for Marcus (and other analysts who need performance knowledge)
"""

WEB_VITALS = """
Core Web Vitals Performance Optimization:

1. LCP Optimization:
   - Optimize server response time (TTFB <600ms)
   - Preload critical resources
   - Use modern image formats (AVIF > WebP > JPEG)
   - Implement lazy loading
   - Use CDN for static assets

2. INP Optimization:
   - Break up long JavaScript tasks
   - Use web workers for heavy computation
   - Defer non-critical JavaScript
   - Minimize main thread work

3. CLS Optimization:
   - Set explicit dimensions for images/videos
   - Reserve space for ads/embeds
   - Avoid inserting content above existing content
   - Use transform animations (not top/left)
"""

HTTP2_OPTIMIZATION = """
HTTP/2 & HTTP/3 Best Practices:

Modern approach (2025):
- Multiple small files are GOOD (better caching)
- HTTP/2 multiplexing handles parallel requests
- File-level cache invalidation
- Selective updates without full rebuild

DO NOT consolidate CSS/JS files anymore!
This is outdated 2015 advice for HTTP/1.1
"""

IMAGE_OPTIMIZATION = """
Modern Image Optimization (2025):

1. Format Selection:
   AVIF (best compression, modern browsers)
   WebP (good fallback, wide support)
   JPEG (legacy fallback)

2. Responsive Images:
   <picture>
     <source srcset="image.avif" type="image/avif">
     <source srcset="image.webp" type="image/webp">
     <img src="image.jpg" alt="description">
   </picture>

3. Lazy Loading:
   <img loading="lazy" src="image.jpg">
   Only for below-fold images
   LCP image should NOT be lazy loaded
"""

JAVASCRIPT_OPTIMIZATION = """
JavaScript Performance Best Practices:

1. Code Splitting:
   - Load only what's needed for current page
   - Dynamic imports for heavy features
   - Route-based code splitting

2. Defer/Async:
   - defer: Execute after DOM ready (maintains order)
   - async: Execute ASAP (no order guarantee)
   - Use defer for scripts that need DOM

3. Tree Shaking:
   - Remove unused code
   - Use ES6 modules
   - Modern build tools (Vite, esbuild)
"""

def get_recommendation(metric, current_value):
    """
    Generate performance recommendation based on metric and current value
    """
    recommendations = {
        'lcp': [
            'Preload LCP image with <link rel="preload">',
            'Optimize server response time (TTFB)',
            'Use modern image formats (AVIF/WebP)',
            'Implement CDN for faster delivery'
        ],
        'inp': [
            'Break up long JavaScript tasks (>50ms)',
            'Defer non-critical JavaScript',
            'Use requestIdleCallback for low-priority work',
            'Optimize event handlers'
        ],
        'cls': [
            'Set explicit width/height on images',
            'Reserve space for dynamic content',
            'Avoid inserting content above existing',
            'Use CSS transform for animations'
        ],
        'ttfb': [
            'Enable HTTP/2 or HTTP/3',
            'Optimize database queries',
            'Implement server-side caching',
            'Use CDN with edge caching'
        ]
    }
    
    return recommendations.get(metric.lower(), [])
