#!/usr/bin/env python3
"""
Screenshot Capture Tool for EMMSO Theme
========================================
Automatically captures screenshots of all important pages for Vision AI analysis

IMMEDIATE CAPTURE LOGIC:
- Captures screenshots immediately when Captain runs
- No waiting for deployment
- Timestamps every capture with deployment folder + individual file timestamps
- Store screenshots in deployment-specific folders with timestamps
- Use symlink 'latest/' pointing to most recent deployment
"""
import os
import sys
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta

# Shopify preview URL
PREVIEW_URL = "https://jfnjr52c1q3uk18h-63663472878.shopifypreview.com"

# Pages to capture
PAGES_TO_CAPTURE = [
    {
        'name': 'homepage-desktop',
        'url': PREVIEW_URL,
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Homepage desktop view - Search hero + dark footer'
    },
    {
        'name': 'homepage-mobile',
        'url': PREVIEW_URL,
        'viewport': {'width': 390, 'height': 844},  # iPhone 12 Pro
        'description': 'Homepage mobile view'
    },
    {
        'name': 'collection-page-desktop',
        'url': f"{PREVIEW_URL}/collections/all",
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Collection page - Products with Add to Cart buttons'
    },
    {
        'name': 'collection-page-mobile',
        'url': f"{PREVIEW_URL}/collections/all",
        'viewport': {'width': 390, 'height': 844},
        'description': 'Collection page mobile - Add to Cart buttons visible'
    },
    {
        'name': 'product-page-desktop',
        'url': f"{PREVIEW_URL}/products/floorservice-color-hardwax-oil-classic",
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Product detail page - Full product view'
    },
    {
        'name': 'product-page-mobile',
        'url': f"{PREVIEW_URL}/products/floorservice-color-hardwax-oil-classic",
        'viewport': {'width': 390, 'height': 844},
        'description': 'Product detail page mobile'
    },
    {
        'name': 'cart-desktop',
        'url': f"{PREVIEW_URL}/cart",
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Shopping cart page - CRITICAL for e-commerce visibility'
    },
    {
        'name': 'cart-mobile',
        'url': f"{PREVIEW_URL}/cart",
        'viewport': {'width': 390, 'height': 844},
        'description': 'Shopping cart mobile - CRITICAL'
    },
    {
        'name': 'search-page-desktop',
        'url': f"{PREVIEW_URL}/search?q=Bathrooms",
        'viewport': {'width': 1920, 'height': 1080},
        'description': 'Search results page - Check for translation errors'
    },
    {
        'name': 'search-page-mobile',
        'url': f"{PREVIEW_URL}/search?q=Bathrooms",
        'viewport': {'width': 390, 'height': 844},
        'description': 'Search results mobile - Translation validation'
    },
    {
        'name': 'cart-drawer-open',
        'url': PREVIEW_URL,
        'viewport': {'width': 1920, 'height': 1080},
        'execute_js': "document.querySelector('[data-cart-drawer-toggle]')?.click() || document.querySelector('.cart-icon')?.click()",
        'wait_after_js': 800,  # Wait for drawer slide-in animation
        'description': 'Cart drawer AJAX overlay - Modern e-commerce UX'
    },
    {
        'name': 'header-navigation',
        'url': PREVIEW_URL,
        'viewport': {'width': 1920, 'height': 1080},
        'clip': {'x': 0, 'y': 0, 'width': 1920, 'height': 200},
        'description': 'Header with cart icon + predictive search'
    },
    {
        'name': 'footer-section',
        'url': PREVIEW_URL,
        'viewport': {'width': 2000, 'height': 1080},
        'scroll_to_bottom': True,
        'description': 'Dark footer with brand colors'
    }
]

def get_last_deployment_time():
    """Get timestamp of last git commit (deployment trigger)"""
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%ct'],
            cwd='/Users/Frank/Documents/EMMSO NOV',
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return int(result.stdout.strip())
        return None
    except Exception as e:
        print(f"⚠️  Could not get git commit time: {e}")
        return None

def get_latest_screenshot_deployment():
    """Get the most recent screenshot deployment folder"""
    screenshots_base = Path('/Users/Frank/Documents/EMMSO NOV/screenshots')
    if not screenshots_base.exists():
        return None
    
    deployment_folders = [
        d for d in screenshots_base.iterdir() 
        if d.is_dir() and d.name.startswith('deployment-')
    ]
    
    if not deployment_folders:
        return None
    
    # Sort by timestamp in folder name
    deployment_folders.sort(key=lambda x: x.name, reverse=True)
    return deployment_folders[0]

