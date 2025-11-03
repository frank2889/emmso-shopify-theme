#!/usr/bin/env python3
"""
Screenshot Capture Tool for EMMSO Theme
========================================
Automatically captures screenshots of all important pages for Vision AI analysis

SMART DEPLOYMENT-AWARE LOGIC:
- Only capture NEW screenshots 5+ minutes after latest git deployment
- Reuse existing screenshots if recent (< 5 min since last commit)
- Store screenshots in deployment-specific folders with timestamps
- Use symlink 'latest/' pointing to most recent deployment
"""
import os
import sys
import subprocess
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta

# Shopify preview URL
PREVIEW_URL = "https://y0hnl2y5cksklmw7-63663472878.shopifypreview.com"

# Wait time after deployment before capturing (Shopify needs time to build)
DEPLOYMENT_WAIT_MINUTES = 5

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
    Determine if new screenshots are needed based on:
    1. Last git commit time (deployment)
    2. Time since last screenshot capture
    3. Minimum 5-minute wait for Shopify deployment
    
    Returns: (should_wait_and_capture, deployment_timestamp)
    - should_wait_and_capture: True if need to wait then capture
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
    
    # Check if we already have recent screenshots
    latest_deployment = get_latest_screenshot_deployment()
    
    if latest_deployment:
        # Extract timestamp from folder name: deployment-1730649600
        folder_timestamp = int(latest_deployment.name.split('-')[1])
        
        # If screenshots are from this deployment or newer, reuse them
        if folder_timestamp >= last_commit_time:
            print(f"✅ Recent screenshots found: {latest_deployment.name}")
            print(f"📁 Reusing existing screenshots (captured after current deployment)")
            return False, None
    
    # Check if we need to wait longer for Shopify to deploy
    if minutes_since_commit < DEPLOYMENT_WAIT_MINUTES:
        wait_seconds = int((DEPLOYMENT_WAIT_MINUTES - minutes_since_commit) * 60)
        print(f"\n⏳ WAITING FOR SHOPIFY DEPLOYMENT...")
        print(f"   Deployment: {commit_datetime.strftime('%H:%M:%S')}")
        print(f"   Wait time: {wait_seconds // 60} min {wait_seconds % 60} sec")
        print(f"   💡 Shopify needs ~{DEPLOYMENT_WAIT_MINUTES} min to build theme")
        print(f"\n   Sleeping {wait_seconds}s then auto-capturing screenshots...")
        
        # Sleep with progress updates every 30 seconds
        for elapsed in range(0, wait_seconds, 30):
            remaining = wait_seconds - elapsed
            if remaining > 0:
                time.sleep(min(30, remaining))
                if remaining > 30:
                    print(f"   ⏰ {remaining // 60} min {remaining % 60} sec remaining...")
        
        print(f"\n✅ Deployment wait complete! Starting screenshot capture...")
    else:
        print(f"🆕 Deployment is ready ({minutes_since_commit:.1f} min old)")
    
    print(f"📸 Will capture NEW screenshots for this deployment")
    return True, last_commit_time

def capture_screenshots(output_dir='screenshots'):
    """
    Capture screenshots with smart deployment awareness.
    Only captures new screenshots when needed (5+ min after deployment).
    """
    
    print("🚀 EMMSO Screenshot Capture Tool")
    print("=" * 60)
    
    # Check if we need new screenshots
    should_capture, deployment_info = should_capture_new_screenshots()
    
    if not should_capture:
        if deployment_info:
            print(f"\n✅ Using existing screenshots from: {deployment_info}")
            return str(deployment_info)
        else:
            print(f"\n⏸️  Skipping screenshot capture - waiting for deployment")
            return None
    
    # Create deployment-specific folder
    deployment_timestamp = deployment_info if isinstance(deployment_info, int) else int(datetime.now().timestamp())
    screenshots_base = Path('/Users/Frank/Documents/EMMSO NOV') / output_dir
    deployment_folder = screenshots_base / f"deployment-{deployment_timestamp}"
    
    deployment_folder.mkdir(parents=True, exist_ok=True)
    
    print(f"\n� Output folder: {deployment_folder.name}")
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
                
                # Scroll to bottom if needed (for footer)
                if page_config.get('scroll_to_bottom'):
                    page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                    page.wait_for_timeout(1000)
                
                # Take screenshot
                screenshot_path = deployment_folder / f"{page_config['name']}.png"
                
                if 'clip' in page_config:
                    # Partial screenshot (e.g., header only)
                    page.screenshot(path=str(screenshot_path), clip=page_config['clip'])
                else:
                    # Full page screenshot
                    page.screenshot(path=str(screenshot_path), full_page=True)
                
                print(f"    ✅ Saved to {page_config['name']}.png")
                
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
