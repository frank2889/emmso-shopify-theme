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
        """Perform performance analysis with CSS/JS constraint awareness."""
        
        print(f"  🚀 Marcus (Performance): Performance analysis with STRICT CSS/JS constraints...")
        
        # Check if business constraints are provided
        constraints = site_data.get('business_context', {}).get('technical_constraints', {})
        css_rule = constraints.get('css_rule', 'Unknown')
        js_rule = constraints.get('js_rule', 'Unknown')
        
        print(f"      📋 Constraints: {css_rule}")
        print(f"      📋 Constraints: {js_rule}")
        
        # Analyze theme files for constraint violations
        theme_analysis = self._analyze_theme_performance_constraints(site_data.get('shopify_theme_path'))
        
        # Test preview URL performance
        preview_performance = self._test_preview_performance(site_data.get('shopify_preview_url'))
        
        # Calculate score with constraint compliance
        score = self._calculate_performance_score_with_constraints(theme_analysis, preview_performance)
        
        # Generate constraint-aware recommendations
        recommendations = self._generate_constraint_recommendations(theme_analysis, preview_performance)
        
        analysis_result = {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'iteration': iteration,
            'score': score,
            'findings': {
                'css_js_constraints': {
                    'css_rule': css_rule,
                    'js_rule': js_rule,
                    'violations': theme_analysis.get('violations', [])
                },
                'theme_file_analysis': theme_analysis,
                'preview_performance': preview_performance,
                'constraint_compliance': theme_analysis.get('compliance_score', 0)
            },
            'recommendations': recommendations,
            'critical_issues': theme_analysis.get('violations', [])
        }
        
        print(f"    ⚡ Performance Score: {analysis_result['score']}/100")
        print(f"    🚨 Constraint Violations: {len(theme_analysis.get('violations', []))}")
        return analysis_result
    
    def _analyze_theme_performance_constraints(self, theme_path):
        """Analyze theme files for CSS/JS constraint violations"""
        if not theme_path:
            return {'error': 'No theme path provided', 'violations': [], 'compliance_score': 0}
        
        import os
        violations = []
        compliance_score = 100
        
        try:
            assets_path = os.path.join(theme_path, 'assets')
            if os.path.exists(assets_path):
                asset_files = [f for f in os.listdir(assets_path) if os.path.isfile(os.path.join(assets_path, f))]
                
                # Check for unauthorized CSS files
                css_files = [f for f in asset_files if f.endswith('.css')]
                unauthorized_css = [f for f in css_files if f != 'emmso.css']
                
                # Check for unauthorized JS files  
                js_files = [f for f in asset_files if f.endswith('.js')]
                unauthorized_js = [f for f in js_files if f != 'emmso.js']
                
                if unauthorized_css:
                    violations.append(f"CRITICAL: Unauthorized CSS files found: {', '.join(unauthorized_css)}")
                    compliance_score -= 30
                
                if unauthorized_js:
                    violations.append(f"CRITICAL: Unauthorized JS files found: {', '.join(unauthorized_js)}")
                    compliance_score -= 30
                
                # Check file sizes
                emmso_css_path = os.path.join(assets_path, 'emmso.css')
                emmso_js_path = os.path.join(assets_path, 'emmso.js')
                
                if os.path.exists(emmso_css_path):
                    css_size = os.path.getsize(emmso_css_path)
                    if css_size > 200000:  # >200KB
                        violations.append(f"WARNING: emmso.css is large ({css_size} bytes) - optimize")
                        compliance_score -= 10
                
                if os.path.exists(emmso_js_path):
                    js_size = os.path.getsize(emmso_js_path)
                    if js_size > 300000:  # >300KB
                        violations.append(f"WARNING: emmso.js is large ({js_size} bytes) - optimize")
                        compliance_score -= 10
            
            return {
                'violations': violations,
                'compliance_score': max(0, compliance_score),
                'css_files_found': css_files,
                'js_files_found': js_files,
                'unauthorized_css': unauthorized_css,
                'unauthorized_js': unauthorized_js
            }
            
        except Exception as e:
            return {'error': str(e), 'violations': [f"Analysis failed: {e}"], 'compliance_score': 0}
    
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
    
    def _calculate_performance_score_with_constraints(self, theme_analysis, preview_performance):
        """Calculate MEEDOGENLOOS STRENGE performance score - VEEL STRENGER!"""
        score = 0  # Start at ZERO - must EARN every point
        
        # CONSTRAINT COMPLIANCE - PERFECTIE VEREIST (60% of score)
        compliance_score = theme_analysis.get('compliance_score', 0)
        violations = theme_analysis.get('violations', [])
        
        # ZERO TOLERANCE for violations
        if violations:
            for violation in violations:
                if 'Unauthorized CSS' in violation:
                    score = 0  # IMMEDIATE FAIL - CSS constraint broken
                    return 0
                elif 'Unauthorized JS' in violation:
                    score = 0  # IMMEDIATE FAIL - JS constraint broken  
                    return 0
        
        # Only if NO violations, check compliance score
        if compliance_score == 100:
            score += 60  # Perfect compliance
        elif compliance_score >= 95:
            score += 45  # Near perfect
        elif compliance_score >= 90:
            score += 30  # Acceptable but not great
        else:
            score += 0   # Below 90% = FAIL
        
        # PERFORMANCE METRICS - GOOGLE STANDARDS (40% of score)
        if 'error' not in preview_performance:
            response_time = preview_performance.get('response_time', 5000)
            page_size = preview_performance.get('page_size', 0)
            
            # Response time scoring - VEEL STRENGER
            if response_time <= 500:      # Google's "fast" threshold
                score += 25
            elif response_time <= 1000:   # Acceptable
                score += 20
            elif response_time <= 1500:   # Poor but not terrible
                score += 10
            elif response_time <= 2000:   # Bad
                score += 5
            else:                         # Disaster
                score += 0
            
            # Page size penalty - VEEL STRENGER
            if page_size > 1000000:       # >1MB = penalty
                score -= 15
            elif page_size > 500000:      # >500KB = penalty
                score -= 10
            elif page_size > 300000:      # >300KB = small penalty
                score -= 5
            
            # File size penalties from theme analysis
            if 'css_files_found' in theme_analysis:
                for css_file in theme_analysis['css_files_found']:
                    if css_file == 'emmso.css':
                        # Check emmso.css size
                        css_path = '/Users/Frank/Documents/EMMSO/assets/emmso.css'
                        try:
                            import os
                            if os.path.exists(css_path):
                                css_size = os.path.getsize(css_path)
                                if css_size > 150000:    # >150KB CSS = major penalty
                                    score -= 20
                                elif css_size > 100000:  # >100KB CSS = penalty
                                    score -= 10
                                elif css_size > 75000:   # >75KB CSS = small penalty
                                    score -= 5
                        except:
                            pass
            
            if 'js_files_found' in theme_analysis:
                for js_file in theme_analysis['js_files_found']:
                    if js_file == 'emmso.js':
                        # Check emmso.js size
                        js_path = '/Users/Frank/Documents/EMMSO/assets/emmso.js'
                        try:
                            import os
                            if os.path.exists(js_path):
                                js_size = os.path.getsize(js_path)
                                if js_size > 200000:     # >200KB JS = major penalty
                                    score -= 20
                                elif js_size > 150000:   # >150KB JS = penalty
                                    score -= 10
                                elif js_size > 100000:   # >100KB JS = small penalty
                                    score -= 5
                        except:
                            pass
        else:
            score = 0  # Can't test performance = FAIL
        
        return min(100, max(0, score))
    
    def _generate_constraint_recommendations(self, theme_analysis, preview_performance):
        """Generate performance recommendations considering constraints"""
        recommendations = []
        
        violations = theme_analysis.get('violations', [])
        for violation in violations:
            if 'Unauthorized CSS' in violation:
                recommendations.append("CRITICAL: Consolidate all CSS into emmso.css - remove unauthorized CSS files")
            elif 'Unauthorized JS' in violation:
                recommendations.append("CRITICAL: Consolidate all JavaScript into emmso.js - remove unauthorized JS files")
            elif 'emmso.css is large' in violation:
                recommendations.append("OPTIMIZE: Reduce emmso.css file size - minify and remove unused styles")
            elif 'emmso.js is large' in violation:
                recommendations.append("OPTIMIZE: Reduce emmso.js file size - minify and optimize code")
        
        if 'error' not in preview_performance:
            response_time = preview_performance.get('response_time', 0)
            if response_time > 2000:
                recommendations.append(f"PERFORMANCE: Response time {response_time}ms is slow - optimize server response")
        
        if not recommendations:
            recommendations.append("GOOD: CSS/JS constraints followed correctly - monitor file sizes")
        
        return recommendations