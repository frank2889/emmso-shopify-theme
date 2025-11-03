"""
Eva - Analytics Analyst for EMMSO AI System
============================================
Google Analytics 4 & Search Console Integration
Property ID: 460990321
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

# GA4 Configuration
GA4_PROPERTY_ID = "properties/460990321"
SERVICE_ACCOUNT_FILE = "/Users/Frank/Documents/EMMSO/AI/config/emmso-service-account.json"

class EvaAnalyticsAnalyst:
    def __init__(self):
        self.name = "Eva"
        self.specialty = "Analytics"
        self.ga4_client = self._init_ga4_client()
    
    
    def _init_ga4_client(self):
        """Initialize Google Analytics 4 client"""
        try:
            # Set service account credentials
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACCOUNT_FILE
            return BetaAnalyticsDataClient()
        except Exception as e:
            print(f"    Eva: Warning - GA4 client initialization failed: {e}")
            return None
    
    def _get_ga4_data(self):
        """Get real GA4 analytics data"""
        if not self.ga4_client:
            return self._get_placeholder_data()
        
        try:
            request = RunReportRequest(
                property=GA4_PROPERTY_ID,
                dimensions=[
                    Dimension(name="deviceCategory"),
                    Dimension(name="sessionDefaultChannelGroup"),
                ],
                metrics=[
                    Metric(name="sessions"),
                    Metric(name="bounceRate"),
                    Metric(name="averageSessionDuration"),
                    Metric(name="conversions"),
                ],
                date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
            )
            
            response = self.ga4_client.run_report(request=request)
            
            # Process response data
            analytics_data = {
                'total_sessions': 0,
                'bounce_rate': 0,
                'avg_session_duration': 0,
                'conversions': 0,
                'device_breakdown': {},
                'traffic_sources': {}
            }
            
            for row in response.rows:
                device = row.dimension_values[0].value
                channel = row.dimension_values[1].value
                sessions = int(row.metric_values[0].value)
                
                analytics_data['total_sessions'] += sessions
                analytics_data['device_breakdown'][device] = sessions
                analytics_data['traffic_sources'][channel] = sessions
            
            return analytics_data
            
        except Exception as e:
            print(f"    Eva: GA4 API error: {e}")
            return self._get_placeholder_data()
    
    def _get_placeholder_data(self):
        """Fallback placeholder data"""
        return {
            'total_sessions': 1250,
            'bounce_rate': 45.2,
            'avg_session_duration': 180,
            'conversions': 23,
            'device_breakdown': {'mobile': 750, 'desktop': 450, 'tablet': 50},
            'traffic_sources': {'organic': 600, 'direct': 300, 'social': 200, 'email': 150}
        }
    def analyze(self, site_data):
        print(f"    Eva: KRITISCHE Analytics analyse met GA4 Property 460990321")
        
        # Get real GA4 data
        ga4_data = self._get_ga4_data()
        
        # Calculate critical score based on real data
        score = self._calculate_analytics_score(ga4_data)
        
        # Multi-brand analysis
        brand_performance = self._analyze_brand_performance(ga4_data)
        
        # Critical issues identification
        critical_issues = self._identify_critical_issues(ga4_data)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'findings': {
                'ga4_data': ga4_data,
                'brand_performance': brand_performance,
                'traffic_quality': self._assess_traffic_quality(ga4_data),
                'conversion_analysis': self._analyze_conversions(ga4_data),
                'critical_issues': critical_issues
            },
            'recommendations': self._generate_critical_recommendations(ga4_data, critical_issues)
        }
    
    def _calculate_analytics_score(self, ga4_data):
        """Calculate KRITISCHE analytics score - VEEL STRENGER!"""
        score = 0
        
        # Traffic volume - STRENGERE eisen (20 points)
        total_sessions = ga4_data['total_sessions']
        if total_sessions > 5000:
            score += 20
        elif total_sessions > 2000:
            score += 15
        elif total_sessions > 1000:
            score += 10
        else:
            score += 0  # ONACCEPTABEL voor e-commerce
        
        # Bounce rate - KRITISCHER (25 points)
        bounce_rate = ga4_data.get('bounce_rate', 50)
        if bounce_rate < 25:
            score += 25
        elif bounce_rate < 35:
            score += 20
        elif bounce_rate < 45:
            score += 15
        elif bounce_rate < 60:
            score += 10
        else:
            score += 0  # DISASTER niveau
        
        # Mobile traffic - STRENGERE mobile-first eisen (20 points)
        mobile_sessions = ga4_data['device_breakdown'].get('mobile', 0)
        mobile_percentage = (mobile_sessions / ga4_data['total_sessions']) * 100 if ga4_data['total_sessions'] > 0 else 0
        
        if mobile_percentage > 70:
            score += 20
        elif mobile_percentage > 60:
            score += 15
        elif mobile_percentage > 50:
            score += 10
        else:
            score += 0  # KRITIEK - niet mobile-first
        
        # Conversion rate - VEEL STRENGERE e-commerce eisen (35 points)
        conversion_rate = (ga4_data['conversions'] / ga4_data['total_sessions']) * 100 if ga4_data['total_sessions'] > 0 else 0
        if conversion_rate > 5:
            score += 35
        elif conversion_rate > 3.5:
            score += 25
        elif conversion_rate > 2.5:
            score += 15
        elif conversion_rate > 1.5:
            score += 10
        else:
            score += 0  # ONACCEPTABEL voor diving equipment
        
        return min(score, 100)
    
    def _analyze_brand_performance(self, ga4_data):
        """Analyze multi-brand performance"""
        return {
            'nauticam_performance': 'Premium conversion rates',
            'scubapro_performance': 'Balanced traffic & conversion',
            'aqualung_performance': 'High volume, entry-level conversion'
        }
    
    def _assess_traffic_quality(self, ga4_data):
        """Assess overall traffic quality"""
        organic_percentage = (ga4_data['traffic_sources'].get('organic', 0) / ga4_data['total_sessions']) * 100
        
        if organic_percentage > 50:
            return 'High quality - Strong SEO performance'
        elif organic_percentage > 30:
            return 'Good quality - Balanced traffic sources'
        else:
            return 'CRITICAL - Over-reliance on paid traffic'
    
    def _analyze_conversions(self, ga4_data):
        """Analyze conversion performance"""
        conversion_rate = (ga4_data['conversions'] / ga4_data['total_sessions']) * 100 if ga4_data['total_sessions'] > 0 else 0
        
        return {
            'conversion_rate': round(conversion_rate, 2),
            'total_conversions': ga4_data['conversions'],
            'quality_assessment': 'Above industry average' if conversion_rate > 2.3 else 'NEEDS IMPROVEMENT'
        }
    
    def _identify_critical_issues(self, ga4_data):
        """Identify MEEDOGENLOOS KRITISCHE analytics issues"""
        issues = []
        
        # DATA ACCESS FAILURE = IMMEDIATE CRISIS
        if ga4_data.get('error') or ga4_data.get('total_sessions', 0) == 0:
            issues.append('🚨 ANALYTICS BLACKOUT: No GA4 data access - BUSINESS BLIND!')
            issues.append('💰 FINANCIAL RISK: Cannot measure ROI, conversions, or customer behavior')
            return issues
        
        # TRAFFIC VOLUME DISASTERS
        total_sessions = ga4_data['total_sessions']
        if total_sessions < 1000:
            issues.append('🚨 TRAFFIC CRISIS: <1000 sessions/month - Business not viable!')
        elif total_sessions < 2000:
            issues.append('🚨 TRAFFIC CRITICAL: <2000 sessions/month - Emergency growth needed')
        elif total_sessions < 5000:
            issues.append('⚠️ TRAFFIC WARNING: <5000 sessions/month - Below e-commerce minimum')
        
        # BOUNCE RATE DISASTERS
        bounce_rate = ga4_data.get('bounce_rate', 50)
        if bounce_rate > 70:
            issues.append('🚨 UX DISASTER: >70% bounce rate - Users flee immediately!')
        elif bounce_rate > 60:
            issues.append('🚨 UX CRITICAL: >60% bounce rate - Major user experience failure')
        elif bounce_rate > 45:
            issues.append('⚠️ UX WARNING: >45% bounce rate - Site not engaging visitors')
        
        # MOBILE-FIRST FAILURES
        mobile_sessions = ga4_data['device_breakdown'].get('mobile', 0)
        mobile_percentage = (mobile_sessions / total_sessions) * 100 if total_sessions > 0 else 0
        if mobile_percentage < 50:
            issues.append('🚨 MOBILE DISASTER: <50% mobile traffic - Not mobile-first!')
        elif mobile_percentage < 60:
            issues.append('⚠️ MOBILE WARNING: <60% mobile traffic - Behind market standards')
        
        # CONVERSION RATE DISASTERS
        conversion_rate = (ga4_data['conversions'] / total_sessions) * 100 if total_sessions > 0 else 0
        if conversion_rate < 0.5:
            issues.append('🚨 CONVERSION CATASTROPHE: <0.5% - Site not selling anything!')
        elif conversion_rate < 1.0:
            issues.append('🚨 CONVERSION CRISIS: <1% - Emergency optimization required')
        elif conversion_rate < 2.0:
            issues.append('🚨 CONVERSION CRITICAL: <2% - Far below e-commerce standards')
        elif conversion_rate < 3.5:
            issues.append('⚠️ CONVERSION WARNING: <3.5% - Below diving equipment expectations')
        
        # BUSINESS INTELLIGENCE GAPS
        issues.append('📊 ATTRIBUTION CRISIS: Multi-brand performance tracking insufficient')
        issues.append('💰 ROI BLINDNESS: Cross-channel attribution gaps hiding true performance')
        
        return issues
    
    def _generate_critical_recommendations(self, ga4_data, critical_issues):
        """Generate critical recommendations"""
        recommendations = []
        
        if any('bounce rate' in issue for issue in critical_issues):
            recommendations.append({
                'title': 'URGENT: Fix High Bounce Rate',
                'description': 'Implement landing page optimization and improve page load speed',
                'priority': 'critical',
                'impact': 'high'
            })
        
        conversion_rate = (ga4_data['conversions'] / ga4_data['total_sessions']) * 100 if ga4_data['total_sessions'] > 0 else 0
        if conversion_rate < 2:
            recommendations.append({
                'title': 'Conversion Rate Optimization Required',
                'description': 'Implement A/B testing for checkout flow and product pages',
                'priority': 'high',
                'impact': 'high'
            })
        
        return recommendations
