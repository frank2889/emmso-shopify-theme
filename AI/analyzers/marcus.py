"""
Marcus - Performance Analyst for EMMSO AI System
================================================

Specializes in:
- Site speed optimization
- Core Web Vitals analysis
- Lighthouse performance audits
- Resource optimization
- Caching strategies
- Mobile performance
+ GPT-4 Vision voor Performance-focused screenshot analyse

EXPERT KNOWLEDGE BASE - Web Performance Optimization
====================================================
Based on Web.dev Learn Performance documentation (8,000 tokens)

CORE WEB VITALS:
- LCP (Largest Contentful Paint): Target <2.5s. Optimize hero images with fetchpriority="high", avoid loading="lazy" above fold
- CLS (Cumulative Layout Shift): Target <0.1. Set width/height on images, reserve space for ads, avoid layout-shifting animations
- FID/INP (First Input Delay/Interaction to Next Paint): Target <200ms. Minimize JavaScript execution, use web workers for heavy computation
- TTFB (Time to First Byte): Target <600ms. Optimize server response, use CDN, implement proper caching headers

IMAGE OPTIMIZATION:
- Use fetchpriority="high" for LCP images (hero images, above-fold content)
- Apply loading="lazy" for below-fold images only
- Implement responsive images: <picture> with <source> for art direction, srcset for resolution switching
- Formats: WebP/AVIF with JPEG fallback, use image_url filter with width/height params
- Preload critical images: <link rel="preload" as="image" href="hero.jpg" fetchpriority="high">

RESOURCE LOADING:
- CSS: Inline critical CSS in <head>, load non-critical async, avoid @import (blocks parallel downloads)
- JavaScript: Use defer for scripts, async for analytics, avoid render-blocking JS
- Fonts: Preconnect to font domains, use font-display: swap, subset fonts
- Code splitting: Dynamic import() for deferred code loading, webpack for chunking

CACHING STRATEGIES:
- Cache First: Serve from cache, fallback to network (for static assets)
- Network First: Try network, fallback to cache (for dynamic content)
- Stale-While-Revalidate: Serve cached, update in background
- Service Workers: Implement proper caching strategies with workbox

PERFORMANCE API:
- Navigation Timing: performance.getEntriesByType('navigation') for page load metrics
- Resource Timing: Track individual resource load times
- Custom marks: performance.mark() and performance.measure() for custom timing
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
                'js_count': len(js_files),
                'total_css_size_kb': round(total_css_size / 1024, 1),
                'total_js_size_kb': round(total_js_size / 1024, 1),
                'css_files': css_files,
                'js_files': js_files
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
        """Generate recommendations based on findings"""
        recommendations = []
        
        if 'error' not in theme_analysis:
            css_count = theme_analysis.get('css_count', 0)
            if css_count > 15:
                recommendations.append(f"Consider consolidating {css_count} CSS files for better performance")
            
            js_count = theme_analysis.get('js_count', 0)
            if js_count > 10:
                recommendations.append(f"Consider consolidating {js_count} JS files")
            
            total_css_kb = theme_analysis.get('total_css_size_kb', 0)
            if total_css_kb > 150:
                recommendations.append(f"Total CSS size is {total_css_kb}KB - consider optimization")
        
        if 'error' not in preview_performance:
            response_time = preview_performance.get('response_time', 0)
            if response_time > 2000:
                recommendations.append(f"Page load time is {response_time}ms - optimize")
        
        if not recommendations:
            recommendations.append("Performance looks good")
        
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
