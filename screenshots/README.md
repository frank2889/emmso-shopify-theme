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

---

## 📋 RECOMMENDED ADDITIONAL SCREENSHOTS

### 🔴 HIGH PRIORITY (Next Analysis Cycle)

| Screenshot | Suggested URL | Purpose | Business Impact |
|-----------|---------------|---------|-----------------|
| `cart-desktop.png` | `https://emmso.eu/en/cart` | Shopping cart page | **CRITICAL** - Checkout flow, conversion optimization |
| `cart-mobile.png` | `https://emmso.eu/en/cart` | Mobile cart | **CRITICAL** - Mobile revenue 40%→65% goal |
| `blog-article-desktop.png` | `https://emmso.eu/en/blogs/news/[article]` | Blog post layout | **HIGH** - Content marketing, SEO, bounce rate |
| `404-error-desktop.png` | `https://emmso.eu/en/404` | Error page | **HIGH** - User retention, professional UX |
| `search-no-results-desktop.png` | `https://emmso.eu/en/search?q=xyz123notfound` | No results state | **HIGH** - Search-first vision, fallback UX |

**Expected Impact:**
- Cart analysis: Identifies friction in checkout flow (conversion 3.5%→6%)
- Blog: Content SEO optimization
- 404: Professional error handling reduces bounce rate
- No results: Search experience completeness (25%→75% usage goal)

### 🟡 MEDIUM PRIORITY (Enhanced Coverage)

| Screenshot | Suggested URL | Purpose | Business Impact |
|-----------|---------------|---------|-----------------|
| `mobile-nav-expanded.png` | `https://emmso.eu/en/` (tap menu) | Mobile navigation open | **MEDIUM** - Mobile UX, navigation accessibility |
| `collection-filters-active.png` | `https://emmso.eu/en/collections/all?filter.p.vendor=Brand` | Active filters | **MEDIUM** - Filter UX, search experience |
| `product-comparison.png` | `https://emmso.eu/en/pages/compare` | Comparison feature | **MEDIUM** - Product comparison UX |
| `account-login.png` | `https://emmso.eu/en/account/login` | Login page | **MEDIUM** - Customer account experience |

### 🟢 NICE TO HAVE (Edge Cases)

| Screenshot | Suggested URL | Purpose | Business Impact |
|-----------|---------------|---------|-----------------|
| `product-out-of-stock.png` | Find out-of-stock product | Inventory messaging | **LOW** - Edge case handling |
| `search-voice-active.png` | `https://emmso.eu/en/` (activate voice) | Voice search UI | **LOW** - Future feature validation |
| `loading-state.png` | Slow connection simulation | Loading indicators | **LOW** - Performance perception |

---

## 🎯 IMPLEMENTATION PLAN

### Phase 1 - Next Analysis (November 10, 2025)
Add these 5 screenshots before running Captain:
1. ✅ `cart-desktop.png`
2. ✅ `cart-mobile.png`
3. ✅ `blog-article-desktop.png`
4. ✅ `404-error-desktop.png`
5. ✅ `search-no-results-desktop.png`

**Why:** These cover critical user flows (cart, content, errors) that directly impact business metrics.

### Phase 2 - After Major Features
Add mobile navigation and filters when implementing navigation improvements.

### Phase 3 - Complete Coverage
Add edge cases once core experience is optimized.

---

## 📊 COVERAGE METRICS

**Current:** 10 screenshots covering 6 core page types
**Target:** 15-20 screenshots covering all user flows
**Priority Focus:** Checkout flow (cart) + Content (blog) + Error handling (404/no-results)

