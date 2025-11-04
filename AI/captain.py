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
    EMMSORevenueCalculator = None

class EMMSOCaptain:
    """
    EMMSO AI Captain - Simplified Version
    =====================================
    
    Captain stuurt het AI team en slaat alle bevindingen op in:
    - DEFINITION-OF-DONE.md: Taken (ACTION PLAN), checkboxes, summaries ONLY
    - DESIGN-SYSTEM.md: Design wijzigingen en aanbevelingen
    
    ⚠️ DOD DOCUMENTATION POLICY:
    - DO: Add tasks with clear descriptions
    - DO: Reference file names and commit hashes
    - DO: Mark tasks complete with brief summary
    - DON'T: Include full code blocks
    - DON'T: Add detailed JSON analyzer outputs
    - DON'T: Create duplicate ACTION PLAN sections
    
    Rule: If it's longer than 10 lines, it doesn't belong in DOD.
    """
    
    def __init__(self):
        print("🚢 EMMSO AI Captain reporting for duty!")
        print("   Simplified version - tracking in DoD only (single source of truth)")
        
        self.ai_team = {}
        
        # Path to documentation file (single source of truth)
        self.theme_root = '/Users/Frank/Documents/EMMSO NOV'
        self.definition_of_done_path = os.path.join(self.theme_root, 'DEFINITION-OF-DONE.md')
        
        # Load the goals and vision from DoD
        self.project_goals = self._load_project_goals()
        
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
        
        print(f"\n   📋 Documentation tracking:")
        print(f"      ✅ DEFINITION-OF-DONE.md (single source of truth)")
        
        if self.project_goals:
            print(f"\n   🎯 Project Goals Loaded:")
            print(f"      • Vision: {self.project_goals.get('vision', 'N/A')[:80]}...")
            print(f"      • Target Conversion: {self.project_goals.get('target_conversion', 'N/A')}")
            print(f"      • Languages: {self.project_goals.get('languages', 'N/A')}")
    
    def _load_project_goals(self):
        """Load project goals from DEFINITION-OF-DONE.md and DESIGN-SYSTEM.md"""
        goals = {}
        
        try:
            # Read DEFINITION-OF-DONE.md for business goals
            with open(self.definition_of_done_path, 'r', encoding='utf-8') as f:
                dod_content = f.read()
            
            # Extract key goals
            if 'search-first e-commerce theme' in dod_content.lower():
                goals['vision'] = 'Search-first e-commerce theme'
            
            if '3.5% → 6%' in dod_content:
                goals['target_conversion'] = '6% (from 3.5%)'
            
            if '20 languages' in dod_content.lower():
                goals['languages'] = '20 languages, 14 countries'
            
            if 'Voice-First' in dod_content:
                goals['voice_search'] = 'Web Speech API integration required'
            
            if 'Mobile-Obsessed' in dod_content:
                goals['mobile_first'] = 'Thumb-optimized, 44px touch targets'
            
            if 'Lighthouse Score' in dod_content:
                goals['lighthouse_target'] = '95+ (Performance/Accessibility/SEO)'
            
            # Design principles from DoD
            if 'Brutalist Simplicity' in dod_content:
                goals['design_principle'] = 'Brutalist Simplicity - Function over decoration'
            
            if 'WCAG 2.1 AA' in dod_content:
                goals['accessibility'] = 'WCAG 2.1 AA compliance required'
            
            print(f"   📖 Loaded {len(goals)} project goals from DEFINITION-OF-DONE.md")
            return goals
            
        except Exception as e:
            print(f"   ⚠️  Could not load project goals: {e}")
            return {}
    
    def _save_to_definition_of_done(self, content: str, section: str = "AI Analysis"):
        """
        APPEND to DEFINITION-OF-DONE.md (single source of truth)
        
        Following DOD Documentation Policy:
        - Appends at end (chronological history)
        - NO code blocks, NO JSON dumps
        - Only summaries and ACTION PLAN tasks
        
        Note: Duplicates are OK - they show history of Captain runs
        User manually cleans old ACTION PLANs when tasks are done
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(self.definition_of_done_path, 'a', encoding='utf-8') as f:
                f.write(f"\n\n---\n\n## {section} - {timestamp}\n\n{content}\n")
            
            print(f"   ✅ Saved to DEFINITION-OF-DONE.md ({section})")
            print(f"   📋 Single source of truth - all documentation in DoD")
            return True
        except Exception as e:
            print(f"   ❌ Error saving to DoD: {e}")
            return False
    
    def _convert_to_phase_tasks(self, mission_results: Dict, overall_score: int) -> str:
        """Convert analyst recommendations to concrete Phase tasks"""
        
        # Categorize by priority based on scores and violations
        critical_tasks = []  # Score < 30 or critical violations
        high_tasks = []      # Score < 60
        medium_tasks = []    # Score < 80
        low_tasks = []       # Score >= 80
        
        for analyst_name, result in mission_results.items():
            if 'error' in result:
                continue
                
            score = result.get('score', 0)
            recommendations = result.get('recommendations', [])
            findings = result.get('findings', {})
            
            # Check for critical issues
            critical_issues = []
            if 'critical_issues' in findings:
                critical_issues = findings['critical_issues']
            if 'project_goals_check' in findings:
                goal_violations = findings['project_goals_check'].get('violations', [])
                critical_issues.extend([v for v in goal_violations if 'CRITICAL' in v or 'BLOCKER' in v])
            
            # Categorize each recommendation
            for rec in recommendations:
                task = {
                    'analyst': analyst_name.title(),
                    'description': rec,
                    'score': score
                }
                
                # Determine priority
                if 'CRITICAL' in rec or 'BLOCKER' in rec or score < 30:
                    critical_tasks.append(task)
                elif 'GOAL' in rec or 'HIGH' in rec or score < 60:
                    high_tasks.append(task)
                elif score < 80:
                    medium_tasks.append(task)
                else:
                    low_tasks.append(task)
        
        # Build Phase structure
        phase_content = ""
        
        if critical_tasks:
            phase_content += "### 🚨 Phase 1: CRITICAL - Immediate Action Required\n\n"
            phase_content += "**Priority**: BLOCKER - Must fix before launch\n"
            phase_content += "**Timeline**: This week\n\n"
            for i, task in enumerate(critical_tasks, 1):
                phase_content += f"- [ ] **{task['analyst']}** (Score: {task['score']}/100): {task['description']}\n"
            phase_content += "\n"
        
        if high_tasks:
            phase_content += "### 🔥 Phase 2: HIGH PRIORITY - Core Functionality\n\n"
            phase_content += "**Priority**: HIGH - Essential for project goals\n"
            phase_content += "**Timeline**: Next 2 weeks\n\n"
            for i, task in enumerate(high_tasks, 1):
                phase_content += f"- [ ] **{task['analyst']}** (Score: {task['score']}/100): {task['description']}\n"
            phase_content += "\n"
        
        if medium_tasks:
            phase_content += "### ⚡ Phase 3: MEDIUM - Optimization & Polish\n\n"
            phase_content += "**Priority**: MEDIUM - Improve user experience\n"
            phase_content += "**Timeline**: Next sprint\n\n"
            for i, task in enumerate(medium_tasks, 1):
                phase_content += f"- [ ] **{task['analyst']}** (Score: {task['score']}/100): {task['description']}\n"
            phase_content += "\n"
        
        if low_tasks:
            phase_content += "### 💡 Phase 4: LOW - Future Enhancements\n\n"
            phase_content += "**Priority**: LOW - Nice to have\n"
            phase_content += "**Timeline**: Future iteration\n\n"
            for i, task in enumerate(low_tasks, 1):
                phase_content += f"- [ ] **{task['analyst']}** (Score: {task['score']}/100): {task['description']}\n"
            phase_content += "\n"
        
        # Add summary
        total_tasks = len(critical_tasks) + len(high_tasks) + len(medium_tasks) + len(low_tasks)
        phase_content += f"""
