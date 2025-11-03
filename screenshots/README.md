# 📸 EMMSO Theme Screenshots

This folder contains screenshots for Vision AI analysis.

## Purpose

The Vision AI analyst analyzes these screenshots after each deployment to evaluate:
- Visual hierarchy and design quality
- Search-first interface implementation
- Mobile-first/responsive design
- Brutalist simplicity principles
- Accessibility (contrast, readability)
- Brand consistency

## Screenshot Naming Convention

Use descriptive names that indicate what's shown:

- `homepage-desktop.png` - Desktop homepage view
- `homepage-mobile.png` - Mobile homepage view
- `search-hero-desktop.png` - Search hero section
- `search-results-desktop.png` - Search results page
- `product-page-desktop.png` - Product detail page
- `collection-page-desktop.png` - Collection page
- `cart-drawer.png` - Shopping cart drawer
- `header-navigation.png` - Header and navigation
- `footer-section.png` - Footer section

## How to Add Screenshots

1. **Automated** (Recommended):
   - Use Shopify's theme preview screenshots
   - Or use browser dev tools to capture full page
   
2. **Manual**:
   - Take screenshots of live theme at https://vloerproducten.myshopify.com/?preview_theme_id=main
   - Save to this folder with descriptive names
   - Supported formats: PNG, JPG, WEBP

## Analysis Flow

```
Git Push → Shopify Deploy → Take Screenshots → Vision AI Analysis → Recommendations
```

Vision AI will automatically analyze all images in this folder on each captain.py run.

## Tips for Good Screenshots

- ✅ Full viewport (1920x1080 for desktop, 375x667 for mobile)
- ✅ Actual content loaded (not placeholder/lorem ipsum)
- ✅ Realistic user state (with items in cart, search query entered, etc.)
- ✅ Light and dark mode if applicable
- ❌ Don't crop - show full pages
- ❌ Don't include browser UI (unless testing for something specific)

## Current Screenshots

**Last Updated:** November 3, 2025

### Desktop Screenshots (1920x1080+)

| Screenshot | URL Used | Purpose |
|-----------|----------|---------|
| `homepage-desktop.png` | `https://emmso.eu/en/` | Homepage with search hero |
| `search-results-desktop.png` | `https://emmso.eu/en/search?q=Floors` | Search results page |
| `product-page-desktop.png` | `https://emmso.eu/en/products/floorservice-color-hardwax-oil-classic` | Product detail page |
| `collection-page-desktop.png` | `https://emmso.eu/en/collections/all` | Collection/category page |
| `header-navigation.png` | `https://emmso.eu/en/` (cropped) | Header close-up |

### Mobile Screenshots (375-438px width)

| Screenshot | URL Used | Purpose |
|-----------|----------|---------|
| `homepage-mobile.png` | `https://emmso.eu/en/` | Mobile homepage |
| `search-results-mobile.png` | `https://emmso.eu/en/search?q=Floors` | Mobile search results |
| `product-page-mobile.png` | `https://emmso.eu/en/products/floorservice-color-hardwax-oil-classic` | Mobile product page |
| `collection-page-mobile.png` | `https://emmso.eu/en/collections/all` | Mobile collection |

### Component Screenshots

| Screenshot | URL Used | Purpose |
|-----------|----------|---------|
| `footer-section.png` | `https://emmso.eu/en/` (footer only) | Footer section detail |

### Screenshot Guidelines

**When to Update:**
- After implementing major UI changes
- Before running Captain analysis
- After deploying to production
- Weekly during active development

**How to Capture:**
1. Open URL in browser (Chrome recommended)
2. Desktop: Set viewport to 1920x1080
3. Mobile: Use DevTools device emulation (iPhone 12 Pro, 390x844)
4. Wait for full page load (all images, fonts)
5. Take full-page screenshot (Chrome: Cmd+Shift+P → "Capture full size screenshot")
6. Save to this folder with correct filename

**Quality Requirements:**
- ✅ Full viewport - no cropping
- ✅ Real content - no placeholders
- ✅ All assets loaded - no broken images
- ✅ Realistic state - search query entered, products visible
- ❌ No browser UI (address bar, bookmarks)
- ❌ No dev tools visible
- ❌ No overlays or popups (unless testing that feature)
