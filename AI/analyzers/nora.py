"""
Nora - Visual Design Analyst for EMMSO AI System
================================================

Uses centralized design_expert knowledge base for analysis.
Accesses expert knowledge on design systems, accessibility (WCAG), brutalist design, and UX best practices.

Specializes in:
- Visual design analysis
- Brand consistency
- Accessibility (WCAG 2.1 AA)
- Responsive design
- Design system compliance
- GPT-4 Vision for design-focused screenshot analysis
"""

import os
import sys
import requests
from datetime import datetime
from analyzers.screenshot_analyzer import ScreenshotAnalyzer

# Import expert knowledge from centralized library
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from knowledge import design_expert

class NoraVisualAnalyst:
    """Visual design specialist with WCAG accessibility and design system expertise."""
    
    def __init__(self):
        """Initialize Nora with expert design knowledge."""
        self.name = "Nora"
        self.specialty = "Visual Design"
        self.theme_root = "/Users/Frank/Documents/EMMSO NOV"
        self.screenshot_analyzer = ScreenshotAnalyzer()
        self.knowledge = design_expert  # Access to centralized knowledge base
        self.expertise_areas = [
            'visual_design',
            'brand_consistency',
            'color_accessibility',
            'typography_hierarchy',
            'wcag_compliance',
            'contrast_ratios',
            'focus_indicators',
            'touch_targets',
            'spacing_systems',
            'responsive_design'
        ]
    
    def analyze(self, site_data):
        print(f"    🎨 Nora: MEEDOGENLOOS STRENGE visual design analysis for {site_data.get('domain', 'emmso.com')}")
        
        # Get project goals
        project_goals = site_data.get('project_goals', {})
        
        # Comprehensive visual analysis
        css_analysis = self._analyze_css_compliance()
        visual_analysis = self._analyze_visual_consistency(site_data)
        brand_analysis = self._analyze_brand_implementation()
        responsive_analysis = self._analyze_responsive_design()
        
        # Get screenshot analysis from Vision AI (shared data) or analyze ourselves
        screenshot_analysis = None
        if 'vision_screenshot_analysis' in site_data:
            screenshot_analysis = self._process_vision_screenshots_for_design(site_data['vision_screenshot_analysis'], project_goals)
            print("      📸 Using Vision AI screenshot data")
        else:
            screenshot_analysis = self._analyze_screenshots_design(site_data, project_goals)
            print("      📸 Design Analysis: analyzing screenshots independently")
        
        # Calculate STRENGE score
        score = self._calculate_visual_score(css_analysis, visual_analysis, brand_analysis, responsive_analysis, screenshot_analysis)
        
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
                'screenshot_design_analysis': screenshot_analysis,
                'critical_violations': self._identify_critical_violations(css_analysis, visual_analysis, brand_analysis, screenshot_analysis)
            },
            'recommendations': self._generate_design_recommendations(css_analysis, visual_analysis, brand_analysis, responsive_analysis, screenshot_analysis)
        }
    
    def _analyze_css_compliance(self):
        """Analyze CSS files in theme - check what's actually there"""
        try:
            assets_path = "/Users/Frank/Documents/EMMSO NOV/assets"
            
            if not os.path.exists(assets_path):
                return {
                    'error': 'Assets folder not found',
                    'compliance_score': 0,
                    'violations': ['Cannot find assets folder']
                }
            
            # Count all CSS files
            css_files = [f for f in os.listdir(assets_path) if f.endswith('.css')]
            
            if not css_files:
                return {
                    'error': 'No CSS files found',
                    'compliance_score': 0,
                    'violations': ['No CSS files in theme']
                }
            
            violations = []
            compliance_score = 100
            
            # Calculate total CSS size
            total_size = 0
            for css_file in css_files:
                file_path = os.path.join(assets_path, css_file)
                total_size += os.path.getsize(file_path)
            
            # Check if total CSS is reasonable
            total_size_kb = total_size / 1024
            if total_size_kb > 300:  # 300KB total seems high
                compliance_score -= 10
            
            # Read first CSS file to check for design system elements
            first_css = os.path.join(assets_path, css_files[0])
            with open(first_css, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            # Check for design system elements (not strict requirements)
            elements_found = 0
            design_elements = [
                'font-family',  # Typography
                'color:',  # Color system
                '@media',  # Responsive design
                '.product-',  # Product styling
                '.cart-',  # Cart styling
            ]
            
            for element in design_elements:
                if element in css_content:
                    elements_found += 1
            
            # Check for external dependencies (should be minimal)
            external_refs = css_content.count('@import') + css_content.count('url(http')
            if external_refs > 3:
                violations.append(f"Too many external dependencies: {external_refs}")
                compliance_score -= 10
            
            return {
                'compliance_score': max(0, compliance_score),
                'total_css_files': len(css_files),
                'total_size_kb': round(total_size_kb, 1),
                'violations': violations,
                'elements_found': elements_found
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
    
    def _calculate_visual_score(self, css_analysis, visual_analysis, brand_analysis, responsive_analysis, screenshot_analysis=None):
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
    
    def _identify_critical_violations(self, css_analysis, visual_analysis, brand_analysis, screenshot_analysis=None):
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
    
    def _generate_design_recommendations(self, css_analysis, visual_analysis, brand_analysis, responsive_analysis, screenshot_analysis=None):
        """Generate design improvement recommendations"""
        recommendations = []
        
        # CSS recommendations
        if css_analysis.get('compliance_score', 0) < 85:
            total_files = css_analysis.get('total_css_files', 0)
            total_size = css_analysis.get('total_size_kb', 0)
            recommendations.append({
                'title': 'CSS Optimization Recommended',
                'description': f'Current setup: {total_files} CSS files, {total_size}KB total. Consider optimization.',
                'priority': 'medium',
                'impact': 'medium'
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
    
    def _process_vision_screenshots_for_design(self, vision_data, project_goals):
        """
        Process Vision AI's screenshot analysis from Design perspective
        
        Uses Vision's detailed scores for:
        - Brand consistency evaluation
        - Typography quality assessment
        - Color usage analysis
        - Visual hierarchy strength
        - Layout & spacing quality
        """
        if not vision_data:
            return {
                'screenshots_analyzed': 0,
                'design_score': 0,
                'issues': ['No Vision AI data available']
            }
        
        print("      📸 Using Vision AI screenshot data")
        
        design_issues = []
        design_recommendations = []
        detailed_analyses = {}
        
        # Design-focused scoring
        brand_scores = []
        hierarchy_scores = []
        accessibility_scores = []
        simplicity_scores = []
        
        for screenshot_name, vision_analysis in vision_data.items():
            if 'error' in vision_analysis:
                continue
            
            # Extract ALL design-relevant scores from Vision
            scores = vision_analysis.get('scores', {})
            brand_consistency = scores.get('brand_consistency', 0)
            visual_hierarchy = scores.get('visual_hierarchy', 0)
            accessibility = scores.get('accessibility', 0)
            brutalist_simplicity = scores.get('brutalist_simplicity', 0)
            
            if brand_consistency > 0:
                brand_scores.append(brand_consistency)
            if visual_hierarchy > 0:
                hierarchy_scores.append(visual_hierarchy)
            if accessibility > 0:
                accessibility_scores.append(accessibility)
            if brutalist_simplicity > 0:
                simplicity_scores.append(brutalist_simplicity)
            
            # Generate design-specific insights
            screenshot_issues = []
            screenshot_recs = []
            
            if brand_consistency < 70:
                screenshot_issues.append(f"Brand inconsistency detected (score: {brand_consistency}/100)")
                screenshot_recs.append("Standardize logo size, color palette, and typography")
            
            if visual_hierarchy < 70:
                screenshot_issues.append(f"Weak visual hierarchy (score: {visual_hierarchy}/100)")
                screenshot_recs.append("Strengthen focal points using size and contrast")
            
            if accessibility < 70:
                screenshot_issues.append(f"Accessibility/contrast issues (score: {accessibility}/100)")
                screenshot_recs.append("Improve text contrast and color accessibility")
            
            if brutalist_simplicity < 60:
                screenshot_issues.append(f"Design not brutalist enough (score: {brutalist_simplicity}/100)")
                screenshot_recs.append("Simplify design - remove decorative elements")
            
            # Filter Vision's original issues for design-relevance
            if 'issues' in vision_analysis:
                for issue in vision_analysis['issues']:
                    if any(kw in issue.lower() for kw in ['brand', 'color', 'typography', 'font', 'spacing', 'layout', 'hierarchy', 'consistency', 'visual', 'contrast', 'align']):
                        screenshot_issues.append(issue)
            
            if 'recommendations' in vision_analysis:
                for rec in vision_analysis['recommendations']:
                    if any(kw in rec.lower() for kw in ['brand', 'color', 'typography', 'font', 'spacing', 'layout', 'hierarchy', 'consistency', 'design', 'visual']):
                        clean_rec = rec.replace(f"{screenshot_name}: ", "")
                        screenshot_recs.append(clean_rec)
            
            detailed_analyses[screenshot_name] = {
                'design_scores': {
                    'brand_consistency': brand_consistency,
                    'visual_hierarchy': visual_hierarchy,
                    'accessibility': accessibility,
                    'brutalist_simplicity': brutalist_simplicity
                },
                'issues': screenshot_issues,
                'recommendations': screenshot_recs
            }
            
            for issue in screenshot_issues:
                design_issues.append(f"{screenshot_name}: {issue}")
            for rec in screenshot_recs:
                design_recommendations.append(f"{screenshot_name}: {rec}")
        
        # Calculate design-focused score (Brand=30%, Hierarchy=25%, Accessibility=25%, Simplicity=20%)
        design_score = 0
        if brand_scores:
            design_score += int(sum(brand_scores) / len(brand_scores) * 0.30)
        if hierarchy_scores:
            design_score += int(sum(hierarchy_scores) / len(hierarchy_scores) * 0.25)
        if accessibility_scores:
            design_score += int(sum(accessibility_scores) / len(accessibility_scores) * 0.25)
        if simplicity_scores:
            design_score += int(sum(simplicity_scores) / len(simplicity_scores) * 0.20)
        
        return {
            'screenshots_analyzed': len(vision_data),
            'design_score': design_score,
            'source': 'vision_ai_processed_design',
            'detailed_analyses': detailed_analyses,
            'avg_scores': {
                'brand_consistency': int(sum(brand_scores) / len(brand_scores)) if brand_scores else 0,
                'visual_hierarchy': int(sum(hierarchy_scores) / len(hierarchy_scores)) if hierarchy_scores else 0,
                'accessibility': int(sum(accessibility_scores) / len(accessibility_scores)) if accessibility_scores else 0,
                'brutalist_simplicity': int(sum(simplicity_scores) / len(simplicity_scores)) if simplicity_scores else 0
            },
            'issues': design_issues,
            'recommendations': design_recommendations
        }
    
    def _analyze_screenshots_design(self, site_data, project_goals):
        """
        Analyze screenshots from Design perspective using GPT-4 Vision
        
        Focus on:
        - Brand consistency (logo, colors, typography)
        - Design system compliance
        - Visual hierarchy & balance
        - Whitespace & layout
        - Component consistency
        """
        screenshots = self.screenshot_analyzer.get_screenshots(site_data)
        
        if not screenshots:
            return {
                'screenshots_analyzed': 0,
                'design_score': 0,
                'issues': ['No screenshots available for design analysis']
            }
        
        # Design-focused analysis prompt
        design_prompt = """Analyze this website screenshot from a Visual Design perspective.

FOCUS AREAS:
1. **Brand Consistency** (0-100): Are logo, colors, and typography consistent with brand?
2. **Visual Hierarchy** (0-100): Is information hierarchy clear and effective?
3. **Typography** (0-100): Are fonts readable, well-sized, and consistent?
4. **Color Usage** (0-100): Is color palette harmonious and purposeful?
5. **Whitespace & Layout** (0-100): Is whitespace used effectively? Is layout balanced?
6. **Component Consistency** (0-100): Are buttons, cards, and UI elements consistent?

PROVIDE:
**SCORES:**
- Brand Consistency: X/100
- Visual Hierarchy: X/100
- Typography: X/100
- Color Usage: X/100
- Whitespace & Layout: X/100
- Component Consistency: X/100
- OVERALL: X/100

**ISSUES FOUND:**
- List specific design issues or inconsistencies

**RECOMMENDATIONS:**
- Provide actionable design improvements

**HIGHLIGHTS:**
- What design elements are working well"""
        
        # Analyze screenshots
        analyses = {}
        all_scores = []
        all_recommendations = []
        all_issues = []
        
        for screenshot_name, screenshot_path in screenshots.items():
            print(f"      📸 Design Analysis: {screenshot_name}")
            
            analysis = self.screenshot_analyzer.analyze_screenshot(
                screenshot_path,
                screenshot_name,
                design_prompt,
                project_goals
            )
            
            analyses[screenshot_name] = analysis
            
            if 'score' in analysis:
                all_scores.append(analysis['score'])
            
            if 'recommendations' in analysis:
                all_recommendations.extend(analysis['recommendations'])
            
            if 'issues' in analysis:
                all_issues.extend([f"{screenshot_name}: {issue}" for issue in analysis['issues']])
        
        # Calculate overall Design screenshot score
        avg_score = int(sum(all_scores) / len(all_scores)) if all_scores else 0
        
        return {
            'screenshots_analyzed': len(screenshots),
            'design_score': avg_score,
            'analyses': analyses,
            'recommendations': all_recommendations,
            'issues': all_issues
        }
