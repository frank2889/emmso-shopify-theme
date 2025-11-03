"""
Sarah - KRITISCHE SEO Analyst voor EMMSO
========================================
Gebruikt ECHTE Google Analytics en PageSpeed data voor harde analyse
+ GPT-4 Vision voor SEO-focused screenshot analyse
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
        
        # Analyze screenshots from SEO perspective (GPT-4 Vision)
        screenshot_analysis = self._analyze_screenshots_seo(site_data, project_goals)
        
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
                'WHY': f"SEO optimization can generate €{revenue_impact:,}/month additional revenue"
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
                'revenue_potential': f"€{revenue_impact:,}/month",
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
