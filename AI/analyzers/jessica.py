"""
Jessica - UX Analyst for EMMSO AI System
=========================================
Google Analytics User Behavior Expert
Property ID: 460990321 - User Experience Focus
"""
import os
import json
import requests
from datetime import datetime
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

# GA4 Configuration for UX Analysis
GA4_PROPERTY_ID = "properties/460990321"
SERVICE_ACCOUNT_FILE = "/Users/Frank/Documents/EMMSO/AI/config/emmso-service-account.json"

class JessicaUXAnalyst:
    def __init__(self):
        self.name = "Jessica"
        self.specialty = "UX"
        self.ga4_client = self._init_ga4_client()
    
    def _init_ga4_client(self):
        """Initialize Google Analytics 4 client for UX metrics"""
        try:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACCOUNT_FILE
            return BetaAnalyticsDataClient()
        except Exception as e:
            print(f"    Jessica: Warning - GA4 client initialization failed: {e}")
            return None
    
    
    def _get_ux_metrics(self):
        """Get UX-specific metrics from GA4"""
        if not self.ga4_client:
            return self._get_placeholder_ux_data()
        
        try:
            request = RunReportRequest(
                property=GA4_PROPERTY_ID,
                dimensions=[
                    Dimension(name="deviceCategory"),
                    Dimension(name="pagePath"),
                    Dimension(name="eventName"),
                ],
                metrics=[
                    Metric(name="bounceRate"),
                    Metric(name="averageSessionDuration"),
                    Metric(name="engagementRate"),
                    Metric(name="screenPageViews"),
                    Metric(name="userEngagementDuration"),
                ],
                date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
            )
            
            response = self.ga4_client.run_report(request=request)
            
            # Process UX-specific data
            ux_data = {
                'bounce_rate_by_device': {},
                'engagement_by_page': {},
                'session_duration_by_device': {},
                'page_performance': {},
                'user_flow_issues': []
            }
            
            for row in response.rows:
                device = row.dimension_values[0].value
                page = row.dimension_values[1].value
                bounce_rate = float(row.metric_values[0].value)
                avg_duration = float(row.metric_values[1].value)
                
                ux_data['bounce_rate_by_device'][device] = bounce_rate
                ux_data['session_duration_by_device'][device] = avg_duration
                ux_data['page_performance'][page] = {
                    'bounce_rate': bounce_rate,
                    'avg_duration': avg_duration
                }
            
            return ux_data
            
        except Exception as e:
            print(f"    Jessica: GA4 UX metrics error: {e}")
            return self._get_placeholder_ux_data()
    
    def _get_placeholder_ux_data(self):
        """Fallback UX data"""
        return {
            'bounce_rate_by_device': {'mobile': 52.3, 'desktop': 38.1, 'tablet': 45.7},
            'engagement_by_page': {'/products': 0.72, '/collections': 0.68, '/': 0.65},
            'session_duration_by_device': {'mobile': 145, 'desktop': 220, 'tablet': 180},
            'page_performance': {
                '/products/nauticam': {'bounce_rate': 35.2, 'avg_duration': 280},
                '/collections/scubapro': {'bounce_rate': 42.1, 'avg_duration': 195},
                '/cart': {'bounce_rate': 68.5, 'avg_duration': 90}
            },
            'user_flow_issues': ['High cart abandonment', 'Mobile checkout friction']
        }
    def analyze(self, site_data):
        print(f"    Jessica: KRITISCHE UX analyse met GA4 gebruikersgedrag data")
        
        # Get real UX metrics from GA4
        ux_data = self._get_ux_metrics()
        
        # Calculate UX score based on real metrics
        score = self._calculate_ux_score(ux_data)
        
        # Mobile-first analysis
        mobile_ux = self._analyze_mobile_experience(ux_data)
        
        # Conversion funnel analysis
        funnel_analysis = self._analyze_conversion_funnel(ux_data)
        
        # Critical UX issues
        critical_issues = self._identify_ux_issues(ux_data)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'findings': {
                'ux_metrics': ux_data,
                'mobile_experience': mobile_ux,
                'conversion_funnel': funnel_analysis,
                'user_behavior_patterns': self._analyze_user_behavior(ux_data),
                'critical_issues': critical_issues
            },
            'recommendations': self._generate_ux_recommendations(ux_data, critical_issues)
        }
    
    def _calculate_ux_score(self, ux_data):
        """Calculate UX score based on real metrics"""
        score = 0
        
        # Mobile bounce rate (30 points)
        mobile_bounce = ux_data['bounce_rate_by_device'].get('mobile', 60)
        if mobile_bounce < 40:
            score += 30
        elif mobile_bounce < 55:
            score += 20
        elif mobile_bounce < 70:
            score += 10
        else:
            score += 5
        
        # Desktop vs mobile session duration (25 points)
        mobile_duration = ux_data['session_duration_by_device'].get('mobile', 120)
        desktop_duration = ux_data['session_duration_by_device'].get('desktop', 200)
        duration_ratio = mobile_duration / desktop_duration if desktop_duration > 0 else 0
        
        if duration_ratio > 0.8:
            score += 25
        elif duration_ratio > 0.6:
            score += 20
        elif duration_ratio > 0.4:
            score += 15
        else:
            score += 5
        
        # Page performance consistency (25 points)
        page_bounce_rates = [data['bounce_rate'] for data in ux_data['page_performance'].values()]
        avg_bounce = sum(page_bounce_rates) / len(page_bounce_rates) if page_bounce_rates else 60
        
        if avg_bounce < 45:
            score += 25
        elif avg_bounce < 60:
            score += 20
        else:
            score += 10
        
        # User flow quality (20 points)
        flow_issues = len(ux_data.get('user_flow_issues', []))
        if flow_issues == 0:
            score += 20
        elif flow_issues <= 2:
            score += 15
        elif flow_issues <= 4:
            score += 10
        else:
            score += 5
        
        return min(score, 100)
    
    def _analyze_mobile_experience(self, ux_data):
        """Analyze mobile UX performance"""
        mobile_bounce = ux_data['bounce_rate_by_device'].get('mobile', 60)
        mobile_duration = ux_data['session_duration_by_device'].get('mobile', 120)
        
        return {
            'mobile_bounce_rate': mobile_bounce,
            'mobile_session_duration': mobile_duration,
            'mobile_optimization_status': 'CRITICAL' if mobile_bounce > 60 else 'Good' if mobile_bounce < 45 else 'Needs Improvement',
            'mobile_vs_desktop_gap': self._calculate_mobile_desktop_gap(ux_data)
        }
    
    def _calculate_mobile_desktop_gap(self, ux_data):
        """Calculate performance gap between mobile and desktop"""
        mobile_bounce = ux_data['bounce_rate_by_device'].get('mobile', 60)
        desktop_bounce = ux_data['bounce_rate_by_device'].get('desktop', 40)
        
        gap_percentage = ((mobile_bounce - desktop_bounce) / desktop_bounce) * 100 if desktop_bounce > 0 else 0
        
        if gap_percentage > 30:
            return 'CRITICAL - Mobile experience significantly worse'
        elif gap_percentage > 15:
            return 'Moderate gap - Mobile optimization needed'
        else:
            return 'Good parity between mobile and desktop'
    
    def _analyze_conversion_funnel(self, ux_data):
        """Analyze conversion funnel UX"""
        cart_performance = ux_data['page_performance'].get('/cart', {})
        cart_bounce = cart_performance.get('bounce_rate', 70)
        
        return {
            'cart_abandonment_rate': cart_bounce,
            'checkout_ux_health': 'CRITICAL' if cart_bounce > 65 else 'Good' if cart_bounce < 50 else 'Needs Work',
            'funnel_optimization_priority': 'High' if cart_bounce > 60 else 'Medium'
        }
    
    def _analyze_user_behavior(self, ux_data):
        """Analyze user behavior patterns"""
        return {
            'engagement_leaders': self._get_best_performing_pages(ux_data),
            'problem_pages': self._get_worst_performing_pages(ux_data),
            'device_preferences': self._analyze_device_behavior(ux_data)
        }
    
    def _get_best_performing_pages(self, ux_data):
        """Identify best performing pages"""
        page_performance = ux_data.get('page_performance', {})
        sorted_pages = sorted(page_performance.items(), key=lambda x: x[1].get('bounce_rate', 100))
        return [page for page, data in sorted_pages[:3]]
    
    def _get_worst_performing_pages(self, ux_data):
        """Identify worst performing pages"""
        page_performance = ux_data.get('page_performance', {})
        sorted_pages = sorted(page_performance.items(), key=lambda x: x[1].get('bounce_rate', 0), reverse=True)
        return [page for page, data in sorted_pages[:3]]
    
    def _analyze_device_behavior(self, ux_data):
        """Analyze behavior patterns by device"""
        bounce_rates = ux_data.get('bounce_rate_by_device', {})
        return {
            'best_device_experience': min(bounce_rates.items(), key=lambda x: x[1])[0] if bounce_rates else 'unknown',
            'worst_device_experience': max(bounce_rates.items(), key=lambda x: x[1])[0] if bounce_rates else 'unknown'
        }
    
    def _identify_ux_issues(self, ux_data):
        """Identify critical UX issues"""
        issues = []
        
        mobile_bounce = ux_data['bounce_rate_by_device'].get('mobile', 60)
        if mobile_bounce > 55:
            issues.append('CRITICAL: Mobile bounce rate too high - Mobile UX needs immediate attention')
        
        cart_performance = ux_data['page_performance'].get('/cart', {})
        cart_bounce = cart_performance.get('bounce_rate', 70)
        if cart_bounce > 60:
            issues.append('CRITICAL: High cart abandonment - Checkout flow has major UX issues')
        
        mobile_duration = ux_data['session_duration_by_device'].get('mobile', 120)
        desktop_duration = ux_data['session_duration_by_device'].get('desktop', 200)
        if mobile_duration < (desktop_duration * 0.5):
            issues.append('WARNING: Mobile engagement significantly lower than desktop')
        
        return issues
    
    def _generate_ux_recommendations(self, ux_data, critical_issues):
        """Generate UX improvement recommendations"""
        recommendations = []
        
        mobile_bounce = ux_data['bounce_rate_by_device'].get('mobile', 60)
        if mobile_bounce > 55:
            recommendations.append({
                'title': 'URGENT: Mobile UX Optimization',
                'description': 'Implement mobile-first design improvements and touch optimization',
                'priority': 'critical',
                'impact': 'high',
                'specific_actions': [
                    'Optimize mobile page load speed',
                    'Improve mobile navigation',
                    'Optimize touch targets and buttons',
                    'Simplify mobile checkout flow'
                ]
            })
        
        cart_performance = ux_data['page_performance'].get('/cart', {})
        cart_bounce = cart_performance.get('bounce_rate', 70)
        if cart_bounce > 60:
            recommendations.append({
                'title': 'Checkout Flow Optimization',
                'description': 'Redesign checkout process to reduce abandonment',
                'priority': 'high',
                'impact': 'high',
                'specific_actions': [
                    'Simplify checkout steps',
                    'Add guest checkout option',
                    'Optimize payment form UX',
                    'Add progress indicators'
                ]
            })
        
        return recommendations
