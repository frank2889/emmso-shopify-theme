"""
Shared Screenshot Analysis Module
==================================
GPT-4 Vision helper for all analysts to analyze screenshots
Each analyst uses this with their own specialized prompt
"""

import os
import base64
from openai import OpenAI
from pathlib import Path
from typing import Dict, List, Optional

class ScreenshotAnalyzer:
    """Shared GPT-4 Vision screenshot analyzer"""
    
    def __init__(self):
        """Initialize OpenAI client"""
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = None
        
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            print("      ⚠️  OPENAI_API_KEY not set - Screenshot analysis unavailable")
    
    def get_screenshots(self, site_data: Dict) -> Dict[str, str]:
        """Get available screenshots from /screenshots folder"""
        screenshots = {}
        
        theme_path = site_data.get('shopify_theme_path', '/Users/Frank/Documents/EMMSO NOV')
        screenshots_dir = os.path.join(theme_path, 'screenshots')
        
        if not os.path.exists(screenshots_dir):
            return screenshots
        
        # Collect all .png files
        for file in os.listdir(screenshots_dir):
            if file.endswith('.png'):
                screenshot_name = file.replace('.png', '')
                screenshots[screenshot_name] = os.path.join(screenshots_dir, file)
        
        return screenshots
    
    def analyze_screenshot(
        self,
        screenshot_path: str,
        screenshot_name: str,
        analysis_prompt: str,
        project_goals: Dict = None
    ) -> Dict:
        """
        Analyze a screenshot with GPT-4 Vision using custom prompt
        
        Args:
            screenshot_path: Path to screenshot file
            screenshot_name: Name of screenshot (e.g., 'homepage-desktop')
            analysis_prompt: Custom prompt for specific analysis perspective
            project_goals: Optional project goals for context
        
        Returns:
            Analysis results with scores, issues, recommendations
        """
        if not self.client:
            return {
                'error': 'OpenAI API not available',
                'score': 0
            }
        
        try:
            # Read and encode image
            with open(screenshot_path, 'rb') as img_file:
                image_data = base64.b64encode(img_file.read()).decode('utf-8')
            
            # Build context from project goals
            goals_context = ""
            if project_goals:
                goals_context = f"""
                
PROJECT GOALS FOR CONTEXT:
- Vision: {project_goals.get('vision', 'N/A')}
- Languages: {project_goals.get('languages', 'N/A')}
- Mobile-First: {project_goals.get('mobile_first', 'N/A')}
- Voice Search: {project_goals.get('voice_search', 'N/A')}
- Design: {project_goals.get('design_principle', 'N/A')}
- Accessibility: {project_goals.get('accessibility', 'N/A')}
"""
            
            # Call GPT-4 Vision
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"{analysis_prompt}{goals_context}\n\nScreenshot: {screenshot_name}"
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{image_data}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1500,
                temperature=0.3
            )
            
            # Parse response
            analysis_text = response.choices[0].message.content
            
            # Extract structured data
            result = self._parse_analysis_response(analysis_text, screenshot_name)
            
            return result
            
        except Exception as e:
            return {
                'error': f'Screenshot analysis failed: {str(e)}',
                'score': 0
            }
    
    def _parse_analysis_response(self, response_text: str, screenshot_name: str) -> Dict:
        """Parse GPT-4 Vision response into structured data"""
        
        result = {
            'screen': screenshot_name,
            'raw_analysis': response_text,
            'scores': {},
            'issues': [],
            'recommendations': [],
            'highlights': []
        }
        
        # Extract scores (looking for "Score: X/100" patterns)
        lines = response_text.split('\n')
        for line in lines:
            if '/100' in line or 'Score:' in line:
                # Try to extract numeric score
                try:
                    if 'OVERALL:' in line:
                        parts = line.split(':')
                        if len(parts) > 1:
                            score_text = parts[1].strip().split('/')[0].strip()
                            result['score'] = int(score_text)
                except:
                    pass
        
        # Extract issues (lines starting with - under **ISSUES FOUND:**)
        in_issues = False
        in_recommendations = False
        in_highlights = False
        
        for line in lines:
            line = line.strip()
            
            if '**ISSUES FOUND:**' in line or 'ISSUES:' in line:
                in_issues = True
                in_recommendations = False
                in_highlights = False
                continue
            elif '**RECOMMENDATIONS:**' in line or 'RECOMMENDATIONS:' in line:
                in_issues = False
                in_recommendations = True
                in_highlights = False
                continue
            elif '**HIGHLIGHTS:**' in line or 'STRENGTHS:' in line:
                in_issues = False
                in_recommendations = False
                in_highlights = True
                continue
            elif line.startswith('**') and line.endswith(':**'):
                # Reset on new section
                in_issues = False
                in_recommendations = False
                in_highlights = False
                continue
            
            if in_issues and line.startswith('-'):
                result['issues'].append(line[1:].strip())
            elif in_recommendations and line.startswith('-'):
                result['recommendations'].append(f"{screenshot_name}: {line[1:].strip()}")
            elif in_highlights and line.startswith('-'):
                result['highlights'].append(line[1:].strip())
        
        # Set default score if not found
        if 'score' not in result:
            result['score'] = 50  # Default middle score
        
        return result
