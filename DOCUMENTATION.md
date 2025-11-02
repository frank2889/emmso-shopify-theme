# EMMSO Shopify Theme - Technical Documentation

## Table of Contents
1. [Multilingual Architecture](#multilingual-architecture)
2. [Search Intelligence](#search-intelligence)
3. [Product Comparison](#product-comparison)
4. [Query Normalization](#query-normalization)
5. [Testing Guide](#testing-guide)

---

## Multilingual Architecture

### Overview
The theme is **fully multilingual by design**, supporting 8 base languages across 13 regional markets. Every feature works seamlessly in all languages.

### Supported Languages
- **Dutch (NL)** - Netherlands, Belgium
- **English (EN)** - Ireland, UK, International
- **German (DE)** - Austria, Germany
- **French (FR)** - France, Belgium
- **Spanish (ES)** - Spain
- **Italian (IT)** - Italy
- **Portuguese (PT)** - Portugal
- **Danish (DA)** - Denmark

### Language Detection
Automatically detects from:
1. HTML `lang` attribute
2. URL path (`/nl/`, `/de/`, `/fr/`)
3. Shopify locale (`window.Shopify.locale`)
4. Fallback to 'en'

### Multilingual Search Features

#### 1. Cross-Language Search
Search in ANY language, find products in ALL languages:
```javascript
// User searches: "parket" (Dutch)
// System finds:
//   - Products tagged "parquet" (English)
//   - Products tagged "parkett" (German)
//   - Products tagged "parket" (Dutch)
```

#### 2. Synonym Dictionary
150+ synonym mappings across 8 languages:
- **Product types**: laminate, vinyl, parquet, wood, tile, stone
- **Characteristics**: waterproof, scratch-resistant, pet-friendly
- **Colors**: oak, walnut, white, grey, natural (all 8 languages)
- **Materials**: PVC, LVT, SPC, WPC, etc.

#### 3. Parallel Search
Query analyzed and expanded to synonym variations:
```javascript
// Query: "laminate"
// Searches in parallel:
//   - "laminate" (EN)
//   - "laminaat" (NL)
//   - "laminat" (DE)
// Merges and deduplicates results
```

#### 4. Smart Deduplication
- Merges results from multiple language searches
- Removes duplicates by product ID/handle
- Maintains performance with Map() data structure

### Related Products - Multilingual

#### Intelligent Matching
Analyzes across languages:
- **Product type** → Finds synonyms in all languages
- **Vendor/Brand** → Exact and variant matches
- **Tags** → Cross-language characteristic matching
- **Colors** → Multilingual color extraction from titles

#### Relevance Ranking
9-tier scoring system:
- Same brand: +50 points
- Same product type: +40 points
- Shared tags: +10 points each
- Similar price: +20 points (within 30%)
- In stock: +15 points
- Title similarity: +5 points per word match

#### Localized Display
Everything adapts to current language:
- "Related Products" → "Gerelateerde Producten" (NL)
- "Best Match" → "Beste Übereinstimmung" (DE)
- "Loading..." → "Chargement..." (FR)
- Price formatting per locale (€1.234,56 vs €1,234.56)

---

## Search Intelligence

### Core Features

#### 1. Instant Predictive Search
- Real-time autocomplete (debounced at 150ms)
- Product suggestions with thumbnails, prices, availability
- Category suggestions based on intent
- Search history (localStorage)
- Voice search support (Web Speech API)

#### 2. Advanced Filtering
- **Faceted search**: Category, Brand, Price, Room, Characteristics
- **Dynamic filters**: Only show relevant options
- **Multi-select**: Combine multiple filters (AND/OR logic)
- **Price range slider**: Min/Max with histogram
- **Instant updates**: No page reload, URL persistence
- **Active filter chips**: Easy removal

#### 3. Smart Algorithm
- **Fuzzy matching**: Handle typos and misspellings
- **Synonym support**: Multi-language synonyms
- **Weighted relevance**: Title (100%), Tags (80%), Description (60%)
- **Boost logic**: New products, sale items, high stock

#### 4. Intent Recognition
- **Question detection** → Learning Center suggestion
- **Problem-solving** → Care products
- **Comparison** → Side-by-side view
- **Purchase** → Product focus

#### 5. Context Detection
- **Room type**: kitchen, bathroom, living, bedroom
- **Usage characteristics**: pet-friendly, waterproof, high-traffic
- **Installation**: DIY-friendly, professional

### Performance Targets
- **First Input Delay**: < 100ms
- **Search Response**: < 200ms
- **Results Display**: < 300ms
- **Total Time to Interactive**: < 2s

---

## Product Comparison

### Overview
Side-by-side comparison of up to 4 products with comprehensive feature analysis.

### Features

#### 1. Smart Comparison
- Max 4 products (prevents overwhelm)
- Auto-notification on max reached
- Real-time count updates
- Persistent across sessions (localStorage)
- Keyboard shortcut: Press 'C' to open

#### 2. Comparison Table
- Product images, titles, vendors
- Price comparison (best price highlighted ★)
- Availability badges (in stock / out of stock)
- Product type comparison
- Variant count comparison
- Feature tags comparison (✓/✗)
- Remove products inline

#### 3. User Experience
- Floating comparison bar (bottom of page)
- Modal comparison view
- Mobile responsive (full-screen modal)
- Smooth animations
- ESC to close
- Disabled states (min 2 products required)

#### 4. Data Intelligence
- Extracts from DOM first (fast)
- Falls back to Shopify API if needed
- Handles missing data gracefully
- Supports metafields (future extensibility)

### Multilingual Support
All labels translated for 8 languages:
- 'Products selected for comparison'
- 'Clear All' / 'Compare Products'
- 'Price', 'Availability', 'Type', 'Variants', 'Features'
- 'In Stock' / 'Out of Stock'
- Notification messages

---

## Query Normalization

### Purpose
Prevents duplicate collections from search queries through intelligent normalization.

### Features

#### 1. Normalization Process
```javascript
// Input variations:
"waterproof vinyl flooring"
"vinyl waterproof flooring"
"flooring vinyl waterproof"

// Normalized output:
handle: "flooring-vinyl-waterproof"
canonical: "flooring vinyl waterproof"
```

#### 2. Quality Scoring (0-1 scale)
Factors:
- **Word count**: 2-4 optimal (+0.2)
- **Length**: 10-30 chars optimal (+0.1)
- **Product terms**: Contains product keywords (+0.2)
- **Specificity**: Non-generic terms (+0.1)
- **Generic penalty**: Weak queries (-0.3)

#### 3. Spam Detection
Blocks patterns:
- `/^test$/i` - Test queries
- `/^asdf/i` - Keyboard mashing
- `/^\d+$/` - Numbers only
- `/^[a-z]{1,2}$/i` - Single/double letters
- `/(.)\1{4,}/` - Repeated characters (aaaa)
- `/^[^a-z0-9\s]{3,}/i` - Special characters

#### 4. Similarity Detection
- Levenshtein distance algorithm
- 80%+ similarity threshold
- Prevents duplicates like:
  - "waterproof vinyl" vs "waterproof vinyl flooring"
  - "oak laminate" vs "laminate oak"

#### 5. Collection Matching
```javascript
findMatchingCollection(query, existingCollections, locale)
// Returns: { collection, matchType, confidence }
// Match types: 'exact', 'similar', 'title'
// Confidence: 0-1 (1 = perfect match)
```

### Multi-language Support
- Stop word removal (8 languages)
- Synonym canonicalization
- Locale-aware normalization

### Integration
- Integrated into `unified-filters.js`
- Auto-redirect to existing collections
- Optional webhook for auto-collection creation
- Quality threshold: 0.5 minimum
- Min products: 10 required

---

## Testing Guide

### Basic Search Tests

#### Single-Language
```
Test: "laminate"
Expected: All laminate products
```

#### Multi-Language Synonyms
```
Test: "laminaat" (Dutch)
Expected: Matches "laminate" products

Test: "parket" (Dutch)
Expected: Matches "parquet" products

Test: "holz" (German)
Expected: Matches "wood" products
```

### Intent Detection Tests

#### Questions
```
Test: "how to clean marble floors?"
Expected: Suggest Learning Center

Test: "what floor for kitchen?"
Expected: Kitchen flooring products + guides

Test: "which adhesive for tiles?"
Expected: Tile adhesives + installation guides
```

#### Problem-Solving
```
Test: "remove stains from wood floor"
Expected: Care products (cleaners, removers)

Test: "fix scratches on laminate"
Expected: Repair kits, maintenance products
```

#### Comparison
```
Test: "laminate vs vinyl"
Expected: Side-by-side comparison view

Test: "bona or woca oil"
Expected: Brand comparison
```

### Context Detection Tests

#### Room Context
```
Test: "kitchen flooring"
Expected: Kitchen-specific filters active

Test: "bathroom vinyl"
Expected: Waterproof products prioritized

Test: "living room parquet"
Expected: Living room characteristics
```

#### Usage Characteristics
```
Test: "pet friendly flooring"
Expected: Pet-friendly tag filter

Test: "waterproof vinyl for bathroom"
Expected: Waterproof + bathroom filters

Test: "underfloor heating compatible"
Expected: UFH-compatible products

Test: "high traffic laminate"
Expected: Commercial-grade products
```

### Complex Query Tests

#### Multi-Criteria
```
Test: "waterproof vinyl for kitchen under €25"
Expected:
  - Material: vinyl
  - Characteristic: waterproof
  - Room: kitchen
  - Price: max €25

Test: "diy friendly oak laminate"
Expected:
  - Characteristic: easy to install
  - Color: oak
  - Type: laminate

Test: "pet friendly wood oil bona"
Expected:
  - Characteristic: pet-friendly
  - Product: wood oil
  - Brand: Bona
```

### Fuzzy Matching Tests

#### Typo Handling
```
Test: "laminat" (missing 'e')
Expected: Suggest "laminate"

Test: "vynil" (wrong spelling)
Expected: Suggest "vinyl"

Test: "cleener" (typo)
Expected: Suggest "cleaner"
```

### Natural Language Tests

#### Conversational Queries
```
Test: "I need flooring for my bathroom that won't get damaged by water"
Expected:
  - Detect: bathroom, waterproof
  - Show: Waterproof vinyl products

Test: "what's the best oil for oak floors?"
Expected:
  - Detect: question intent, product (oil), wood type (oak)
  - Show: Wood oils for oak + guides
```

### Comparison Tool Tests

#### Adding Products
```
Test: Select 3 products, click compare
Expected: Comparison modal opens with 3 products

Test: Try to add 5th product
Expected: Warning "Maximum 4 products can be compared"
```

#### Comparison Features
```
Test: Compare products with different prices
Expected: Lowest price highlighted with ★

Test: Compare products with different features
Expected: ✓/✗ indicators for each feature

Test: Remove product from comparison
Expected: Product removed, table updates
```

#### Persistence
```
Test: Add 2 products, refresh page
Expected: Products still in comparison bar

Test: Clear all, check localStorage
Expected: Comparison data cleared
```

### Query Normalizer Tests

#### Duplicate Detection
```
Test: "waterproof vinyl flooring" vs "vinyl waterproof flooring"
Expected: Same normalized handle

Test: Quality score for "test"
Expected: isSpam: true, score: 0

Test: Quality score for "waterproof vinyl kitchen"
Expected: High score (0.7+), shouldCreateCollection: true
```

#### Collection Matching
```
Test: Search "vinyl flooring" (existing collection exists)
Expected: Redirect to existing collection

Test: Search "vinyl floor" (similar to "vinyl flooring")
Expected: 
  - matchType: 'similar'
  - confidence: 0.9+
  - Redirect to collection
```

---

## Performance Benchmarks

### Expected Results

#### Search Performance
- First keystroke response: < 100ms
- Autocomplete suggestions: < 200ms
- Full results display: < 300ms
- Filter application: < 150ms

#### Query Normalization
- Single query normalization: < 2ms
- Batch normalization (100 queries): < 200ms
- Memory usage: < 50KB

#### Product Comparison
- Add product to comparison: < 50ms
- Open comparison modal: < 100ms
- Render comparison table (4 products): < 200ms

#### Page Load
- Time to Interactive: < 2s
- First Contentful Paint: < 1s
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.1

---

## Files Reference

### JavaScript Assets
- `assets/unified-filters.js` - Unified filtering for Collections, Products, Search
- `assets/search-intelligence.js` - Search intent, synonyms, NLP
- `assets/search-engine.js` - Predictive search engine
- `assets/related-products.js` - Cross-language product matching
- `assets/product-comparison.js` - Product comparison tool
- `assets/query-normalizer.js` - Query normalization & deduplication

### Liquid Templates
- `sections/search-results.liquid` - Search results page
- `sections/collection.liquid` - Collection page with filters
- `sections/product.liquid` - Product page with related products
- `snippets/comparison-bar.liquid` - Floating comparison bar
- `snippets/comparison-checkbox.liquid` - Comparison checkbox component
- `snippets/meta-tags.liquid` - Multilingual SEO meta tags
- `snippets/image.liquid` - Responsive images (AVIF/WebP/JPEG)

### CSS Assets
- `assets/product-card.css` - Product card styles
- `assets/product-comparison.css` - Comparison tool styles
- `assets/critical.css` - Critical above-fold CSS

### Documentation
- `README.md` - Main project documentation
- `QUERY_NORMALIZER.md` - Query normalization deep dive
- `DOCUMENTATION.md` - This file (technical reference)

---

## Best Practices

### Development
1. Always test in multiple languages
2. Use `detectLanguage()` for locale detection
3. Follow product-agnostic naming (not floor-specific)
4. Test with real multilingual data
5. Validate query normalization results

### Performance
1. Use localStorage for client-side caching
2. Debounce search inputs (150ms)
3. Lazy load non-critical scripts
4. Use DOM extraction before API calls
5. Implement proper error handling

### Accessibility
1. Use semantic HTML
2. Add ARIA labels to controls
3. Keyboard navigation support
4. Focus states on interactive elements
5. Screen reader friendly labels

### SEO
1. Use hreflang tags (13 markets)
2. Dynamic meta tags per language
3. Schema.org structured data
4. Clean URL structure
5. Canonical tags for duplicates

---

**Last Updated**: November 2025  
**Theme Version**: 2.0 (Product-Agnostic)  
**Shopify CLI**: 3.86.1
