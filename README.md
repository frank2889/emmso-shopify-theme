<h1 align="center" style="position: relative;">
  <br>
    <img src="./assets/shoppy-x-ray.svg" alt="logo" width="200">
  <br>
  EMMSO Custom Shopify Theme
</h1>

Custom Shopify theme for EMMSO - A pan-European flooring and pet products specialist. Built from scratch using Shopify's modern theme architecture with multi-language support and optimized for B2B/B2C commerce.

<p align="center">
  <a href="./LICENSE.md"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <a href="https://github.com/frank2889/emmso-shopify-theme"><img src="https://img.shields.io/badge/GitHub-Repository-blue.svg" alt="GitHub"></a>
</p>

## 📊 Business Overview

### 🏢 Company Information
**EMMSO** - Floor Products & Pet Supplies Specialist  
**Store URL:** vloerproducten.myshopify.com  
**GSC Account:** emmso-461@positive-karma-475015-h7.iam.gserviceaccount.com

### 🌍 Markets & Languages

**Active Markets:**
- 🇳🇱 **Netherlands (NL)** - Primary Market
- ��🇪 **Belgium** - Dutch (NL) & French (FR)
- 🇩🇪 **Germany (DE)**
- 🇦🇹 **Austria (AT)** - German (DE)
- 🇫🇷 **France (FR)**
- 🇪🇸 **Spain (ES)**
- 🇮🇹 **Italy (IT)**
- 🇵🇹 **Portugal (PT)**
- 🇩🇰 **Denmark (DA)**
- 🇮🇪 **Ireland (IE)** - English (EN)

**Total Markets:** 10 European countries

**Multi-Language Strategy:**
- **Powered by:** Translate & Adapt app (Shopify)
- **Unlimited Languages & Nuances:** Can create regional variations (e.g., BE-NL vs NL-NL, BE-FR vs FR-FR)
- **Current Active Languages:** 8 base languages (expandable on demand)
- **Auto-detection:** Via URL path structure (`/en/`, `/de/`, `/nl-be/`, etc.)
- **SEO-Optimized:** Each language version fully indexed separately

**Base Languages:**
- Dutch (NL) - Netherlands, Belgium
- English (EN) - Ireland, UK, International
- German (DE) - Austria, Germany
- French (FR) - France, Belgium
- Spanish (ES) - Spain
- Italian (IT) - Italy
- Portuguese (PT) - Portugal
- Danish (DA) - Denmark

**Future Expansion Potential:**
- Regional variations (Swiss German, Austrian German, Belgian Dutch)
- Additional markets (Sweden, Norway, Finland, Poland)
- Dialect-specific content per market
- B2B vs B2C language nuances

**Market-Language Matrix:**
- **Austria:** German (DE)
- **Belgium:** Dutch (NL), French (FR), German (DE)
- **Denmark:** Danish (DA)
- **France:** French (FR)
- **Germany:** German (DE)
- **Ireland:** English (EN)
- **Italy:** Italian (IT)
- **Netherlands:** Dutch (NL)
- **Portugal:** Portuguese (PT)
- **Spain:** Spanish (ES)

---

## 🔧 Technology Stack

### Shopify Apps
1. **Translate & Adapt** - Multi-language content management with unlimited language support
2. **Instaindex** - Instant Google indexing for new products and content
3. **Wuunder Shipping** - Smart European shipping integration

### Core Policies
- ❌ **No Free Shipping** - Transparent shipping costs
- ❌ **No Discounts** - Value-based pricing strategy
- ✅ **Smart Shopping** - Intelligent product recommendations and search

### Brand Assets
- Logo: `emmso-logo-homepage.webp` (color version)
- Logo Inverted: `emmso-logo-invert.webp` (for dark backgrounds)
- Trust Marks: 5 certification badges (Trusted Shops, Thuiswinkel, WebwinkelKeur, etc.)

---

## 🔍 Search-First Architecture

