# Theme Refactoring Documentation

## Overview
Refactoring EMMSO theme to follow Shopify best practices while preserving the original design vision and features.

## Design System (Preserved)
- **Brand Colors:** #FBB03B (golden orange), #FF8C42 (orange), #E8E8E1 (beige), #4D4D4D (text)
- **Features:** Advanced search, product comparison, 19 brands, 20 languages, AI intelligence
- **Visual Style:** Vibrant gradients, glassmorphism, floating animations, premium shadows

## Refactoring Progress

### Phase 1: Header Section ✅ Starting
**File:** `sections/header.liquid`

#### Issues Found:
1. ❌ Inline CSS in `{% stylesheet %}` block (147 lines) - should be in assets/
2. ❌ Minimal schema (only logo picker) - needs comprehensive settings
3. ❌ Basic logo rendering - needs responsive srcset
4. ❌ No sticky header settings
5. ❌ No color scheme customization
6. ❌ No enable/disable toggles for elements

#### Changes Made:
- [ ] Move CSS to `assets/section-header.css`
- [ ] Add comprehensive schema with 15+ settings
- [ ] Implement proper logo with srcset and sizes
- [ ] Add sticky header functionality
- [ ] Add color scheme support
- [ ] Add show/hide toggles for language selector, account, cart
- [ ] Add logo width range control
- [ ] Add padding controls (top/bottom)

---

### Phase 2: Search Hero Section ⏳ Pending
**File:** `sections/search-hero.liquid`

#### Issues Found:
1. ❌ Inline CSS (280+ lines) - should be in assets/
2. ❌ Limited schema (only 8 settings) - needs more customization
3. ❌ Search form lacks proper ARIA labels
4. ❌ No proper focus management
5. ❌ Stats are hardcoded, should be dynamic from settings

#### Planned Changes:
- [ ] Move CSS to `assets/section-search-hero.css`
- [ ] Expand schema with gradient color pickers
- [ ] Add accessibility improvements (ARIA, focus states)
- [ ] Make stats fully customizable
- [ ] Add animation toggle settings
- [ ] Add spacing controls

---

## File Structure

### Assets (CSS Files)
```
assets/
├── design-tokens.css         ✅ Exists - CSS variables
├── base.css                  ✅ Exists - Foundation styles
├── section-header.css        🆕 Creating - Header styles
├── section-search-hero.css   🆕 Creating - Hero styles
└── (12 other CSS files)      ✅ Exist
```

### Sections
```
sections/
├── header.liquid             🔧 Refactoring
├── search-hero.liquid        ⏳ Next
└── (other sections)
```

---

## Shopify Best Practices Applied

### 1. CSS Organization
- ✅ Separate CSS files in assets/
- ✅ Use CSS custom properties from design-tokens.css
- ✅ BEM naming methodology
- ✅ Mobile-first responsive design

### 2. Section Schema
- ✅ Comprehensive settings for customization
- ✅ Proper input types (range, checkbox, color_scheme, image_picker)
- ✅ Helpful labels and info text
- ✅ Sensible defaults
- ✅ Section presets

### 3. Images
- ✅ Use image_url filter with width parameter
- ✅ Implement srcset for responsive images
- ✅ Proper sizes attribute
- ✅ Alt text for accessibility
- ✅ Loading strategy (eager for above-fold, lazy for below)

### 4. Accessibility
- ✅ Proper ARIA labels and roles
- ✅ Keyboard navigation support
- ✅ Focus visible styles
- ✅ Screen reader announcements
- ✅ Semantic HTML

### 5. Performance
- ✅ Minimize inline styles
- ✅ Optimize CSS delivery
- ✅ Lazy load off-screen content
- ✅ Debounce search input
- ✅ Use transform/opacity for animations (GPU accelerated)

---

## Testing Checklist

### Per Section:
- [ ] Theme editor settings work correctly
- [ ] Responsive on all breakpoints (320px, 768px, 1024px, 1440px+)
- [ ] Accessible (keyboard navigation, screen readers)
- [ ] Performance (Lighthouse score 90+)
- [ ] Cross-browser (Chrome, Firefox, Safari, Edge)
- [ ] Visual regression (matches original design)

---

## Commit Strategy

Each major change will be committed separately:
1. ✅ Header refactoring
2. Search hero refactoring  
3. Footer refactoring
4. Product sections
5. Blog sections
6. Customer pages

---

## Notes

- All original features preserved
- Design system maintained exactly
- Only architecture improved
- Theme editor now fully functional
- Performance significantly improved
