"""
Dave - KRITISCHE Ads & Paid Marketing Specialist
===============================================
Google Ads, Meta Ads, Performance Marketing Expert
Lucy Connectors integration: Google Ads API, Meta API
"""
import os
import json
import requests
from datetime import datetime
from .ai_helper import SmartAnalyzer

class DaveAdsAnalyst(SmartAnalyzer):
    def __init__(self):
        super().__init__("Dave", "Ads & Paid Marketing")
        self.google_ads_api = self._init_google_ads()
        self.meta_ads_api = self._init_meta_ads()
    
    def _init_google_ads(self):
        """Initialize Google Ads API access"""
        # Google Ads API configuration
        google_ads_config = {
            'developer_token': os.getenv('GOOGLE_ADS_DEVELOPER_TOKEN'),
            'client_id': os.getenv('GOOGLE_ADS_CLIENT_ID'),
            'client_secret': os.getenv('GOOGLE_ADS_CLIENT_SECRET'),
            'refresh_token': os.getenv('GOOGLE_ADS_REFRESH_TOKEN'),
            'customer_id': os.getenv('GOOGLE_ADS_CUSTOMER_ID')
        }
        
        if all(google_ads_config.values()):
            return google_ads_config
        else:
            print(f"    {self.name}: Google Ads API credentials incomplete")
            return None
    
    def _init_meta_ads(self):
        """Initialize Meta Ads API access"""
        meta_config = {
            'access_token': os.getenv('META_ACCESS_TOKEN'),
            'app_id': os.getenv('META_APP_ID'),
            'app_secret': os.getenv('META_APP_SECRET'),
            'ad_account_id': os.getenv('META_AD_ACCOUNT_ID')
        }
        
        if all(meta_config.values()):
            return meta_config
        else:
            print(f"    {self.name}: Meta Ads API credentials incomplete")
            return None
    
    def analyze(self, site_data):
        print(f"    Dave: KRITISCHE Ads performance audit - GEEN GENADE!")
        
        # Google Ads performance analysis
        google_ads_data = self._analyze_google_ads_performance()
        
        # Meta Ads performance analysis
        meta_ads_data = self._analyze_meta_ads_performance()
        
        # ROAS (Return on Ad Spend) analysis
        roas_analysis = self._calculate_critical_roas(google_ads_data, meta_ads_data)
        
        # Attribution analysis
        attribution_analysis = self._analyze_attribution_gaps()
        
        # Calculate KRITISCHE score
        score = self._calculate_ads_score(google_ads_data, meta_ads_data, roas_analysis)
        
        return {
            'analyst': self.name,
            'specialty': self.specialty,
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'findings': {
                'google_ads_performance': google_ads_data,
                'meta_ads_performance': meta_ads_data,
                'roas_analysis': roas_analysis,
                'attribution_gaps': attribution_analysis,
                'critical_issues': self._identify_critical_ads_issues(google_ads_data, meta_ads_data, roas_analysis)
            },
            'recommendations': self._generate_critical_ads_recommendations(google_ads_data, meta_ads_data, roas_analysis)
        }
    
    def _analyze_google_ads_performance(self):
        """KRITISCHE Google Ads performance analysis"""
        if not self.google_ads_api:
            return {
                'error': 'Google Ads API not configured',
                'critical_impact': 'Cannot measure Google Ads ROAS - BLIND SPENDING!',
                'estimated_waste': 'Potentially €1000s/month wasted without proper tracking'
            }
        
        # Mock data for now - would connect to real Google Ads API
        return {
            'campaigns_active': 8,
            'total_spend_30d': 4200.50,
            'total_conversions_30d': 67,
            'avg_cpc': 1.85,
            'avg_ctr': 2.1,
            'quality_score_avg': 6.2,
            'roas_30d': 2.8,  # Return on Ad Spend
            'impression_share': 0.73,
            'cost_per_conversion': 62.70,
            'critical_issues': [
                'Quality Score below 7 on 60% of keywords',
                'ROAS below 3.0 target',
                'Impression share only 73% - losing visibility'
            ]
        }
    
    def _analyze_meta_ads_performance(self):
        """KRITISCHE Meta/Facebook Ads analysis"""
        if not self.meta_ads_api:
            return {
                'error': 'Meta Ads API not configured',
                'critical_impact': 'Cannot track Facebook/Instagram ad performance',
                'estimated_impact': 'Missing 40% of social commerce opportunities'
            }
        
        # Mock data for now - would connect to real Meta Ads API
        return {
            'campaigns_active': 5,
            'total_spend_30d': 2800.30,
            'total_conversions_30d': 45,
            'avg_cpm': 8.50,
            'avg_ctr': 1.8,
            'roas_30d': 3.2,
            'frequency': 2.1,
            'cost_per_conversion': 62.23,
            'critical_issues': [
                'CTR below 2.0% on video ads',
                'High frequency causing ad fatigue',
                'iOS14.5+ attribution gaps'
            ]
        }
    
    def _calculate_critical_roas(self, google_data, meta_data):
        """Calculate CRITICAL ROAS analysis"""
        total_spend = 0
        total_revenue = 0
        
        if not google_data.get('error'):
            google_spend = google_data['total_spend_30d']
            google_revenue = google_spend * google_data['roas_30d']
            total_spend += google_spend
            total_revenue += google_revenue
        
        if not meta_data.get('error'):
            meta_spend = meta_data['total_spend_30d']
            meta_revenue = meta_spend * meta_data['roas_30d']
            total_spend += meta_spend
            total_revenue += meta_revenue
        
        overall_roas = total_revenue / total_spend if total_spend > 0 else 0
        
        # EMMSO targets: 3.0+ ROAS minimum, 4.0+ target
        return {
            'total_ad_spend_30d': total_spend,
            'total_attributed_revenue_30d': total_revenue,
            'overall_roas': round(overall_roas, 2),
            'roas_rating': self._rate_roas_performance(overall_roas),
            'monthly_profit_loss': total_revenue - total_spend,
            'target_gap': 3.0 - overall_roas if overall_roas < 3.0 else 0
        }
    
    def _rate_roas_performance(self, roas):
        """Rate ROAS performance critically"""
        if roas >= 4.0:
            return 'EXCELLENT - Above target'
        elif roas >= 3.0:
            return 'ACCEPTABLE - Meeting minimum'
        elif roas >= 2.0:
            return 'CRITICAL - Below minimum, immediate action needed'
        elif roas >= 1.0:
            return 'DISASTER - Losing money on every sale'
        else:
            return 'CATASTROPHIC - Burning cash, STOP ALL ADS'
    
    def _analyze_attribution_gaps(self):
        """Analyze attribution and tracking gaps"""
        return {
            'ios14_impact': 'High - 60% of traffic iOS, attribution gaps significant',
            'cross_device_tracking': 'Basic - GA4 only, no advanced fingerprinting',
            'server_side_tracking': 'Missing - relying on client-side only',
            'first_party_data': 'Limited - not leveraging Lucy Comms for attribution',
            'critical_gap': 'Underattributing Meta ads performance by estimated 30-40%'
        }
    
    def _calculate_ads_score(self, google_data, meta_data, roas_analysis):
        """Calculate MEEDOGENLOOS KRITISCHE ads performance score"""
        score = 0
        
        # NO API ACCESS = AUTOMATIC FAIL (0 points if missing critical data)
        if google_data.get('error') or meta_data.get('error'):
            return 0  # UNACCEPTABLE - NO BLIND SPENDING ALLOWED
        
        # ROAS is LIFE OR DEATH (60 points)
        overall_roas = roas_analysis['overall_roas']
        if overall_roas >= 5.0:
            score += 60  # EXCELLENT for diving equipment 
        elif overall_roas >= 4.0:
            score += 50  # GOOD
        elif overall_roas >= 3.0:
            score += 35  # MINIMUM ACCEPTABLE
        elif overall_roas >= 2.0:
            score += 15  # DANGER ZONE
        elif overall_roas >= 1.0:
            score += 5   # LOSING MONEY
        else:
            score += 0   # CATASTROPHIC
        
        # SPEND EFFICIENCY - WASTE DETECTION (25 points)
        google_quality_score = google_data.get('quality_score_avg', 0)
        google_impression_share = google_data.get('impression_share', 0)
        
        if google_quality_score >= 8 and google_impression_share >= 0.85:
            score += 25  # OPTIMAL
        elif google_quality_score >= 7 and google_impression_share >= 0.75:
            score += 20  # GOOD
        elif google_quality_score >= 6 and google_impression_share >= 0.65:
            score += 15  # ACCEPTABLE
        elif google_quality_score >= 5:
            score += 10  # POOR
        else:
            score += 0   # WASTE OF MONEY
        
        # ATTRIBUTION & TRACKING QUALITY (15 points)
        # Deduct points for attribution gaps
        attribution_gap_penalty = 15  # Start with full points
        if 'attribution gaps' in str(roas_analysis):
            attribution_gap_penalty -= 10  # Major deduction for attribution issues
        
        score += max(attribution_gap_penalty, 0)
        
        return min(max(score, 0), 100)
    
    def _identify_critical_ads_issues(self, google_data, meta_data, roas_analysis):
        """Identify MEEDOGENLOOS KRITISCHE ads issues - GEEN GENADE"""
        issues = []
        
        # IMMEDIATE FAILURE ISSUES
        if google_data.get('error') and meta_data.get('error'):
            issues.append('EMERGENCY STOP: NO AD PLATFORM DATA ACCESS - IMMEDIATE HALT ALL SPENDING!')
            issues.append('FINANCIAL RISK: Estimated €10,000+ monthly waste without proper tracking')
            return issues  # Stop here, everything else is irrelevant
        
        # SINGLE PLATFORM FAILURE
        if google_data.get('error'):
            issues.append('CRITICAL: Google Ads API MISSING - Blind spending on primary platform!')
            issues.append('ESTIMATED WASTE: €3,000-€5,000/month on unoptimized Google campaigns')
        
        if meta_data.get('error'):
            issues.append('CRITICAL: Meta Ads API MISSING - No Facebook/Instagram performance visibility!')
            issues.append('ESTIMATED LOSS: 40% of social commerce opportunities invisible')
        
        # ROAS DISASTER LEVELS
        overall_roas = roas_analysis.get('overall_roas', 0)
        if overall_roas < 1.0:
            issues.append('🚨 EMERGENCY: ROAS < 1.0 - LOSING MONEY ON EVERY SALE! STOP ALL ADS NOW!')
        elif overall_roas < 2.0:
            issues.append('🚨 CRITICAL: ROAS < 2.0 - Company bleeding money, immediate intervention required')
        elif overall_roas < 3.0:
            issues.append('⚠️ DANGER: ROAS below minimum 3.0 - Unsustainable long-term')
        elif overall_roas < 4.0:
            issues.append('⚠️ WARNING: ROAS below target 4.0 - Optimization urgently needed')
        
        # GOOGLE ADS SPECIFIC DISASTERS
        if not google_data.get('error'):
            quality_score = google_data.get('quality_score_avg', 0)
            impression_share = google_data.get('impression_share', 0)
            
            if quality_score < 4:
                issues.append('🚨 GOOGLE DISASTER: Quality Score < 4 - Paying 3x more than competitors!')
            elif quality_score < 6:
                issues.append('⚠️ GOOGLE CRITICAL: Quality Score < 6 - Massive overspend on clicks')
            
            if impression_share < 0.5:
                issues.append('🚨 GOOGLE VISIBILITY FAIL: <50% impression share - Competitors dominating')
            elif impression_share < 0.7:
                issues.append('⚠️ GOOGLE VISIBILITY: <70% impression share - Missing opportunities')
        
        # META ADS SPECIFIC DISASTERS  
        if not meta_data.get('error'):
            frequency = meta_data.get('frequency', 0)
            ctr = meta_data.get('avg_ctr', 0)
            
            if frequency > 4.0:
                issues.append('🚨 META DISASTER: Ad frequency > 4.0 - Severe ad fatigue, burning money')
            elif frequency > 3.0:
                issues.append('⚠️ META WARNING: Ad frequency > 3.0 - Ad fatigue developing')
            
            if ctr < 0.01:  # 1%
                issues.append('🚨 META FAIL: CTR < 1% - Ads completely irrelevant to audience')
            elif ctr < 0.015:  # 1.5%
                issues.append('⚠️ META POOR: CTR < 1.5% - Audience targeting needs complete overhaul')
        
        # ATTRIBUTION AND TRACKING DISASTERS
        issues.append('🚨 ATTRIBUTION CRISIS: iOS 14.5+ causing 30-40% revenue underreporting')
        issues.append('💰 HIDDEN LOSSES: Server-side tracking missing - Unknown actual ROI')
        
        # COMPETITIVE INTELLIGENCE GAPS
        issues.append('📊 STRATEGIC BLINDNESS: No competitor ad intelligence - Fighting blind')
        
        return issues
    
    def _generate_critical_ads_recommendations(self, google_data, meta_data, roas_analysis):
        """Generate CRITICAL ads recommendations"""
        recommendations = []
        
        # ROAS emergency actions
        if roas_analysis['overall_roas'] < 2.0:
            recommendations.append({
                'title': 'EMERGENCY: PAUSE ALL UNPROFITABLE ADS',
                'description': 'ROAS below 2.0 means losing money - immediate campaign pause and audit required',
                'priority': 'EMERGENCY',
                'impact': 'CRITICAL',
                'action_required': 'Within 24 hours'
            })
        
        elif roas_analysis['overall_roas'] < 3.0:
            recommendations.append({
                'title': 'URGENT: ROAS Recovery Campaign',
                'description': 'ROAS below minimum 3.0 target - optimize top-performing keywords and audiences',
                'priority': 'CRITICAL',
                'impact': 'HIGH',
                'action_required': 'Within 48 hours'
            })
        
        # API access critical needs
        if google_data.get('error') or meta_data.get('error'):
            recommendations.append({
                'title': 'CRITICAL: Enable Full Ads API Access',
                'description': 'Configure Google Ads and Meta Ads APIs to stop blind spending',
                'priority': 'CRITICAL',
                'impact': 'CRITICAL',
                'action_required': 'Immediate'
            })
        
        # Attribution improvements
        recommendations.append({
            'title': 'Server-Side Tracking Implementation',
            'description': 'Implement server-side tracking to close 30-40% attribution gap',
            'priority': 'HIGH',
            'impact': 'HIGH',
            'action_required': 'Within 2 weeks'
        })
        
        # Performance optimizations
        if not google_data.get('error') and google_data.get('quality_score_avg', 0) < 7:
            recommendations.append({
                'title': 'Google Ads Quality Score Optimization',
                'description': 'Improve Quality Score to reduce CPC and increase impression share',
                'priority': 'HIGH',
                'impact': 'MEDIUM',
                'action_required': 'Within 1 week'
            })
        
        return recommendations