### Core Concept
**Homepage = Search Engine**: Ultra-fast, predictive search as the primary navigation method. Users find products in seconds, not clicks.

### Search Performance Targets
- **First Input Delay:** < 100ms
- **Search Response Time:** < 200ms
- **Results Display:** < 300ms
- **Total Time to Interactive:** < 2s

### Search Features

#### **1. Instant Predictive Search**
- **Real-time autocomplete** as user types (debounced at 150ms)
- **Product suggestions** with thumbnails, prices, availability
- **Category suggestions** based on query intent
- **Search history** (last 5 searches, localStorage)
- **Trending searches** for empty state
- **Voice search** support (Web Speech API)

#### **2. Advanced Filtering (Search Results Page)**
- **Faceted search:** Category, Brand, Price, Color, Material, Size
- **Dynamic filters:** Only show relevant filters based on results
- **Multi-select:** Combine multiple filters (AND/OR logic)
- **Price range slider:** Min/Max with histogram
- **Instant filter updates:** No page reload, URL updates for sharing
- **Active filter chips:** Easy removal of applied filters

#### **3. Smart Search Algorithm**
- **Fuzzy matching:** Handle typos and misspellings
- **Synonym support:** "laminate" = "laminaat" = "laminat"
- **Multi-language:** Search across all 8 languages
- **Product field search:** Title, Description, SKU, Brand, Tags, Metafields
- **Weighted relevance:** Title (100%), Tags (80%), Description (60%)
- **Boost logic:** New products, sale items, high stock priority

#### **4. Search Result Optimization**
- **Infinite scroll** OR **Load More** button (A/B test)
- **Grid/List view toggle**
- **Sort options:** Relevance, Price (Low-High), Price (High-Low), Newest, Best Selling
- **Quick view modal:** Product details without page navigation
- **Add to cart** directly from results
- **Result count** and query display ("147 results for 'oak laminate'")

#### **5. Zero-Results Handling**
- **Suggestions:** "Did you mean...?" based on Levenshtein distance
- **Alternative products:** Show similar categories
- **Popular products:** Fallback to trending items
- **Search tips:** Help users refine their query
- **Contact support:** CTA for specific product requests

---

## 💡 Search-Based Store Innovations

### 1. **AI-Powered Search Intent Recognition**
- Detect user intent: "how to clean marble" → Show products + How-To content
- Question-based search: "what floor for kitchen?" → Guided recommendations
- Problem-solving: "remove stains from wood" → Care products + tutorials
- Natural language: "cheap vinyl that looks like oak" → Filtered results

### 2. **Visual Search & Image Upload**
- **Upload floor photo:** Match products by color, texture, pattern
- **Room visualization:** AR preview of flooring in user's space
- **Style matching:** Find similar products to uploaded inspiration images
- **Color extraction:** Search by dominant colors in uploaded photos

### 3. **Smart Filters & Faceted Search**
- **Dynamic filters:** Only show relevant options (if no red products, hide red filter)
- **Multi-attribute search:** "waterproof vinyl under €30/m²"
- **Room-based filtering:** Kitchen, Bathroom, Living Room (auto-filter compatible products)
- **Usage filters:** Pet-friendly, High-traffic, Underfloor heating compatible
- **Installation complexity:** DIY-friendly vs Professional installation

### 4. **Contextual Search Results**
- **Weather-aware:** Promote fast-drying products on rainy days
- **Seasonal:** Winter = underfloor heating compatible, Summer = outdoor products
- **Geographic:** Show products available in user's shipping region first
- **Time-sensitive:** "need it tomorrow" → In-stock + fast shipping filter

### 5. **Search-Driven Product Discovery**
- **Autocomplete with product previews:** Show thumbnail + price as user types
- **Related searches:** "People also searched for..." horizontal scroll
- **Search history timeline:** "You searched for vinyl 3 days ago - prices dropped!"
- **Saved searches:** Get alerts when matching products added/on sale
- **Search trends dashboard:** "Trending in Belgium this week: Oak laminate"

