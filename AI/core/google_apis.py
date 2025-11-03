"""
Google APIs Integration for EMMSO AI System
==========================================

Centralizes Google API integrations including:
- Google Analytics Data API v1beta
- Google PageSpeed Insights API
- Service Account Authentication

🔥 NEW: Real API credentials provided by user!
- Service Account: emmso-461@positive-karma-475015-h7.iam.gserviceaccount.com
- PageSpeed API Key: AIzaSyDUVxUrmf8lbUn2eO6_WTk5ZBOOdE_fAGk
"""

import os
import json
import requests
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta

# Google PageSpeed API key from user
PAGESPEED_API_KEY = "AIzaSyDUVxUrmf8lbUn2eO6_WTk5ZBOOdE_fAGk"

# EMMSO Google Analytics 4 Property ID
GA4_PROPERTY_ID = "properties/460990321"

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
    from google.oauth2 import service_account
    GOOGLE_ANALYTICS_AVAILABLE = True
except ImportError:
    GOOGLE_ANALYTICS_AVAILABLE = False
    print("⚠️ Google Analytics API not available - install google-analytics-data")

class GoogleAPIsManager:
    """
    Central manager for all Google API integrations used by EMMSO AI analysts.
    
    🔥 NEW: Real credentials from user for production data!
    """
    
    def __init__(self):
        """Initialize Google APIs manager."""
        
        self.pagespeed_api_key = PAGESPEED_API_KEY
        self.ga4_property_id = GA4_PROPERTY_ID
        self.service_account_path = os.path.join(os.path.dirname(__file__), '..', 'emmso-google.json')
        
        # Initialize Analytics client
        self.analytics_client = None
        if GOOGLE_ANALYTICS_AVAILABLE:
            self._init_analytics_client()
    
    def _init_analytics_client(self):
        """Initialize Google Analytics client with service account."""
        
        try:
            if os.path.exists(self.service_account_path):
                # Try service account authentication
                try:
                    credentials = service_account.Credentials.from_service_account_file(self.service_account_path)
                    self.analytics_client = BetaAnalyticsDataClient(credentials=credentials)
                    print("✅ Google Analytics client initialized with service account")
                except Exception as service_error:
                    print(f"⚠️ Service account failed ({service_error}), trying user auth...")
                    from google.auth import default
                    credentials, project = default()
                    self.analytics_client = BetaAnalyticsDataClient(credentials=credentials)
                    print("✅ Google Analytics client initialized with user auth")
            else:
                # Fallback to user authentication
                print("⚠️ No service account file, trying user auth...")
                from google.auth import default
                credentials, project = default()
                self.analytics_client = BetaAnalyticsDataClient(credentials=credentials)
                print("✅ Google Analytics client initialized with user auth")
                
        except Exception as e:
            print(f"❌ Failed to initialize Google Analytics client: {e}")
            self.analytics_client = None
    
    def get_analytics_data(self, metrics: List[str], dimensions: List[str] = None, 
                          date_range: str = "30daysAgo") -> Dict[str, Any]:
        """
        Get data from Google Analytics 4.
        
        Args:
            metrics: List of metric names (e.g., ['sessions', 'pageviews'])
            dimensions: List of dimension names (e.g., ['country', 'deviceCategory'])
            date_range: Date range string (e.g., '30daysAgo', '7daysAgo')
        """
        
        if not self.analytics_client:
            return {'error': 'Google Analytics client not initialized'}
        
        try:
            # Build request
            request_metrics = [Metric(name=metric) for metric in metrics]
            request_dimensions = [Dimension(name=dim) for dim in (dimensions or [])]
            
            request = RunReportRequest(
                property=self.ga4_property_id,
                date_ranges=[DateRange(start_date=date_range, end_date="today")],
                metrics=request_metrics,
                dimensions=request_dimensions
            )
            
            # Execute request
            response = self.analytics_client.run_report(request=request)
            
            # Process response
            data = {
                'rows': [],
                'totals': {},
                'metadata': {
                    'metric_names': metrics,
                    'dimension_names': dimensions or [],
                    'date_range': date_range,
                    'row_count': len(response.rows)
                }
            }
            
            # Extract data rows
            for row in response.rows:
                row_data = {}
                
                # Extract dimensions
                for i, dim_name in enumerate(dimensions or []):
                    row_data[dim_name] = row.dimension_values[i].value
                
                # Extract metrics
                for i, metric_name in enumerate(metrics):
                    value = row.metric_values[i].value
                    # Convert to float if numeric
                    try:
                        row_data[metric_name] = float(value) if value else 0
                    except ValueError:
                        row_data[metric_name] = value
                
                data['rows'].append(row_data)
            
            # Calculate totals
            for metric in metrics:
                total = sum(row.get(metric, 0) for row in data['rows'] if isinstance(row.get(metric), (int, float)))
                data['totals'][metric] = total
            
            print(f"✅ Google Analytics data retrieved: {len(response.rows)} rows")
            return data
            
        except Exception as e:
            print(f"❌ Google Analytics data fetch failed: {e}")
            return {'error': f'Analytics fetch failed: {str(e)}'}
    
    def get_pagespeed_insights(self, url: str, strategy: str = 'mobile') -> Dict[str, Any]:
        """
        Get PageSpeed Insights data using Google API.
        
        Args:
            url: URL to analyze
            strategy: 'mobile' or 'desktop'
        """
        
        try:
            api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
            
            params = {
                'url': url,
                'key': self.pagespeed_api_key,
                'category': ['PERFORMANCE', 'ACCESSIBILITY', 'BEST_PRACTICES', 'SEO'],
                'strategy': strategy.upper()
            }
            
            response = requests.get(api_url, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract key data
                lighthouse_result = data.get('lighthouseResult', {})
                categories = lighthouse_result.get('categories', {})
                audits = lighthouse_result.get('audits', {})
                
                processed_data = {
                    'url': url,
                    'strategy': strategy,
                    'timestamp': datetime.now().isoformat(),
                    'scores': {
                        'performance': categories.get('performance', {}).get('score', 0) * 100,
                        'accessibility': categories.get('accessibility', {}).get('score', 0) * 100,
                        'best_practices': categories.get('best-practices', {}).get('score', 0) * 100,
                        'seo': categories.get('seo', {}).get('score', 0) * 100
                    },
                    'core_web_vitals': {
                        'lcp': audits.get('largest-contentful-paint', {}).get('displayValue', 'N/A'),
                        'fid': audits.get('max-potential-fid', {}).get('displayValue', 'N/A'),
                        'cls': audits.get('cumulative-layout-shift', {}).get('displayValue', 'N/A'),
                        'fcp': audits.get('first-contentful-paint', {}).get('displayValue', 'N/A'),
                        'tti': audits.get('interactive', {}).get('displayValue', 'N/A')
                    },
                    'opportunities': [],
                    'diagnostics': []
                }
                
                # Extract optimization opportunities
                for audit_key, audit_data in audits.items():
                    if audit_data.get('score') is not None and audit_data.get('score') < 1:
                        savings = audit_data.get('details', {}).get('overallSavingsMs', 0)
                        if savings and savings > 100:  # 100ms+ savings
                            processed_data['opportunities'].append({
                                'id': audit_key,
                                'title': audit_data.get('title', audit_key),
                                'savings_ms': savings,
                                'description': audit_data.get('description', ''),
                                'score': audit_data.get('score', 0)
                            })
                
                print(f"✅ PageSpeed Insights retrieved: {processed_data['scores']['performance']:.0f}% performance")
                return processed_data
                
            else:
                return {'error': f'PageSpeed API returned {response.status_code}: {response.text}'}
                
        except Exception as e:
            print(f"❌ PageSpeed Insights fetch failed: {e}")
            return {'error': f'PageSpeed fetch failed: {str(e)}'}
    
    def get_seo_metrics(self) -> Dict[str, Any]:
        """Get SEO-specific metrics from Google Analytics."""
        
        return self.get_analytics_data(
            metrics=[
                'organicGoogleSearchClicks',
                'organicGoogleSearchImpressions', 
                'organicGoogleSearchCTR',
                'organicGoogleSearchAveragePosition',
                'sessions',
                'pageviews'
            ],
            dimensions=['pagePath', 'country'],
            date_range='30daysAgo'
        )
    
    def get_ux_metrics(self) -> Dict[str, Any]:
        """Get UX-specific metrics from Google Analytics."""
        
        return self.get_analytics_data(
            metrics=[
                'bounceRate',
                'averageSessionDuration',
                'engagementRate',
                'userEngagementDuration',
                'screenPageViews'
            ],
            dimensions=['deviceCategory', 'country'],
            date_range='30daysAgo'
        )
    
    def get_conversion_metrics(self) -> Dict[str, Any]:
        """Get conversion-specific metrics from Google Analytics."""
        
        return self.get_analytics_data(
            metrics=[
                'conversions',
                'conversionRate',
                'totalRevenue',
                'purchaseRevenue',
                'addToCarts',
                'checkouts'
            ],
            dimensions=['source', 'medium', 'deviceCategory'],
            date_range='30daysAgo'
        )
    
    def get_content_metrics(self) -> Dict[str, Any]:
        """Get content performance metrics from Google Analytics."""
        
        return self.get_analytics_data(
            metrics=[
                'screenPageViews',
                'averageSessionDuration',
                'bounceRate',
                'engagementRate'
            ],
            dimensions=['pagePath', 'pageTitle'],
            date_range='30daysAgo'
        )
    
    def test_apis(self) -> Dict[str, bool]:
        """Test all Google APIs availability."""
        
        results = {
            'analytics_working': False,
            'pagespeed_working': False,
            'service_account_available': os.path.exists(self.service_account_path)
        }
        
        # Test Analytics
        if self.analytics_client:
            test_data = self.get_analytics_data(['sessions'], date_range='7daysAgo')
            results['analytics_working'] = 'error' not in test_data
        
        # Test PageSpeed
        test_pagespeed = self.get_pagespeed_insights('https://emmso.com')
        results['pagespeed_working'] = 'error' not in test_pagespeed
        
        return results

# Global instance for use by analysts
google_apis = GoogleAPIsManager()

def get_google_apis() -> GoogleAPIsManager:
    """Get the global Google APIs manager instance."""
    return google_apis