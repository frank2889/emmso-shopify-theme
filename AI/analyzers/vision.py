"""
Vision AI Analyst - Visual Design & UX Analysis
Uses centralized vision_expert knowledge base
"""
import os
import base64
import json
from datetime import datetime
from openai import OpenAI
from knowledge import vision_expert

class VisionAIAnalyst:
    def __init__(self):
        self.name = "Vision AI"
        self.specialty = "Visual Design & Screenshot Analysis"
        self.knowledge = vision_expert  # Access to centralized UX/UI expertise
        
        # Initialize OpenAI client (optional - graceful degradation)
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("      ⚠️  OPENAI_API_KEY not set - Vision AI will run in limited mode")
            self.client = None
        else:
            try:
                self.client = OpenAI(api_key=api_key)
            except Exception as e:
                print(f"      ⚠️  OpenAI client initialization failed: {e}")
                self.client = None
    
    def analyze(self, site_data):
        """Analyze visual design using screenshots"""
        print(f"    👁️  Vision AI: Analyzing visual design from screenshots...")
        
        # Check if OpenAI client is available
        if not self.client:
            return {
                'analyst': self.name,
                'specialty': self.specialty,
                'timestamp': datetime.now().isoformat(),
                'score': 0,
                'findings': {
                    'info': 'Vision AI requires OPENAI_API_KEY - Add screenshots to /screenshots folder and set API key'
                },
                'recommendations': [
                    'Set OPENAI_API_KEY environment variable to enable Vision AI analysis',
                    'Add screenshots to /screenshots folder (homepage, search, product pages)',
                    'Vision AI will automatically analyze visual design and UX after deployment'
                ]
            }
        
        # Get project goals for context
        project_goals = site_data.get('project_goals', {})
        
        # Screenshots to analyze
        screenshots, deployment_info = self._get_screenshots(site_data)
        
        if not screenshots:
            return {
                'analyst': self.name,
                'specialty': self.specialty,
                'timestamp': datetime.now().isoformat(),
                'score': 0,
                'findings': {
                    'error': 'No screenshots available for analysis'
                },
                'recommendations': []
            }
        
        # Analyze each screenshot
        visual_analysis = {}
        all_recommendations = []
        scores = []
        
        for screenshot_name, screenshot_path in screenshots.items():
            print(f"      📸 Analyzing: {screenshot_name}")
            
            analysis = self._analyze_screenshot(
                screenshot_path,
                screenshot_name,
                project_goals
            )
            
            visual_analysis[screenshot_name] = analysis
            
            if 'score' in analysis:
                scores.append(analysis['score'])
            
            if 'recommendations' in analysis:
                all_recommendations.extend(analysis['recommendations'])
        
        # Calculate overall visual score
        overall_score = int(sum(scores) / len(scores)) if scores else 0
        
        print(f"      Score: {overall_score}/100")
        
        # Cleanup old screenshot folders after analysis
        self._cleanup_old_screenshots(site_data, deployment_info)
        
        # Build findings with deployment info
        findings = {
            'visual_analysis': visual_analysis,
            'screenshots_analyzed': len(screenshots),
            'project_goals_alignment': self._check_visual_goals(visual_analysis, project_goals)
        }
        
        # Add deployment timestamp if available
        if deployment_info:
            findings['deployment'] = deployment_info
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': overall_score,
            'findings': findings,
            'recommendations': all_recommendations
        }
    
    def _get_screenshots(self, site_data):
        """
        Get screenshots from latest deployment folder.
        Uses screenshots/latest/ symlink to automatically use most recent deployment.
        Returns: (screenshots_dict, deployment_info)
        """
        base_path = site_data.get('shopify_theme_path', '/Users/Frank/Documents/EMMSO NOV')
        
        # Try 'latest' symlink first (new deployment-aware structure)
        latest_dir = os.path.join(base_path, 'screenshots', 'latest')
        deployment_info = None
        
        if os.path.exists(latest_dir) and os.path.islink(latest_dir):
            screenshots_dir = latest_dir
            deployment_folder = os.readlink(latest_dir)
            
            # Extract timestamp from folder name: deployment-20251104-181523-1730649600
            if deployment_folder.startswith('deployment-'):
                parts = deployment_folder.split('-')
                if len(parts) >= 4:
                    date_str = parts[1]  # 20251104
                    time_str = parts[2]  # 181523
                    timestamp = parts[3]  # 1730649600
                    
                    # Format: 2025-11-04 18:15:23
                    formatted_datetime = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]} {time_str[:2]}:{time_str[2:4]}:{time_str[4:6]}"
                    deployment_info = {
                        'folder': deployment_folder,
                        'timestamp': timestamp,
                        'datetime': formatted_datetime
                    }
            
            print(f"      📁 Using deployment: {deployment_folder}")
            if deployment_info:
                print(f"      📅 Screenshots captured: {deployment_info['datetime']}")
        else:
            # Fallback to old flat structure
            screenshots_dir = os.path.join(base_path, 'screenshots')
            if os.path.exists(screenshots_dir):
                print(f"      📁 Using screenshots folder (legacy structure)")
        
        screenshots = {}
        
        if os.path.exists(screenshots_dir):
            for filename in os.listdir(screenshots_dir):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    name = os.path.splitext(filename)[0]
                    screenshots[name] = os.path.join(screenshots_dir, filename)
        
        return screenshots, deployment_info
    
    def _cleanup_old_screenshots(self, site_data, current_deployment_info):
        """
        Delete old screenshot folders after analysis.
        Keeps only the current deployment folder.
        """
        import shutil
        
        base_path = site_data.get('shopify_theme_path', '/Users/Frank/Documents/EMMSO NOV')
        screenshots_base = os.path.join(base_path, 'screenshots')
        
        if not current_deployment_info:
            return
        
        current_folder = current_deployment_info.get('folder')
        if not current_folder:
            return
        
        try:
            # List all deployment folders
            if os.path.exists(screenshots_base):
                for item in os.listdir(screenshots_base):
                    item_path = os.path.join(screenshots_base, item)
                    
                    # Skip the 'latest' symlink and current deployment
                    if item == 'latest' or item == current_folder:
                        continue
                    
                    # Delete old deployment folders
                    if os.path.isdir(item_path) and item.startswith('deployment-'):
                        shutil.rmtree(item_path)
                        print(f"      🗑️  Deleted old screenshots: {item}")
        
        except Exception as e:
            print(f"      ⚠️  Screenshot cleanup warning: {e}")
    
    def _analyze_screenshot(self, image_path, screen_name, project_goals):
        """Analyze a single screenshot using OpenAI Vision API"""
        
        try:
            # Read and encode image
            with open(image_path, 'rb') as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
            
            # Determine image format
            ext = os.path.splitext(image_path)[1].lower()
            mime_type = {
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.webp': 'image/webp'
            }.get(ext, 'image/png')
            
            # Build analysis prompt based on project goals
            prompt = self._build_analysis_prompt(screen_name, project_goals)
            
            # Call OpenAI Vision API
            response = self.client.chat.completions.create(
                model="gpt-4o",  # GPT-4 with vision
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{mime_type};base64,{image_data}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1500,
                temperature=0.3  # Lower temperature for more consistent analysis
            )
            
            # Parse response
            analysis_text = response.choices[0].message.content
            
            # Extract structured data from response
            return self._parse_vision_response(analysis_text, screen_name)
            
        except Exception as e:
            print(f"      ❌ Vision analysis failed for {screen_name}: {e}")
            return {
                'error': str(e),
                'score': 0,
                'recommendations': []
            }
    
    def _build_analysis_prompt(self, screen_name, project_goals):
        """Build analysis prompt using expert vision knowledge base"""
        
        # Determine if mobile or desktop analysis
        is_mobile = 'mobile' in screen_name.lower() or 'phone' in screen_name.lower()
        
        # Get expert prompt from knowledge base
        expert_analysis = self.knowledge.get_mobile_analysis_prompt() if is_mobile else self.knowledge.get_analysis_prompt()
        
        # Add project-specific context
        context_prompt = f"""
SCREENSHOT CONTEXT:
- Page/Section: {screen_name}
- Project Vision: {project_goals.get('vision', 'Search-first e-commerce marketplace')}
- Design Principle: {project_goals.get('design_principle', 'Brutalist Simplicity - Function over decoration')}
- Accessibility Target: {project_goals.get('accessibility', 'WCAG 2.1 AA compliance')}

CRITICAL E-COMMERCE CHECKS:
- Shopping cart icon visible in header (with item count badge if applicable)
- Product pricing clearly displayed
- "Add to Cart" or "Buy Now" buttons prominent
- Design immediately communicates "this is a shop"
- Trust signals visible (payment icons, security badges, guarantees)

{expert_analysis}

SCORING RUBRIC (0-100 for each category):
1. E-Commerce Visibility (0-100)
   - Cart icon visible: 40 points
   - Product prices visible: 20 points
   - CTA buttons prominent: 20 points
   - Trust signals present: 10 points
   - Cart count badge visible: 10 points

2. Visual Hierarchy (0-100)
   - Clear focal points: 30 points
   - Proper size/contrast: 30 points
   - Adequate spacing: 20 points
   - Logical flow: 20 points

3. Search-First Design (0-100)
   - Search prominent: 40 points
   - Search accessible: 30 points
   - Autocomplete visible: 20 points
   - Voice search option: 10 points

4. Mobile-First/Responsive (0-100)
   - Touch targets 48px+: 30 points
   - Thumb-zone optimization: 25 points
   - Readable text (16px+): 25 points
   - No horizontal scroll: 20 points

5. Brutalist Simplicity (0-100)
   - Function over form: 40 points
   - Minimal decoration: 30 points
   - Clear purpose: 30 points

6. Accessibility (0-100)
   - Text contrast 4.5:1: 40 points
   - Focus indicators: 30 points
   - Readable typography: 30 points

7. Brand Consistency (0-100)
   - Consistent colors: 35 points
   - Consistent typography: 35 points
   - Brand visibility: 30 points

OUTPUT FORMAT:
**SCORES:**
- E-Commerce Visibility: X/100
- Visual Hierarchy: X/100
- Search-First Design: X/100
- Mobile-First: X/100
- Brutalist Simplicity: X/100
- Accessibility: X/100
- Brand Consistency: X/100
- OVERALL: X/100

**CRITICAL ISSUES:** [List with severity, location, fix]
**RECOMMENDED FIXES:** [Actionable with measurements]
**WHAT WORKS WELL:** [Positive highlights]

Provide MEEDOGENLOOS STRENGE (ruthlessly strict) analysis.
"""
        return context_prompt
    
    def _parse_vision_response(self, response_text, screen_name):
        """Parse Vision API response into structured data for sharing with other analysts"""
        
        analysis = {
            'screen': screen_name,
            'raw_analysis': response_text,
            'scores': {
                'ecommerce_visibility': 0,  # NEW - CRITICAL
                'visual_hierarchy': 0,
                'search_first': 0,
                'mobile_first': 0,
                'brutalist_simplicity': 0,
                'accessibility': 0,
                'brand_consistency': 0
            },
            'ecommerce_check': {
                'cart_icon_visible': False,
                'pricing_visible': False,
                'add_to_cart_buttons': False,
                'shopping_intent_clear': False
            },
            'issues': [],
            'recommendations': [],
            'highlights': []
        }
        
        lines = response_text.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            # Parse E-COMMERCE CHECK section
            if 'cart icon visible?' in line.lower():
                analysis['ecommerce_check']['cart_icon_visible'] = 'yes' in line.lower()
            elif 'pricing visible?' in line.lower():
                analysis['ecommerce_check']['pricing_visible'] = 'yes' in line.lower()
            elif 'add to cart buttons?' in line.lower():
                analysis['ecommerce_check']['add_to_cart_buttons'] = 'yes' in line.lower()
            elif 'shopping intent clear?' in line.lower():
                analysis['ecommerce_check']['shopping_intent_clear'] = 'yes' in line.lower()
            
            # Parse individual scores
            if ':' in line and '/100' in line:
                try:
                    parts = line.split(':')
                    if len(parts) >= 2:
                        label = parts[0].strip('*- ').lower()
                        score_str = parts[1].strip().split('/')[0].strip()
                        score = int(score_str)
                        
                        # Map to score keys
                        if 'e-commerce' in label or 'ecommerce' in label:
                            analysis['scores']['ecommerce_visibility'] = score
                        elif 'visual hierarchy' in label:
                            analysis['scores']['visual_hierarchy'] = score
                        elif 'search' in label and 'first' in label:
                            analysis['scores']['search_first'] = score
                        elif 'mobile' in label:
                            analysis['scores']['mobile_first'] = score
                        elif 'brutalist' in label or 'simplicity' in label:
                            analysis['scores']['brutalist_simplicity'] = score
                        elif 'accessibility' in label:
                            analysis['scores']['accessibility'] = score
                        elif 'brand' in label:
                            analysis['scores']['brand_consistency'] = score
                        elif 'overall' in label:
                            analysis['score'] = score
                except:
                    pass
            
            # Detect sections
            if '**ISSUES' in line.upper():
                current_section = 'issues'
            elif '**RECOMMENDATIONS' in line.upper():
                current_section = 'recommendations'
            elif '**HIGHLIGHTS' in line.upper():
                current_section = 'highlights'
            
            # Parse bullet points
            if line.startswith('-') or line.startswith('*'):
                item = line[1:].strip()
                if current_section == 'issues':
                    analysis['issues'].append(item)
                elif current_section == 'recommendations':
                    analysis['recommendations'].append(f"{screen_name}: {item}")
                elif current_section == 'highlights':
                    analysis['highlights'].append(item)
        
        # Calculate overall score from sub-scores if not found
        if 'score' not in analysis:
            subscores = [s for s in analysis['scores'].values() if s > 0]
            analysis['score'] = int(sum(subscores) / len(subscores)) if subscores else 50
        
        # Flag critical issue if cart not visible
        if not analysis['ecommerce_check']['cart_icon_visible']:
            critical_rec = f"{screen_name}: 🚨 CRITICAL - Shopping cart icon not visible! Increase size to 28-32px, add prominent positioning, ensure users immediately recognize this as e-commerce."
            if critical_rec not in analysis['recommendations']:
                analysis['recommendations'].insert(0, critical_rec)
        
        return analysis
    
    def _check_visual_goals(self, visual_analysis, project_goals):
        """Check how well visual design aligns with project goals"""
        
        alignment = {
            'search_first_visual': False,
            'mobile_optimized': False,
            'brutalist_design': False,
            'accessible': False,
            'issues_found': []
        }
        
        # Analyze all screenshots for goal alignment
        for screen_name, analysis in visual_analysis.items():
            if 'error' in analysis:
                continue
            
            # Check for search prominence
            highlights = ' '.join(analysis.get('highlights', [])).lower()
            issues = ' '.join(analysis.get('issues', [])).lower()
            
            if 'search' in highlights and 'prominent' in highlights:
                alignment['search_first_visual'] = True
            
            if 'mobile' in highlights or 'responsive' in highlights:
                alignment['mobile_optimized'] = True
            
            if 'clean' in highlights or 'minimal' in highlights or 'simple' in highlights:
                alignment['brutalist_design'] = True
            
            if 'contrast' in highlights and 'accessible' in highlights:
                alignment['accessible'] = True
            
            # Collect visual issues
            if 'search not visible' in issues or 'search hidden' in issues:
                alignment['issues_found'].append(f"{screen_name}: Search not prominent")
            
            if 'small text' in issues or 'contrast' in issues:
                alignment['issues_found'].append(f"{screen_name}: Accessibility issues")
        
        return alignment