### 📊 Summary

- 🚨 Critical: {len(critical_tasks)} tasks
- 🔥 High: {len(high_tasks)} tasks  
- ⚡ Medium: {len(medium_tasks)} tasks
- 💡 Low: {len(low_tasks)} tasks
- **Total**: {total_tasks} tasks

**Next Action**: Start with Phase 1 critical tasks
"""
        
        return phase_content
    
    def _analyze_theme_structure(self) -> dict:
        """Analyze local Shopify theme file structure for team analysis"""
        theme_base = '/Users/Frank/Documents/EMMSO NOV'
        
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
        print("   📋 Recruiting website builders & optimizers...")
        
        # Core team for building and improving the website
        analysts = [
            ('sarah', 'SarahSEOAnalyst', 'SEO & Technical Audit'),
            ('alex', 'AlexShopifyAnalyst', 'Shopify Platform & E-commerce'),
            ('marcus', 'MarcusPerformanceAnalyst', 'Site Performance & Speed'),
            ('nora', 'NoraVisualAnalyst', 'Visual Design & Branding'),
            ('vision', 'VisionAIAnalyst', '👁️  Visual Screenshot Analysis (GPT-4 Vision)'),
            # ('rachel', 'RachelContentAnalyst', 'Content Strategy & Structured Data'),  # Disabled - hangs on OpenAI
        ]
        
        # Disabled - Not needed for website building:
        # ('rachel', 'RachelContentAnalyst') - Hangs on OpenAI calls
        # ('mike', 'MikeConversionAnalyst') - CRO komt later
        # ('dave', 'DaveAdsAnalyst') - Ads optimization komt later
        # ('sophie', 'SophieSocialAnalyst') - Social media komt later
        # ('emma', 'EmmaEmailAnalyst') - Email marketing komt later
        # ('jessica', 'JessicaUXAnalyst') - Google Analytics dependency
        # ('eva', 'EvaAnalyticsAnalyst') - Google Analytics dependency
        
        team_ready = 0
        for name, class_name, specialty in analysts:
            try:
                module = __import__(f'analyzers.{name}', fromlist=[class_name])
                analyst_class = getattr(module, class_name)
                self.ai_team[name] = analyst_class()
                print(f"     ✅ {name.title()} ({specialty}) - READY")
                team_ready += 1
            except Exception as e:
                print(f"     ❌ {name.title()} ({specialty}) - UNAVAILABLE: {e}")
        
        print(f"   🎯 Team Status: {team_ready}/{len(analysts)} analysts operational")
    
    def execute_mission(self, mission_type: str = "FULL_AUDIT") -> Dict[str, Any]:
        """Execute mission and save results to DoD and Design System"""
        print(f"🚀 MISSION START: {mission_type}")
        print("   Deploying AI team for analysis...")
        
        self.mission_status = "ACTIVE"
        
        # Create site data
        site_data = {
            'domain': 'emmso.com',
            'shopify_preview_url': 'https://vloerproducten.myshopify.com/?preview_theme_id=main',
            'shopify_theme_path': '/Users/Frank/Documents/EMMSO NOV',
            'theme_structure': self._analyze_theme_structure(),
            'timestamp': datetime.now().isoformat(),
            'mission_type': mission_type,
            'project_goals': self.project_goals  # Pass goals to analysts!
        }
        
        # Deploy team
        mission_results = {}
        all_recommendations = []
        all_findings = []
        design_recommendations = []
        
        print("   🔍 Analysis in progress...")
        
        # STEP 0: Capture fresh screenshots BEFORE Vision AI analysis
        print(f"      📸 Capturing fresh screenshots...")
        try:
            from tools.screenshot_capture import capture_screenshots
            capture_screenshots()
            print(f"         ✅ Screenshots captured successfully")
        except Exception as e:
            print(f"         ⚠️  Screenshot capture skipped: {e}")
            print(f"         💡 Install Playwright: pip install playwright && playwright install chromium")
        
        # STEP 1: Vision AI analyzes screenshots (now with fresh captures)
        screenshot_data = None
        if 'vision' in self.ai_team:
            try:
                print(f"      👁️  Vision AI: Creating & analyzing screenshots...")
                vision_result = self.ai_team['vision'].analyze(site_data)
                mission_results['vision'] = vision_result
                
                # Extract screenshot analysis for sharing
                if 'findings' in vision_result and 'visual_analysis' in vision_result['findings']:
                    screenshot_data = vision_result['findings']['visual_analysis']
                    print(f"         ✅ {len(screenshot_data)} screenshots analyzed and ready to share")
                
                score = vision_result.get('score', 0)
                print(f"         Score: {score}/100")
                
                # Collect Vision's recommendations
                if 'recommendations' in vision_result:
                    for rec in vision_result['recommendations']:
                        all_recommendations.append(f"**Vision**: {rec}")
                
                # Collect Vision's findings
                all_findings.append(f"### Vision ({score}/100)\n\n" + json.dumps(vision_result['findings'], indent=2))
                
            except Exception as e:
                print(f"         ❌ Vision analysis failed: {e}")
                mission_results['vision'] = {'error': str(e), 'score': 0}
        
        # Add screenshot data to site_data for other analysts
        if screenshot_data:
            site_data['vision_screenshot_analysis'] = screenshot_data
            print(f"      📸 Screenshot data added to site_data for other analysts")
        
        # STEP 2: Other analysts analyze code + use Vision's screenshot insights
        for name, analyst in self.ai_team.items():
            if name == 'vision':  # Already analyzed
                continue
                
            try:
                print(f"      👤 {name.title()}: Analyzing...")
                
                result = analyst.analyze(site_data)
                mission_results[name] = result
                
                score = result.get('score', 0)
                print(f"         Score: {score}/100")
                
                # Collect recommendations
                if 'recommendations' in result:
                    for rec in result['recommendations']:
                        all_recommendations.append(f"**{name.title()}**: {rec}")
                
                # Collect findings
                if 'findings' in result:
                    all_findings.append(f"### {name.title()} ({score}/100)\n\n" + json.dumps(result['findings'], indent=2))
                
                # Collect design recommendations
                if name in ['jessica', 'nora', 'marcus']:
                    if 'recommendations' in result:
                        for rec in result['recommendations']:
                            design_recommendations.append(f"**{name.title()}**: {rec}")
                    
            except Exception as e:
                print(f"         ❌ Analysis failed: {e}")
                mission_results[name] = {'error': str(e), 'score': 0}
        
        # Calculate overall score
        scores = [r.get('score', 0) for r in mission_results.values() if 'error' not in r]
        overall_score = int(sum(scores) / len(scores)) if scores else 0
        
        self.mission_status = "COMPLETE"
        
        # Convert recommendations to concrete Phase tasks
        phase_tasks = self._convert_to_phase_tasks(mission_results, overall_score)
        
        # Save to DEFINITION-OF-DONE.md (SUMMARY ONLY - NO CODE)
        # Following DOD Documentation Policy:
        # - Task lists with checkboxes ✅
        # - References to files/commits ✅
        # - High-level summaries ✅
        # - NO full code blocks ❌
        # - NO detailed implementation ❌
        # - NO large JSON dumps ❌
        
        dod_content = f"""
