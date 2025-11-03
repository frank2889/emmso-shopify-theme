"""
AI Helper Class voor EMMSO Analyzers
===================================
Ondersteunende class die OpenAI integratie biedt aan alle analyzers.
Dit is GEEN captain - gewoon een tool voor slimme analysis.

Captain.py is de echte leider die opdrachten geeft!
"""
import os
import json
import requests
from datetime import datetime
from openai import OpenAI

class SmartAnalyzer:
    """Base class met OpenAI integration voor slimme analysis"""
    
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.openai_client = self._init_openai()
        
    def _init_openai(self):
        """Initialize OpenAI client als beschikbaar"""
        try:
            # Check voor OpenAI API key in environment
            api_key = os.getenv('OPENAI_API_KEY')
            if api_key and api_key.strip():
                return OpenAI(api_key=api_key)
            else:
                print(f"    {self.name}: No OpenAI API key found - using basic analysis")
                return None
        except Exception as e:
            print(f"    {self.name}: OpenAI initialization failed: {e}")
            return None
    
    def smart_analyze_content(self, content, analysis_prompt):
        """Use OpenAI to analyze content smartly"""
        if not self.openai_client:
            return {"error": "OpenAI not available", "fallback": True}
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": f"You are {self.name}, an expert {self.specialty} analyst for EMMSO. Analyze the provided content and return actionable insights in JSON format."},
                    {"role": "user", "content": f"{analysis_prompt}\n\nContent to analyze:\n{content}"}
                ],
                max_tokens=1000,
                temperature=0.3
            )
            
            result = response.choices[0].message.content
            
            # Try to parse as JSON, fallback to text
            try:
                return json.loads(result)
            except:
                return {"analysis": result, "ai_powered": True}
                
        except Exception as e:
            print(f"    {self.name}: OpenAI analysis failed: {e}")
            return {"error": str(e), "fallback": True}
    
    def analyze_website_live(self, url=None, use_preview=True):
        """Analyze live website with smart insights - supports Shopify preview"""
        
        # Determine which URL to use
        if url is None:
            if use_preview:
                # Use Shopify preview URL by default
                url = "https://vloerproducten.myshopify.com/?preview_theme_id=main"
            else:
                url = "https://emmso.com"
        
        try:
            # Get basic website data
            response = requests.get(url, timeout=15, headers={
                'User-Agent': 'EMMSO-AI-Analyzer/1.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            })
            
            if response.status_code != 200:
                return {"error": f"Website returned {response.status_code}", "url": url}
            
            # Extract key information
            content = response.text
            page_size = len(content)
            
            basic_data = {
                "url": url,
                "is_preview": use_preview,
                "status_code": response.status_code,
                "page_size": page_size,
                "page_size_kb": round(page_size / 1024, 2),
                "response_time": response.elapsed.total_seconds(),
                "content_type": response.headers.get('content-type', 'unknown'),
                "shopify_theme": "preview" if use_preview else "live"
            }
            
            # If OpenAI available, get smart analysis
            if self.openai_client:
                smart_analysis = self.smart_analyze_content(
                    content[:3000],  # First 3000 chars
                    f"Analyze this {self.specialty} aspects of the EMMSO Shopify theme. Focus on {self.specialty}-specific issues and opportunities. This is {'preview theme data' if use_preview else 'live website data'}."
                )
                basic_data.update(smart_analysis)
            
            return basic_data
            
        except Exception as e:
            return {"error": f"Website analysis failed: {e}", "url": url}
    
    def get_file_content(self, file_path):
        """Safely read file content for analysis"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading {file_path}: {e}"
    
    def count_files_in_directory(self, directory_path):
        """Count files in directory safely"""
        try:
            if os.path.exists(directory_path):
                return len([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])
            return 0
        except:
            return 0
    
    def analyze_shopify_theme_files(self, theme_base_path="/Users/Frank/Documents/EMMSO", focus_areas=None):
        """Analyze Shopify theme files based on analyst specialty"""
        if focus_areas is None:
            focus_areas = ['assets', 'sections', 'snippets', 'templates', 'locales']
        
        analysis = {
            'theme_path': theme_base_path,
            'analyst_focus': self.specialty,
            'file_analysis': {}
        }
        
        for area in focus_areas:
            area_path = os.path.join(theme_base_path, area)
            if os.path.exists(area_path):
                try:
                    files = [f for f in os.listdir(area_path) if os.path.isfile(os.path.join(area_path, f))]
                    analysis['file_analysis'][area] = {
                        'file_count': len(files),
                        'files': files[:10],  # First 10 files
                        'relevant_files': self._filter_relevant_files(files, area)
                    }
                    
                    # Add specific analysis based on specialty
                    if self.specialty == 'Performance' and area == 'assets':
                        analysis['file_analysis'][area]['performance_concerns'] = self._check_asset_performance(area_path, files)
                    elif self.specialty == 'SEO' and area == 'templates':
                        analysis['file_analysis'][area]['seo_templates'] = self._check_seo_templates(area_path, files)
                        
                except Exception as e:
                    analysis['file_analysis'][area] = {'error': str(e)}
            else:
                analysis['file_analysis'][area] = {'status': 'directory_not_found'}
        
        return analysis
    
    def _filter_relevant_files(self, files, area):
        """Filter files relevant to analyst's specialty"""
        relevant = []
        
        if self.specialty == 'Performance':
            relevant = [f for f in files if f.endswith(('.css', '.js', '.png', '.jpg', '.webp', '.svg'))]
        elif self.specialty == 'SEO':
            relevant = [f for f in files if f.endswith(('.liquid', '.json'))]
        elif self.specialty == 'UX':
            relevant = [f for f in files if 'section' in f or 'template' in f or f.endswith('.liquid')]
        elif self.specialty == 'Visual':
            relevant = [f for f in files if f.endswith(('.css', '.png', '.jpg', '.webp', '.svg'))]
        elif self.specialty == 'Shopify':
            relevant = files  # Alex needs access to everything
        else:
            relevant = [f for f in files if f.endswith('.liquid')]  # Default to Liquid files
            
        return relevant[:5]  # Return top 5 relevant files
    
    def _check_asset_performance(self, area_path, files):
        """Check asset files for performance issues"""
        concerns = []
        for file in files:
            file_path = os.path.join(area_path, file)
            try:
                file_size = os.path.getsize(file_path)
                if file.endswith('.css') and file_size > 100000:  # >100KB CSS
                    concerns.append(f"{file}: Large CSS file ({file_size} bytes)")
                elif file.endswith('.js') and file_size > 200000:  # >200KB JS
                    concerns.append(f"{file}: Large JS file ({file_size} bytes)")
            except:
                pass
        return concerns
    
    def _check_seo_templates(self, area_path, files):
        """Check template files for SEO elements"""
        seo_files = []
        for file in files:
            if file.endswith('.liquid'):
                seo_files.append(file)
        return seo_files