### 6. **Comparison & Decision Tools**
- **Side-by-side comparison:** Select products from search results to compare specs
- **Pros/Cons generator:** AI-generated based on use case
- **Compatibility checker:** "Works with Bona cleaner?" instant answers
- **Calculator integration:** m² calculator directly in search results
- **ROI estimator:** Durability vs price over 10 years

### 7. **Expert Search Modes**
- **Professional Mode:** B2B pricing, bulk quantities, project management tools
- **DIY Mode:** Beginner-friendly, installation guides included
- **Quick Reorder:** Scan barcode or enter SKU for instant reorder
- **Brand-specific search:** Deep dive into single brand catalog

### 8. **Search Performance Features**
- **Instant filters:** Apply filters without page reload (AJAX)
- **Infinite scroll:** Lazy load results as user scrolls
- **Search preview cache:** Preload next 24 results in background
- **Offline search:** Service Worker cache for previously searched terms
- **Voice search expansion:** "Show me all Bona products under €50"

### 9. **Social Proof in Search**
- **Review snippets:** Star rating + review count in search results
- **"Most purchased":** Badge for popular items in search results
- **"Verified compatible":** Show verified product combinations
- **User photos:** Real customer images in search previews
- **Pro recommendations:** "Preferred by 87% of installers"

### 10. **Smart Shopping Features (No Discounts Strategy)**
- **Value indicators:** "Best value per m²" badges
- **Bundle suggestions:** "Complete your floor care kit" in search
- **Stock urgency:** "Only 3 in stock" (transparent, not fake scarcity)
- **Shipping cost preview:** Show total cost including Wuunder shipping
- **Coverage calculator:** "Covers X m² for €Y" in search results
- **Quality indicators:** Premium/Professional/Budget tier badges

### 11. **Content-Integrated Search**
- **Mixed results:** Products + Blog posts + How-To videos + FAQs
- **Learning center:** Search triggers educational content
- **Video tutorials:** Embedded in search results for relevant queries
- **Case studies:** "See this product in action" customer projects
- **Expert advice:** Live chat trigger for complex searches

### 12. **Multi-Language Search Intelligence**
- **Cross-language search:** Search in English, find Dutch product names
- **Local terminology:** "parket" (NL) = "parquet" (EN) = "parkett" (DE)
- **Brand name normalization:** Different spellings across markets
- **Unit conversion:** Display m² in UK, ft² for international
- **Regional product variations:** Same product, localized names

### Implementation Priority (Search-First Focus)
**Phase 1 - Core Search (Weeks 1-2):**
- ✅ Instant predictive search with Shopify API
- ✅ Visual design with brand colors
- ✅ Performance optimization (< 200ms response)
- ⬜ Smart filters (category, brand, price, specs)
- ⬜ Infinite scroll results page

**Phase 2 - Intelligence (Weeks 3-4):**
- ⬜ Search intent recognition
- ⬜ Natural language processing
- ⬜ Fuzzy matching & spell correction
- ⬜ Multi-language search normalization
- ⬜ Search analytics dashboard

**Phase 3 - Advanced Features (Weeks 5-6):**
- ⬜ Visual search (image upload)
- ⬜ Comparison tools
- ⬜ Smart recommendations
- ⬜ Voice search refinement
- ⬜ Saved searches & alerts

**Phase 4 - Optimization (Weeks 7-8):**
- ⬜ A/B testing search layouts
- ⬜ Conversion funnel optimization
- ⬜ Performance monitoring
- ⬜ Search-to-purchase analytics
- ⬜ User behavior heatmaps

---

## 🎨 Brand & Design System

### Color Palette

**Primary Brand Colors:**
- **Brand Orange:** `#FBB03B` - Primary CTA, Accents, Active states
- **Dark Gray:** `#4D4D4D` - Text, Headers, Footer
- **Light Gray:** `#E8E8E1` - Backgrounds, Borders, Subtle sections
- **White:** `#FFFFFF` - Primary background, Cards, Clean areas

