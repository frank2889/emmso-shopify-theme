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

_(Add screenshots after each deployment)_
