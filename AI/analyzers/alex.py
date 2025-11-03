"""
Alex - Shopify Specialist for EMMSO AI System
=============================================
SMART SHOPIFY ANALYSIS - Heeft toegang tot alle Shopify theme data!
Analyseert ECHTE Shopify files: templates, sections, snippets, assets
+ GPT-4 Vision voor Shopify-focused screenshot analyse

EXPERT KNOWLEDGE BASE - Shopify Theme Development Best Practices
================================================================
Based on official Shopify.dev and Liquid documentation (13,000 tokens)

SECTION/BLOCK ARCHITECTURE:
- Use {% schema %} tag for all sections with JSON object (validate against schemas/section.json)
- Settings types: text, image_picker, color_background, checkbox, range, select, product, collection
- Block types: @theme (any theme block), @app (app blocks), local blocks, static blocks
- Presets: Quick merchant configuration with default blocks
- Online Store 2.0: JSON templates + dynamic section rendering via {% sections 'name' %}

LIQUID TEMPLATING BEST PRACTICES:
- Filters: Use | t for translations, | asset_url for assets, | image_url for responsive images
- Tags: {% render 'snippet' %} for includes, {% liquid %} for multi-line logic
- Responsive images (MODERN): Use <picture> with <source> elements for art direction + format switching
  * <picture> → <source type="image/avif"> → <source type="image/webp"> → <img> fallback
  * Add srcset with width descriptors (400w, 800w, 1200w) per source
  * Use sizes attribute for responsive sizing: sizes="(min-width: 768px) 50vw, 100vw"
  * Legacy: Plain <img srcset=""> for simple resolution switching only
- Performance: fetchpriority="high" for LCP images, loading="eager" above fold, loading="lazy" below
- Forms: {% form 'type' %} with proper autocomplete attributes
- Localization: All static text via {{ 'key' | t }}, hierarchical keys in locales/*.json

SHOPIFY-SPECIFIC PATTERNS:
- content_for 'blocks' for dynamic block rendering
- content_for 'block' for static blocks with type/id
- Block nesting: sections can have blocks with 'blocks' property
- Settings schema: required name, id, type, label; optional default, info, placeholder
- Section limits: Use 'limit' in schema to control max sections
- App blocks: {% content_for 'block', type: '@app' %}
"""

import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path
from analyzers.screenshot_analyzer import ScreenshotAnalyzer