**Color Usage Rules (CRO Optimized):**

#### **Conversion-Focused Elements:**
1. **Primary CTA Buttons** 
   - Background: `#FBB03B` (Orange)
   - Text: `#FFFFFF` (White)
   - Hover: Darken by 10% (`#E29F2A`)
   - Use for: Add to Cart, Checkout, Buy Now, Subscribe

2. **Secondary CTA Buttons**
   - Background: `#4D4D4D` (Dark Gray)
   - Text: `#FFFFFF` (White)
   - Hover: Lighten by 10% (`#666666`)
   - Use for: View Product, Learn More, Contact

3. **Urgency/Scarcity Indicators**
   - Use Orange `#FBB03B` for low stock warnings
   - Subtle background: `#FBB03B` at 10% opacity
   - Bold text: `#4D4D4D`

#### **Trust & Readability:**
4. **Body Text**
   - Primary: `#4D4D4D` (Dark Gray)
   - Secondary: `#4D4D4D` at 70% opacity
   - Always ensure 4.5:1 contrast ratio minimum

5. **Headings**
   - H1-H2: `#4D4D4D` (Dark Gray)
   - H3-H6: `#4D4D4D` at 90% opacity

6. **Backgrounds**
   - Primary: `#FFFFFF` (White)
   - Alternate sections: `#E8E8E1` (Light Gray)
   - Cards/Panels: `#FFFFFF` with subtle shadow

#### **Interactive Elements:**
7. **Links**
   - Default: `#FBB03B` (Orange)
   - Hover: `#4D4D4D` (Dark Gray)
   - Visited: `#FBB03B` at 80% opacity
   - Underline on hover for accessibility

8. **Form Elements**
   - Border: `#E8E8E1` (Light Gray)
   - Focus: `#FBB03B` (Orange) 2px border
   - Error: `#D32F2F` (Red - outside palette for errors)
   - Success: `#388E3C` (Green - outside palette for success)

9. **Navigation**
   - Background: `#FFFFFF` (White)
   - Active/Hover: `#FBB03B` (Orange) underline or background tint
   - Text: `#4D4D4D` (Dark Gray)

#### **E-commerce Specific:**
10. **Product Cards**
    - Background: `#FFFFFF` (White)
    - Border: `#E8E8E1` (Light Gray) 1px
    - Hover: Lift with shadow, Orange accent line
    - Price: `#4D4D4D` (Dark Gray) - Bold
    - Sale Price: `#FBB03B` (Orange) - Bold

11. **Badges & Labels**
    - Sale/Discount: `#FBB03B` background, white text
    - New: `#4D4D4D` background, white text
    - Out of Stock: `#E8E8E1` background, `#4D4D4D` text

12. **Icons**
    - Default: `#4D4D4D` (Dark Gray)
    - Active/Selected: `#FBB03B` (Orange)
    - Cart counter: `#FBB03B` background, white text

### Accessibility Standards
- **WCAG 2.1 AA Compliance** minimum
- Orange `#FBB03B` on white = 3.9:1 (Use for large text 18px+ only)
- Dark Gray `#4D4D4D` on white = 9.7:1 (Excellent for all text)
- Never use Light Gray `#E8E8E1` for text on white
- Provide focus indicators (2px Orange outline)

### Design Principles
1. **High Contrast:** Use Dark Gray for maximum readability
2. **Orange Sparingly:** Reserve for CTAs and key interactions
3. **White Space:** Use generously for clean, professional look
4. **Consistency:** Maintain color roles across all 10 markets
5. **Trust:** Professional Dark Gray + Clean White = Reliability
6. **Energy:** Strategic Orange = Action & Conversion

---

## ⚡ Performance Architecture

### Speed Optimization Strategy
**Goal:** Fastest Shopify theme for search-based e-commerce in Europe.

