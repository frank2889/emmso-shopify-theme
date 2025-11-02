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

**Supported Languages:** 8 Languages
- Dutch (NL) - Primary (Netherlands, Belgium)
- English (EN) - International (Ireland, UK)
- German (DE) - Germany, Austria
- French (FR) - France, Belgium
- Spanish (ES) - Spain
- Italian (IT) - Italy
- Portuguese (PT) - Portugal
- Danish (DA) - Denmark

**Language Detection:** Automatic via URL path (`/en/`, `/de/`, `/fr/`, etc.)

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
