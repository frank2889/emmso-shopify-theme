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
"""

from typing import Dict, List, Any, Optional
from datetime import datetime

class MarcusPerformanceAnalyst:
    """Performance optimization specialist."""
    
    def __init__(self):
        """Initialize Marcus Performance analyst."""
        self.name = "Marcus"
        self.specialty = "Performance"
        self.expertise_areas = [
            'site_speed',
            'core_web_vitals',
            'lighthouse_audits',
            'resource_optimization',
            'caching',
            'mobile_performance'
        ]
    
    def analyze(self, site_data: Dict[str, Any], previous_findings: Dict[str, Any] = None, iteration: int = 1) -> Dict[str, Any]:
        """Perform performance analysis of current website."""
        
        print(f"  ⚡ Marcus: Analyzing current website performance...")
        
        # Analyze theme files
        theme_analysis = self._analyze_theme_files(site_data.get('shopify_theme_path'))
        
        # Test preview URL performance
        preview_performance = self._test_preview_performance(site_data.get('shopify_preview_url'))
        
        # Calculate score
        score = self._calculate_performance_score(theme_analysis, preview_performance)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(theme_analysis, preview_performance)
        
        analysis_result = {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'iteration': iteration,
            'score': score,
            'findings': {
                'theme_file_analysis': theme_analysis,
                'preview_performance': preview_performance
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
    
    def _calculate_performance_score(self, theme_analysis, preview_performance):
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
    
    def _generate_recommendations(self, theme_analysis, preview_performance):
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