#### **Critical Performance Metrics**
- **Lighthouse Score:** 95+ (Mobile & Desktop)
- **First Contentful Paint (FCP):** < 1.2s
- **Largest Contentful Paint (LCP):** < 2.5s
- **Time to Interactive (TTI):** < 2.0s
- **Cumulative Layout Shift (CLS):** < 0.1
- **First Input Delay (FID):** < 100ms

#### **1. Asset Optimization**
```liquid
{%- # Critical CSS inline in <head> -%}
{%- # Defer non-critical CSS -%}
{%- # Lazy load images with native loading="lazy" -%}
{%- # WebP images with fallback -%}
{%- # Minified JavaScript modules -%}
{%- # Preload hero images and fonts -%}
```

**Implementation:**
- **Inline critical CSS** (above-the-fold: search bar, header, hero)
- **Defer non-critical CSS** (footer, modals, drawers)
- **Code splitting:** Separate bundles for homepage, product, collection
- **Tree shaking:** Remove unused JavaScript
- **Gzip/Brotli compression** on all text assets

#### **2. Image Strategy**
- **Modern formats:** WebP primary, JPEG fallback
- **Responsive images:** `srcset` with 5 breakpoints (320, 640, 960, 1280, 1920)
- **Lazy loading:** Native `loading="lazy"` for below-fold images
- **Aspect ratio boxes:** Prevent layout shift
- **Blur placeholder:** Low-quality image placeholders (LQIP)
- **CDN delivery:** Shopify CDN with edge caching

#### **3. JavaScript Performance**
- **Vanilla JS first:** Avoid heavy frameworks
- **Async/Defer:** Non-blocking script loading
- **Event delegation:** Minimize event listeners
- **Debouncing:** Search input (150ms), scroll events (200ms)
- **Intersection Observer:** Lazy load images and components
- **Web Workers:** Offload search filtering to background thread

#### **4. Caching Strategy**
- **Browser caching:** Aggressive headers for static assets
- **Service Worker:** Offline support and asset caching
- **LocalStorage:** Search history, recently viewed products
- **SessionStorage:** Cart state, filter selections
- **CDN edge caching:** Shopify CDN for global delivery

#### **5. Database & API Optimization**
- **Shopify Ajax API:** Fast cart updates without reload
- **Predictive Search API:** Native Shopify search endpoint
- **Pagination:** Limit to 24-48 products per page
- **Lean queries:** Only fetch required fields
- **Prefetching:** Preload next page on scroll proximity

#### **6. Rendering Strategy**
- **Progressive enhancement:** Core functionality without JS
- **Skeleton screens:** Instant visual feedback during load
- **Optimistic UI:** Update UI before server confirmation
- **No render-blocking:** All CSS/JS non-blocking
- **Font display swap:** Prevent invisible text

---

### 🏭 Product Brands (19)

**Floor Care & Maintenance:**
1. **Lithofin** - Stone & tile care
2. **HMK** - Stone protection
3. **Lecol** - Adhesives
4. **Woca** - Wood care
5. **Bona** - Hardwood floor care
6. **Loba** - Wood floor systems
7. **FloorService** - Floor maintenance
8. **Blue Dolphin** - Cleaning products
9. **Dr. Schutz** - Floor care systems
10. **Blanchon** - Wood finishes

**Flooring Products:**
11. **Forbo** - Flooring solutions
12. **Mflor** - Luxury vinyl flooring
13. **Kerakoll** - Tile adhesives
14. **Bauwerk** - Parquet flooring
15. **StoneTech** - Stone care

**Pet Products:**
16. **Excellent Pets** - Pet supplies
17. **Elanco** - Pet health
18. **Milbemax** - Pet medications
19. **ProPad** - Pet products

### 📈 Business Model
- **B2B & B2C** Multi-market e-commerce
- **Multi-language** SEO optimization
- **Product feeds** for Google Shopping (8 languages)
- **Content marketing** via blogs in all languages
- **Pan-European** distribution

---