class AlexShopifyAnalyst:
    """Shopify platform specialist met ECHTE toegang tot theme files + expert knowledge base."""
    
    def __init__(self):
        """Initialize Alex Shopify analyst with expert Shopify knowledge."""
        self.name = "Alex"
        self.specialty = "Shopify"
        self.shopify_root = "/Users/Frank/Documents/EMMSO NOV"
        self.screenshot_analyzer = ScreenshotAnalyzer()
        self.expertise_areas = [
            'shopify_theme_analysis',
            'liquid_templates',
            'sections_optimization',
            'assets_performance',
            'shopify_configuration',
            'online_store_2.0',
            'liquid_best_practices',
            'shopify_schema_validation'
        ]
    
    def analyze(self, site_data: Dict[str, Any], previous_findings: Dict[str, Any] = None, iteration: int = 1) -> Dict[str, Any]:
        """Perform SMART Shopify analysis met echte data."""
        
        print(f"  🛍️ Alex (Shopify): SMART analyse van ECHTE Shopify theme...")
        
        # Get project goals
        project_goals = site_data.get('project_goals', {})
        
        # Analyseer echte Shopify structure
        theme_analysis = self._analyze_theme_structure()
        
        # Check Liquid templates
        template_analysis = self._analyze_templates()
        
        # Sections performance check
        sections_analysis = self._analyze_sections()
        
        # Assets optimization check
        assets_analysis = self._analyze_assets()
        
        # Shopify config analysis
        config_analysis = self._analyze_shopify_config()
        
        # Get screenshot analysis from Vision AI (shared data) or analyze ourselves
        screenshot_analysis = None
        if 'vision_screenshot_analysis' in site_data:
            screenshot_analysis = self._process_vision_screenshots_for_shopify(site_data['vision_screenshot_analysis'], project_goals)
            print("      📸 Using Vision AI screenshot data")
        else:
            screenshot_analysis = self._analyze_screenshots_shopify(site_data, project_goals)
            print("      📸 Shopify Analysis: analyzing screenshots independently")
        
        # Calculate smart score
        score = self._calculate_shopify_score(theme_analysis, template_analysis, sections_analysis, assets_analysis, screenshot_analysis)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'iteration': iteration,
            'score': score,
            'findings': {
                'theme_structure': theme_analysis,
                'template_quality': template_analysis,
                'sections_performance': sections_analysis,
                'assets_optimization': assets_analysis,
                'shopify_config': config_analysis,
                'screenshot_shopify_analysis': screenshot_analysis,
                'multi_brand_support': self._check_multi_brand_support()
            },
            'recommendations': self._generate_smart_recommendations(theme_analysis, template_analysis, sections_analysis, assets_analysis, screenshot_analysis)
        }
    
    def _analyze_theme_structure(self):
        """Analyseer ECHTE Shopify theme structure"""
        try:
            theme_files = {
                'layouts': self._count_files('layout'),
                'templates': self._count_files('templates'),
                'sections': self._count_files('sections'),
                'snippets': self._count_files('snippets'),
                'assets': self._count_files('assets')
            }
            
            # Check critical files
            critical_files = {
                'theme_liquid': os.path.exists(f"{self.shopify_root}/layout/theme.liquid"),
                'product_template': os.path.exists(f"{self.shopify_root}/templates/product.json"),
                'collection_template': os.path.exists(f"{self.shopify_root}/templates/collection.json"),
                'cart_template': os.path.exists(f"{self.shopify_root}/templates/cart.json")
            }
            
            return {
                'file_structure': theme_files,
                'critical_files_present': critical_files,
                'theme_completeness': sum(critical_files.values()) / len(critical_files) * 100
            }
        except Exception as e:
            return {'error': f"Theme analysis failed: {e}"}
    
    def _count_files(self, directory):
        """Count files in directory"""
        try:
            path = Path(f"{self.shopify_root}/{directory}")
            if path.exists():
                return len([f for f in path.iterdir() if f.is_file()])
            return 0
        except:
            return 0
    
    def _analyze_templates(self):
        """Analyseer Liquid templates kwaliteit"""
        try:
            templates_path = Path(f"{self.shopify_root}/templates")
            if not templates_path.exists():
                return {'error': 'Templates directory not found'}
            
            template_analysis = {}
            
            for template_file in templates_path.glob("*.json"):
                try:
                    with open(template_file, 'r', encoding='utf-8') as f:
                        template_data = json.load(f)
                        
                    template_analysis[template_file.name] = {
                        'sections_count': len(template_data.get('sections', {})),
                        'has_wrapper': 'wrapper' in template_data.get('sections', {}),
                        'order_defined': 'order' in template_data,
                        'settings_present': bool(template_data.get('settings', {}))
                    }
                except Exception as e:
                    template_analysis[template_file.name] = {'error': str(e)}
            
            return {
                'templates_analyzed': len(template_analysis),
                'template_details': template_analysis,
                'quality_score': self._calculate_template_quality(template_analysis)
            }
        except Exception as e:
            return {'error': f"Template analysis failed: {e}"}
    
    def _analyze_sections(self):
        """Analyseer Shopify sections performance"""
        try:
            sections_path = Path(f"{self.shopify_root}/sections")
            if not sections_path.exists():
                return {'error': 'Sections directory not found'}
            
            sections_analysis = {}
            critical_sections = ['header.liquid', 'footer.liquid', 'main-product.liquid', 'cart-drawer.liquid']
            
            for section_file in sections_path.glob("*.liquid"):
                section_name = section_file.name
                is_critical = section_name in critical_sections
                
                try:
                    with open(section_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    sections_analysis[section_name] = {
                        'file_size': len(content),
                        'is_critical': is_critical,
                        'has_schema': '{% schema %}' in content,
                        'has_stylesheet': '{% stylesheet %}' in content,
                        'has_javascript': '{% javascript %}' in content,
                        'liquid_tags_count': content.count('{%'),
                        'performance_rating': self._rate_section_performance(content)
                    }
                except Exception as e:
                    sections_analysis[section_name] = {'error': str(e)}
            
            return {
                'total_sections': len(sections_analysis),
                'critical_sections_present': sum(1 for s in sections_analysis.values() if s.get('is_critical')),
                'sections_details': sections_analysis,
                'overall_sections_score': self._calculate_sections_score(sections_analysis)
            }
        except Exception as e:
            return {'error': f"Sections analysis failed: {e}"}
    
    def _analyze_assets(self):
        """Analyseer assets performance"""
        try:
            assets_path = Path(f"{self.shopify_root}/assets")
            if not assets_path.exists():
                return {'error': 'Assets directory not found'}
            
            assets_analysis = {
                'css_files': [],
                'js_files': [],
                'images': [],
                'other_files': []
            }
            
            total_size = 0
            
            for asset_file in assets_path.iterdir():
                if asset_file.is_file():
                    file_size = asset_file.stat().st_size
                    total_size += file_size
                    
                    file_info = {
                        'name': asset_file.name,
                        'size': file_size,
                        'size_mb': round(file_size / 1024 / 1024, 2)
                    }
                    
                    if asset_file.suffix in ['.css', '.scss']:
                        assets_analysis['css_files'].append(file_info)
                    elif asset_file.suffix in ['.js']:
                        assets_analysis['js_files'].append(file_info)
                    elif asset_file.suffix in ['.png', '.jpg', '.jpeg', '.webp', '.svg']:
                        assets_analysis['images'].append(file_info)
                    else:
                        assets_analysis['other_files'].append(file_info)
            
            # Check for EMMSO specific files
            emmso_css = any(f['name'] == 'emmso.css' for f in assets_analysis['css_files'])
            emmso_js = any(f['name'] == 'emmso.js' for f in assets_analysis['js_files'])
            
            return {
                'total_assets': sum(len(assets_analysis[key]) for key in assets_analysis),
                'total_size_mb': round(total_size / 1024 / 1024, 2),
                'assets_breakdown': assets_analysis,
                'emmso_architecture': {
                    'emmso_css_present': emmso_css,
                    'emmso_js_present': emmso_js,
                    'single_file_architecture': emmso_css and emmso_js
                },
                'performance_rating': self._rate_assets_performance(total_size, assets_analysis)
            }
        except Exception as e:
            return {'error': f"Assets analysis failed: {e}"}
    
    def _analyze_shopify_config(self):
        """Analyseer Shopify configuratie"""
        try:
            config_analysis = {}
            
            # Check settings_data.json
            settings_path = f"{self.shopify_root}/config/settings_data.json"
            if os.path.exists(settings_path):
                with open(settings_path, 'r', encoding='utf-8') as f:
                    settings_data = json.load(f)
                config_analysis['settings_configured'] = bool(settings_data.get('current'))
            
            # Check settings_schema.json
            schema_path = f"{self.shopify_root}/config/settings_schema.json"
            if os.path.exists(schema_path):
                with open(schema_path, 'r', encoding='utf-8') as f:
                    schema_data = json.load(f)
                config_analysis['theme_settings_count'] = len(schema_data)
            
            return config_analysis
        except Exception as e:
            return {'error': f"Config analysis failed: {e}"}
    
    def _check_multi_brand_support(self):
        """Check multi-brand support implementation"""
        try:
            # Check for metafields usage in templates
            brand_support = {
                'metafields_usage': False,
                'brand_switching': False,
                'dynamic_styling': False
            }
            
            # Check snippets for brand-related code
            snippets_path = Path(f"{self.shopify_root}/snippets")
            if snippets_path.exists():
                for snippet in snippets_path.glob("*.liquid"):
                    try:
                        with open(snippet, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        if 'metafields.brand' in content or 'metafields.custom.brand' in content:
                            brand_support['metafields_usage'] = True
                        if 'brand-primary' in content or 'brand-accent' in content:
                            brand_support['dynamic_styling'] = True
                    except:
                        continue
            
            return brand_support
        except Exception as e:
            return {'error': f"Multi-brand check failed: {e}"}
    
    def _calculate_shopify_score(self, theme_analysis, template_analysis, sections_analysis, assets_analysis, screenshot_analysis=None):
        """Calculate MEEDOGENLOOS STRENGE Shopify score - ZERO TOLERANCE voor mediocrity"""
        score = 0
        
        # THEME STRUCTURE PERFECTION REQUIRED (25 points) - PERFECTIE OF NIETS
        if theme_analysis.get('error'):
            return 0  # IMMEDIATE FAIL - No access = No business
        
        theme_completeness = theme_analysis.get('theme_completeness', 0)
        if theme_completeness >= 100:
            score += 25  # PERFECTION ONLY
        elif theme_completeness >= 95:
            score += 15  # BARELY ACCEPTABLE
        elif theme_completeness >= 90:
            score += 8   # POOR ARCHITECTURE
        else:
            score += 0   # ONACCEPTABEL - Missing templates = broken user experience
        
        # TEMPLATE QUALITY - PROFESSIONAL STANDARDS ONLY (25 points)
        if template_analysis.get('error'):
            score += 0  # FAIL - Can't evaluate broken templates
        else:
            template_quality = template_analysis.get('quality_score', 0)
            if template_quality >= 95:
                score += 25  # PROFESSIONAL EXCELLENCE
            elif template_quality >= 90:
                score += 18  # GOOD BUT NOT GREAT
            elif template_quality >= 85:
                score += 12  # MEDIOCRE
            elif template_quality >= 80:
                score += 6   # BARELY FUNCTIONING
            else:
                score += 0   # AMATEUR HOUR - Broken templates = lost sales
        
        # SECTIONS PERFORMANCE - SPEED IS CONVERSION (25 points)
        if sections_analysis.get('error'):
            score += 0  # FAIL - Can't evaluate broken sections
        else:
            sections_score = sections_analysis.get('overall_sections_score', 0)
            if sections_score >= 95:
                score += 25  # LIGHTNING FAST
            elif sections_score >= 90:
                score += 18  # ACCEPTABLE SPEED
            elif sections_score >= 85:
                score += 12  # SLOW = LOST CUSTOMERS
            elif sections_score >= 80:
                score += 6   # PAINFULLY SLOW
            else:
                score += 0   # SPEED DISASTER = BUSINESS DISASTER
        
        # ASSETS & EMMSO ARCHITECTURE - NON-NEGOTIABLE COMPLIANCE (25 points)
        if assets_analysis.get('error'):
            score += 0  # FAIL - Can't evaluate broken assets
        else:
            # EMMSO ARCHITECTURE IS ABSOLUTE REQUIREMENT
            emmso_arch = assets_analysis.get('emmso_architecture', {})
            if not emmso_arch.get('single_file_architecture'):
                score += 0  # ZERO POINTS - Architecture violation = immediate fail
                return score  # STOP HERE - No architecture compliance = No points
            
            # Only if architecture is compliant, check performance
            score += 10  # BASE POINTS for architecture compliance
            
            assets_rating = assets_analysis.get('performance_rating', 0)
            if assets_rating >= 95:
                score += 15  # OPTIMIZATION PERFECTION
            elif assets_rating >= 90:
                score += 12  # GOOD OPTIMIZATION
            elif assets_rating >= 85:
                score += 8   # ACCEPTABLE
            elif assets_rating >= 80:
                score += 4   # POOR OPTIMIZATION
            else:
                score += 0   # OPTIMIZATION DISASTER
        
        # ADDITIONAL STRICT REQUIREMENTS
        violations = []
        
        # Check for CSS/JS architecture violations
        css_files = assets_analysis.get('assets_breakdown', {}).get('css_files', [])
        js_files = assets_analysis.get('assets_breakdown', {}).get('js_files', [])
        
        # Must have EXACTLY emmso.css and emmso.js
        if len(css_files) > 1 or (len(css_files) == 1 and 'emmso.css' not in str(css_files)):
            violations.append("CSS architecture violation")
            score = max(0, score - 25)  # SEVERE PENALTY
            
        if len(js_files) > 1 or (len(js_files) == 1 and 'emmso.js' not in str(js_files)):
            violations.append("JS architecture violation")
            score = max(0, score - 25)  # SEVERE PENALTY
        
        # File size violations (copied from Marcus' strict standards)
        total_size = assets_analysis.get('total_size', 0)
        if total_size > 5 * 1024 * 1024:  # 5MB limit
            violations.append("Asset size violation")
            score = max(0, score - 20)
        
        # Template performance violations
        if template_analysis.get('quality_score', 0) < 80:
            violations.append("Template quality below professional standards")
            score = max(0, score - 15)
        
        # Log violations for transparency
        if violations:
            print(f"🚨 ALEX VIOLATIONS DETECTED: {', '.join(violations)}")
        
        return min(max(score, 0), 100)
    
    def _calculate_template_quality(self, template_analysis):
        """Calculate template quality score"""
        if not template_analysis:
            return 0
        
        total_score = 0
        valid_templates = 0
        
        for template_name, details in template_analysis.items():
            if 'error' not in details:
                template_score = 0
                if details.get('sections_count', 0) > 0:
                    template_score += 25
                if details.get('has_wrapper'):
                    template_score += 25
                if details.get('order_defined'):
                    template_score += 25
                if details.get('settings_present'):
                    template_score += 25
                
                total_score += template_score
                valid_templates += 1
        
        return total_score / valid_templates if valid_templates > 0 else 0
    
    def _rate_section_performance(self, content):
        """Rate individual section performance"""
        score = 100
        
        # Penalize large files
        if len(content) > 5000:
            score -= 20
        
        # Reward schema presence
        if '{% schema %}' in content:
            score += 10
        
        # Penalize excessive Liquid tags
        liquid_tags = content.count('{%')
        if liquid_tags > 50:
            score -= 15
        
        return max(0, min(100, score))
    
    def _calculate_sections_score(self, sections_analysis):
        """Calculate overall sections score"""
        if not sections_analysis:
            return 0
        
        total_score = 0
        valid_sections = 0
        
        for section_name, details in sections_analysis.items():
            if 'error' not in details:
                performance_rating = details.get('performance_rating', 0)
                total_score += performance_rating
                valid_sections += 1
        
        return total_score / valid_sections if valid_sections > 0 else 0
    
    def _rate_assets_performance(self, total_size, assets_breakdown):
        """Rate assets performance"""
        score = 100
        
        # Penalize large total size
        total_mb = total_size / 1024 / 1024
        if total_mb > 10:
            score -= 30
        elif total_mb > 5:
            score -= 15
        
        # Check for EMMSO single-file architecture
        css_files = len(assets_breakdown.get('css_files', []))
        js_files = len(assets_breakdown.get('js_files', []))
        
        if css_files == 1 and js_files == 1:
            score += 20  # Reward single-file architecture
        
        return max(0, min(100, score))
    
    def _generate_smart_recommendations(self, theme_analysis, template_analysis, sections_analysis, assets_analysis, screenshot_analysis=None):
        """Generate smart Shopify recommendations"""
        recommendations = []
        
        # Theme structure recommendations
        if theme_analysis.get('theme_completeness', 100) < 100:
            recommendations.append({
                'title': 'CRITICAL: Incomplete Theme Structure',
                'description': 'Missing critical Shopify template files',
                'priority': 'critical',
                'impact': 'high'
            })
        
        # Template quality recommendations
        template_quality = template_analysis.get('quality_score', 0)
        if template_quality < 70:
            recommendations.append({
                'title': 'Template Quality Improvement Needed',
                'description': 'Optimize Liquid template structure and settings',
                'priority': 'high',
                'impact': 'medium'
            })
        
        # Sections performance recommendations
        sections_score = sections_analysis.get('overall_sections_score', 0)
        if sections_score < 80:
            recommendations.append({
                'title': 'Sections Performance Optimization',
                'description': 'Optimize Liquid sections for better performance',
                'priority': 'medium',
                'impact': 'medium'
            })
        
        # Assets optimization recommendations
        assets_rating = assets_analysis.get('performance_rating', 0)
        if assets_rating < 75:
            recommendations.append({
                'title': 'Assets Optimization Required',
                'description': 'Optimize CSS, JS, and image assets for better performance',
                'priority': 'medium',
                'impact': 'high'
            })
        
        # EMMSO-specific recommendations
        emmso_arch = assets_analysis.get('emmso_architecture', {})
        if not emmso_arch.get('single_file_architecture'):
            recommendations.append({
                'title': 'EMMSO Architecture Compliance',
                'description': 'Implement single emmso.css and emmso.js file architecture',
                'priority': 'high',
                'impact': 'high'
            })
        
        return recommendations
    
    def _process_vision_screenshots_for_shopify(self, vision_data, project_goals):
        """
        Process Vision AI's screenshot analysis from Shopify platform perspective
        
        Uses Vision's detailed scores to evaluate:
        - E-commerce UX patterns
        - Section rendering quality
        - Cart/checkout visibility
        - Product display effectiveness
        """
        if not vision_data:
            return {
                'screenshots_analyzed': 0,
                'shopify_score': 0,
                'issues': ['No Vision AI data available']
            }
        
        print("      📸 Using Vision AI screenshot data")
        
        shopify_issues = []
        shopify_recommendations = []
        detailed_analyses = {}
        
        # Shopify-focused scoring
        brand_scores = []
        hierarchy_scores = []
        mobile_scores = []
        
        for screenshot_name, vision_analysis in vision_data.items():
            if 'error' in vision_analysis:
                continue
            
            # Extract Vision's detailed scores
            scores = vision_analysis.get('scores', {})
            brand_consistency = scores.get('brand_consistency', 0)
            visual_hierarchy = scores.get('visual_hierarchy', 0)
            mobile_first = scores.get('mobile_first', 0)
            
            # Track scores
            if brand_consistency > 0:
                brand_scores.append(brand_consistency)
            if visual_hierarchy > 0:
                hierarchy_scores.append(visual_hierarchy)
            if mobile_first > 0:
                mobile_scores.append(mobile_first)
            
            # Generate Shopify-specific insights
            screenshot_issues = []
            screenshot_recs = []
            
            if brand_consistency < 70:
                screenshot_issues.append(f"Brand inconsistency (score: {brand_consistency}/100)")
                screenshot_recs.append("Standardize logo, colors, and typography across sections")
            
            if 'product' in screenshot_name.lower() or 'collection' in screenshot_name.lower():
                if visual_hierarchy < 70:
                    screenshot_issues.append(f"Product display hierarchy weak (score: {visual_hierarchy}/100)")
                    screenshot_recs.append("Improve product title/price/CTA prominence")
            
            # Filter Vision's issues for Shopify-relevance
            if 'issues' in vision_analysis:
                for issue in vision_analysis['issues']:
                    if any(kw in issue.lower() for kw in ['cart', 'checkout', 'product', 'collection', 'navigation', 'section', 'shopify', 'brand', 'logo']):
                        screenshot_issues.append(issue)
            
            if 'recommendations' in vision_analysis:
                for rec in vision_analysis['recommendations']:
                    if any(kw in rec.lower() for kw in ['cart', 'checkout', 'product', 'collection', 'navigation', 'e-commerce', 'brand', 'section']):
                        clean_rec = rec.replace(f"{screenshot_name}: ", "")
                        screenshot_recs.append(clean_rec)
            
            detailed_analyses[screenshot_name] = {
                'shopify_scores': {
                    'brand_consistency': brand_consistency,
                    'section_hierarchy': visual_hierarchy,
                    'mobile_commerce': mobile_first
                },
                'issues': screenshot_issues,
                'recommendations': screenshot_recs
            }
            
            for issue in screenshot_issues:
                shopify_issues.append(f"{screenshot_name}: {issue}")
            for rec in screenshot_recs:
                shopify_recommendations.append(f"{screenshot_name}: {rec}")
        
        # Calculate Shopify-focused score (Brand=40%, Hierarchy=30%, Mobile=30%)
        shopify_score = 0
        if brand_scores:
            shopify_score += int(sum(brand_scores) / len(brand_scores) * 0.40)
        if hierarchy_scores:
            shopify_score += int(sum(hierarchy_scores) / len(hierarchy_scores) * 0.30)
        if mobile_scores:
            shopify_score += int(sum(mobile_scores) / len(mobile_scores) * 0.30)
        
        return {
            'screenshots_analyzed': len(vision_data),
            'shopify_score': shopify_score,
            'source': 'vision_ai_processed_shopify',
            'detailed_analyses': detailed_analyses,
            'avg_scores': {
                'brand_consistency': int(sum(brand_scores) / len(brand_scores)) if brand_scores else 0,
                'section_hierarchy': int(sum(hierarchy_scores) / len(hierarchy_scores)) if hierarchy_scores else 0,
                'mobile_commerce': int(sum(mobile_scores) / len(mobile_scores)) if mobile_scores else 0
            },
            'issues': shopify_issues,
            'recommendations': shopify_recommendations
        }
    
    def _analyze_screenshots_shopify(self, site_data, project_goals):
        """
        Analyze screenshots from Shopify platform perspective using GPT-4 Vision
        
        Focus on:
        - Shopify sections rendering correctly
        - Cart icon & functionality visible
        - Navigation structure clear
        - E-commerce best practices
        - Product display optimization
        """
        screenshots = self.screenshot_analyzer.get_screenshots(site_data)
        
        if not screenshots:
            return {
                'screenshots_analyzed': 0,
                'shopify_score': 0,
                'issues': ['No screenshots available for Shopify analysis']
            }
        
        # Shopify-focused analysis prompt
        shopify_prompt = """Analyze this Shopify e-commerce website screenshot from a Shopify platform perspective.

FOCUS AREAS:
1. **Shopify Sections** (0-100): Are sections rendering correctly? Is the layout modular?
2. **Cart & Checkout** (0-100): Is the cart icon visible? Are checkout flows clear?
3. **Navigation** (0-100): Is the menu structure intuitive? Is mobile navigation accessible?
4. **Product Display** (0-100): Are products displayed optimally for conversions?
5. **E-commerce UX** (0-100): Does it follow Shopify e-commerce best practices?

PROVIDE:
**SCORES:**
- Shopify Sections: X/100
- Cart & Checkout: X/100
- Navigation: X/100
- Product Display: X/100
- E-commerce UX: X/100
- OVERALL: X/100

**ISSUES FOUND:**
- List specific Shopify platform or e-commerce issues

**RECOMMENDATIONS:**
- Provide actionable recommendations to improve Shopify theme quality

**HIGHLIGHTS:**
- What Shopify best practices are being followed well"""
        
        # Analyze screenshots
        analyses = {}
        all_scores = []
        all_recommendations = []
        all_issues = []
        
        for screenshot_name, screenshot_path in screenshots.items():
            print(f"      📸 Shopify Analysis: {screenshot_name}")
            
            analysis = self.screenshot_analyzer.analyze_screenshot(
                screenshot_path,
                screenshot_name,
                shopify_prompt,
                project_goals
            )
            
            analyses[screenshot_name] = analysis
            
            if 'score' in analysis:
                all_scores.append(analysis['score'])
            
            if 'recommendations' in analysis:
                all_recommendations.extend(analysis['recommendations'])
            
            if 'issues' in analysis:
                all_issues.extend([f"{screenshot_name}: {issue}" for issue in analysis['issues']])
        
        # Calculate overall Shopify screenshot score
        avg_score = int(sum(all_scores) / len(all_scores)) if all_scores else 0
        
        return {
            'screenshots_analyzed': len(screenshots),
            'shopify_score': avg_score,
            'analyses': analyses,
            'recommendations': all_recommendations,
            'issues': all_issues
        }
        return recommendations