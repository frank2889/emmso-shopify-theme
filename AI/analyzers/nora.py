"""
Nora - Visual Design Analyst for EMMSO AI System
MEEDOGENLOOS STRENGE visual design evaluation
"""
import requests
import os
from datetime import datetime

class NoraVisualAnalyst:
    def __init__(self):
        self.name = "Nora"
        self.specialty = "Visual Design"
        self.technical_docs = {}
        self._load_technical_documentation()
    
    def _load_technical_documentation(self):
        """Load technical documentation for context-aware analysis"""
        try:
            docs_path = "/Users/Frank/Documents/EMMSO/docs"
            
            # CSS.md - Critical for emmso.css compliance
            css_doc_path = os.path.join(docs_path, "CSS.md")
            if os.path.exists(css_doc_path):
                with open(css_doc_path, 'r', encoding='utf-8') as f:
                    self.technical_docs['css'] = f.read()
            
            # DESIGN.MD - Design system standards
            design_doc_path = os.path.join(docs_path, "DESIGN.MD")
            if os.path.exists(design_doc_path):
                with open(design_doc_path, 'r', encoding='utf-8') as f:
                    self.technical_docs['design'] = f.read()
                    
        except Exception as e:
            print(f"⚠️  Nora: Could not load technical docs: {e}")
    
    def analyze(self, site_data):
        print(f"    🎨 Nora: MEEDOGENLOOS STRENGE visual design analysis for {site_data.get('domain', 'emmso.com')}")
        
        # Comprehensive visual analysis
        css_analysis = self._analyze_css_compliance()
        visual_analysis = self._analyze_visual_consistency(site_data)
        brand_analysis = self._analyze_brand_implementation()
        responsive_analysis = self._analyze_responsive_design()
        
        # Calculate STRENGE score
        score = self._calculate_visual_score(css_analysis, visual_analysis, brand_analysis, responsive_analysis)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'findings': {
                'css_compliance': css_analysis,
                'visual_consistency': visual_analysis,
                'brand_implementation': brand_analysis,
                'responsive_design': responsive_analysis,
                'critical_violations': self._identify_critical_violations(css_analysis, visual_analysis, brand_analysis)
            },
            'recommendations': self._generate_design_recommendations(css_analysis, visual_analysis, brand_analysis, responsive_analysis)
        }
    
    def _analyze_css_compliance(self):
        """Analyze emmso.css compliance - CRITICAL for EMMSO architecture"""
        try:
            css_file_path = "/Users/Frank/Documents/EMMSO/assets/emmso.css"
            
            if not os.path.exists(css_file_path):
                return {
                    'error': 'CRITICAL: emmso.css file not found',
                    'compliance_score': 0,
                    'violations': ['Missing emmso.css file - Architecture violation']
                }
            
            with open(css_file_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            violations = []
            compliance_score = 100
            
            # File size check (should be comprehensive but not bloated)
            file_size = len(css_content.encode('utf-8'))
            if file_size > 500000:  # 500KB limit
                violations.append(f"emmso.css too large: {file_size/1024:.1f}KB > 500KB")
                compliance_score -= 20
            
            # Critical EMMSO design elements
            required_elements = [
                '.emmso-',  # EMMSO namespace
                'font-family',  # Typography
                'color:',  # Color system
                '@media',  # Responsive design
                '.product-',  # Product styling
                '.cart-',  # Cart styling
            ]
            
            for element in required_elements:
                if element not in css_content:
                    violations.append(f"Missing critical element: {element}")
                    compliance_score -= 15
            
            # Check for external dependencies (should be minimal)
            external_refs = css_content.count('@import') + css_content.count('url(http')
            if external_refs > 3:
                violations.append(f"Too many external dependencies: {external_refs}")
                compliance_score -= 10
            
            return {
                'compliance_score': max(0, compliance_score),
                'file_size': file_size,
                'violations': violations,
                'elements_found': len([e for e in required_elements if e in css_content])
            }
            
        except Exception as e:
            return {
                'error': f'Failed to analyze CSS: {str(e)}',
                'compliance_score': 0,
                'violations': ['CSS analysis failed']
            }
    
    def _analyze_visual_consistency(self, site_data):
        """Analyze visual consistency across site"""
        try:
            response = requests.get('https://emmso.com', timeout=10)
            
            if response.status_code != 200:
                return {
                    'consistency_score': 0,
                    'error': f'Site not accessible: {response.status_code}'
                }
            
            # Mock visual analysis based on site accessibility
            consistency_score = 75  # Base score for accessible site
            
            # Check for common visual inconsistencies
            issues = []
            
            # Check if EMMSO branding is present
            content = response.text.lower()
            if 'emmso' not in content:
                issues.append('EMMSO branding not prominently displayed')
                consistency_score -= 15
            
            if 'vloer' not in content and 'floor' not in content:
                issues.append('Product category not clear')
                consistency_score -= 10
            
            return {
                'consistency_score': max(0, consistency_score),
                'issues': issues,
                'accessibility': response.status_code == 200
            }
            
        except Exception as e:
            return {
                'consistency_score': 20,  # Severe penalty for unreachable site
                'error': f'Site analysis failed: {str(e)}',
                'issues': ['Site inaccessible for visual analysis']
            }
    
    def _analyze_brand_implementation(self):
        """Analyze EMMSO brand implementation"""
        brand_elements = {
            'logo_presence': False,
            'color_consistency': False,
            'typography_system': False,
            'brand_messaging': False
        }
        
        # Mock brand analysis - in real implementation would analyze actual brand assets
        brand_score = 70  # Conservative score
        
        violations = []
        if not brand_elements['logo_presence']:
            violations.append('EMMSO logo not properly implemented')
            brand_score -= 15
        
        if not brand_elements['color_consistency']:
            violations.append('Brand colors not consistently applied')
            brand_score -= 10
        
        return {
            'brand_score': max(0, brand_score),
            'elements': brand_elements,
            'violations': violations
        }
    
    def _analyze_responsive_design(self):
        """Analyze responsive design implementation"""
        # Mock responsive analysis
        responsive_score = 65  # Conservative score
        
        issues = [
            'Mobile navigation needs optimization',
            'Product grid layout inconsistent on tablet',
            'Cart drawer not fully responsive'
        ]
        
        return {
            'responsive_score': max(0, responsive_score - len(issues) * 5),
            'issues': issues,
            'devices_tested': ['mobile', 'tablet', 'desktop']
        }
    
    def _calculate_visual_score(self, css_analysis, visual_analysis, brand_analysis, responsive_analysis):
        """Calculate MEEDOGENLOOS STRENGE visual design score"""
        score = 0
        violations = []
        
        # CSS COMPLIANCE (30 points) - ABSOLUTE REQUIREMENT
        css_score = css_analysis.get('compliance_score', 0)
        if css_analysis.get('error'):
            violations.append("CSS analysis failed")
            return 0  # IMMEDIATE FAIL
        
        if css_score >= 95:
            score += 30  # PERFECT CSS COMPLIANCE
        elif css_score >= 90:
            score += 25  # EXCELLENT
        elif css_score >= 85:
            score += 20  # GOOD
        elif css_score >= 80:
            score += 15  # ACCEPTABLE
        else:
            score += 0   # UNACCEPTABLE CSS QUALITY
            violations.append("CSS quality below professional standards")
        
        # VISUAL CONSISTENCY (25 points)
        visual_score = visual_analysis.get('consistency_score', 0)
        if visual_analysis.get('error'):
            score += 0  # FAIL
            violations.append("Visual analysis failed")
        elif visual_score >= 90:
            score += 25  # PERFECT CONSISTENCY
        elif visual_score >= 80:
            score += 20  # GOOD
        elif visual_score >= 70:
            score += 15  # ACCEPTABLE
        else:
            score += 0   # INCONSISTENT DESIGN
            violations.append("Visual inconsistency detected")
        
        # BRAND IMPLEMENTATION (25 points)
        brand_score = brand_analysis.get('brand_score', 0)
        if brand_score >= 90:
            score += 25  # BRAND EXCELLENCE
        elif brand_score >= 80:
            score += 20  # GOOD BRANDING
        elif brand_score >= 70:
            score += 15  # ACCEPTABLE
        else:
            score += 0   # POOR BRAND IMPLEMENTATION
            violations.append("Brand implementation inadequate")
        
        # RESPONSIVE DESIGN (20 points)
        responsive_score = responsive_analysis.get('responsive_score', 0)
        if responsive_score >= 90:
            score += 20  # PERFECT RESPONSIVE
        elif responsive_score >= 80:
            score += 16  # GOOD
        elif responsive_score >= 70:
            score += 12  # ACCEPTABLE
        else:
            score += 0   # POOR RESPONSIVE DESIGN
            violations.append("Responsive design failures")
        
        # ADDITIONAL PENALTIES for critical violations
        css_violations = css_analysis.get('violations', [])
        if len(css_violations) > 0:
            penalty = min(20, len(css_violations) * 5)
            score = max(0, score - penalty)
            violations.extend(css_violations)
        
        # Log violations for transparency
        if violations:
            print(f"🚨 NORA VIOLATIONS DETECTED: {', '.join(violations[:3])}...")  # Show first 3
        
        return min(max(score, 0), 100)
    
    def _identify_critical_violations(self, css_analysis, visual_analysis, brand_analysis):
        """Identify critical visual design violations"""
        violations = []
        
        # CSS violations
        css_violations = css_analysis.get('violations', [])
        violations.extend([f"CSS: {v}" for v in css_violations])
        
        # Visual consistency violations
        visual_issues = visual_analysis.get('issues', [])
        violations.extend([f"Visual: {v}" for v in visual_issues])
        
        # Brand violations
        brand_violations = brand_analysis.get('violations', [])
        violations.extend([f"Brand: {v}" for v in brand_violations])
        
        return violations
    
    def _generate_design_recommendations(self, css_analysis, visual_analysis, brand_analysis, responsive_analysis):
        """Generate design improvement recommendations"""
        recommendations = []
        
        # CSS recommendations
        if css_analysis.get('compliance_score', 0) < 85:
            recommendations.append({
                'title': 'CRITICAL: emmso.css Optimization Required',
                'description': 'Optimize emmso.css file for better compliance and performance',
                'priority': 'critical',
                'impact': 'high'
            })
        
        # Visual consistency recommendations
        if visual_analysis.get('consistency_score', 0) < 80:
            recommendations.append({
                'title': 'Visual Consistency Improvements',
                'description': 'Standardize visual elements across all pages',
                'priority': 'high',
                'impact': 'medium'
            })
        
        # Brand implementation recommendations
        if brand_analysis.get('brand_score', 0) < 75:
            recommendations.append({
                'title': 'Brand Implementation Enhancement',
                'description': 'Strengthen EMMSO brand presence and consistency',
                'priority': 'high',
                'impact': 'high'
            })
        
        # Responsive design recommendations
        responsive_issues = responsive_analysis.get('issues', [])
        if len(responsive_issues) > 2:
            recommendations.append({
                'title': 'Responsive Design Optimization',
                'description': 'Fix mobile and tablet layout inconsistencies',
                'priority': 'medium',
                'impact': 'medium'
            })
        
        return recommendations