def should_capture_new_screenshots():
    """
    ALWAYS captures new screenshots - no deployment wait time.
    
    Returns: (should_capture, deployment_timestamp)
    - should_capture: Always True
    - deployment_timestamp: Timestamp to use for folder name
    """
    last_commit_time = get_last_deployment_time()
    
    if not last_commit_time:
        print("⚠️  No git commit found - will capture new screenshots")
        return True, int(datetime.now().timestamp())
    
    commit_datetime = datetime.fromtimestamp(last_commit_time)
    minutes_since_commit = (datetime.now() - commit_datetime).total_seconds() / 60
    
    print(f"📅 Last deployment: {commit_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️  Time since deployment: {minutes_since_commit:.1f} minutes")
    print(f"📸 Capturing NEW screenshots immediately (no wait time)")
    
    return True, last_commit_time

def capture_screenshots(output_dir='screenshots'):
    """
    Capture screenshots immediately - no deployment wait.
    Always captures fresh screenshots when Captain runs.
    """
    
    print("🚀 EMMSO Screenshot Capture Tool")
    print("=" * 60)
    
    # Check if we need new screenshots
    should_capture, deployment_info = should_capture_new_screenshots()
    
    if not should_capture:
        print(f"\n⏸️  Screenshot capture cancelled")
        return None
    
    # Create deployment-specific folder with timestamp
    deployment_timestamp = deployment_info if isinstance(deployment_info, int) else int(datetime.now().timestamp())
    deployment_datetime = datetime.fromtimestamp(deployment_timestamp)
    
    screenshots_base = Path('/Users/Frank/Documents/EMMSO NOV') / output_dir
    
    # Folder name: deployment-YYYYMMDD-HHMMSS-timestamp
    folder_name = f"deployment-{deployment_datetime.strftime('%Y%m%d-%H%M%S')}-{deployment_timestamp}"
    deployment_folder = screenshots_base / folder_name
    
    deployment_folder.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📁 Output folder: {deployment_folder.name}")
    print(f"📅 Timestamp: {deployment_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📸 Capturing {len(PAGES_TO_CAPTURE)} screenshots...")
    print("=" * 60 + "\n")
    
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
                
                # Execute custom JavaScript if provided (e.g., open cart drawer)
                if 'execute_js' in page_config:
                    page.evaluate(page_config['execute_js'])
                    wait_time = page_config.get('wait_after_js', 500)
                    page.wait_for_timeout(wait_time)
                
                # Scroll to bottom if needed (for footer)
                if page_config.get('scroll_to_bottom'):
                    page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                    page.wait_for_timeout(1000)
                
                # Take screenshot with timestamp in filename
                timestamp_suffix = datetime.now().strftime('%H%M%S')
                screenshot_filename = f"{page_config['name']}-{timestamp_suffix}.png"
                screenshot_path = deployment_folder / screenshot_filename
                
                if 'clip' in page_config:
                    # Partial screenshot (e.g., header only)
                    page.screenshot(path=str(screenshot_path), clip=page_config['clip'])
                else:
                    # Full page screenshot
                    page.screenshot(path=str(screenshot_path), full_page=True)
                
                print(f"    ✅ Saved to {screenshot_filename}")
                
                page.close()
                
            except Exception as e:
                print(f"    ❌ Failed: {e}")
        
        browser.close()
    
    # Create/update 'latest' symlink
    latest_link = screenshots_base / 'latest'
    if latest_link.exists() or latest_link.is_symlink():
        latest_link.unlink()
    
    latest_link.symlink_to(deployment_folder.name, target_is_directory=True)
    
    print(f"\n✅ Screenshot capture complete!")
    print(f"📁 {len(PAGES_TO_CAPTURE)} screenshots saved to: {deployment_folder.name}")
    print(f"🔗 Symlink updated: screenshots/latest -> {deployment_folder.name}")
    print(f"\n🎯 Next steps:")
    print(f"   1. Review screenshots in screenshots/{deployment_folder.name}")
    print(f"   2. Run: cd AI && python3 captain.py")
    print(f"   3. Vision AI will analyze screenshots from latest deployment")
    
    return str(deployment_folder)

def main():
    """Main entry point"""
    try:
        result = capture_screenshots()
        if result:
            print(f"\n✅ Screenshots ready for Vision AI analysis")
            return str(result)
        else:
            print(f"\n⏸️  No new screenshots needed")
            return None
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Make sure Playwright is installed:")
        print("   pip install playwright")
        print("   playwright install chromium")
        sys.exit(1)

if __name__ == "__main__":
    main()