### Mission: {mission_type}
**Overall Score**: {overall_score}/100

#### Action Items

{chr(10).join(all_recommendations)}

#### Status
- ✅ Analysis complete
- 📋 {len(all_recommendations)} recommendations generated
- 🎯 Next: Implement high-priority items

---

## 🎯 ACTION PLAN - {datetime.now().strftime('%Y-%m-%d')}

{phase_tasks}
"""
        self._save_to_definition_of_done(dod_content, f"AI Analysis - {mission_type}")
        
        # Save design recommendations to DEFINITION-OF-DONE.md (single source of truth)
        if design_recommendations:
            design_content = f"""
### Design Analysis Results
**Score**: {overall_score}/100

#### Design Recommendations

{chr(10).join(design_recommendations)}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement
"""
            self._save_to_definition_of_done(design_content, f"AI Design Analysis - {mission_type}")
        
        self.last_analysis = {
            'timestamp': datetime.now().isoformat(),
            'overall_score': overall_score,
            'mission_results': mission_results
        }
        
        # Report to human
        print(f"""
🎯 MISSION COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🎖️  Overall Score: {overall_score}/100
📋 Recommendations: {len(all_recommendations)}
📄 Saved to DEFINITION-OF-DONE.md
🎨 Design items saved to DESIGN-SYSTEM.md

Ready for next orders.
        """)
        
        return self.last_analysis

def main():
    """Simple command interface"""
    print("🚢 EMMSO AI COMMAND CENTER ONLINE")
    
    captain = EMMSOCaptain()
    
    # Auto-run full audit
    print("\n🚀 Running full audit...")
    captain.execute_mission("FULL_AUDIT")
    
    print("\n✅ Mission complete. Check DEFINITION-OF-DONE.md and DESIGN-SYSTEM.md for results.")

if __name__ == "__main__":
    main()