## 🔧 Technical Implementation

### 📦 Metafields Structure

EMMSO uses custom metafields for advanced functionality and SEO optimization:

#### **Product Metafields**
| Metafield | Type | Namespace | Purpose |
|-----------|------|-----------|---------|
| `wwk_rating_value` | Number | `custom` | Product rating (for Schema.org ratings) |
| `wwk_review_count` | Number | `custom` | Number of reviews (for Schema.org) |
| `faq` | List | `custom` | FAQ questions/answers for product pages |
| `tools` | Product Reference List | `custom` | Related tools/products for HowTo schema |
| `howto` | JSON/List | `custom` | Step-by-step usage instructions |

#### **Article/Blog Metafields**
| Metafield | Type | Namespace | Purpose |
|-----------|------|-----------|---------|
| `featured_products` | Product Reference | `custom` | Product featured in article (for Schema.org) |
| `related_posts` | List | `custom` | Related article handles for cross-linking |
| `parent_blog` | Text | `custom` | Parent blog handle for article relationships |
| `views` | Number | `custom` | Article view count for analytics |

#### **Collection Metafields**
| Metafield | Type | Namespace | Purpose |
|-----------|------|-----------|---------|
| `faq` | List | `custom` | FAQ for collection pages |
| `parent_collection` | Text | `custom` | Parent collection for blog article filtering |

#### **Video Metafields**
| Metafield | Type | Namespace | Purpose |
|-----------|------|-----------|---------|
| `video_file` | File | `custom` | Video file for VideoObject schema |
| `video_thumbnail` | Image | `custom` | Video thumbnail image |
| `video_title` | Text | `custom` | Video title for schema markup |

### 🎯 Schema.org Implementation

**Structured Data Types:**
- `Product` - Product pages with GTIN/SKU, ratings, prices
- `BlogPosting` - Article pages with author, dates, featured products
- `FAQPage` - Dynamic FAQ sections on products/collections/articles
- `HowTo` - Step-by-step product usage guides
- `VideoObject` - Embedded video content
- `BreadcrumbList` - Navigation breadcrumbs
- `Organization` - Company information
- `WebPage` - Page metadata
- `ItemList` - Collection articles, related products
- `Review` - Product reviews with ratings

**SEO Features:**
- Multi-language hreflang tags
- Dynamic meta descriptions from content
- Open Graph tags for social sharing
- Twitter Card meta tags
- Canonical URLs per market/language
- Structured data for rich snippets

### 🌐 Multi-Market Configuration

**URL Structure:**
```
vloerproducten.myshopify.com/
├── /nl/           # Dutch (Primary)
├── /en/           # English
├── /de/           # German
├── /fr/           # French
├── /es/           # Spanish
├── /it/           # Italian
├── /pt/           # Portuguese
└── /da/           # Danish
```

**SEO Per Market:**
- Language-specific sitemaps (`/nl/pages/sitemap-blogs-nl`)
- Google Shopping product feeds per language
- Localized blog content (19 brand blogs × 8 languages)
- Market-specific meta descriptions

### 📊 Analytics & Tracking

**Google Services:**
- **Service Account:** emmso-461@positive-karma-475015-h7.iam.gserviceaccount.com
- **Google Search Console:** Multi-market property
- **Google Analytics:** (Connected via Shopify admin)
- **Google Shopping Feeds:** 8 language-specific feeds

**Tracking Capabilities:**
- Multi-language page views
- E-commerce transactions per market
- Product performance by language
- Blog article views (via metafields)
- Cross-market conversion tracking

---

## 🚀 Getting started

### Prerequisites

Before starting, ensure you have the latest Shopify CLI installed:

