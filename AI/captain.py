#!/usr/bin/env python3

import os
import sys
import json
from datetime import datetime
from typing import Dict, List, Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Import revenue calculator
try:
    from revenue_calculator import EMMSORevenueCalculator
except ImportError:
    print("⚠️  Revenue Calculator not found - installing...")
    EMMSORevenueCalculator = None

class EMMSOCaptain:
    """
    EMMSO AI Captain - De Commandant van het AI Team
    ===============================================
    
    Captain stuurt het team, geeft opdrachten gebaseerd op EMMSO.md business plan,
    en rapporteert terug aan de human. Hij is de schakel tussen human management 
    en AI workforce.
    
    Business Intelligence:
    - Leest EMMSO.md voor strategische context
    - Geeft team opdrachten gebaseerd op business goals
    - Monitort KPI's en OKR's zoals gedefinieerd in business plan
    """
    
    def __init__(self):
        print("🚢 EMMSO AI Captain reporting for duty!")
        print("   Initializing tactical command center...")
        
        self.ai_team = {}
        self.business_plan = self._load_business_plan()
        
        # Initialize Revenue Calculator for business impact analysis
        self.revenue_calculator = EMMSORevenueCalculator() if EMMSORevenueCalculator else None
        if self.revenue_calculator:
            print("   💰 Revenue Impact Calculator activated")
        else:
            print("   ⚠️  Revenue Calculator not available")
        
        self.load_analysts()
        self.mission_status = "STANDBY"
        self.last_analysis = None
        self.human_commands = []
        
        # Show business context
        self._display_business_context()
        
    def _load_business_plan(self) -> dict:
        """Load EMMSO.md business plan + documentation for strategic guidance"""
        try:
            emmso_path = os.path.join(os.path.dirname(__file__), 'docs', 'EMMSO.md')
            with open(emmso_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Load additional technical documentation
            docs_path = '/Users/Frank/Documents/EMMSO/docs'
            technical_docs = self._load_technical_documentation(docs_path)
            
            # Extract key business metrics and goals
            business_context = {
                'north_star': 'aantal qualifying brands live × GMV via licentiemodel × AI Quality Score',
                'okrs': [
                    '12 premium merken live - time-to-brand-launch ≤ 21 dagen',
                    'AI Quality Score ≥ 90/100 over content/search/UX',
                    'Royalty-GMV +40% YoY - Ads ROI +20%, Organic +20%'
                ],
                'brand_fit_score_target': 70,
                'revenue_model': 'License + Performance Royalty',
                'key_metrics': ['Brand Health >95%', 'CTR uplift ≥10%', 'Time-to-live ≤21 dagen'],
                'target_markets': {
                    'primary_countries': ['Nederland', 'Denemarken', 'België', 'Duitsland', 'Frankrijk', 'Oostenrijk', 'Ierland', 'Italië', 'Spanje', 'Portugal'],
                    'url_structure': {
                        '/': 'Nederlands (primary)',
                        '/da': 'Deens/Denemarken', 
                        '/de': 'Duits/Duitsland+Oostenrijk',
                        '/en': 'Engels/Ierland',
                        '/it': 'Italiaans/Italië', 
                        '/es': 'Spaans/Spanje',
                        '/fr': 'Frans/Frankrijk+België',
                        '/pt': 'Portugees/Portugal (MISSING URL)'
                    },
                    'missing_markets': ['Portugal (/pt URL missing)']
                },
                'technical_constraints': {
                    'css_rule': 'ALL CSS must be written ONLY in emmso.css - NO other CSS files allowed',
                    'js_rule': 'ALL JavaScript must be written ONLY in emmso.js - NO other JS files allowed',
                    'affected_analysts': ['Marcus (Performance)', 'Nora (Visual)', 'Alex (Shopify)', 'Jessica (UX)']
                },
                'technical_documentation': technical_docs,
                'full_content': content
            }
            
            print(f"   📊 Business plan + {len(technical_docs)} technical docs loaded")
            return business_context
            
        except Exception as e:
            print(f"   ⚠️  Business plan not found: {e}")
            return {'error': 'Business plan unavailable', 'full_content': ''}
    
    def _load_technical_documentation(self, docs_path: str) -> dict:
        """Load technical documentation and map to analysts"""
        docs = {}
        doc_mapping = {
            'ARCHITECT.MD': ['Alex', 'Marcus', 'Sarah'],  # Architecture affects Shopify, Performance, SEO
            'CSS.md': ['Marcus', 'Nora', 'Jessica'],      # CSS affects Performance, Visual, UX
            'JS.md': ['Marcus', 'Alex', 'Jessica'],       # JS affects Performance, Shopify, UX
            'DESIGN.MD': ['Nora', 'Jessica', 'Alex'],     # Design affects Visual, UX, Shopify
            'SECTIONS-CLEANUP-CHECKLIST.md': ['Alex', 'Nora', 'Jessica']  # Sections affect Shopify, Visual, UX
        }
        
        try:
            for filename, analysts in doc_mapping.items():
                doc_path = os.path.join(docs_path, filename)
                if os.path.exists(doc_path):
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    docs[filename] = {
                        'content': content[:2000],  # First 2000 chars for context
                        'assigned_analysts': analysts,
                        'priority': 'HIGH' if filename in ['ARCHITECT.MD', 'CSS.md', 'JS.md'] else 'MEDIUM'
                    }
                    print(f"      📄 {filename} → {', '.join(analysts)}")
        except Exception as e:
            print(f"      ❌ Error loading docs: {e}")
        
        return docs
    
    def _display_business_context(self):
        """Display key business context for human awareness"""
        if 'error' in self.business_plan:
            print("   ❌ No business context available")
            return
            
        print(f"""
   🎯 BUSINESS CONTEXT LOADED:
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   North Star: {self.business_plan['north_star']}
   
   Key OKRs:
   • {self.business_plan['okrs'][0]}
   • {self.business_plan['okrs'][1]} 
   • {self.business_plan['okrs'][2]}
   
   Target Markets: {len(self.business_plan['target_markets']['primary_countries'])} countries
   🌍 {', '.join(self.business_plan['target_markets']['primary_countries'])}
   
   � TECHNICAL DOCUMENTATION:
   {self._format_doc_assignments()}
   
   �🚨 CRITICAL TECHNICAL CONSTRAINTS:
   • CSS: ONLY emmso.css allowed (affects Marcus, Nora, Alex, Jessica)
   • JS: ONLY emmso.js allowed (affects Marcus, Alex, Jessica)
   
   Target Brand Fit Score: {self.business_plan['brand_fit_score_target']}/100
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """)
    
    def _format_doc_assignments(self) -> str:
        """Format documentation assignments for display"""
        docs = self.business_plan.get('technical_documentation', {})
        if not docs:
            return "   No technical docs loaded"
        
        lines = []
        for doc_name, doc_info in docs.items():
            analysts = ', '.join(doc_info['assigned_analysts'])
            priority = doc_info['priority']
            lines.append(f"   • {doc_name} → {analysts} ({priority})")
        
        return '\n'.join(lines)
    
    def _analyze_theme_structure(self) -> dict:
        """Analyze local Shopify theme file structure for team analysis"""
        theme_base = '/Users/Frank/Documents/EMMSO'
        
        structure = {
            'assets': [],
            'sections': [],
            'snippets': [],
            'templates': [],
            'locales': [],
            'layout': [],
            'config': []
        }
        
        # Scan each critical directory
        for directory in structure.keys():
            dir_path = os.path.join(theme_base, directory)
            if os.path.exists(dir_path):
                try:
                    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
                    structure[directory] = files
                    print(f"   📁 {directory}: {len(files)} files detected")
                except Exception as e:
                    print(f"   ❌ {directory}: Error reading - {e}")
            else:
                print(f"   ⚠️  {directory}: Directory not found")
        
        return structure
        
    def load_analysts(self):
        """Recruit and organize the AI team under my command"""
        print("   📋 Recruiting AI specialists...")
        
        # My elite team of 11 AI specialists
        analysts = [
            ('sarah', 'SarahSEOAnalyst', 'SEO & Technical Audit'),
            ('jessica', 'JessicaUXAnalyst', 'User Experience & Design'),
            ('eva', 'EvaAnalyticsAnalyst', 'Data Analytics & Intelligence'),
            ('mike', 'MikeConversionAnalyst', 'Conversion Rate Optimization'),
            ('rachel', 'RachelContentAnalyst', 'Content Strategy & Structured Data'),
            ('alex', 'AlexShopifyAnalyst', 'Shopify Platform & E-commerce'),
            ('marcus', 'MarcusPerformanceAnalyst', 'Site Performance & Speed'),
            ('nora', 'NoraVisualAnalyst', 'Visual Design & Branding'),
            ('dave', 'DaveAdsAnalyst', 'Paid Media & ROAS Intelligence'),
            ('sophie', 'SophieSocialAnalyst', 'Social Media & Community'),
            ('emma', 'EmmaEmailAnalyst', 'Email Marketing & Automation')
        ]
        
        team_ready = 0
        for name, class_name, specialty in analysts:
            try:
                module = __import__(f'analyzers.{name}', fromlist=[class_name])
                analyst_class = getattr(module, class_name)
                self.ai_team[name] = analyst_class()
                print(f"     ✅ {name.title()} ({specialty}) - READY FOR ORDERS")
                team_ready += 1
            except Exception as e:
                print(f"     ❌ {name.title()} ({specialty}) - UNAVAILABLE: {e}")
        
        print(f"   🎯 Team Status: {team_ready}/{len(analysts)} analysts operational")
        if team_ready < len(analysts):
            print("   ⚠️  WARNING: Squad incomplete - some analysts missing!")
    
    def receive_human_command(self, command: str, priority: str = "NORMAL") -> str:
        """Receive orders from human command and acknowledge"""
        timestamp = datetime.now().isoformat()
        
        command_log = {
            'timestamp': timestamp,
            'command': command,
            'priority': priority,
            'status': 'RECEIVED'
        }
        
        self.human_commands.append(command_log)
        
        response = f"""
🎯 COMMAND RECEIVED AND LOGGED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Time: {timestamp}
Priority: {priority}
Command: "{command}"
Status: ACKNOWLEDGED - PREPARING EXECUTION

Next Steps:
1. Deploy relevant AI specialists
2. Execute comprehensive analysis  
3. Report findings back to command
4. Await further orders

Captain out. 🚢
        """
        
        print(response)
        return response
    
    def execute_mission(self, mission_type: str = "FULL_AUDIT") -> Dict[str, Any]:
        """Execute strategic mission with business-driven objectives"""
        print(f"🚀 MISSION START: {mission_type}")
        print("   Deploying AI team for business intelligence gathering...")
        
        self.mission_status = "ACTIVE"
        
        # Create business-driven site data with strategic context
        site_data = {
            'domain': 'emmso.com',
            'shopify_preview_url': 'https://vloerproducten.myshopify.com/?preview_theme_id=main',  # Shopify preview
            'shopify_theme_path': '/Users/Frank/Documents/EMMSO',  # Local theme files
            'theme_structure': self._analyze_theme_structure(),
            'timestamp': datetime.now().isoformat(),
            'mission_type': mission_type,
            'captain_orders': self.human_commands[-1] if self.human_commands else None,
            'business_context': self.business_plan,
            'strategic_priorities': self._get_strategic_priorities()
        }
        
        # Deploy team with specific business objectives
        mission_results = {}
        critical_issues = []
        tactical_recommendations = []
        business_impact_analysis = []
        revenue_opportunities = {}  # Track revenue potential per analyst
        directed_deliverables = {}  # Track d.o.d outputs per analyst
        
        print("   🔍 Business intelligence gathering in progress...")
        
        # Give specific orders to each analyst based on business goals
        analyst_orders = self._generate_analyst_orders()
        
        for name, analyst in self.ai_team.items():
            try:
                # Give specific business-focused order
                order = analyst_orders.get(name, "Standard analysis")
                print(f"      � {name.title()}: {order}")
                
                # Execute analysis with business context
                result = analyst.analyze(site_data)
                mission_results[name] = result
                
                score = result.get('score', 0)
                print(f"         Score: {score}/100")
                
                # REVENUE IMPACT CALCULATION
                if self.revenue_calculator:
                    revenue_impact = self._calculate_revenue_impact_for_analyst(name, score, site_data)
                    revenue_opportunities[name] = revenue_impact
                    result['revenue_impact'] = revenue_impact
                    
                    # Add revenue context to business impact
                    annual_potential = revenue_impact.get('revenue_impact', {}).get('annual_euro', 0)
                    if annual_potential > 0:
                        print(f"         💰 Revenue Potential: €{annual_potential:,}/jaar")
                
                # PROCESS DIRECTED OUTPUT DOCUMENT (d.o.d) FORMAT
                if 'deliverable' in result:
                    deliverable = result['deliverable']
                    if deliverable.get('format') == 'd.o.d':
                        print(f"         📋 d.o.d Output received - {deliverable.get('deliverable_type', 'UNKNOWN')}")
                        
                        # Extract and queue specific actions
                        deliverable_info = self._process_directed_output_document(name, deliverable, result)
                        directed_deliverables[name] = deliverable_info
                
                # Business impact assessment
                impact = self._assess_business_impact(name, score, result)
                business_impact_analysis.append(impact)
                
                # Collect critical intel with business context
                if score < 30:
                    critical_issues.append(f"{name.title()}: BUSINESS CRITICAL - Score {score}/100 - {impact}")
                elif score < 60:
                    critical_issues.append(f"{name.title()}: REVENUE RISK - Score {score}/100 - {impact}")
                
                # Collect business-focused recommendations
                if 'recommendations' in result:
                    business_recs = self._contextualize_recommendations(name, result['recommendations'])
                    tactical_recommendations.extend(business_recs)
                    
            except Exception as e:
                print(f"         ❌ Analysis failed: {e}")
                mission_results[name] = {'error': str(e), 'score': 0}
                critical_issues.append(f"{name.title()}: SYSTEM ERROR - Business intelligence compromised")
        
        # Calculate business metrics
        scores = [r.get('score', 0) for r in mission_results.values() if 'error' not in r]
        overall_score = int(sum(scores) / len(scores)) if scores else 0
        
        # Business impact assessment
        business_health = self._calculate_business_health(overall_score, critical_issues)
        
        self.mission_status = "COMPLETE"
        self.last_analysis = {
            'timestamp': datetime.now().isoformat(),
            'overall_score': overall_score,
            'business_health': business_health,
            'mission_results': mission_results,
            'critical_issues': critical_issues,
            'tactical_recommendations': tactical_recommendations,
            'business_impact_analysis': business_impact_analysis,
            'directed_deliverables': directed_deliverables  # Add d.o.d tracking
        }
        
        # Generate business-focused mission report with deliverables
        revenue_report = self._generate_revenue_opportunity_report(revenue_opportunities) if revenue_opportunities else None
        deliverables_report = self._generate_deliverables_action_plan(directed_deliverables) if directed_deliverables else None
        self.report_to_human_with_business_context(overall_score, critical_issues, tactical_recommendations, business_health, revenue_report, deliverables_report)
        
        # Generate Copilot-ready action items including d.o.d outputs
        copilot_tasks = self._generate_copilot_tasks(mission_results, critical_issues, directed_deliverables)
        self.last_analysis['copilot_tasks'] = copilot_tasks
        
        return self.last_analysis
    
    def _get_strategic_priorities(self) -> List[str]:
        """Extract strategic priorities from business plan"""
        return [
            "AI Quality Score ≥ 90/100 target",
            "Brand Health >95% schema validation", 
            "CTR uplift ≥10% in 60 dagen",
            "Time-to-brand-launch ≤ 21 dagen",
            "Royalty-GMV +40% YoY growth",
            "0 'grijze' URLs target",
            "BESTE WEBSHOP in 10 target markets",
            "Multi-market optimization (NL, DK, BE, DE, FR, AT, IE, IT, ES, PT)",
            "STRICT: CSS only in emmso.css",
            "STRICT: JavaScript only in emmso.js"
        ]
    
    def _generate_analyst_orders(self) -> Dict[str, str]:
        """Generate specific business-driven orders for each analyst - mix of local files and preview URL"""
        return {
            'sarah': "MULTI-MARKET SEO: Check /templates/ for internationalization + test preview URL Core Web Vitals. VERIFY: 10 market URLs (/da, /de, /en, /it, /es, /fr, etc.)",
            'jessica': "UX CONSTRAINTS: Analyze preview URL user flows across 10 markets + inspect /sections/ for UX patterns. CRITICAL: CSS ONLY in emmso.css, JS ONLY in emmso.js", 
            'eva': "MARKET ANALYTICS: Test preview URL analytics for all 10 markets + verify /snippets/ tracking. PRIORITY: Multi-market conversion attribution.",
            'mike': "MARKET CONVERSION: Test preview URL conversion funnels across all markets + check /sections/ CTA patterns. FOCUS: Market-specific optimization.",
            'rachel': "MULTI-MARKET CONTENT: Review preview URL content for 10 markets + analyze /locales/ consistency. VERIFY: Nederland, Denemarken, België, Duitsland, Frankrijk, etc.",
            'alex': "TECHNICAL CONSTRAINTS: Full theme analysis with STRICT rules - CSS ONLY in emmso.css, JS ONLY in emmso.js. CHECK: Multi-market URL structure compliance.",
            'marcus': "PERFORMANCE + CONSTRAINTS: Load preview URL speed for all markets + optimize ONLY emmso.css and emmso.js files. CRITICAL: Single-file CSS/JS architecture.",
            'nora': "VISUAL CONSTRAINTS: Preview URL visual consistency across 10 markets + ALL design changes ONLY in emmso.css. VERIFY: Brand consistency per market.",
            'dave': "MARKET ADS: Preview URL ads pixel testing for all 10 markets - NO design files needed. FOCUS: Multi-market advertising attribution.",
            'sophie': "SOCIAL MULTI-MARKET: Preview URL social features across markets + /snippets/ social widgets. FOCUS: Market-specific social strategies.", 
            'emma': "EMAIL MULTI-MARKET: Preview URL email capture for all 10 markets + /templates/ newsletter integration. VERIFY: Market-specific email flows."
        }
    
    def _assess_business_impact(self, analyst_name: str, score: int, result: dict) -> str:
        """Assess business impact of analyst findings"""
        if score < 30:
            return "IMMEDIATE REVENUE THREAT"
        elif score < 50:
            return "OKR ACHIEVEMENT AT RISK" 
        elif score < 70:
            return "SUBOPTIMAL ROI"
        else:
            return "CONTRIBUTING TO BUSINESS GOALS"
    
    def _calculate_revenue_impact_for_analyst(self, analyst_name: str, score: int, site_data: dict) -> dict:
        """Calculate revenue impact for specific analyst using REAL DATA"""
        if not self.revenue_calculator:
            return {'error': 'Revenue calculator not available'}
        
        # Map analyst names to revenue calculator types
        analyzer_type_mapping = {
            'sarah': 'seo',
            'jessica': 'ux', 
            'eva': 'analytics',
            'mike': 'conversion',
            'rachel': 'content',
            'alex': 'performance',  # Alex is Shopify but impacts performance
            'marcus': 'performance',
            'nora': 'visual',
            'dave': 'ads',
            'sophie': 'social',
            'emma': 'email'
        }
        
        analyzer_type = analyzer_type_mapping.get(analyst_name, 'conversion')
        
        # Get target markets from business plan
        target_markets = self.business_plan.get('target_markets', {}).get('primary_countries', ['Nederland'])
        
        # Determine optimization level based on score
        if score < 30:
            optimization_level = 'high'     # Agressieve approach needed
        elif score < 60:
            optimization_level = 'medium'   # Standard approach
        else:
            optimization_level = 'low'      # Fine-tuning only
        
        try:
            # Use REAL DATA calculation instead of estimates
            revenue_impact = self.revenue_calculator.calculate_revenue_impact_real_data(
                analyzer_type=analyzer_type,
                current_score=score,
                target_markets=target_markets[:3],  # Top 3 markets to keep calculation realistic
                optimization_level=optimization_level
            )
            
            # Add EMMSO-specific context
            revenue_impact['emmso_context'] = {
                'analyst_name': analyst_name,
                'business_priority': self._get_business_priority_for_analyst(analyst_name),
                'okr_alignment': self._get_okr_alignment(analyst_name, score),
                'implementation_urgency': 'HIGH' if score < 40 else 'MEDIUM' if score < 70 else 'LOW'
            }
            
            return revenue_impact
            
        except Exception as e:
            # Fallback to estimates if real data fails
            try:
                revenue_impact = self.revenue_calculator.calculate_revenue_impact(
                    analyzer_type=analyzer_type,
                    current_score=score,
                    target_markets=target_markets[:3],
                    optimization_level=optimization_level
                )
                revenue_impact['data_source'] = 'FALLBACK_ESTIMATES'
                return revenue_impact
            except Exception as e2:
                return {'error': f'Revenue calculation failed: {str(e)} / Fallback: {str(e2)}'}
    
    def _get_business_priority_for_analyst(self, analyst_name: str) -> str:
        """Get business priority level for analyst"""
        high_priority = ['sarah', 'marcus', 'alex', 'mike']  # Direct OKR impact
        medium_priority = ['jessica', 'eva', 'dave']         # Revenue impact
        low_priority = ['rachel', 'nora', 'sophie', 'emma']  # Support functions
        
        if analyst_name in high_priority:
            return 'HIGH - Direct OKR Impact'
        elif analyst_name in medium_priority:
            return 'MEDIUM - Revenue Impact'
        else:
            return 'LOW - Support Function'
    
    def _get_okr_alignment(self, analyst_name: str, score: int) -> str:
        """Determine OKR alignment for analyst"""
        okr_mapping = {
            'sarah': 'AI Quality Score ≥ 90/100',
            'marcus': 'AI Quality Score ≥ 90/100', 
            'alex': 'Brand Health >95% + Time-to-launch ≤21d',
            'mike': 'Royalty-GMV +40% YoY',
            'dave': 'Ads ROI +20%',
            'eva': 'Attribution + Performance Tracking',
            'jessica': 'User Experience Quality',
            'rachel': 'Content Quality + Multi-market',
            'nora': 'Brand Consistency',
            'sophie': 'Social Media Growth',
            'emma': 'Email Marketing ROI'
        }
        
        okr = okr_mapping.get(analyst_name, 'General Business Impact')
        
        if score < 40:
            return f"🚨 BLOCKING: {okr}"
        elif score < 70:
            return f"⚠️ AT RISK: {okr}"
        else:
            return f"✅ SUPPORTING: {okr}"
    
    def _generate_revenue_opportunity_report(self, revenue_opportunities: dict) -> dict:
        """Generate comprehensive revenue opportunity report"""
        if not self.revenue_calculator or not revenue_opportunities:
            return {}
        
        try:
            # Use revenue calculator's report generation
            return self.revenue_calculator.generate_market_opportunity_report(revenue_opportunities)
        except Exception as e:
            print(f"⚠️ Revenue report generation failed: {e}")
            return {}
    
    def _contextualize_recommendations(self, analyst_name: str, recommendations: List[str]) -> List[str]:
        """Add business context to analyst recommendations"""
        business_recs = []
        for rec in recommendations:
            business_context = ""
            if analyst_name in ['sarah', 'marcus']:
                business_context = f"[AI Quality Score Impact] {rec}"
            elif analyst_name in ['dave', 'mike']:
                business_context = f"[Revenue Growth Impact] {rec}"
            elif analyst_name in ['eva']:
                business_context = f"[Attribution Accuracy] {rec}"
            else:
                business_context = f"[Brand Health] {rec}"
            business_recs.append(business_context)
        return business_recs
    
    def _calculate_business_health(self, overall_score: int, critical_issues: List[str]) -> str:
        """Calculate overall business health status"""
        critical_count = len([issue for issue in critical_issues if "CRITICAL" in issue])
        
        if overall_score >= 90 and critical_count == 0:
            return "OPTIMAL - OKR targets achievable"
        elif overall_score >= 70 and critical_count <= 2:
            return "HEALTHY - Minor optimizations needed"
        elif overall_score >= 50:
            return "AT RISK - Business goals threatened"
        else:
            return "CRITICAL - Immediate intervention required"
    
    def _process_directed_output_document(self, analyst_name: str, deliverable: Dict, result: Dict):
        """Process directed output document (d.o.d) from analyst and queue for Captain execution"""
        print(f"         📋 Processing d.o.d from {analyst_name}...")
        
        # Extract key deliverable information
        urgency = deliverable.get('urgency', 'MEDIUM')
        timeline = deliverable.get('implementation_timeline', '1 week')
        target_files = deliverable.get('target_files', [])
        
        # Log the specific actions for Captain tracking
        specific_actions = deliverable.get('specific_actions', {})
        what_actions = specific_actions.get('WHAT', [])
        where_locations = specific_actions.get('WHERE', {})
        
        print(f"         ⚡ Urgency: {urgency} | Timeline: {timeline}")
        print(f"         📁 Target Files: {len(target_files)} files identified")
        
        # Return deliverable info for mission tracking
        deliverable_info = {
            'deliverable': deliverable,
            'processing_status': 'QUEUED',
            'timestamp': datetime.now().isoformat(),
            'captain_priority': self._calculate_captain_priority(urgency, len(target_files)),
            'execution_sequence': self._generate_execution_sequence(target_files)
        }
        
        return deliverable_info
    
    def _process_directed_deliverable(self, analyst_name: str, deliverable: Dict, result: Dict):
        """Legacy alias for _process_directed_output_document"""
        return self._process_directed_output_document(analyst_name, deliverable, result)
        
        # Extract key deliverable information
        urgency = deliverable.get('urgency', 'MEDIUM')
        timeline = deliverable.get('implementation_timeline', '1 week')
        target_files = deliverable.get('target_files', [])
        
        # Log the specific actions for Captain tracking
        specific_actions = deliverable.get('specific_actions', {})
        what_actions = specific_actions.get('WHAT', [])
        where_locations = specific_actions.get('WHERE', {})
        
        print(f"         ⚡ Urgency: {urgency} | Timeline: {timeline}")
        print(f"         📁 Target Files: {len(target_files)} files identified")
        
        # Return deliverable info for mission tracking
        deliverable_info = {
            'deliverable': deliverable,
            'processing_status': 'QUEUED',
            'timestamp': datetime.now().isoformat(),
            'captain_priority': self._calculate_captain_priority(urgency, len(target_files)),
            'execution_sequence': self._generate_execution_sequence(target_files)
        }
        
        return deliverable_info
    
    def _calculate_captain_priority(self, urgency: str, file_count: int) -> int:
        """Calculate Captain execution priority (1-10, 10 = highest)"""
        urgency_scores = {
            'IMMEDIATE': 10,
            'HIGH': 8,
            'MEDIUM': 5,
            'LOW': 2
        }
        
        base_priority = urgency_scores.get(urgency, 5)
        
        # Adjust for complexity (more files = higher complexity)
        complexity_adjustment = min(2, file_count // 3)
        
        return min(10, base_priority + complexity_adjustment)
    
    def _generate_execution_sequence(self, target_files: List[Dict]) -> List[str]:
        """Generate ordered execution sequence for Captain deployment"""
        sequence = []
        
        # Sort by priority first
        high_priority = [f for f in target_files if f.get('priority') == 'HIGH']
        medium_priority = [f for f in target_files if f.get('priority') == 'MEDIUM']
        low_priority = [f for f in target_files if f.get('priority') == 'LOW']
        
        # Generate execution steps
        step = 1
        for file_group, priority_name in [(high_priority, 'HIGH'), (medium_priority, 'MEDIUM'), (low_priority, 'LOW')]:
            for file_info in file_group:
                sequence.append(f"Step {step} ({priority_name}): {file_info.get('file', 'unknown')} - {file_info.get('action', 'no action specified')}")
                step += 1
        
        return sequence
    
    def _generate_deliverables_action_plan(self, directed_deliverables: Dict) -> Dict:
        """Generate comprehensive action plan from all d.o.d outputs"""
        if not directed_deliverables:
            return {}
        
        action_plan = {
            'total_deliverables': len(directed_deliverables),
            'immediate_actions': [],
            'high_priority_actions': [],
            'medium_priority_actions': [],
            'file_deployment_map': {},
            'estimated_total_timeline': '0 hours'
        }
        
        total_hours = 0
        file_map = {}
        
        for analyst_name, deliverable_info in directed_deliverables.items():
            deliverable = deliverable_info.get('deliverable', {})
            urgency = deliverable.get('urgency', 'MEDIUM')
            target_files = deliverable.get('target_files', [])
            
            # Calculate time estimation
            file_count = len(target_files)
            estimated_hours = file_count * 2  # 2 hours per file average
            total_hours += estimated_hours
            
            # Categorize actions by urgency
            action_summary = f"{analyst_name}: {deliverable.get('deliverable_type', 'ANALYSIS')} - {file_count} files"
            
            if urgency == 'IMMEDIATE':
                action_plan['immediate_actions'].append(action_summary)
            elif urgency == 'HIGH':
                action_plan['high_priority_actions'].append(action_summary)
            else:
                action_plan['medium_priority_actions'].append(action_summary)
            
            # Build file deployment map
            for file_info in target_files:
                file_path = file_info.get('file', 'unknown')
                if file_path not in file_map:
                    file_map[file_path] = []
                file_map[file_path].append({
                    'analyst': analyst_name,
                    'action': file_info.get('action', 'no action'),
                    'priority': file_info.get('priority', 'MEDIUM')
                })
        
        action_plan['file_deployment_map'] = file_map
        action_plan['estimated_total_timeline'] = f"{total_hours} hours"
        
        return action_plan
    
    def _generate_copilot_tasks(self, mission_results: Dict[str, Any], critical_issues: List[str], directed_deliverables: Dict = None) -> List[Dict[str, str]]:
        """Generate specific, actionable tasks for Copilot to implement"""
        copilot_tasks = []
        
        # Analyze each analyst's findings and convert to Copilot tasks
        for analyst_name, result in mission_results.items():
            if 'error' in result:
                continue
                
            score = result.get('score', 0)
            recommendations = result.get('recommendations', [])
            
            # Generate specific file-based tasks with market and constraint awareness
            if analyst_name == 'alex' and score < 70:
                copilot_tasks.append({
                    'priority': 'HIGH',
                    'analyst': 'Alex (Shopify)',
                    'task': 'Update /config/settings_schema.json for multi-brand + multi-market architecture (10 countries)',
                    'files_to_modify': ['config/settings_schema.json'],
                    'business_impact': 'Enable multi-brand functionality across 10 target markets',
                    'constraints': 'Ensure internationalization support for NL, DK, BE, DE, FR, AT, IE, IT, ES, PT'
                })
                
            if analyst_name == 'sarah' and score < 70:
                copilot_tasks.append({
                    'priority': 'HIGH', 
                    'analyst': 'Sarah (SEO)',
                    'task': 'Add structured data (JSON-LD) to /templates/product.liquid with multi-market hreflang support',
                    'files_to_modify': ['templates/product.liquid', 'snippets/structured-data.liquid'],
                    'business_impact': 'Improve AI Quality Score + multi-market SEO performance',
                    'constraints': 'Support all market URLs: /, /da, /de, /en, /it, /es, /fr (missing /pt)'
                })
                
            if analyst_name == 'marcus' and score < 70:
                copilot_tasks.append({
                    'priority': 'MEDIUM',
                    'analyst': 'Marcus (Performance)', 
                    'task': 'Optimize /assets/emmso.css and /assets/emmso.js ONLY - consolidate all CSS/JS into these single files',
                    'files_to_modify': ['assets/emmso.css', 'assets/emmso.js'],
                    'business_impact': 'Achieve Core Web Vitals green across all 10 markets',
                    'constraints': 'CRITICAL: ALL CSS must go in emmso.css, ALL JS in emmso.js - NO other files allowed'
                })
                
            if analyst_name == 'jessica' and score < 70:
                copilot_tasks.append({
                    'priority': 'MEDIUM',
                    'analyst': 'Jessica (UX)',
                    'task': 'Improve /sections/ for CTR optimization across 10 markets with CSS/JS constraints',
                    'files_to_modify': ['sections/header.liquid', 'sections/product-form.liquid', 'assets/emmso.css'],
                    'business_impact': 'Achieve CTR uplift ≥10% across all target markets',
                    'constraints': 'ALL styling changes ONLY in emmso.css, ALL interactions ONLY in emmso.js'
                })
                
            if analyst_name == 'nora' and score < 70:
                copilot_tasks.append({
                    'priority': 'LOW',
                    'analyst': 'Nora (Visual)',
                    'task': 'Standardize visual brand elements across 10 markets - update ONLY emmso.css',
                    'files_to_modify': ['assets/emmso.css'],
                    'business_impact': 'Maintain brand consistency across all target markets',
                    'constraints': 'STRICT: ALL visual changes ONLY in emmso.css - no other CSS files permitted'
                })
            
            if analyst_name == 'rachel' and score < 70:
                copilot_tasks.append({
                    'priority': 'MEDIUM',
                    'analyst': 'Rachel (Content)',
                    'task': 'Verify /locales/ files for all 10 markets and add missing Portugal (/pt) translations',
                    'files_to_modify': ['locales/pt.json', 'locales/da.json', 'locales/de.json'],
                    'business_impact': 'Complete market coverage for all target countries',
                    'constraints': 'Ensure Portugal market support is added (/pt URL currently missing)'
                })
        
        # Sort by priority
        priority_order = {'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        copilot_tasks.sort(key=lambda x: priority_order.get(x['priority'], 4))
        
        return copilot_tasks
    
    def report_to_human_with_business_context(self, overall_score: int, critical_issues: List[str], recommendations: List[str], business_health: str, revenue_report: dict = None, deliverables_report: dict = None):
        """Generate business-focused mission report for human command"""
        
        # Business health status with context
        print(f"""
🎯 BUSINESS-DRIVEN MISSION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🎖️  Overall Score: {overall_score}/100
🏥 Business Health: {business_health}

📊 OKR PROGRESS ASSESSMENT:
        """)
        
        # OKR-specific assessment
        if 'error' not in self.business_plan:
            print("   🎯 AI Quality Score ≥ 90/100 target:")
            if overall_score >= 90:
                print("      ✅ ON TRACK - Current score meets target")
            elif overall_score >= 70:
                print("      🟡 NEEDS ATTENTION - Gap to target identified")
            else:
                print("      � CRITICAL GAP - Major improvements needed")
                
            print("   🎯 Brand Health >95% schema validation:")
            schema_issues = [issue for issue in critical_issues if "schema" in issue.lower()]
            if not schema_issues:
                print("      ✅ ON TRACK - No schema validation issues detected")
            else:
                print(f"      🔴 ISSUES FOUND - {len(schema_issues)} schema problems")
        
        # Business impact analysis
        revenue_threats = [issue for issue in critical_issues if "REVENUE" in issue]
        okr_risks = [issue for issue in critical_issues if "OKR" in issue]
        
        if revenue_threats:
            print(f"\n💰 REVENUE THREATS DETECTED ({len(revenue_threats)}):")
            for threat in revenue_threats[:3]:  # Top 3 threats
                print(f"   🚨 {threat}")
        
        if okr_risks:
            print(f"\n�📊 OKR ACHIEVEMENT RISKS ({len(okr_risks)}):")
            for risk in okr_risks[:3]:  # Top 3 risks
                print(f"   ⚠️  {risk}")
        
        # Business-contextualized recommendations
        if recommendations:
            print(f"\n🎯 BUSINESS-DRIVEN ACTION PLAN ({len(recommendations)} items):")
            
            # Group recommendations by business impact
            high_impact = [rec for rec in recommendations if "Revenue Growth" in rec or "AI Quality Score" in rec]
            medium_impact = [rec for rec in recommendations if "Attribution" in rec or "Brand Health" in rec]
            
            if high_impact:
                print("   🔥 HIGH BUSINESS IMPACT:")
                for rec in high_impact[:5]:
                    print(f"      • {rec}")
            
            if medium_impact:
                print("   📈 MEDIUM BUSINESS IMPACT:")
                for rec in medium_impact[:3]:
                    print(f"      • {rec}")
        
        # Strategic recommendations
        print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 CAPTAIN'S STRATEGIC ASSESSMENT:

Business Health: {business_health}
Key Focus: {"REVENUE PROTECTION" if revenue_threats else "GROWTH OPTIMIZATION"}
Next Action: {"IMMEDIATE INTERVENTION" if overall_score < 50 else "TACTICAL IMPROVEMENTS"}

🚢 Recommend: {"EMERGENCY SESSION with development team" if overall_score < 40 else "PROCEED with optimization roadmap"}
        """)
        
        # REVENUE OPPORTUNITY REPORT
        if revenue_report:
            print("\n💰 REVENUE OPPORTUNITY ANALYSIS:")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            total_opp = revenue_report.get('total_opportunity', {})
            annual_potential = total_opp.get('annual_revenue_potential', 0)
            investment_required = total_opp.get('total_investment_required', 0)
            overall_roi = total_opp.get('overall_roi_percentage', 0)
            
            print(f"📈 TOTAL ANNUAL POTENTIAL: €{annual_potential:,}")
            print(f"💸 TOTAL INVESTMENT REQUIRED: €{investment_required:,}")
            print(f"📊 OVERALL ROI: {overall_roi}%")
            print(f"⏱️ PAYBACK PERIOD: {total_opp.get('payback_period_months', 0)} maanden")
            
            # Top opportunities
            top_opportunities = revenue_report.get('prioritized_opportunities', [])[:3]
            if top_opportunities:
                print("\n🎯 TOP 3 REVENUE OPPORTUNITIES:")
                for i, opp in enumerate(top_opportunities, 1):
                    print(f"   {i}. {opp['analyzer'].upper()}: €{opp['annual_impact']:,}/jaar")
                    print(f"      ROI: {opp['roi_percentage']}% | Payback: {opp['payback_months']} maanden")
            
            # Quick wins
            quick_wins = revenue_report.get('market_analysis', {}).get('quick_wins', [])
            if quick_wins:
                print(f"\n⚡ QUICK WINS (≤6 maanden payback): {len(quick_wins)} opportunities")
                for win in quick_wins[:2]:
                    print(f"   • {win['analyzer'].upper()}: €{win['annual_impact']:,}/jaar")
        
        # DIRECTED OUTPUT DOCUMENTS (d.o.d) REPORT
        if deliverables_report:
            print("\n📋 DIRECTED OUTPUT DOCUMENTS ACTION PLAN:")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            total_deliverables = deliverables_report.get('total_deliverables', 0)
            estimated_timeline = deliverables_report.get('estimated_total_timeline', '0 hours')
            
            print(f"📊 Total d.o.d Outputs: {total_deliverables}")
            print(f"⏱️  Estimated Implementation: {estimated_timeline}")
            
            # Immediate actions
            immediate = deliverables_report.get('immediate_actions', [])
            if immediate:
                print(f"\n🚨 IMMEDIATE ACTIONS REQUIRED ({len(immediate)}):")
                for action in immediate:
                    print(f"   • {action}")
            
            # High priority actions
            high_priority = deliverables_report.get('high_priority_actions', [])
            if high_priority:
                print(f"\n🔥 HIGH PRIORITY ACTIONS ({len(high_priority)}):")
                for action in high_priority:
                    print(f"   • {action}")
            
            # File deployment overview
            file_map = deliverables_report.get('file_deployment_map', {})
            if file_map:
                print(f"\n📁 FILE DEPLOYMENT MAP ({len(file_map)} files affected):")
                for file_path, actions in list(file_map.items())[:5]:  # Top 5 files
                    print(f"   📄 {file_path}:")
                    for action_info in actions:
                        print(f"      → {action_info['analyst']}: {action_info['action']} ({action_info['priority']})")
        
        print(f"""
Ready for follow-up orders from human command.
        """)
        
        # Show Copilot-ready tasks if available
        if hasattr(self, 'last_analysis') and self.last_analysis and 'copilot_tasks' in self.last_analysis:
            self._display_copilot_tasks(self.last_analysis['copilot_tasks'])
    
    def _display_copilot_tasks(self, copilot_tasks: List[Dict[str, str]]):
        """Display actionable tasks for Copilot implementation"""
        if not copilot_tasks:
            print("\n🤖 No specific Copilot tasks generated - system performing well!")
            return
            
        print(f"""
🤖 COPILOT ACTION ITEMS ({len(copilot_tasks)} tasks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ready for implementation - prioritized by business impact:
        """)
        
        for i, task in enumerate(copilot_tasks, 1):
            priority_emoji = "🔥" if task['priority'] == 'HIGH' else "📋" if task['priority'] == 'MEDIUM' else "📝"
            
            print(f"""
{i}. {priority_emoji} {task['priority']} PRIORITY
   Analyst: {task['analyst']}
   Task: {task['task']}
   Files: {', '.join(task['files_to_modify'])}
   Impact: {task['business_impact']}
   Constraints: {task.get('constraints', 'None')}
            """)
        
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("🎯 Captain recommends: Start with HIGH priority tasks for maximum business impact")
    
    def report_to_human(self, overall_score: int, critical_issues: List[str], recommendations: List[str]):
        """Generate basic mission report (legacy function)"""
        print(f"""
🎯 MISSION REPORT TO HUMAN COMMAND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🎖️  Overall Mission Score: {overall_score}/100

📊 SITUATION ASSESSMENT:
        """)
        
        if overall_score >= 80:
            print("   🟢 EXCELLENT - EMMSO systems performing optimally")
        elif overall_score >= 60:
            print("   🟡 GOOD - Some areas need tactical improvement") 
        elif overall_score >= 40:
            print("   🟠 CONCERNING - Multiple systems require attention")
        else:
            print("   🔴 CRITICAL - Immediate intervention required")
        
        if critical_issues:
            print(f"\n⚠️  CRITICAL INTELLIGENCE ({len(critical_issues)} issues):")
            for issue in critical_issues[:5]:  # Top 5 most critical
                print(f"   • {issue}")
        
        if recommendations:
            print(f"\n🎯 TACTICAL RECOMMENDATIONS ({len(recommendations)} actions):")
            for rec in recommendations[:10]:  # Top 10 recommendations
                print(f"   • {rec}")
        
        print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚢 Captain recommends: {"MAINTAIN COURSE" if overall_score >= 70 else "IMMEDIATE ACTION REQUIRED"}

Awaiting further orders from human command.
        """)
    
    def get_specific_analyst_report(self, analyst_name: str) -> Dict[str, Any]:
        """Get detailed report from specific analyst"""
        if analyst_name not in self.ai_team:
            return {"error": f"Analyst {analyst_name} not found in team"}
        
        if not self.last_analysis:
            return {"error": "No recent analysis available. Run mission first."}
        
        return self.last_analysis['mission_results'].get(analyst_name, {"error": "No data"})
    
    def issue_direct_order(self, analyst_name: str, specific_task: str) -> str:
        """Issue direct order to specific analyst"""
        if analyst_name not in self.ai_team:
            return f"❌ ERROR: Analyst {analyst_name} not available for orders"
        
        print(f"📢 DIRECT ORDER to {analyst_name.title()}: {specific_task}")
        
        # This would trigger specific analysis
        # For now, acknowledge order
        order_response = f"""
🎯 ORDER ACKNOWLEDGED
━━━━━━━━━━━━━━━━━━━━━
Analyst: {analyst_name.title()}
Task: {specific_task}
Status: RECEIVED - EXECUTING

{analyst_name.title()} will report back with findings.
        """
        
        print(order_response)
        return order_response

def main():
    """Interactive command interface for human-captain communication"""
    print("🚢 EMMSO AI COMMAND CENTER ONLINE")
    print("   Type 'help' for available commands")
    
    captain = EMMSOCaptain()
    
    while True:
        try:
            human_input = input("\n👤 HUMAN COMMAND > ").strip()
            
            if human_input.lower() in ['exit', 'quit', 'bye']:
                print("🚢 Captain signing off. Over and out.")
                break
            elif human_input.lower() == 'help':
                print("""
🎯 AVAILABLE COMMANDS:
━━━━━━━━━━━━━━━━━━━━━
• mission [type] - Start tactical analysis mission
• status - Get current mission status  
• report [analyst] - Get specific analyst report
• order [analyst] [task] - Give direct order to analyst
• team - Show team roster
• history - Show command history
• exit - End session
                """)
            elif human_input.lower().startswith('mission'):
                mission_type = human_input.split(' ', 1)[1] if ' ' in human_input else "FULL_AUDIT"
                captain.receive_human_command(f"Execute {mission_type} mission", "HIGH")
                captain.execute_mission(mission_type)
            elif human_input.lower() == 'status':
                print(f"🎯 Mission Status: {captain.mission_status}")
                if captain.last_analysis:
                    print(f"📊 Last Analysis: {captain.last_analysis['timestamp']}")
                    print(f"🎖️  Overall Score: {captain.last_analysis['overall_score']}/100")
            elif human_input.lower().startswith('report'):
                parts = human_input.split(' ', 1)
                analyst = parts[1] if len(parts) > 1 else None
                if analyst:
                    report = captain.get_specific_analyst_report(analyst)
                    print(f"📊 Report from {analyst.title()}:")
                    print(json.dumps(report, indent=2))
                else:
                    print("❌ Please specify analyst name")
            elif human_input.lower().startswith('order'):
                parts = human_input.split(' ', 2)
                if len(parts) >= 3:
                    analyst, task = parts[1], parts[2]
                    captain.issue_direct_order(analyst, task)
                else:
                    print("❌ Format: order [analyst] [task]")
            elif human_input.lower() == 'team':
                print("🎯 AI TEAM ROSTER:")
                for name, analyst in captain.ai_team.items():
                    print(f"   • {name.title()} - {analyst.__class__.__name__}")
            elif human_input.lower() == 'history':
                print("📋 COMMAND HISTORY:")
                for cmd in captain.human_commands[-5:]:  # Last 5 commands
                    print(f"   {cmd['timestamp']}: {cmd['command']}")
            else:
                captain.receive_human_command(human_input)
                print("🎯 Command logged. Use 'mission' to execute analysis.")
                
        except KeyboardInterrupt:
            print("\n🚢 Captain signing off. Over and out.")
            break
        except Exception as e:
            print(f"❌ Command error: {e}")

if __name__ == "__main__":
    main()
