"""
Mike - SMART Conversion Specialist for EMMSO AI System
======================================================
AI-Powered Conversion Rate Optimization Expert
"""
import requests
from datetime import datetime
from .ai_helper import SmartAnalyzer

class MikeConversionAnalyst(SmartAnalyzer):
    def __init__(self):
        super().__init__("Mike", "Conversion Optimization")
    
    def analyze(self, site_data):
        print(f"    Mike: SMART Conversion analyse met AI insights...")
        
        # Analyze live website for conversion opportunities
        website_analysis = self.analyze_website_live()
        
        # Smart conversion analysis
        conversion_insights = self._analyze_conversion_elements()
        
        # Calculate smart score
        score = self._calculate_conversion_score(website_analysis, conversion_insights)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'findings': {
                'website_analysis': website_analysis,
                'conversion_insights': conversion_insights,
                'smart_recommendations': self._get_smart_recommendations(website_analysis)
            },
            'recommendations': self._generate_conversion_recommendations(score, conversion_insights)
        }
    
    def _analyze_conversion_elements(self):
        """Analyze conversion elements on EMMSO"""
        if not self.openai_client:
            return {
                "add_to_cart_buttons": "Present",
                "checkout_flow": "Standard Shopify",
                "product_pages": "Basic setup",
                "cart_functionality": "Working"
            }
        
        # AI-powered conversion analysis
        conversion_prompt = """
        Analyze the conversion optimization aspects of this EMMSO diving equipment website.
        Focus on:
        1. Call-to-action button effectiveness
        2. Product presentation for conversion
        3. Trust signals and social proof
        4. Multi-brand user experience (Nauticam, Scubapro, Aqualung)
        5. Mobile conversion optimization
        
        Return analysis in JSON format with specific actionable insights.
        """
        
        return self.smart_analyze_content("EMMSO diving equipment e-commerce site analysis", conversion_prompt)
    
    def _calculate_conversion_score(self, website_analysis, conversion_insights):
        """Calculate conversion score based on analysis"""
        score = 50  # Base score
        
        # Website performance impact
        if website_analysis.get('response_time', 5) < 2:
            score += 15
        elif website_analysis.get('response_time', 5) < 4:
            score += 10
        
        # Page size optimization
        page_size_kb = website_analysis.get('page_size_kb', 1000)
        if page_size_kb < 500:
            score += 10
        elif page_size_kb < 1000:
            score += 5
        
        # AI insights bonus
        if conversion_insights.get('ai_powered'):
            score += 15
        
        # Error penalties
        if website_analysis.get('error'):
            score -= 20
        
        return min(max(score, 0), 100)
    
    def _get_smart_recommendations(self, website_analysis):
        """Get AI-powered recommendations"""
        if not self.openai_client or website_analysis.get('error'):
            return ["Basic conversion optimization needed"]
        
        rec_prompt = f"""
        Based on this website analysis data, provide 3 specific conversion optimization recommendations for EMMSO:
        
        Response time: {website_analysis.get('response_time', 'unknown')}s
        Page size: {website_analysis.get('page_size_kb', 'unknown')}KB
        Status: {website_analysis.get('status_code', 'unknown')}
        
        Focus on multi-brand diving equipment e-commerce conversion optimization.
        Return as JSON array of recommendation objects with title, description, priority.
        """
        
        smart_recs = self.smart_analyze_content("Website performance data", rec_prompt)
        
        if isinstance(smart_recs, dict) and 'analysis' in smart_recs:
            return [smart_recs['analysis']]
        elif isinstance(smart_recs, list):
            return smart_recs
        else:
            return ["AI-powered conversion optimization recommendations generated"]
    
    def _generate_conversion_recommendations(self, score, conversion_insights):
        """Generate final conversion recommendations"""
        recommendations = []
        
        if score < 70:
            recommendations.append({
                'title': 'URGENT: Conversion Rate Optimization Needed',
                'description': 'Implement comprehensive CRO strategy for multi-brand setup',
                'priority': 'critical',
                'impact': 'high'
            })
        
        if conversion_insights.get('error'):
            recommendations.append({
                'title': 'Smart Analysis Enhancement',
                'description': 'Enable AI-powered conversion analysis for deeper insights',
                'priority': 'medium',
                'impact': 'medium'
            })
        
        if score >= 80:
            recommendations.append({
                'title': 'Advanced Conversion Optimization',
                'description': 'Implement A/B testing and advanced personalization',
                'priority': 'low',
                'impact': 'high'
            })
        
        return recommendations