- [Shopify CLI](https://shopify.dev/docs/api/shopify-cli) – helps you download, upload, preview themes, and streamline your workflows

If you use VS Code:

- [Shopify Liquid VS Code Extension](https://shopify.dev/docs/storefronts/themes/tools/shopify-liquid-vscode) – provides syntax highlighting, linting, inline documentation, and auto-completion specifically designed for Liquid templates

### Clone

Clone this repository:

```bash
git clone git@github.com:frank2889/emmso-shopify-theme.git
cd emmso-shopify-theme
```

### Connect to Shopify Store

Connect to your EMMSO Shopify store and start the development server:

```bash
shopify theme dev
```

This will:
- Open authentication in your browser
- Upload theme as development theme
- Start local server at `http://127.0.0.1:9292`
- Enable hot-reload for instant preview

### Push to Store

Push your theme to Shopify:

```bash
# Push as unpublished theme
shopify theme push --unpublished

# Or publish directly
shopify theme publish
```

---

## 🏗️ Theme architecture

```bash
.
├── assets/         # Static assets (CSS, JS, images, fonts, SVGs)
├── blocks/         # Reusable, nestable UI components (Horizon theme blocks)
├── config/         # Global theme settings and customization options
├── layout/         # Top-level wrappers (theme.liquid, password.liquid)
├── locales/        # Translation files (8 languages: NL, EN, DE, FR, ES, IT, PT, DA)
├── sections/       # Modular full-width page components
├── snippets/       # Reusable Liquid code fragments
└── templates/      # JSON templates combining sections for page structures
```

### Multi-Language Support

This theme supports **10 European markets** with **8 languages**:
- **Sitemaps** for each language (SEO optimization)
- **Product feeds** for Google Shopping integration
- **Blog content** for content marketing
- **Locale files** for UI translations

**Market-Language Mapping:**
- Netherlands, Belgium → Dutch (NL)
- Ireland, International → English (EN)
- Germany, Austria → German (DE)
- France, Belgium → French (FR)
- Spain → Spanish (ES)
- Italy → Italian (IT)
- Portugal → Portuguese (PT)
- Denmark → Danish (DA)

### Key Features

✅ **Modern Shopify 2.0 Architecture**
- JSON templates for merchant customization
- Modular sections and blocks
- Horizon theme compatibility
- Theme editor integration

✅ **Multi-Market Optimization**
- 10 markets across Europe (NL, BE, DE, AT, FR, ES, IT, PT, DK, IE)
- 8-language support (NL, EN, DE, FR, ES, IT, PT, DA)
- SEO-optimized sitemaps per market
- Google Shopping feeds per language
- Localized content and blogs

✅ **Performance Optimized**
- Critical CSS inlining
- CSS variables for theming
- Structured data (Schema.org)
- Lazy loading images

✅ **E-commerce Features**
- Product pages with variants
- Collection filtering
- Cart functionality
- Search integration
- Gift card support

---

## 📁 File Structure Details

### Templates
JSON templates combining sections to define page structures. This theme includes:
- `index.json` - Homepage
- `product.json` - Product pages
- `collection.json` - Collection pages
- `cart.json` - Shopping cart
- `404.json` - Error page
- Multi-language sitemaps (NL, EN, DE, FR, ES, IT, PT, DA)
- Multi-language product feeds for Google Shopping

### Sections
Modular, customizable Liquid components:
- `header.liquid` - Site navigation and branding
- `footer.liquid` - Footer content and links
- `product.liquid` - Product display and purchase
- `collection.liquid` - Product grid with filtering
- `cart.liquid` - Shopping cart management
- `search.liquid` - Search functionality
- `article.liquid` - Blog post display
- `custom-section.liquid` - Custom content areas

### Snippets
Reusable code fragments:
- `meta-tags.liquid` - SEO and social meta tags
- `css-variables.liquid` - Theme CSS variables
- `image.liquid` - Responsive image rendering
- `structured-data-*.liquid` - Schema.org markup for:
  - Products
  - Collections
  - Articles
  - Reviews
  - FAQs
  - Videos
  - Breadcrumbs
  - Organization

### Blocks
Horizon-compatible theme blocks:
- `group.liquid` - Container for nested blocks
- `text.liquid` - Text content blocks

---

## 🎨 Development

### CSS Architecture
- **Critical CSS** inlined in `<head>` for performance
- **CSS Variables** for easy theming and customization
- **Modular styles** scoped to components
- **Responsive design** mobile-first approach

### JavaScript
- Vanilla JavaScript for performance
- Modular component-based structure
- Cart API integration
- Product variant selection
- Search functionality

### Schema Configuration
Settings defined in `config/settings_schema.json`:
- Typography settings
- Color schemes
- Layout options
- Page width controls
- Spacing and margins

---

## 🔧 Customization

### Theme Settings
Customize your theme in the Shopify admin:
1. Go to **Online Store > Themes**
2. Click **Customize** on your theme
3. Use the theme editor to modify:
   - Colors and fonts
   - Layout and spacing
   - Header and footer
   - Homepage sections

### Adding Sections
Create new sections in `/sections/`:
```liquid
{% schema %}
{
  "name": "Custom Section",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Welcome"
    }
  ]
}
{% endschema %}
```

### Multi-Language Content
Add translations in `/locales/`:
- Edit `en.default.json` for English
- Create language files for each market
- Use `{{ 'key' | t }}` in Liquid templates

---

## 🚀 Deployment

### Development Workflow
```bash
# Start local development
shopify theme dev

# Check theme
shopify theme check

# Push to store
shopify theme push --unpublished
```

### Production Deployment
```bash
# Publish theme
shopify theme publish

# Or create a new theme version
shopify theme push --unpublished --theme-name="EMMSO v2.0"
```

### GitHub Integration
This theme is version controlled with Git:
```bash
# Commit changes
git add .
git commit -m "Add new product section"

# Push to GitHub
git push origin main
```

---

## 📚 Resources

### Shopify Documentation
- [Theme Architecture](https://shopify.dev/docs/storefronts/themes/architecture)
- [Liquid Reference](https://shopify.dev/docs/api/liquid)
- [Theme Editor](https://shopify.dev/docs/storefronts/themes/tools/online-editor)
- [Shopify CLI](https://shopify.dev/docs/api/shopify-cli)

### EMMSO-Specific
- **Repository:** https://github.com/frank2889/emmso-shopify-theme
- **Store:** vloerproducten.myshopify.com
- **Markets:** 10 European countries (NL, BE, DE, AT, FR, ES, IT, PT, DK, IE)
- **Languages:** NL, EN, DE, FR, ES, IT, PT, DA

---

## 📝 License

This theme is licensed under the MIT License. See [LICENSE.md](./LICENSE.md) for details.

---

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines.

---

**Built with ❤️ for EMMSO** - Pan-European Flooring & Pet Products Specialist
      /* multiple styles */
    }
  {% endstylesheet %}

  {% schema %}
  {
    "settings": [{
      "type": "select",
      "id": "layout",
      "label": "layout",
      "values": [
        { "value": "collection--full-width", "label": "t:options.full" },
        { "value": "collection--narrow", "label": "t:options.narrow" }
      ]
    }]
  }
  {% endschema %}
  ```

## CSS & JavaScript

For CSS and JavaScript, we recommend using the [`{% stylesheet %}`](https://shopify.dev/docs/api/liquid/tags#stylesheet) and [`{% javascript %}`](https://shopify.dev/docs/api/liquid/tags/javascript) tags. They can be included multiple times, but the code will only appear once.

### `critical.css`

The Skeleton Theme explicitly separates essential CSS necessary for every page into a dedicated `critical.css` file.

## Contributing

We're excited for your contributions to the Skeleton Theme! This repository aims to remain as lean, lightweight, and fundamental as possible, and we kindly ask your contributions to align with this intention.

Visit our [CONTRIBUTING.md](./CONTRIBUTING.md) for a detailed overview of our process, guidelines, and recommendations.

## License

Skeleton Theme is open-sourced under the [MIT](./LICENSE.md) License.
