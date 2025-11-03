"""
Shopify API Integration for EMMSO AI System
==========================================

Handles all Shopify API interactions including:
- Store data retrieval
- Product information
- Order analytics
- Theme settings
- App configurations
"""

import os
import json
import requests
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

class ShopifyAPI:
    """Shopify API client for EMMSO store analysis."""
    
    def __init__(self):
        """Initialize Shopify API client."""
        self.shop_url = os.getenv('SHOPIFY_SHOP_URL', 'emmso.myshopify.com')
        self.access_token = os.getenv('SHOPIFY_ACCESS_TOKEN', '')
        self.api_version = '2026-01'
        
        self.base_url = f"https://{self.shop_url}/admin/api/{self.api_version}"
        self.headers = {
            'X-Shopify-Access-Token': self.access_token,
            'Content-Type': 'application/json'
        }
        
    def is_configured(self) -> bool:
        """Check if Shopify API is properly configured."""
        return bool(self.shop_url and self.access_token)
    
    def test_connection(self) -> Dict[str, Any]:
        """Test the API connection."""
        try:
            response = self._make_request('GET', '/shop.json')
            if response:
                return {'status': 'connected', 'shop': response.get('shop', {})}
            return {'status': 'error', 'message': 'No response from API'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def get_store_data(self) -> Dict[str, Any]:
        """Get comprehensive store data for analysis."""
        
        store_data = {
            'shop_info': self.get_shop_info(),
            'products': self.get_products_summary(),
            'orders': self.get_orders_summary(),
            'themes': self.get_themes_info(),
            'apps': self.get_installed_apps(),
            'timestamp': datetime.now().isoformat()
        }
        
        return store_data
    
    def get_shop_info(self) -> Dict[str, Any]:
        """Get basic shop information."""
        try:
            response = self._make_request('GET', '/shop.json')
            if response and 'shop' in response:
                shop = response['shop']
                return {
                    'name': shop.get('name'),
                    'domain': shop.get('domain'),
                    'email': shop.get('email'),
                    'currency': shop.get('currency'),
                    'timezone': shop.get('iana_timezone'),
                    'plan': shop.get('plan_name'),
                    'created_at': shop.get('created_at')
                }
        except Exception as e:
            print(f"Error getting shop info: {e}")
        
        return {}
    
    def get_products_summary(self) -> Dict[str, Any]:
        """Get products summary for analysis."""
        try:
            # Get products count
            count_response = self._make_request('GET', '/products/count.json')
            total_products = count_response.get('count', 0) if count_response else 0
            
            # Get sample products for analysis
            products_response = self._make_request('GET', '/products.json?limit=50')
            products = products_response.get('products', []) if products_response else []
            
            # Analyze products
            published_count = sum(1 for p in products if p.get('status') == 'active')
            avg_variants = sum(len(p.get('variants', [])) for p in products) / len(products) if products else 0
            
            return {
                'total_count': total_products,
                'sample_count': len(products),
                'published_count': published_count,
                'avg_variants_per_product': round(avg_variants, 1),
                'sample_products': [
                    {
                        'id': p.get('id'),
                        'title': p.get('title'),
                        'status': p.get('status'),
                        'variants_count': len(p.get('variants', [])),
                        'images_count': len(p.get('images', []))
                    }
                    for p in products[:10]  # First 10 for analysis
                ]
            }
        except Exception as e:
            print(f"Error getting products: {e}")
            return {'error': str(e)}
    
    def get_orders_summary(self) -> Dict[str, Any]:
        """Get orders summary for conversion analysis."""
        try:
            # Get recent orders (last 30 days)
            since_date = (datetime.now() - timedelta(days=30)).isoformat()
            
            orders_response = self._make_request(
                'GET', 
                f'/orders.json?status=any&created_at_min={since_date}&limit=250'
            )
            orders = orders_response.get('orders', []) if orders_response else []
            
            if not orders:
                return {'message': 'No recent orders found'}
            
            # Calculate metrics
            total_sales = sum(float(order.get('total_price', 0)) for order in orders)
            avg_order_value = total_sales / len(orders) if orders else 0
            
            return {
                'recent_orders_count': len(orders),
                'total_sales_30d': round(total_sales, 2),
                'avg_order_value': round(avg_order_value, 2),
                'currency': orders[0].get('currency') if orders else 'EUR'
            }
        except Exception as e:
            print(f"Error getting orders: {e}")
            return {'error': str(e)}
    
    def get_themes_info(self) -> Dict[str, Any]:
        """Get theme information."""
        try:
            themes_response = self._make_request('GET', '/themes.json')
            themes = themes_response.get('themes', []) if themes_response else []
            
            active_theme = next((t for t in themes if t.get('role') == 'main'), None)
            
            return {
                'total_themes': len(themes),
                'active_theme': {
                    'id': active_theme.get('id'),
                    'name': active_theme.get('name'),
                    'created_at': active_theme.get('created_at'),
                    'updated_at': active_theme.get('updated_at')
                } if active_theme else None,
                'all_themes': [
                    {
                        'id': t.get('id'),
                        'name': t.get('name'),
                        'role': t.get('role')
                    }
                    for t in themes
                ]
            }
        except Exception as e:
            print(f"Error getting themes: {e}")
            return {'error': str(e)}
    
    def get_installed_apps(self) -> Dict[str, Any]:
        """Get information about installed apps (if accessible)."""
        # Note: App information requires specific permissions
        # This is a placeholder for when we have proper app access
        return {
            'message': 'App information requires additional API permissions',
            'suggestion': 'Enable app management scope for detailed app analysis'
        }
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Optional[Dict]:
        """Make a request to the Shopify API."""
        
        if not self.is_configured():
            raise Exception("Shopify API not configured. Set SHOPIFY_SHOP_URL and SHOPIFY_ACCESS_TOKEN")
        
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers, timeout=30)
            elif method == 'POST':
                response = requests.post(url, headers=self.headers, json=data, timeout=30)
            elif method == 'PUT':
                response = requests.put(url, headers=self.headers, json=data, timeout=30)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Shopify API request failed: {e}")
            return None