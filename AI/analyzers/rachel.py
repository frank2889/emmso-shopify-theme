"""
Rachel - SMART Content & Structured Data Specialist for EMMSO AI System
========================================================================
AI-Powered Content Strategy & Schema.org Structured Data Expert
- Content Strategy & Quality Analysis
- Schema.org Implementation & Validation
- JSON-LD Structured Data Optimization
- Product/Organization/BreadcrumbList Schemas
"""
import requests
import os
import json
from datetime import datetime
from pathlib import Path
from .ai_helper import SmartAnalyzer

class RachelContentAnalyst(SmartAnalyzer):
    def __init__(self):
        super().__init__("Rachel", "Content Strategy & Structured Data")
        self.emmso_root = "/Users/Frank/Documents/EMMSO"
        
        # Structured Data Specialization
        self.schema_types = {
            'Organization': 'https://schema.org/Organization',
            'Product': 'https://schema.org/Product', 
            'BreadcrumbList': 'https://schema.org/BreadcrumbList',
            'WebSite': 'https://schema.org/WebSite',
            'Store': 'https://schema.org/Store',
            'Review': 'https://schema.org/Review',
            'AggregateRating': 'https://schema.org/AggregateRating'
        }
        self.structured_data_validator_url = "https://validator.schema.org/"
    
    def analyze(self, site_data):
        print(f"    Rachel: SMART Content analyse met AI content insights...")
        
        # Analyze live website content
        website_content = self.analyze_website_live()
        
        # Analyze template content structure
        template_content = self._analyze_template_content()
        
        # Smart content analysis with AI
        content_insights = self._get_smart_content_analysis()
        
        # STRUCTURED DATA ANALYSIS - Rachel's new specialization
        structured_data_analysis = self._analyze_structured_data()
        
        # Calculate content score (now includes structured data)
        score = self._calculate_content_score(website_content, template_content, content_insights, structured_data_analysis)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'findings': {
                'website_content': website_content,
                'template_structure': template_content,
                'content_insights': content_insights,
                'structured_data_analysis': structured_data_analysis,  # New structured data findings
                'multi_brand_content': self._analyze_multi_brand_content()
            },
            'recommendations': self._generate_content_recommendations(score, content_insights, structured_data_analysis),
            # DIRECTED OUTPUT DOCUMENT (d.o.d) FOR STRUCTURED DATA
            'deliverable': self._generate_structured_data_dod(score, structured_data_analysis, content_insights)
        }
    
    def _analyze_template_content(self):
        """Analyze Shopify templates for content structure"""
        try:
            templates_path = Path(f"{self.emmso_root}/templates")
            content_analysis = {}
            
            if templates_path.exists():
                for template_file in templates_path.glob("*.json"):
                    try:
                        with open(template_file, 'r', encoding='utf-8') as f:
                            template_data = json.load(f)
                        
                        content_analysis[template_file.name] = {
                            'sections_count': len(template_data.get('sections', {})),
                            'content_sections': self._identify_content_sections(template_data),
                            'seo_potential': self._assess_seo_potential(template_data)
                        }
                    except Exception as e:
                        content_analysis[template_file.name] = {'error': str(e)}
            
            return {
                'templates_analyzed': len(content_analysis),
                'content_structure': content_analysis,
                'overall_content_architecture': self._rate_content_architecture(content_analysis)
            }
        except Exception as e:
            return {'error': f"Template content analysis failed: {e}"}
    
    def _identify_content_sections(self, template_data):
        """Identify content-rich sections in template"""
        content_sections = []
        sections = template_data.get('sections', {})
        
        for section_id, section_data in sections.items():
            section_type = section_data.get('type', '')
            if any(keyword in section_type for keyword in ['content', 'text', 'rich-text', 'hero', 'featured']):
                content_sections.append(section_type)
        
        return content_sections
    
    def _assess_seo_potential(self, template_data):
        """Assess SEO potential of template"""
        seo_score = 0
        sections = template_data.get('sections', {})
        
        # Check for SEO-friendly sections
        seo_friendly_sections = ['hero', 'featured-product', 'rich-text', 'content']
        for section_data in sections.values():
            if any(seo_section in section_data.get('type', '') for seo_section in seo_friendly_sections):
                seo_score += 20
        
        return min(seo_score, 100)
    
    def _get_smart_content_analysis(self):
        """Get AI-powered content analysis"""
        if not self.openai_client:
            return {
                "content_quality": "Basic analysis - AI not available",
                "seo_opportunities": "Manual SEO review needed",
                "brand_voice": "Multi-brand setup present"
            }
        
        content_prompt = """
        Analyze the content strategy for EMMSO, a diving equipment e-commerce site with 3 brands:
        - Nauticam (premium technical diving)
        - Scubapro (professional & recreational)  
        - Aqualung (beginner to intermediate)
        
        Focus on:
        1. Content differentiation for different diving skill levels
        2. SEO content opportunities for diving equipment
        3. Brand voice consistency across multi-brand setup
        4. Educational content potential
        5. Product content optimization
        
        Return specific actionable content strategy insights in JSON format.
        """
        
        return self.smart_analyze_content("EMMSO multi-brand diving equipment content", content_prompt)
    
    def _analyze_multi_brand_content(self):
        """Analyze multi-brand content strategy"""
        try:
            # Check for brand-specific content in snippets
            snippets_path = Path(f"{self.emmso_root}/snippets")
            brand_content = {
                'nauticam_content': False,
                'scubapro_content': False,
                'aqualung_content': False,
                'dynamic_content': False
            }
            
            if snippets_path.exists():
                for snippet in snippets_path.glob("*.liquid"):
                    try:
                        content = self.get_file_content(snippet)
                        
                        if 'nauticam' in content.lower():
                            brand_content['nauticam_content'] = True
                        if 'scubapro' in content.lower():
                            brand_content['scubapro_content'] = True
                        if 'aqualung' in content.lower():
                            brand_content['aqualung_content'] = True
                        if 'metafields.brand' in content or 'product.vendor' in content:
                            brand_content['dynamic_content'] = True
                    except:
                        continue
            
            return brand_content
        except Exception as e:
            return {'error': f"Multi-brand content analysis failed: {e}"}
    
    def _rate_content_architecture(self, content_analysis):
        """Rate overall content architecture"""
        if not content_analysis:
            return 0
        
        score = 0
        valid_templates = 0
        
        for template_name, details in content_analysis.items():
            if 'error' not in details:
                # Rate based on content sections
                content_sections = len(details.get('content_sections', []))
                seo_potential = details.get('seo_potential', 0)
                
                template_score = min((content_sections * 20) + (seo_potential * 0.5), 100)
                score += template_score
                valid_templates += 1
        
        return score / valid_templates if valid_templates > 0 else 0
    
    def _calculate_content_score(self, website_content, template_content, content_insights, structured_data_analysis=None):
        """Calculate comprehensive content score including structured data"""
        base_score = 60  # Base content score
        
        # Content quality scoring (40 points)
        if website_content.get('response_code') == 200:
            base_score += 15
        
        if template_content.get('template_count', 0) > 5:
            base_score += 10
        
        if content_insights.get('content_quality') == 'high':
            base_score += 15
        
        # STRUCTURED DATA SCORING (40 points) - Rachel's new specialization
        if structured_data_analysis:
            schema_score = structured_data_analysis.get('structured_data_score', 0)
            # Convert schema score to 40-point contribution
            structured_data_points = (schema_score / 100) * 40
            base_score += structured_data_points
        
        return min(100, max(0, int(base_score)))
    
    def _generate_content_recommendations(self, score, content_insights, structured_data_analysis=None):
        """Generate content optimization recommendations + structured data"""
        recommendations = []
        
        # STRUCTURED DATA RECOMMENDATIONS (Rachel's new specialty)
        if structured_data_analysis:
            schema_score = structured_data_analysis.get('structured_data_score', 0)
            missing_schemas = structured_data_analysis.get('missing_schemas', [])
            
            if schema_score < 30:
                recommendations.append({
                    'title': 'CRITICAL: Implement Basic Structured Data',
                    'description': f'Missing {len(missing_schemas)} critical schema types - immediate SEO impact',
                    'priority': 'critical',
                    'impact': 'high'
                })
            elif schema_score < 70:
                recommendations.append({
                    'title': 'Expand Structured Data Coverage',
                    'description': 'Add Product, Organization, and Review schemas for rich snippets',
                    'priority': 'high',
                    'impact': 'medium'
                })
        
        # Content quality recommendations
        if score < 60:
            recommendations.append({
                'title': 'CRITICAL: Content Strategy Overhaul Needed',
                'description': 'Implement comprehensive content strategy for multi-brand diving equipment',
                'priority': 'critical',
                'impact': 'high'
            })
        
        if score < 75:
            recommendations.append({
                'title': 'Multi-Brand Content Differentiation',
                'description': 'Develop brand-specific content strategies for Nauticam, Scubapro, and Aqualung',
                'priority': 'high',
                'impact': 'high'
            })
        
        if content_insights.get('ai_powered'):
            recommendations.append({
                'title': 'AI-Powered Content Optimization',
                'description': 'Leverage AI insights for advanced content personalization',
                'priority': 'medium',
                'impact': 'medium'
            })
        
        if score >= 80:
            recommendations.append({
                'title': 'Advanced Content Marketing',
                'description': 'Implement educational content series and thought leadership',
                'priority': 'low',
                'impact': 'high'
            })
        
        return recommendations

    def _analyze_structured_data(self):
        """
        RACHEL'S STRUCTURED DATA SPECIALIZATION
        Analyze current structured data implementation and identify opportunities
        """
        print(f"      🔍 Rachel: Analyzing structured data schemas...")
        
        analysis = {
            'current_schemas': {},
            'missing_schemas': [],
            'schema_errors': [],
            'recommendations': [],
            'opportunities': []
        }
        
        try:
            # Check live website for existing structured data
            website_schemas = self._extract_website_schemas()
            analysis['current_schemas'] = website_schemas
            
            # Check theme files for structured data snippets
            theme_schemas = self._check_theme_structured_data()
            analysis['theme_implementation'] = theme_schemas
            
            # Identify missing critical schemas for e-commerce
            missing_schemas = self._identify_missing_schemas(website_schemas)
            analysis['missing_schemas'] = missing_schemas
            
            # Generate schema recommendations
            schema_recommendations = self._generate_schema_recommendations(missing_schemas)
            analysis['recommendations'] = schema_recommendations
            
            # Calculate structured data score
            analysis['structured_data_score'] = self._calculate_schema_score(website_schemas, missing_schemas)
            
        except Exception as e:
            analysis['error'] = f"Structured data analysis failed: {str(e)}"
            analysis['structured_data_score'] = 0
        
        return analysis
    
    def _extract_website_schemas(self):
        """Extract existing JSON-LD schemas from website"""
        schemas_found = {}
        
        try:
            # Check main page
            response = requests.get('https://emmso.com', timeout=10)
            content = response.text
            
            # Look for JSON-LD scripts
            import re
            json_ld_pattern = r'<script type="application/ld\+json">(.*?)</script>'
            json_ld_matches = re.findall(json_ld_pattern, content, re.DOTALL)
            
            for match in json_ld_matches:
                try:
                    schema_data = json.loads(match.strip())
                    schema_type = schema_data.get('@type', 'Unknown')
                    schemas_found[schema_type] = schema_data
                except json.JSONDecodeError:
                    continue
            
            # Check for microdata and RDFa as well
            if 'itemscope' in content:
                schemas_found['microdata_present'] = True
            if 'property=' in content:
                schemas_found['rdfa_present'] = True
                
        except Exception as e:
            schemas_found['error'] = str(e)
        
        return schemas_found
    
    def _check_theme_structured_data(self):
        """Check Shopify theme files for structured data implementation"""
        theme_analysis = {
            'structured_data_snippets': [],
            'json_ld_templates': [],
            'schema_implementations': []
        }
        
        try:
            # Check snippets for structured data
            snippets_path = f"{self.emmso_root}/snippets"
            if os.path.exists(snippets_path):
                snippet_files = os.listdir(snippets_path)
                
                for snippet in snippet_files:
                    if any(keyword in snippet.lower() for keyword in ['schema', 'structured', 'json-ld', 'microdata']):
                        theme_analysis['structured_data_snippets'].append(snippet)
                        
                        # Read snippet content to identify schema types
                        snippet_path = f"{snippets_path}/{snippet}"
                        try:
                            with open(snippet_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                for schema_type in self.schema_types.keys():
                                    if schema_type in content:
                                        theme_analysis['schema_implementations'].append({
                                            'file': snippet,
                                            'schema_type': schema_type,
                                            'implementation': 'detected'
                                        })
                        except Exception:
                            continue
            
            # Check templates for structured data
            templates_path = f"{self.emmso_root}/templates"
            if os.path.exists(templates_path):
                template_files = [f for f in os.listdir(templates_path) if f.endswith('.liquid')]
                
                for template in template_files:
                    template_path = f"{templates_path}/{template}"
                    try:
                        with open(template_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if 'application/ld+json' in content or 'schema.org' in content:
                                theme_analysis['json_ld_templates'].append(template)
                    except Exception:
                        continue
                        
        except Exception as e:
            theme_analysis['error'] = str(e)
        
        return theme_analysis
    
    def _identify_missing_schemas(self, current_schemas):
        """Identify critical missing schemas for EMMSO e-commerce"""
        critical_schemas = [
            'Organization',  # Company information
            'Product',       # Product pages
            'BreadcrumbList', # Navigation
            'WebSite',       # Site search
            'Store',         # Local business
            'Review',        # Product reviews
            'AggregateRating' # Rating aggregation
        ]
        
        missing = []
        for schema in critical_schemas:
            if schema not in current_schemas:
                missing.append({
                    'schema_type': schema,
                    'priority': 'HIGH' if schema in ['Organization', 'Product'] else 'MEDIUM',
                    'business_impact': self._get_schema_business_impact(schema)
                })
        
        return missing
    
    def _get_schema_business_impact(self, schema_type):
        """Get business impact description for schema type"""
        impacts = {
            'Organization': 'Brand visibility in search results, knowledge panel',
            'Product': 'Rich snippets, pricing, availability in search',
            'BreadcrumbList': 'Enhanced navigation in search results',
            'WebSite': 'Sitelinks search box, brand search optimization',
            'Store': 'Local SEO, store information in maps',
            'Review': 'Star ratings in search results, trust signals',
            'AggregateRating': 'Overall rating display, product credibility'
        }
        return impacts.get(schema_type, 'SEO and search visibility improvement')
    
    def _calculate_schema_score(self, current_schemas, missing_schemas):
        """Calculate structured data implementation score"""
        total_critical = 7  # Number of critical schemas
        implemented = len([s for s in current_schemas.keys() if s in ['Organization', 'Product', 'BreadcrumbList', 'WebSite', 'Store', 'Review', 'AggregateRating']])
        missing_count = len(missing_schemas)
        
        base_score = (implemented / total_critical) * 100
        
        # Bonus for proper JSON-LD implementation
        if any('json' in str(schema).lower() for schema in current_schemas.values()):
            base_score += 10
        
        return min(100, max(0, int(base_score)))
    
    def _generate_schema_recommendations(self, missing_schemas):
        """Generate specific schema implementation recommendations"""
        recommendations = []
        
        for schema in missing_schemas:
            schema_type = schema['schema_type']
            priority = schema['priority']
            
            rec = {
                'schema_type': schema_type,
                'implementation_file': self._get_recommended_file(schema_type),
                'priority': priority,
                'action': f"Implement {schema_type} schema markup",
                'example_url': f"https://schema.org/{schema_type}",
                'business_impact': schema['business_impact']
            }
            recommendations.append(rec)
        
        return recommendations
    
    def _get_recommended_file(self, schema_type):
        """Get recommended file location for schema implementation"""
        file_mapping = {
            'Organization': 'snippets/schema-organization.liquid',
            'Product': 'templates/product.liquid',
            'BreadcrumbList': 'snippets/schema-breadcrumbs.liquid',
            'WebSite': 'templates/theme.liquid',
            'Store': 'snippets/schema-store.liquid',
            'Review': 'snippets/schema-reviews.liquid',
            'AggregateRating': 'snippets/schema-rating.liquid'
        }
        return file_mapping.get(schema_type, 'snippets/schema-generic.liquid')
    
    def _generate_structured_data_dod(self, score, structured_data_analysis, content_insights):
        """
        Generate d.o.d (directed.output.document) for structured data implementation
        Rachel's specialty: Content + Structured Data optimization
        """
        
        # Determine urgency based on structured data score
        schema_score = structured_data_analysis.get('structured_data_score', 0)
        if schema_score < 30:
            urgency = "IMMEDIATE"
            timeline = "48 hours"
        elif schema_score < 60:
            urgency = "HIGH"
            timeline = "1 week"
        elif schema_score < 80:
            urgency = "MEDIUM"
            timeline = "2 weeks"
        else:
            urgency = "LOW"
            timeline = "1 month"
        
        # Generate target files for schema implementation
        target_files = []
        missing_schemas = structured_data_analysis.get('missing_schemas', [])
        
        for schema in missing_schemas[:5]:  # Top 5 priority schemas
            target_files.append({
                'file': self._get_recommended_file(schema['schema_type']),
                'action': f"Implement {schema['schema_type']} schema markup",
                'priority': schema['priority'],
                'schema_type': schema['schema_type']
            })
        
        # Add content optimization files
        if score < 70:
            target_files.extend([
                {
                    'file': 'templates/product.liquid',
                    'action': 'Optimize product content with schema integration',
                    'priority': 'HIGH'
                },
                {
                    'file': 'snippets/content-schema.liquid',
                    'action': 'Create unified content-schema snippet',
                    'priority': 'MEDIUM'
                }
            ])
        
        # Revenue impact calculation
        revenue_impact = self._calculate_structured_data_revenue_impact(schema_score)
        
        deliverable = {
            'format': 'd.o.d',
            'analyst': 'Rachel (Content & Structured Data)',
            'deliverable_type': 'STRUCTURED_DATA_CONTENT_PACKAGE',
            'urgency': urgency,
            'implementation_timeline': timeline,
            'target_files': target_files,
            'specific_actions': {
                'WHAT': [
                    f"Implement {len(missing_schemas)} missing schema types",
                    "Create JSON-LD structured data snippets",
                    "Optimize content for rich snippets",
                    "Validate schema markup implementation"
                ],
                'WHERE': {
                    'snippets/': 'Schema markup components',
                    'templates/product.liquid': 'Product schema integration',
                    'templates/theme.liquid': 'Organization/Website schemas'
                },
                'WHEN': timeline,
                'WHY': f"Structured data implementation can generate €{revenue_impact:,}/month additional organic traffic revenue"
            },
            'captain_instructions': {
                'deployment_order': [
                    "1. Create schema snippet infrastructure",
                    "2. Implement Organization schema (brand visibility)",
                    "3. Add Product schemas (rich snippets)",
                    "4. Implement navigation schemas",
                    "5. Validate with Google's Structured Data Testing Tool"
                ],
                'success_metrics': [
                    f"Structured data score > 80 (current: {schema_score})",
                    "Zero schema validation errors",
                    "Rich snippets appearing in search results",
                    "Improved click-through rates from search"
                ],
                'validation_commands': [
                    "Test with Google's Rich Results Test",
                    "Validate JSON-LD syntax",
                    "Check schema.org compliance",
                    "Monitor search console for rich snippet data"
                ]
            },
            'business_context': {
                'okr_impact': 'AI Quality Score ≥ 90/100 + Brand Health >95%',
                'revenue_potential': f"€{revenue_impact:,}/month",
                'market_coverage': 'Nederland, Denemarken, België, Duitsland, Frankrijk, Oostenrijk, Ierland, Italië, Spanje, Portugal',
                'seo_benefits': 'Rich snippets, brand visibility, click-through rate improvement'
            },
            'structured_data_specifics': {
                'missing_schemas': missing_schemas,
                'current_implementation': structured_data_analysis.get('current_schemas', {}),
                'priority_schemas': [s for s in missing_schemas if s['priority'] == 'HIGH']
            }
        }
        
        return deliverable
    
    def _calculate_structured_data_revenue_impact(self, current_score):
        """Calculate potential monthly revenue impact from structured data implementation"""
        # Base monthly organic traffic value
        base_monthly_value = 30000  # €30k base organic traffic value
        
        # Structured data typically improves CTR by 15-30%
        ctr_improvement = 0.25  # 25% average CTR improvement
        
        # Score improvement potential
        improvement_potential = (100 - current_score) / 100
        
        # Calculate potential monthly impact
        monthly_impact = base_monthly_value * improvement_potential * ctr_improvement
        
        return round(monthly_impact)
