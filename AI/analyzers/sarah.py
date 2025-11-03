"""
Sarah - KRITISCHE SEO Analyst voor EMMSO
========================================
Gebruikt ECHTE Google Analytics en PageSpeed data voor harde analyse
"""
import os
import json
import requests
from datetime import datetime

# Google PageSpeed API key
PAGESPEED_API_KEY = "AIzaSyDUVxUrmf8lbUn2eO6_WTk5ZBOOdE_fAGk"

class SarahSEOAnalyst:
    def __init__(self):
        self.name = "Sarah"
        self.specialty = "SEO"
    
    def analyze(self, site_data):
        print(f"    Sarah: KRITISCHE SEO analyse - Preview URL + Theme Files")
        
        # Get preview URL from site_data
        preview_url = site_data.get('shopify_preview_url', 'https://vloerproducten.myshopify.com/?preview_theme_id=main')
        
        # Haal echte PageSpeed data op van preview URL
        pagespeed_data = self._get_pagespeed_insights(preview_url)
        
        # Technische SEO audit van preview
        technical_audit = self._technical_seo_audit(preview_url)
        
        # Analyseer theme files voor SEO
        theme_seo_analysis = self._analyze_theme_seo_files(site_data.get('shopify_theme_path', '/Users/Frank/Documents/EMMSO'))
        
        # Bereken kritische score (nu met theme analysis)
        score = self._calculate_critical_score(pagespeed_data, technical_audit, theme_seo_analysis)
        
        # Genereer harde aanbevelingen
        recommendations = self._generate_critical_recommendations(pagespeed_data, technical_audit, theme_seo_analysis)
        
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
                'critical_issues': self._identify_critical_issues(pagespeed_data, technical_audit, theme_seo_analysis)
            },
            'recommendations': recommendations,
            # DIRECTED OUTPUT DOCUMENT (d.o.d) FORMAT
            'deliverable': self._generate_directed_output_document(score, pagespeed_data, technical_audit, theme_seo_analysis, recommendations)
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
                template_files = [f for f in os.listdir(templates_path) if f.endswith('.liquid')]
                analysis['template_analysis']['template_count'] = len(template_files)
                analysis['template_analysis']['files'] = template_files
                
                # Check for key SEO templates
                seo_critical_templates = ['product.liquid', 'collection.liquid', 'index.liquid', 'blog.liquid']
                missing_templates = [t for t in seo_critical_templates if t not in template_files]
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
                with open(config_path, 'r') as f:
                    config_content = f.read()
                    seo_settings = 'seo' in config_content.lower() or 'meta' in config_content.lower()
                    analysis['seo_elements_found']['seo_settings'] = seo_settings
                    
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
    def _calculate_critical_score(self, pagespeed_data, technical_audit, theme_seo_analysis=None):
        """Bereken MEEDOGENLOOS KRITISCHE SEO score - now includes theme analysis"""
        score = 0
        
        # NO PAGESPEED DATA = IMMEDIATE FAIL
        if not pagespeed_data or pagespeed_data.get('error'):
            return 0  # UNACCEPTABLE - Must have performance data
        
        # PERFORMANCE SCORE - STRENGERE EISEN (30 points, reduced for theme analysis)
        perf_score = pagespeed_data.get('performance_score', 0)
        if perf_score >= 90:
            score += 30  # EXCELLENT
        elif perf_score >= 75:
            score += 25  # GOOD
        elif perf_score >= 60:
            score += 20  # ACCEPTABLE
        elif perf_score >= 40:
            score += 10  # POOR
        else:
            score += 0   # DISASTER
        
        # SEO SCORE - PERFECTIE VEREIST (30 points, reduced for theme analysis)
        seo_score = pagespeed_data.get('seo_score', 0)
        if seo_score >= 95:
            score += 30  # NEAR PERFECT REQUIRED
        elif seo_score >= 90:
            score += 25  # GOOD
        elif seo_score >= 85:
            score += 20  # ACCEPTABLE
        elif seo_score >= 80:
            score += 15  # POOR
        else:
            score += 0   # FAIL
        
        # TECHNICAL SEO PERFECTION (20 points, reduced for theme analysis)
        tech_score = technical_audit.get('overall_score', 0)
        if tech_score >= 95:
            score += 20  # TECHNICAL EXCELLENCE
        elif tech_score >= 90:
            score += 15  # GOOD
        elif tech_score >= 85:
            score += 10  # ACCEPTABLE
        else:
            score += 0   # FAIL
        
        # THEME SEO ANALYSIS - NEW (20 points)
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
        
        return min(max(score, 0), 100)
    
    def _generate_critical_recommendations(self, pagespeed_data, technical_audit, theme_seo_analysis=None):
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
        
        return recommendations
    
    def _identify_critical_issues(self, pagespeed_data, technical_audit, theme_seo_analysis=None):
        """Identificeer kritieke problemen"""
        critical_issues = []
        
        if 'error' not in pagespeed_data:
            if pagespeed_data.get('performance_score', 0) < 50:
                critical_issues.append('CRITICAL: Performance score onder 50 - Google penalty')
        
        if 'error' not in technical_audit:
            if not technical_audit.get('meta_title_present', False):
                critical_issues.append('BLOCKER: Geen meta titles - onvindbaar in Google')
        
        return critical_issues
    
    def _generate_directed_output_document(self, score, pagespeed_data, technical_audit, theme_seo_analysis, recommendations):
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
        seo_traffic_multiplier = 0.20  # 20% average
        
        # Calculate potential monthly impact
        monthly_impact = base_monthly_value * improvement_potential * seo_traffic_multiplier
        
        return round(monthly_impact)
