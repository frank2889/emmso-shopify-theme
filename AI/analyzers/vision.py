"""
Vision AI Analyst - Visual Design & UX Analysis
================================================
Analyzes screenshots and visual appearance of the live theme
Uses OpenAI Vision API to evaluate design, layout, and user experience
"""
import os
import base64
import json
from datetime import datetime
from openai import OpenAI

class VisionAIAnalyst:
    def __init__(self):
        self.name = "Vision AI"
        self.specialty = "Visual Design & Screenshot Analysis"
        
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
        screenshots = self._get_screenshots(site_data)
        
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
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': overall_score,
            'findings': {
                'visual_analysis': visual_analysis,
                'screenshots_analyzed': len(screenshots),
                'project_goals_alignment': self._check_visual_goals(visual_analysis, project_goals)
            },
            'recommendations': all_recommendations
        }
    
    def _get_screenshots(self, site_data):
        """
        Get screenshots from latest deployment folder.
        Uses screenshots/latest/ symlink to automatically use most recent deployment.
        """
        base_path = site_data.get('shopify_theme_path', '/Users/Frank/Documents/EMMSO NOV')
        
        # Try 'latest' symlink first (new deployment-aware structure)
        latest_dir = os.path.join(base_path, 'screenshots', 'latest')
        
        if os.path.exists(latest_dir) and os.path.islink(latest_dir):
            screenshots_dir = latest_dir
            print(f"      📁 Using deployment folder: {os.readlink(latest_dir)}")
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
        
        return screenshots
    
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
        """Build analysis prompt based on screen type and project goals"""
        
        base_prompt = f"""Analyze this screenshot of the {screen_name} page/section of an e-commerce website.

PROJECT GOALS:
- Vision: {project_goals.get('vision', 'Search-first e-commerce marketplace')}
- Design: {project_goals.get('design_principle', 'Brutalist Simplicity - Function over decoration')}
- Mobile: {project_goals.get('mobile_first', 'Thumb-optimized, 44px touch targets')}
- Accessibility: {project_goals.get('accessibility', 'WCAG 2.1 AA compliance')}

CRITICAL: This is an **E-COMMERCE PLATFORM** (online shopping). Look for shopping cart indicators!

EVALUATE THE FOLLOWING (Score 0-100 for each):

1. **E-Commerce Visibility** (0-100) **[NEW - CRITICAL]**
   - Is there a visible shopping cart icon/button in the header?
   - Can you see product pricing clearly displayed?
   - Are there "Add to Cart" or "Buy Now" buttons visible?
   - Does the design communicate "this is a shop" immediately?
   - Is the cart count badge visible (if items in cart)?
   - **Score 0 if no cart icon visible, even if other e-commerce elements present**

2. **Visual Hierarchy** (0-100)
   - Is the most important content immediately visible?
   - Clear focal points and visual flow?
   - Proper use of size, contrast, and spacing?

3. **Search-First Design** (0-100)
   - Is search prominent and easy to find?
   - Does it feel like a search-focused experience?
   - Voice search visible/accessible?

4. **Mobile-First/Responsive** (0-100)
   - Touch-friendly targets (44px minimum)?
   - Thumb-reachable navigation?
   - Readable text sizes (16px+ for body)?

5. **Brutalist Simplicity** (0-100)
   - Function over decoration?
   - Clean, minimal design?
   - No unnecessary visual clutter?

6. **Accessibility** (0-100)
   - Sufficient color contrast (4.5:1 for text)?
   - Clear visual states (hover, focus)?
   - Readable typography?

7. **Brand Consistency** (0-100)
   - Consistent colors and typography?
   - Professional appearance?
   - EMMSO brand visible/clear?

PROVIDE YOUR ANALYSIS IN THIS FORMAT:

**SCORES:**
- E-Commerce Visibility: X/100 (CRITICAL - Must see cart icon!)
- Visual Hierarchy: X/100
- Search-First Design: X/100
- Mobile-First: X/100
- Brutalist Simplicity: X/100
- Accessibility: X/100
- Brand Consistency: X/100
- OVERALL: X/100

**E-COMMERCE CHECK:**
- Cart icon visible? YES/NO (describe location and size)
- Pricing visible? YES/NO
- Add to Cart buttons? YES/NO
- Shopping intent clear? YES/NO

**ISSUES FOUND:**
- [List specific visual problems you see]
- [Flag if cart icon is missing or too small to notice]

**RECOMMENDATIONS:**
- [Specific actionable improvements]
- [If cart not visible: "Make shopping cart icon more prominent (increase size, add animation, ensure visibility)"]

**HIGHLIGHTS:**
- [What works well visually]

Be critical and specific. Focus on what you can actually SEE in the screenshot. 
If you cannot see a shopping cart icon in the header, FLAG THIS IMMEDIATELY as critical issue."""

        return base_prompt
    
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

