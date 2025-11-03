#!/usr/bin/env python3
"""
Screenshot Capture Tool for EMMSO Theme
========================================
Automatically captures screenshots of all important pages for Vision AI analysis
"""
import os
import sys
from playwright.sync_api import sync_playwright
from datetime import datetime

# Shopify preview URL
PREVIEW_URL = "https://y0hnl2y5cksklmw7-63663472878.shopifypreview.com"

# Pages to capture
PAGES_TO_CAPTURE = [
    {
        'name': 'homepage-desktop',
        'url': PREVIEW_URL,
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Homepage desktop view - Search hero'
    },
    {
        'name': 'homepage-mobile',
        'url': PREVIEW_URL,
        'viewport': {'width': 375, 'height': 812},  # iPhone X
        'description': 'Homepage mobile view'
    },
    {
        'name': 'search-results-desktop',
        'url': f"{PREVIEW_URL}/search?q=flooring",
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Search results page - test search functionality'
    },
    {
        'name': 'search-results-mobile',
        'url': f"{PREVIEW_URL}/search?q=flooring",
        'viewport': {'width': 375, 'height': 812},
        'description': 'Search results mobile'
    },
    {
        'name': 'collection-page-desktop',
        'url': f"{PREVIEW_URL}/collections/all",
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Collection page with products'
    },
    {
        'name': 'collection-page-mobile',
        'url': f"{PREVIEW_URL}/collections/all",
        'viewport': {'width': 375, 'height': 812},
        'description': 'Collection page mobile'
    },
    {
        'name': 'product-page-desktop',
        'url': f"{PREVIEW_URL}/products/example-product",
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Product detail page'
    },
    {
        'name': 'product-page-mobile',
        'url': f"{PREVIEW_URL}/products/example-product",
        'viewport': {'width': 375, 'height': 812},
        'description': 'Product detail page mobile'
    },
    {
        'name': 'header-navigation',
        'url': PREVIEW_URL,
        'viewport': {'width': 1920, 'height': 1080},
        'clip': {'x': 0, 'y': 0, 'width': 1920, 'height': 200},
        'description': 'Header and navigation bar closeup'
    },
    {
        'name': 'footer-section',
        'url': PREVIEW_URL,
        'viewport': {'width': 1920, 'height': 1080},
        'scroll_to_bottom': True,
        'description': 'Footer section'
    }
]

def capture_screenshots(output_dir='screenshots'):
    """Capture all screenshots using Playwright"""
    
    # Ensure output directory exists
    screenshots_path = os.path.join('/Users/Frank/Documents/EMMSO NOV', output_dir)
    os.makedirs(screenshots_path, exist_ok=True)
    
    print("🚀 EMMSO Screenshot Capture Tool")
    print(f"📸 Capturing {len(PAGES_TO_CAPTURE)} screenshots...")
    print(f"📁 Output: {screenshots_path}\n")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        
        for i, page_config in enumerate(PAGES_TO_CAPTURE, 1):
            try:
                print(f"[{i}/{len(PAGES_TO_CAPTURE)}] 📸 {page_config['name']}")
                print(f"    URL: {page_config['url']}")
                print(f"    Viewport: {page_config['viewport']['width']}x{page_config['viewport']['height']}")
                
                # Create page with viewport
                page = browser.new_page(
                    viewport=page_config['viewport']
                )
                
                # Navigate to page
                page.goto(page_config['url'], wait_until='networkidle', timeout=30000)
                
                # Wait for content to load
                page.wait_for_timeout(2000)  # 2 second wait for animations
                
                # Scroll to bottom if needed (for footer)
                if page_config.get('scroll_to_bottom'):
                    page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                    page.wait_for_timeout(1000)
                
                # Take screenshot
                screenshot_path = os.path.join(screenshots_path, f"{page_config['name']}.png")
                
                if 'clip' in page_config:
                    # Partial screenshot (e.g., header only)
                    page.screenshot(path=screenshot_path, clip=page_config['clip'])
                else:
                    # Full page screenshot
                    page.screenshot(path=screenshot_path, full_page=True)
                
                print(f"    ✅ Saved to {page_config['name']}.png")
                
                page.close()
                
            except Exception as e:
                print(f"    ❌ Failed: {e}")
        
        browser.close()
    
    print(f"\n✅ Screenshot capture complete!")
    print(f"📁 {len(PAGES_TO_CAPTURE)} screenshots saved to: {screenshots_path}")
    print(f"\n🎯 Next steps:")
    print(f"   1. Review screenshots in {screenshots_path}")
    print(f"   2. Run: cd AI && python3 captain.py")
    print(f"   3. Vision AI will analyze all screenshots automatically")

def main():
    """Main entry point"""
    try:
        capture_screenshots()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Make sure Playwright is installed:")
        print("   pip install playwright")
        print("   playwright install chromium")
        sys.exit(1)

if __name__ == "__main__":
    main()
