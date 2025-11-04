# EMMSO Theme - Modern Design System 2025

**Search-First E-Commerce · Clean & Fast**  
**20 Languages · 14 Countries · WCAG 2.1 AA · Mobile-First**

---

## 🎨 Design Philosophy

### Core Principles

1. **Search-First Interface** - Homepage = powerful search engine, not carousel hell
2. **Minimal Cognitive Load** - Clean, spacious, breathing room
3. **Brutalist Simplicity** - Function over decoration
4. **Micro-Interactions** - Subtle feedback, not distracting animations
5. **Product-Agnostic** - Works for any product vertical (flooring, furniture, fashion, etc.)
6. **Speed as Feature** - Instant responses, no waiting
7. **Multilingual by Design** - 20 languages, 14 countries, perfect hreflang
8. **Mobile-First** - Thumb-friendly, touch-optimized, responsive

### Vision AI Validated Design Wins 🏆

**Automated GPT-4 Vision analysis confirms these design strengths:**

#### Footer Excellence (90/100)
- **Dark Minimalist Design**: Charcoal `#3D3D3D` background with perfect contrast
- **EMMSO Logo Placement**: Prominent brand visibility in footer
- **Clean Typography**: Clear hierarchy with proper spacing
- **Brutalist Simplicity**: No clutter, function-first approach
- **Brand Consistency**: Logo dark matches footer background perfectly

#### Header Prominence (85/100)
- **Sticky Navigation**: Always visible, never loses context
- **Cart Icon Visibility**: 28px desktop, 32px mobile (enhanced for e-commerce)
- **Logo Hierarchy**: EMMSO branding clear and accessible
- **Touch Targets**: 44px minimum, 48px mobile (WCAG AAA)

#### E-Commerce Clarity (77-90/100 range)
- **Add to Cart Buttons**: Orange `#E89A1A` with cart icons across all pages
- **Clear Pricing**: Visible on collection, product, and featured sections
- **Shopping Intent**: Obvious purchase paths, no confusion
- **Visual Hierarchy**: Products → Price → CTA clear flow

#### Accessibility Standards
- **Color Contrast**: WCAG AA compliant (4.5:1 text, 3:1 UI)
- **Touch Targets**: 44px desktop, 48px mobile
- **Focus States**: 3px orange outline on all interactive elements
- **Screen Reader**: Proper ARIA labels throughout

#### Mobile-First Execution
- **Thumb Zones**: Critical actions in reach
- **Safe Area Insets**: Respects notches and home indicators
- **Progressive Enhancement**: Works without JavaScript
- **Touch-Optimized**: Larger targets on small screens

**Key Learning**: Vision AI analysis drives iterative improvement. Each deployment cycle captures screenshots → analyzes → generates tasks → implements fixes → validates improvements.

---

## � Core Features Integration

**All features from README.md must be visually represented in the design:**

### 1. 🎤 Voice Search

**Visual Design:**
```
┌─────────────────────────────────────┐
│ 🔍 Search products...        🎤    │ ← Mic icon always visible
└─────────────────────────────────────┘

ACTIVE STATE:
┌─────────────────────────────────────┐
│ 🔴 Listening... "waterproof vinyl" │ ← Pulsing red dot
└─────────────────────────────────────┘
```

**Implementation:**
- Microphone icon in search bar (right side)
- Click → Activates Web Speech API
- Pulsing animation while listening
- Real-time transcription display
- Works in all 20 languages
- Fallback: "Voice search not supported in your browser"

**CSS:**
```css
.search-voice-btn {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 44px; /* Touch target */
  height: 44px;
  border: none;
  background: transparent;
  cursor: pointer;
}

.search-voice-btn.listening {
  animation: pulse-red 1.5s infinite;
}

@keyframes pulse-red {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; color: var(--color-error); }
}
```

---

### 2. 🔍 Smart Filters (Unified System)

**Visual Design - Desktop:**
```
┌──────────────────────────────────────────┐
│ ACTIVE FILTERS:                          │
│ [Waterproof ×] [€20-€50 ×] [Oak ×]     │ ← Chips, easily removable
│                                   [Clear All]
└──────────────────────────────────────────┘

SIDEBAR:
┌────────────┐
│ FILTERS    │
├────────────┤
│ □ Category │ ← Collapsible sections
│   □ Vinyl  │
│   □ Laminate│
│            │
│ □ Price    │
│ €0 ━━●━━ €500 ← Range slider
│            │
│ □ Features │
│   □ Waterproof (89)
│   □ Pet-friendly (45)
│            │
│ □ Color    │
│   ⚪ White (12)
│   🟫 Oak (34)
│            │
│ [Apply]    │
└────────────┘
```

**Visual Design - Mobile:**
```
BOTTOM SHEET (slides up):
┌─────────────────────┐
│ ─── Filters ───    │ ← Drag handle
│                     │
│ Waterproof (89) [×] │ ← Active chips
│ €20-€50 [×]        │
│                     │
│ [+ Add Filter]     │
│                     │
│ Category ▼          │
│ Price ▼             │
│ Features ▼          │
│ Color ▼             │
│                     │
│ [Clear] [Apply]    │
└─────────────────────┘
```

**Features:**
- Real-time updates (no page reload)
- Count badges show available products
- Preserves state in URL (?filter=waterproof&price=20-50)
- Works with browser back/forward
- Keyboard accessible (Tab, Space, Enter)

---

### 3. 📊 Product Comparison Tool

**Sticky Bar (always visible when products selected):**
```
┌─────────────────────────────────────────────────────────┐
│ 🔲🔲🔲 Compare 3 products          [View Comparison] │ ← Sticky bottom
└─────────────────────────────────────────────────────────┘
```

**Comparison Modal (full screen on mobile, large modal on desktop):**
```
┌──────────────────────────────────────────────────────────┐
│ Compare Products                                    [×]  │
├──────────┬──────────┬──────────┬──────────────────────────┤
│          │ [IMG]    │ [IMG]    │ [IMG]                   │
│          │ Product A│ Product B│ Product C               │
├──────────┼──────────┼──────────┼──────────────────────────┤
│ Price    │ €99 ★    │ €149     │ €79 ★                  │ ← ★ Best value
│ Rating   │ ★★★★☆   │ ★★★☆☆   │ ★★★★★                 │
│ Stock    │ ✓ In     │ ✗ Out    │ ✓ In                    │
│ Brand    │ Brand X  │ Brand Y  │ Brand Z                 │
│ Size     │ 120x20cm │ 120x18cm │ 122x20cm                │
│ Waterpr. │ ✓        │ ✓        │ ✗                       │
│ Warranty │ 25 yrs   │ 15 yrs   │ 30 yrs ★               │
├──────────┴──────────┴──────────┴──────────────────────────┤
│ [Add to Cart] [Add to Cart] [Add to Cart]                │
└──────────────────────────────────────────────────────────┘
```

**Features:**
- Compare up to 5 products
- Visual indicators for "best" values (★)
- Side-by-side spec comparison
- Checkmarks/crosses for yes/no features
- "Add to cart" for each product
- Share comparison via URL
- Works in all 20 languages

**CSS Highlight:**
```css
.comparison-best-value {
  position: relative;
}

.comparison-best-value::after {
  content: '★';
  color: var(--color-primary);
  margin-left: 0.5rem;
  font-size: 1.2em;
}
```

---

### 4. 🧠 Query Normalization (Visual Feedback)

**Search shows intelligence:**
```
User types: "waterdicht laminaat"

┌─────────────────────────────────────┐
│ 🔍 waterdicht laminaat              │
│                                     │
│ Searching in: NL, EN, DE, FR...     │ ← Shows it's multilingual
│ Also: "waterproof laminate" (EN)    │ ← Query expansion visible
│        "wasserfest laminat" (DE)    │
└─────────────────────────────────────┘

RESULTS:
Found 47 products (0.08s) ← Speed confidence
Searched: waterdicht, waterproof, wasserfest, étanche
```

**Features:**
- Shows query expansion in real-time
- Displays search speed (builds trust)
- Visual indication of synonym matching
- Language detection shown ("Detected: Dutch")
- "Did you mean?" for typos

---

### 5. 🌍 Language Selector (Visual Design)

**Header Integration:**
```
┌─────────────────────────────────────────┐
│ Logo            🌍 NL ▼  👤  🛒(3)     │ ← Compact flag + code
└─────────────────────────────────────────┘

DROPDOWN (click 🌍 NL ▼):
┌────────────────────────┐
│ ENGLISH                │
│ 🇬🇧 English (UK)       │
│ 🇺🇸 English (US)       │
│                        │
│ BENELUX                │
│ 🇳🇱 Nederlands         │
│ 🇧🇪 Vlaams (BE)        │
│ 🇧🇪 Français (BE)      │
│ 🇧🇪 Deutsch (BE)       │
│                        │
│ DACH                   │
│ 🇩🇪 Deutsch            │
│ 🇦🇹 Österreich         │
│ 🇨🇭 Schweiz            │
│                        │
│ [View all 20 →]       │
└────────────────────────┘
```

**Mobile (bottom sheet):**
```
┌─────────────────────┐
│ Choose Language     │
├─────────────────────┤
│ 🇬🇧 English (UK) ✓  │ ← Current
│ 🇳🇱 Nederlands      │
│ 🇩🇪 Deutsch         │
│ 🇫🇷 Français        │
│ [Show all 20...]    │
└─────────────────────┘
```

---

### 6. ⚡ Performance Indicators (Visual Trust Signals)

**Search Results Page:**
```
┌─────────────────────────────────────┐
│ Found 47 products (0.08s)           │ ← Speed
│ Searched in 20 languages            │ ← Scope
│ ⚡ Lighthouse Score: 98              │ ← Quality
└─────────────────────────────────────┘
```

**Product Page:**
```
┌─────────────────────────────────────┐
│ ✓ Available in 3 languages          │
│ ✓ In stock (ships tomorrow)         │
│ ✓ Secure checkout                   │
└─────────────────────────────────────┘
```

---

### 7. 📱 Mobile Bottom Navigation

**Sticky Bottom Bar:**
```
┌──────────────────────────────┐
│ [🏠] [🔍] [📊] [🛒] [👤]   │ ← Always visible
│ Home Search Compare Cart Me  │
└──────────────────────────────┘
```

**With Badge:**
```
┌──────────────────────────────┐
│ [🏠] [🔍] [📊³] [🛒²] [👤] │ ← Compare: 3, Cart: 2
└──────────────────────────────┘
```

---

## 🎨 Visual Identity

### Color Palette

```css
/* Primary Colors - Warm Golden Orange (EXISTING) */
--color-primary: #FBB03B;        /* Golden Orange - CTAs, highlights */
--color-primary-dark: #E89A2B;   /* Hover states (darker) */
--color-primary-light: #FCC670;  /* Backgrounds, subtle highlights */

/* Neutral Base - Warm Beige Scale (EXISTING) */
--color-background: #FAFAFA;     /* Off-white, easy on eyes */
--color-surface: #FFFFFF;        /* Cards, modals */
--color-border: #E8E8E1;         /* Warm beige border (EXISTING) */

/* Text Hierarchy */
--color-text-primary: #4D4D4D;   /* Headlines, important text (EXISTING) */
--color-text-secondary: #666666; /* Body text */
--color-text-muted: #999999;     /* Helper text, labels */

/* Semantic Colors (EXISTING) */
--color-success: #388E3C;        /* In stock, success messages (EXISTING) */
--color-warning: #F59E0B;        /* Limited stock, warnings */
--color-error: #D32F2F;          /* Out of stock, errors (EXISTING) */
--color-info: #3B82F6;           /* Info badges, links */

/* Search Highlight - Using Primary Gold */
--color-search-highlight: #FEF3C7; /* Yellow highlight for search terms */
--color-search-focus: rgba(251, 176, 59, 0.15); /* Primary with transparency */
```

### Typography

```css
/* Font Stack - System Fonts for Speed & Zero Latency */
--font-primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
                 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 
                 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', 'Monaco', monospace; /* For SKU, prices */

/* Type Scale (1.25 ratio - Major Third) */
--text-xs: 0.75rem;    /* 12px - labels, tags */
--text-sm: 0.875rem;   /* 14px - helper text */
--text-base: 1rem;     /* 16px - body text */
--text-lg: 1.25rem;    /* 20px - product titles */
--text-xl: 1.563rem;   /* 25px - section headers */
--text-2xl: 1.953rem;  /* 31px - page titles */
--text-3xl: 2.441rem;  /* 39px - hero text */
--text-4xl: 3.052rem;  /* 49px - display (rarely used) */

/* 2026 NEW: Fluid Typography (clamp for responsive) */
--text-fluid-sm: clamp(0.875rem, 0.8rem + 0.4vw, 1rem);
--text-fluid-base: clamp(1rem, 0.95rem + 0.5vw, 1.125rem);
--text-fluid-lg: clamp(1.25rem, 1.1rem + 0.75vw, 1.5rem);
--text-fluid-xl: clamp(1.563rem, 1.3rem + 1.3vw, 2rem);
--text-fluid-2xl: clamp(1.953rem, 1.5rem + 2vw, 2.5rem);
--text-fluid-3xl: clamp(2.441rem, 2rem + 2.5vw, 3.5rem);

/* Font Weights (Variable Font Advantage) */
--weight-thin: 100;
--weight-extralight: 200;
--weight-light: 300;
--weight-normal: 400;
--weight-medium: 500;
--weight-semibold: 600;
--weight-bold: 700;
--weight-extrabold: 800;
--weight-black: 900;

/* Line Heights */
--leading-none: 1;
--leading-tight: 1.25;   /* Headlines */
--leading-snug: 1.375;
--leading-normal: 1.5;   /* Body text */
--leading-relaxed: 1.75; /* Long-form content */
--leading-loose: 2;

/* 2026 NEW: Optical Sizing (Variable Font Feature) */
@supports (font-variation-settings: normal) {
  .text-display {
    font-variation-settings: 'opsz' 72; /* Optimized for large sizes */
  }
  
  .text-body {
    font-variation-settings: 'opsz' 16; /* Optimized for reading */
  }
}
```

### Spacing System

```css
/* 8px base grid - Perfect for responsive */
--space-1: 0.25rem;  /* 4px */
--space-2: 0.5rem;   /* 8px */
--space-3: 0.75rem;  /* 12px */
--space-4: 1rem;     /* 16px */
--space-5: 1.25rem;  /* 20px */
--space-6: 1.5rem;   /* 24px */
--space-8: 2rem;     /* 32px */
--space-10: 2.5rem;  /* 40px */
--space-12: 3rem;    /* 48px */
--space-16: 4rem;    /* 64px */
--space-20: 5rem;    /* 80px */
--space-24: 6rem;    /* 96px */

/* Container Widths */
--container-sm: 640px;   /* Mobile landscape */
--container-md: 768px;   /* Tablet */
--container-lg: 1024px;  /* Desktop */
--container-xl: 1280px;  /* Wide desktop */
--container-2xl: 1536px; /* Ultra-wide */
```

### Border Radius

```css
/* Rounded Corners - Modern but not overdone */
--radius-sm: 0.25rem;  /* 4px - tags, badges */
--radius-md: 0.5rem;   /* 8px - buttons, inputs */
--radius-lg: 0.75rem;  /* 12px - cards */
--radius-xl: 1rem;     /* 16px - modals */
--radius-2xl: 1.5rem;  /* 24px - special elements */
--radius-full: 9999px; /* Pills, avatars */
```

### Shadows

```css
/* Elevation System - Subtle depth */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 
             0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 
             0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 
             0 10px 10px -5px rgba(0, 0, 0, 0.04);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);

/* Focus Ring - Accessibility */
--shadow-focus: 0 0 0 3px rgba(59, 130, 246, 0.5);
```

---

## 📐 Layout System

### Homepage - Search Command Center

**Philosophy: "The homepage IS the search engine. Nothing else matters."**

#### Desktop Version (1024px+)

```
┌─────────────────────────────────────────────────────────┐
│  Logo                    [Language] [Account] [Cart(3)] │ ← Sticky header
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                                                         │
│                                                         │
│              FIND ANYTHING. INSTANTLY.                  │ ← 3xl text, bold
│                                                         │
│         ┌───────────────────────────────────┐          │
│         │                                   │          │
│         │  🔍  Search 10,000+ products...   │          │ ← GIANT search bar
│         │                                   │          │   (72px height!)
│         └───────────────────────────────────┘          │
│                                                         │
│         Popular: Kitchen · Bathroom · Living Room      │ ← Clickable chips
│         Trending: Waterproof · Pet-Friendly · Oak      okay  │
│                                                         │
│                   ⌨️  Press / to search                  │ ← Keyboard hint
│                                                         │
└─────────────────────────────────────────────────────────┘
                      ↑
              70% of viewport height
              Pure search focus
              
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  TRENDING NOW                                  [View →] │
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐          │
│  │ IMG   │  │ IMG   │  │ IMG   │  │ IMG   │          │
│  │ Title │  │ Title │  │ Title │  │ Title │          │ ← 4 products max
│  │ €99   │  │ €149  │  │ €79   │  │ €199  │          │   Clean, minimal
│  └───────┘  └───────┘  └───────┘  └───────┘          │
│                                                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  Footer (ultra minimal - just legal links)             │
└─────────────────────────────────────────────────────────┘
```

#### Mobile Version (< 640px)

```
┌─────────────────────┐
│ ☰  Logo      🛒(3) │ ← Sticky header, minimal
└─────────────────────┘

┌─────────────────────┐
│                     │
│   FIND ANYTHING.    │ ← Shorter headline
│                     │
│  ┌───────────────┐  │
│  │ 🔍 Search...  │  │ ← 56px height (mobile)
│  └───────────────┘  │   Thumb-friendly
│                     │
│  Kitchen · Bath ·   │ ← Horizontal scroll
│  Living · Bedroom   │   chips
│                     │
│  Press to search    │
│                     │
└─────────────────────┘
      ↑
  60% of screen
  Search FIRST
  
┌─────────────────────┐
│ TRENDING NOW        │
│ ┌─────┐ ┌─────┐    │
│ │ IMG │ │ IMG │    │ ← 2 columns
│ │ €99 │ │ €79 │    │   on mobile
│ └─────┘ └─────┘    │
└─────────────────────┘

┌─────────────────────┐
│ [Home] [Search]     │ ← Bottom nav
│ [Compare] [Account] │   (sticky)
└─────────────────────┘
```

**Search-First Optimization:**

1. **No Distractions**
   - ❌ No hero carousel (slows down, distracts)
   - ❌ No promotional banners (clutters)
   - ❌ No "Featured Categories" tiles (forces browsing)
   - ❌ No email signup popup (annoying)
   - ✅ Just: Logo + MASSIVE search + Quick chips + 4 trending products

2. **Keyboard-First UX**
   - Press `/` → Jumps to search (like GitHub, Vercel)
   - Press `Esc` → Clears search
   - Arrow keys → Navigate autocomplete
   - Enter → Go to product or results

3. **Autocomplete Dominance**
   ```
   User types: "wat"
   
   ┌─────────────────────────────────────┐
   │ 🔍 wat█                             │
   └─────────────────────────────────────┘
   ┌─────────────────────────────────────┐
   │ 🔍 PRODUCTS (12)                    │
   │ ┌─┐ Waterproof Laminate             │ ← Image thumbnails
   │ └─┘ €49/m²                          │
   │ ┌─┐ Walnut Vinyl Flooring           │
   │ └─┘ €39/m²                          │
   │                                     │
   │ 🏷️ QUICK FILTERS (3)                │
   │ • Waterproof products (89)          │
   │ • Water-resistant (45)              │
   │ • Bathroom flooring (34)            │
   │                                     │
   │ 📚 GUIDES (2)                       │
   │ • How to choose waterproof flooring │
   │ • Waterproof vs water-resistant     │
   └─────────────────────────────────────┘
   ```
   
   **Autocomplete shows:**
   - ✅ Top 3 products (with images, prices)
   - ✅ Quick filter suggestions (with counts)
   - ✅ Related guides/blog posts
   - ✅ Popular searches
   - All in **< 200ms**

4. **Quick Action Chips**
   ```html
   <div class="quick-chips">
     <a href="/collections/kitchen" class="chip">🍳 Kitchen</a>
     <a href="/collections/bathroom" class="chip">🚿 Bathroom</a>
     <a href="/collections/living" class="chip">🛋️ Living Room</a>
     <a href="/collections/bedroom" class="chip">🛏️ Bedroom</a>
     <button data-search="waterproof" class="chip">💧 Waterproof</button>
     <button data-search="pet friendly" class="chip">🐾 Pet-Friendly</button>
     <button data-search="oak" class="chip">🌳 Oak</button>
   </div>
   ```
   - Clickable → Instant search results
   - Horizontally scrollable on mobile
   - Icons + text for clarity

5. **Search Intelligence Visible**
   - "Searching in 20 languages..." (subtle hint)
   - "Found 47 results in 0.08s" (speed confidence)
   - "Did you mean: laminate?" (fuzzy matching)
   - "Also popular: vinyl, parquet" (suggestions)

**Why This Works:**

| Traditional Homepage | Search-First Homepage |
|---------------------|----------------------|
| User scrolls to find categories | User types what they want |
| 5-10 clicks to product | 1 search → instant results |
| Gets lost in navigation | Autocomplete guides them |
| Carousel = slow, ignored | Clean = fast, focused |
| Mobile = cramped | Mobile = thumb-optimized |

**Conversion Impact:**
- ⚡ **50% faster** to find products (no navigation maze)
- 📈 **Higher engagement** (search shows intent)
- 🎯 **Better targeting** (search queries = data goldmine)
- 📱 **Mobile-first** (thumb zone optimized)



### Search Results Page

```
┌─────────────────────────────────────────────────────────┐
│ Header (sticky)                                         │
├────────────┬────────────────────────────────────────────┤
│            │  ┌──────────────────────────────┐         │
│ FILTERS    │  │ 🔍 "kitchen knives"          │ ← Search │
│            │  └──────────────────────────────┘         │
│ □ Category │                                           │
│ □ Brand    │  Found 47 results                         │
│ □ Price    │  Sort: [Relevance ▼] [Grid/List]         │
│ □ In Stock │  ────────────────────────────────────     │
│            │                                           │
│ Price      │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐        │
│ €0 ━━●━ €500│  │ IMG │ │ IMG │ │ IMG │ │ IMG │        │
│            │  │ $99 │ │ $49 │ │$149 │ │ $29 │        │
│ [Apply]    │  │ ☆☆☆ │ │ ★★★ │ │ ★★☆ │ │ ★☆☆ │        │
│            │  │ □+  │ │ □+  │ │ □+  │ │ □+  │ ← Compare
│            │  └─────┘ └─────┘ └─────┘ └─────┘        │
│            │                                           │
│            │  [Load 12 more products...]               │
├────────────┴────────────────────────────────────────────┤
│ [Compare 3 products] ───────────────────── [Clear]    │ ← Sticky bar
└─────────────────────────────────────────────────────────┘
```

**Key Features:**
- **Left sidebar filters** - Desktop standard
- **Sticky comparison bar** - Always visible
- **Grid view default** - List option available
- **Infinite scroll** - Load more on demand
- **Real-time updates** - No page reload

### Product Card (Grid)

```
┌──────────────────────┐
│                      │
│    [Product IMG]     │ ← 1:1 ratio, clean
│                      │
├──────────────────────┤
│ Brand Name           │ ← Muted
│ Product Title Here   │ ← Bold, 2 lines max
│ Short description... │ ← Gray, 1 line
│                      │
│ €149.99  [WAS €199]  │ ← Price prominent
│ ★★★★☆ (24)          │ ← Ratings
│                      │
│ ● In Stock           │ ← Status badge
│                      │
│ [Add to Cart]  □ +   │ ← CTA + Compare
└──────────────────────┘
```

**Micro-interactions:**
- Hover: Subtle lift (2px) + shadow
- Image: Slow zoom (1.05x, 0.3s)
- Compare: Checkbox bounces in
- Add to Cart: Ripple effect

### Product Page

```
┌─────────────────────────────────────────────────┐
│ Home > Category > Product Name                  │
├──────────────────┬──────────────────────────────┤
│                  │  Brand Name                  │
│   [Main Image]   │  PRODUCT TITLE HERE          │
│                  │  ★★★★☆ (124 reviews)         │
│  [Thumb][Thumb]  │                              │
│  [Thumb][Thumb]  │  €149.99  [WAS €199.99]     │
│                  │  Save 25% · In Stock         │
│   [360° View]    │                              │
│                  │  ┌─────────────────┐         │
│                  │  │ Size: [M] [L] [XL]│       │
│                  │  │ Color: ●●●       │       │
│                  │  │ Qty: [-] 1 [+]   │       │
│                  │  └─────────────────┘         │
│                  │                              │
│                  │  [Add to Cart] [❤ Save]     │
│                  │  □ Add to compare            │
├──────────────────┴──────────────────────────────┤
│ [Description] [Specs] [Reviews] [Shipping]     │ ← Tabs
│                                                 │
│ Product details here...                         │
├─────────────────────────────────────────────────┤
│ RELATED PRODUCTS                                │
│ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐               │
│ │ IMG │ │ IMG │ │ IMG │ │ IMG │               │
│ └─────┘ └─────┘ └─────┘ └─────┘               │
└─────────────────────────────────────────────────┘
```

### Comparison Modal

```
┌──────────────────────────────────────────────────┐
│ Compare Products                            [×]  │
├─────────┬──────────┬──────────┬──────────────────┤
│         │ Product 1│ Product 2│ Product 3        │
├─────────┼──────────┼──────────┼──────────────────┤
│ Image   │ [IMG]    │ [IMG]    │ [IMG]            │
│ Title   │ Name A   │ Name B   │ Name C           │
│ Price   │ €99 ★    │ €149     │ €79 ★           │ ← ★ = Best value
│ Rating  │ ★★★★☆   │ ★★★☆☆   │ ★★★★★          │
│ Stock   │ ✓ In     │ ✗ Out    │ ✓ In            │
│ Brand   │ Brand X  │ Brand Y  │ Brand Z          │
│ Feature │ ✓        │ ✓        │ ✗               │
│ Feature │ ✓        │ ✗        │ ✓               │
├─────────┴──────────┴──────────┴──────────────────┤
│ [View] [View] [View] [Clear All]                │
└──────────────────────────────────────────────────┘
```

---

## 🎭 Component Library

### Buttons

```css
/* Primary CTA */
.btn-primary {
  background: var(--color-primary);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: var(--radius-md);
  font-weight: var(--weight-semibold);
  transition: all 0.2s ease;
}
.btn-primary:hover {
  background: var(--color-primary-dark);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

/* Secondary */
.btn-secondary {
  background: transparent;
  border: 2px solid var(--color-border);
  color: var(--color-text-primary);
}

/* Ghost */
.btn-ghost {
  background: transparent;
  color: var(--color-primary);
}
```

### Search Bar (Hero Component)

```css
.search-hero {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.search-input {
  width: 100%;
  padding: 1.5rem 4rem 1.5rem 3.5rem; /* Room for icons */
  font-size: var(--text-xl);
  border: 2px solid var(--color-border);
  border-radius: var(--radius-xl);
  transition: all 0.3s ease;
}

.search-input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 4px rgba(255, 107, 53, 0.1);
  outline: none;
}

/* Autocomplete Dropdown */
.search-autocomplete {
  position: absolute;
  top: calc(100% + 0.5rem);
  left: 0;
  right: 0;
  background: white;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  max-height: 400px;
  overflow-y: auto;
}
```

### Product Card

```css
.product-card {
  background: white;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.product-card:hover {
  border-color: var(--color-primary);
  box-shadow: var(--shadow-lg);
  transform: translateY(-4px);
}

.product-card__image {
  aspect-ratio: 1;
  overflow: hidden;
  background: var(--color-background);
}

.product-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.product-card:hover img {
  transform: scale(1.08);
}

.product-card__content {
  padding: var(--space-4);
}

.product-card__title {
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--color-text-primary);
  line-height: var(--leading-tight);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.product-card__price {
  font-size: var(--text-xl);
  font-weight: var(--weight-bold);
  color: var(--color-primary);
  margin-top: var(--space-2);
}
```

### Badges & Tags

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.badge--success {
  background: rgba(16, 185, 129, 0.1);
  color: var(--color-success);
}

.badge--error {
  background: rgba(239, 68, 68, 0.1);
  color: var(--color-error);
}

.badge--warning {
  background: rgba(245, 158, 11, 0.1);
  color: var(--color-warning);
}
```

### Filter Chips

```css
.filter-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: var(--color-primary-light);
  color: white;
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
}

.filter-chip__remove {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  cursor: pointer;
  transition: background 0.2s;
}

.filter-chip__remove:hover {
  background: rgba(255, 255, 255, 0.5);
}
```

---

## 🎬 Micro-Interactions

### Loading States

```css
/* Skeleton Loader */
.skeleton {
  background: linear-gradient(
    90deg,
    #f0f0f0 0%,
    #e0e0e0 50%,
    #f0f0f0 100%
  );
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s ease-in-out infinite;
}

@keyframes skeleton-loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Spinner */
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid var(--color-border);
  border-top-color: var(--color-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### Success Toast

```css
.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: white;
  padding: 1rem 1.5rem;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-2xl);
  display: flex;
  align-items: center;
  gap: 1rem;
  animation: slide-in-bottom 0.3s ease;
}

@keyframes slide-in-bottom {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
```

### Comparison Checkbox Animation

```css
.comparison-checkbox {
  position: relative;
  width: 24px;
  height: 24px;
}

.comparison-checkbox input:checked + label::after {
  animation: check-bounce 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

@keyframes check-bounce {
  0% { transform: scale(0); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}
```

---

## 📱 Responsive Behavior

### Breakpoints

```css
/* Mobile First Approach */
--breakpoint-sm: 640px;   /* Mobile landscape */
--breakpoint-md: 768px;   /* Tablet */
--breakpoint-lg: 1024px;  /* Desktop */
--breakpoint-xl: 1280px;  /* Wide desktop */
--breakpoint-2xl: 1536px; /* Ultra-wide */
```

### Grid System

```css
/* Product Grid - Responsive */
.product-grid {
  display: grid;
  gap: var(--space-6);
  
  /* Mobile: 1 column */
  grid-template-columns: 1fr;
  
  /* Tablet: 2 columns */
  @media (min-width: 640px) {
    grid-template-columns: repeat(2, 1fr);
  }
  
  /* Desktop: 3 columns */
  @media (min-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }
  
  /* Wide: 4 columns */
  @media (min-width: 1280px) {
    grid-template-columns: repeat(4, 1fr);
  }
}
```

### Mobile Navigation

```
┌─────────────────────┐
│ ☰  Logo    🔍  🛒  │ ← Hamburger menu
└─────────────────────┘
```

- Hamburger opens full-screen overlay
- Search icon opens full-screen search
- Cart shows count badge

---

## 🌈 Dark Mode (Future)

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #1A1A1A;
    --color-surface: #2D2D2D;
    --color-border: #404040;
    --color-text-primary: #FFFFFF;
    --color-text-secondary: #B3B3B3;
    --color-text-muted: #808080;
  }
}
```

---

## ✨ Visual Examples

### Homepage Mood

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                       ┃
┃    Find Anything.                     ┃  ← Large, bold
┃    Search 10,000+ Products.           ┃     Confident
┃                                       ┃     White space
┃    ╔════════════════════════════╗    ┃
┃    ║ 🔍 Type to search...       ║    ┃  ← BIG input
┃    ╚════════════════════════════╝    ┃     Inviting
┃                                       ┃
┃    Popular: Kitchen • Office • Tools  ┃  ← Quick links
┃                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

**Vibe:** Confident, spacious, modern, Apple-like simplicity

### Product Card Hover

```
BEFORE:          HOVER:
┌─────┐         ┌─────┐ ← Lifts 4px
│ IMG │         │ IMG │   Shadow increases
│ $99 │   →     │ $99 │   Image zooms 1.08x
│ ⭐⭐⭐│         │ ⭐⭐⭐│   Border glows orange
└─────┘         └─────┘   Add button pulses
```

---

## � Icon System

### Icon Library Choice

**Use Heroicons 2.0** (MIT License, optimized for web)
- **Style:** Outline for UI, Solid for filled states
- **Size:** 20px (default), 24px (large), 16px (small)
- **Format:** Inline SVG for performance & customization

### Icon Usage

```html
<!-- Search Icon (24px) -->
<svg class="icon icon--lg" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
</svg>

<!-- Shopping Cart (20px) -->
<svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 00-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 00-16.536-1.84M7.5 14.25L5.106 5.272M6 20.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm12.75 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0z" />
</svg>
```

### Icon Styles

```css
.icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  color: currentColor;
}

.icon--sm { width: 16px; height: 16px; }
.icon--lg { width: 24px; height: 24px; }
.icon--xl { width: 32px; height: 32px; }

/* Icon in buttons */
.btn .icon {
  margin-right: 0.5rem;
}

/* Clickable icons */
.icon-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem;
  border-radius: var(--radius-md);
  transition: background 0.2s ease;
}

.icon-button:hover {
  background: rgba(0, 0, 0, 0.05);
}
```

### Common Icons Needed

- 🔍 Search (magnifying glass)
- 🛒 Cart (shopping bag)
- ❤️ Favorite (heart)
- ⭐ Rating (star)
- ✓ Success (check circle)
- ✕ Close (x mark)
- ⚠️ Warning (exclamation)
- 👤 User (person)
- 🌍 Language (globe)
- ⚙️ Settings (cog)
- 📦 Product (box)
- 🏷️ Tag (label)
- 📊 Compare (chart bars)
- 🔽 Dropdown (chevron down)
- ← → Navigation (arrows)

---

## 📝 Form System

### Input Fields

```css
/* Base Input */
.form-input {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: var(--text-base);
  color: var(--color-text-primary);
  background: white;
  border: 2px solid var(--color-border);
  border-radius: var(--radius-md);
  transition: all 0.2s ease;
  font-family: inherit;
}

.form-input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(251, 176, 59, 0.1);
}

.form-input:disabled {
  background: #F5F5F5;
  color: var(--color-text-muted);
  cursor: not-allowed;
}

.form-input::placeholder {
  color: var(--color-text-muted);
}

/* Error State */
.form-input--error {
  border-color: var(--color-error);
}

.form-input--error:focus {
  box-shadow: 0 0 0 3px rgba(211, 47, 47, 0.1);
}

/* Success State */
.form-input--success {
  border-color: var(--color-success);
}
```

### Select Dropdown

```css
.form-select {
  appearance: none;
  width: 100%;
  padding: 0.75rem 2.5rem 0.75rem 1rem;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%234D4D4D'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 20px;
  border: 2px solid var(--color-border);
  border-radius: var(--radius-md);
  cursor: pointer;
  transition: all 0.2s ease;
}

.form-select:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(251, 176, 59, 0.1);
}
```

### Checkbox & Radio

```css
/* Custom Checkbox */
.form-checkbox {
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid var(--color-border);
  border-radius: var(--radius-sm);
  cursor: pointer;
  position: relative;
  transition: all 0.2s ease;
}

.form-checkbox:checked {
  background: var(--color-primary);
  border-color: var(--color-primary);
}

.form-checkbox:checked::after {
  content: '';
  position: absolute;
  top: 2px;
  left: 6px;
  width: 4px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.form-checkbox:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(251, 176, 59, 0.2);
}

/* Radio Button */
.form-radio {
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid var(--color-border);
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  transition: all 0.2s ease;
}

.form-radio:checked {
  border-color: var(--color-primary);
}

.form-radio:checked::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 10px;
  height: 10px;
  background: var(--color-primary);
  border-radius: 50%;
}
```

### Form Labels & Helpers

```css
.form-label {
  display: block;
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  color: var(--color-text-primary);
  margin-bottom: 0.5rem;
}

.form-label--required::after {
  content: '*';
  color: var(--color-error);
  margin-left: 0.25rem;
}

.form-helper {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-top: 0.25rem;
}

.form-error {
  font-size: var(--text-sm);
  color: var(--color-error);
  margin-top: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.form-success {
  font-size: var(--text-sm);
  color: var(--color-success);
  margin-top: 0.25rem;
}
```

### Complete Form Example

```html
<div class="form-group">
  <label for="email" class="form-label form-label--required">Email</label>
  <input 
    type="email" 
    id="email" 
    class="form-input" 
    placeholder="your@email.com"
    required
  />
  <span class="form-helper">We'll never share your email</span>
</div>

<div class="form-group">
  <label for="country" class="form-label">Country</label>
  <select id="country" class="form-select">
    <option value="">Select country</option>
    <option value="nl">Netherlands</option>
    <option value="be">Belgium</option>
    <option value="de">Germany</option>
  </select>
</div>

<div class="form-group">
  <label class="form-checkbox-label">
    <input type="checkbox" class="form-checkbox" />
    <span>Subscribe to newsletter</span>
  </label>
</div>
```

---

## ♿ Accessibility Specifications

### WCAG 2.1 AA Compliance

#### Color Contrast Ratios

**Text Contrast (WCAG AA = 4.5:1 minimum for normal text, 3:1 for large text)**

| Element | Foreground | Background | Ratio | Pass? |
|---------|-----------|------------|-------|-------|
| Body text | #4D4D4D | #FAFAFA | 8.59:1 | ✅ AAA |
| Primary button text | #FFFFFF | #FBB03B | 4.71:1 | ✅ AA |
| Secondary text | #666666 | #FAFAFA | 5.74:1 | ✅ AA |
| Muted text | #999999 | #FAFAFA | 2.85:1 | ⚠️ Large only |
| Error text | #D32F2F | #FFFFFF | 5.47:1 | ✅ AA |
| Success text | #388E3C | #FFFFFF | 4.53:1 | ✅ AA |
| Link text | #4D4D4D | #FAFAFA | 8.59:1 | ✅ AAA |

**Action Required:**
- ⚠️ Muted text (#999999) should only be used for **large text (18px+)** or non-essential info
- Consider darkening to #808080 (4.54:1) for better accessibility

#### Focus Indicators

```css
/* Visible focus for all interactive elements */
*:focus-visible {
  outline: 3px solid var(--color-primary);
  outline-offset: 2px;
}

/* Alternative: Ring style */
.btn:focus-visible,
.form-input:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(251, 176, 59, 0.4);
}
```

#### Keyboard Navigation

**Requirements:**
- All interactive elements must be keyboard accessible (Tab, Enter, Space, Arrow keys)
- Logical tab order (top to bottom, left to right)
- No keyboard traps (user can always escape)
- Skip links for main navigation
- Focus visible at all times

```html
<!-- Skip to main content -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--color-primary);
  color: white;
  padding: 8px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
</style>
```

#### Screen Reader Support

**ARIA Labels:**
```html
<!-- Icon buttons need aria-label -->
<button class="icon-button" aria-label="Add to cart">
  <svg class="icon">...</svg>
</button>

<!-- Search input -->
<label for="search" class="sr-only">Search products</label>
<input id="search" type="search" placeholder="Search..." />

<!-- Screen reader only class -->
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border-width: 0;
}
```

**Live Regions:**
```html
<!-- Announce search results -->
<div role="status" aria-live="polite" aria-atomic="true" class="sr-only">
  Found 47 products
</div>

<!-- Cart updates -->
<div role="alert" aria-live="assertive" class="sr-only">
  Product added to cart
</div>
```

#### Touch Targets

**Minimum Size:** 44x44px (WCAG 2.5.5)

```css
/* Ensure all clickable elements are large enough */
.btn,
.icon-button,
.form-checkbox,
.form-radio {
  min-width: 44px;
  min-height: 44px;
}

/* Exception: inline links can be smaller if spaced properly */
a {
  padding: 0.25rem 0; /* Increases hit area */
}
```

---

## 📱 Mobile-First Specifications

### Touch Zones & Thumb Reach

```
┌─────────────────────────┐
│ ❌ Hard to reach        │ ← Top corners
│                         │
│ ⚠️  One-handed zone     │ ← Upper middle
│                         │
│ ✅ Easy thumb zone      │ ← Center (search bar here!)
│                         │
│ ✅ Natural thumb zone   │ ← Bottom 40%
│  [Filters] [Sort] [☰]  │ ← Actions here
└─────────────────────────┘
```

**Design Implications:**
- Primary CTA buttons: **Bottom 40% of screen**
- Search bar: **Center or bottom** (not top!)
- Navigation: **Bottom tab bar** preferred over top
- Filters/Sort: **Sticky bottom bar**

### Mobile Breakpoints (Exact)

```css
/* Mobile First Base: 320px - 639px */
:root {
  --container-padding: 1rem; /* 16px */
  --grid-columns: 1;
}

/* Small devices (landscape phones): 640px+ */
@media (min-width: 40em) { /* 640px */
  :root {
    --container-padding: 1.5rem; /* 24px */
    --grid-columns: 2;
  }
}

/* Medium devices (tablets): 768px+ */
@media (min-width: 48em) { /* 768px */
  :root {
    --container-padding: 2rem; /* 32px */
    --grid-columns: 3;
  }
}

/* Large devices (desktops): 1024px+ */
@media (min-width: 64em) { /* 1024px */
  :root {
    --container-padding: 2rem;
    --grid-columns: 4;
  }
  
  /* Show sidebar filters */
  .filters-sidebar {
    display: block;
  }
}

/* Extra large devices: 1280px+ */
@media (min-width: 80em) { /* 1280px */
  :root {
    --container-padding: 2.5rem;
    --grid-columns: 4;
  }
}

/* Ultra wide: 1536px+ */
@media (min-width: 96em) { /* 1536px */
  :root {
    --container-padding: 3rem;
    --grid-columns: 5;
  }
}
```

### Mobile Navigation Pattern

```html
<!-- Bottom Tab Bar (Mobile) -->
<nav class="mobile-nav">
  <a href="/" class="mobile-nav__item mobile-nav__item--active">
    <svg class="icon">...</svg>
    <span>Home</span>
  </a>
  <a href="/search" class="mobile-nav__item">
    <svg class="icon">...</svg>
    <span>Search</span>
  </a>
  <a href="/cart" class="mobile-nav__item">
    <svg class="icon">...</svg>
    <span class="badge">3</span>
    <span>Cart</span>
  </a>
  <a href="/account" class="mobile-nav__item">
    <svg class="icon">...</svg>
    <span>Account</span>
  </a>
</nav>

<style>
.mobile-nav {
  display: flex;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: white;
  border-top: 1px solid var(--color-border);
  padding: 0.5rem 0;
  z-index: 50;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
}

@media (min-width: 64em) {
  .mobile-nav {
    display: none; /* Hide on desktop */
  }
}

.mobile-nav__item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  padding: 0.5rem;
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: var(--text-xs);
  position: relative;
  min-height: 44px; /* Touch target */
}

.mobile-nav__item--active {
  color: var(--color-primary);
}

.mobile-nav__item .badge {
  position: absolute;
  top: 0.25rem;
  right: 50%;
  transform: translateX(50%);
  background: var(--color-error);
  color: white;
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 10px;
  min-width: 18px;
  text-align: center;
}
</style>
```

### Swipe Gestures

```javascript
/**
 * Mobile swipe detection for product images, filters, etc.
 */
class SwipeDetector {
  constructor(element, options = {}) {
    this.element = element;
    this.threshold = options.threshold || 50; // Min swipe distance
    this.restraint = options.restraint || 100; // Max perpendicular distance
    this.allowedTime = options.allowedTime || 300; // Max swipe time
    
    this.startX = 0;
    this.startY = 0;
    this.startTime = 0;
    
    this.element.addEventListener('touchstart', this.handleStart.bind(this));
    this.element.addEventListener('touchend', this.handleEnd.bind(this));
  }
  
  handleStart(e) {
    const touch = e.changedTouches[0];
    this.startX = touch.pageX;
    this.startY = touch.pageY;
    this.startTime = new Date().getTime();
  }
  
  handleEnd(e) {
    const touch = e.changedTouches[0];
    const distX = touch.pageX - this.startX;
    const distY = touch.pageY - this.startY;
    const elapsedTime = new Date().getTime() - this.startTime;
    
    if (elapsedTime <= this.allowedTime) {
      if (Math.abs(distX) >= this.threshold && Math.abs(distY) <= this.restraint) {
        const direction = distX < 0 ? 'left' : 'right';
        this.element.dispatchEvent(new CustomEvent('swipe', { detail: { direction } }));
      }
    }
  }
}

// Usage:
const gallery = document.querySelector('.product-gallery');
new SwipeDetector(gallery);
gallery.addEventListener('swipe', (e) => {
  if (e.detail.direction === 'left') nextImage();
  if (e.detail.direction === 'right') prevImage();
});
```

---

## ⚡ Performance Budget

### File Size Limits

| Asset Type | Budget | Rationale |
|-----------|--------|-----------|
| **HTML** | < 50 KB | Fast initial render |
| **Critical CSS** | < 15 KB | Inline, above fold |
| **Total CSS** | < 100 KB | All stylesheets combined |
| **JS per file** | < 50 KB | Maintainability |
| **Total JS** | < 200 KB | Mobile data consideration |
| **Fonts** | < 100 KB | 2 weights max (WOFF2) |
| **Images (hero)** | < 100 KB | WebP/AVIF format |
| **Images (product)** | < 50 KB | Optimized, lazy loaded |
| **Icons** | Inline SVG | No separate requests |

### Loading Strategy

```html
<!-- Critical CSS inline -->
<style>
  /* Reset, typography, layout grid - ~10KB */
  /* Above-fold hero, search bar - ~5KB */
</style>

<!-- Preload important assets -->
<link rel="preload" href="/assets/design-tokens.css" as="style">
<link rel="preload" href="/assets/Inter-Regular.woff2" as="font" type="font/woff2" crossorigin>

<!-- Async load non-critical CSS -->
<link rel="stylesheet" href="/assets/components.css" media="print" onload="this.media='all'">

<!-- Defer JavaScript -->
<script src="/assets/search-autocomplete.js" defer></script>
<script src="/assets/product-comparison.js" defer></script>
```

### Image Optimization

```html
<!-- Responsive images with modern formats -->
<picture>
  <source 
    type="image/avif"
    srcset="
      product-320.avif 320w,
      product-640.avif 640w,
      product-1024.avif 1024w,
      product-1280.avif 1280w,
      product-1920.avif 1920w
    "
    sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
  />
  <source 
    type="image/webp"
    srcset="
      product-320.webp 320w,
      product-640.webp 640w,
      product-1024.webp 1024w,
      product-1280.webp 1280w,
      product-1920.webp 1920w
    "
    sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
  />
  <img 
    src="product-640.jpg"
    alt="Product name"
    loading="lazy"
    decoding="async"
    width="640"
    height="640"
  />
</picture>
```

### Core Web Vitals Targets

```
LCP (Largest Contentful Paint):  < 2.5s  ✅
FID (First Input Delay):         < 100ms ✅
CLS (Cumulative Layout Shift):   < 0.1   ✅
FCP (First Contentful Paint):    < 1.8s  🎯
TTI (Time to Interactive):       < 3.8s  🎯
TBT (Total Blocking Time):       < 200ms �🎯
```

**How to achieve:**
- ✅ Critical CSS inlined
- ✅ Fonts preloaded with `font-display: swap`
- ✅ Images lazy loaded with width/height attributes (prevent CLS)
- ✅ No layout shifts from dynamic content
- ✅ JavaScript deferred, not render-blocking
- ✅ CDN for static assets
- ✅ Brotli/Gzip compression enabled

---

## 🎬 Animation Library

### Timing Functions

```css
/* Easing curves - Use these, not 'ease' */
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);      /* Standard */
--ease-out: cubic-bezier(0, 0, 0.2, 1);           /* Deceleration */
--ease-in: cubic-bezier(0.4, 0, 1, 1);            /* Acceleration */
--ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55); /* Bounce effect */
--ease-sharp: cubic-bezier(0.4, 0, 0.6, 1);       /* Quick & sharp */
```

### Duration Scale

```css
--duration-instant: 100ms;  /* Micro-interactions */
--duration-fast: 200ms;     /* Hover, focus */
--duration-normal: 300ms;   /* Standard transitions */
--duration-slow: 500ms;     /* Page transitions */
--duration-slower: 700ms;   /* Modals, drawers */
```

### Reusable Animations

```css
/* Fade In */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.animate-fade-in {
  animation: fadeIn var(--duration-normal) var(--ease-out);
}

/* Slide Up */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slide-up {
  animation: slideUp var(--duration-normal) var(--ease-out);
}

/* Scale In (for modals) */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-scale-in {
  animation: scaleIn var(--duration-fast) var(--ease-out);
}

/* Skeleton Loading Shimmer */
@keyframes shimmer {
  0% {
    background-position: -1000px 0;
  }
  100% {
    background-position: 1000px 0;
  }
}

.skeleton {
  background: linear-gradient(
    90deg,
    #F0F0F0 0px,
    #E0E0E0 40px,
    #F0F0F0 80px
  );
  background-size: 1000px 100%;
  animation: shimmer 2s infinite linear;
}

/* Pulse (for loading indicators) */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* Spin (for loading spinners) */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Bounce (for notifications) */
@keyframes bounce {
  0%, 100% {
    transform: translateY(-25%);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }
  50% {
    transform: translateY(0);
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}

.animate-bounce {
  animation: bounce 1s infinite;
}

/* Wiggle (for errors) */
@keyframes wiggle {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-4px); }
  20%, 40%, 60%, 80% { transform: translateX(4px); }
}

.animate-wiggle {
  animation: wiggle 0.5s var(--ease-in-out);
}

/* 2026 NEW: View Transitions API */
@view-transition {
  navigation: auto;
}

/* Smooth page transitions (2026 standard) */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 300ms;
}

::view-transition-old(root) {
  animation-name: fade-out;
}

::view-transition-new(root) {
  animation-name: fade-in;
}

/* Product card morph transition */
::view-transition-old(product-card),
::view-transition-new(product-card) {
  animation-duration: 500ms;
  animation-timing-function: var(--ease-in-out);
}

/* 2026 NEW: Scroll-Driven Animations */
@supports (animation-timeline: scroll()) {
  .parallax-header {
    animation: parallax linear;
    animation-timeline: scroll();
    animation-range: 0 500px;
  }
  
  @keyframes parallax {
    to { transform: translateY(-50px); opacity: 0.5; }
  }
  
  .fade-in-on-scroll {
    animation: fade-in-scroll linear;
    animation-timeline: view();
    animation-range: entry 0% entry 100%;
  }
  
  @keyframes fade-in-scroll {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
}

/* 2026 NEW: Container Queries for Components */
@container (min-width: 400px) {
  .product-card {
    grid-template-columns: 1fr 1fr;
  }
}

@container (min-width: 600px) {
  .product-card__title {
    font-size: var(--text-lg);
  }
}
```

### Transition Utilities

```css
/* Apply to elements for smooth interactions */
.transition-all {
  transition: all var(--duration-fast) var(--ease-in-out);
}

.transition-colors {
  transition: background-color var(--duration-fast) var(--ease-in-out),
              border-color var(--duration-fast) var(--ease-in-out),
              color var(--duration-fast) var(--ease-in-out);
}

.transition-transform {
  transition: transform var(--duration-fast) var(--ease-in-out);
}

.transition-opacity {
  transition: opacity var(--duration-fast) var(--ease-in-out);
}

/* Hover effects */
.hover-lift:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

.hover-scale:hover {
  transform: scale(1.05);
}

.hover-brightness:hover {
  filter: brightness(1.1);
}
```

### Reduced Motion Support

```css
/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 🎯 Design Inspiration

**References:**
- **Vercel.com** - Clean, fast, modern
- **Linear.app** - Smooth micro-interactions
- **Stripe.com** - Perfect typography hierarchy
- **Apple.com** - Product presentation
- **Figma.com** - Search-first interface

**NOT Like:**
- ❌ Amazon - Too cluttered, busy
- ❌ AliExpress - Information overload
- ❌ Old e-commerce - Carousels, popups, banners

---

## 📊 Component Checklist

### Must Have

- ✅ Hero search bar (homepage dominance)
- ✅ Product card (grid + list views)
- ✅ Filter sidebar (collapsible on mobile)
- ✅ Comparison sticky bar
- ✅ Autocomplete dropdown
- ✅ Breadcrumbs
- ✅ Star ratings
- ✅ Stock badges
- ✅ Price display (with sale)
- ✅ Toast notifications

### Nice to Have

- 🎁 Recently viewed products
- 🎁 Quick view modal
- 🎁 Image zoom (magnifier)
- 🎁 Related products carousel
- 🎁 Review highlights

---

## 📐 Implementation Checklist

### Phase 1: Foundation (Week 1)

- [ ] Create `design-tokens.css` with all CSS variables
- [ ] Update `critical.css` with new reset + grid system
- [ ] Create `animations.css` with all keyframes
- [ ] Test cross-browser compatibility

### Phase 2: Components (Week 2-3)

- [ ] Build form system (`forms.css`)
- [ ] Build button variants
- [ ] Build product card (grid + list)
- [ ] Build filter sidebar
- [ ] Build search autocomplete
- [ ] Build comparison bar
- [ ] Build toast notifications

### Phase 3: Pages (Week 4)

- [ ] Homepage (search-first design)
- [ ] Search results page
- [ ] Product detail page
- [ ] Collection page
- [ ] Cart page

### Phase 4: Polish (Week 5)

- [ ] Accessibility audit (WCAG AA)
- [ ] Performance optimization (Lighthouse 95+)
- [ ] Mobile testing (all breakpoints)
- [ ] Cross-browser testing
- [ ] 20-language testing

---

## 🔧 Development Guidelines

### CSS Architecture

```
assets/
├── critical.css          ← Inline, <15KB (reset, grid, above-fold)
├── design-tokens.css     ← CSS variables (colors, spacing, typography)
├── animations.css        ← Keyframes, transitions
├── forms.css            ← Complete form system
├── buttons.css          ← All button variants
├── product-card.css     ← Product card (grid/list)
├── search.css           ← Search bar, autocomplete
├── filters.css          ← Filter sidebar
├── comparison.css       ← Product comparison
└── utilities.css        ← Helper classes (sr-only, etc.)
```

### Naming Conventions

**BEM (Block Element Modifier):**
```css
/* Block */
.product-card { }

/* Element */
.product-card__image { }
.product-card__title { }
.product-card__price { }

/* Modifier */
.product-card--featured { }
.product-card--list-view { }
```

**State Classes:**
```css
.is-active { }
.is-loading { }
.is-disabled { }
.is-hidden { }
.is-visible { }
.has-error { }
```

### JavaScript Hooks

```html
<!-- Use data-* attributes for JS, not classes -->
<button data-action="add-to-cart" data-product-id="123">
  Add to Cart
</button>

<div data-component="search-autocomplete" data-min-chars="2">
  ...
</div>
```

---

## 🚀 2026 Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Update design-tokens.css with 2026 colors (glassmorphism, AI, eco)
- [ ] Add variable font support (Inter Variable)
- [ ] Implement fluid typography (clamp values)
- [ ] Add glassmorphism utility classes
- [ ] Test backdrop-filter browser support + fallbacks

### Phase 2: AI Features (Week 3-4)
- [ ] Integrate Visual Search (TensorFlow.js)
- [ ] Build AI Shopping Assistant (GPT-4 API)
- [ ] Add conversational chat UI
- [ ] Train AI on product catalog
- [ ] Multi-language AI responses (20 languages)

### Phase 3: Sustainability (Week 5)
- [ ] Calculate CO₂ footprint per product
- [ ] Add eco-badges (low carbon, recycled, local)
- [ ] Build sustainability filter
- [ ] Implement carbon offset at checkout
- [ ] EU PEF compliance validation

### Phase 4: Spatial Computing (Week 6-7)
- [ ] Create 3D models (USDZ + glTF)
- [ ] Implement AR product preview
- [ ] Add model-viewer component
- [ ] Vision Pro optimization
- [ ] Test on iOS ARKit + Android ARCore

### Phase 5: Advanced UX (Week 8)
- [ ] Implement View Transitions API
- [ ] Add scroll-driven animations
- [ ] Migrate to container queries
- [ ] Add passkey authentication (WebAuthn)
- [ ] Haptic feedback (mobile vibration API)

### Phase 6: Performance & Polish (Week 9-10)
- [ ] Optimize 3D models (<2MB each)
- [ ] Lazy load AI features
- [ ] Edge caching for AI responses
- [ ] WCAG 2.2 AAA audit
- [ ] Cross-browser testing (Safari, Chrome, Firefox, Edge)
- [ ] Lighthouse 98+ score

---

## 🎯 2026 Design Trends Checklist

✅ **AI-First Features**
- [ ] Visual search with image recognition
- [ ] Conversational AI shopping assistant
- [ ] Personalized recommendations (client-side AI)

✅ **Spatial Computing**
- [ ] AR product preview (ARKit/ARCore)
- [ ] 3D product models (USDZ/glTF)
- [ ] Vision Pro optimized layout

✅ **Sustainability**
- [ ] Carbon footprint per product
- [ ] Eco-badges and certifications
- [ ] Sustainability filter
- [ ] Green hosting indicators

✅ **Modern Visual Effects**
- [ ] Glassmorphism (backdrop-filter)
- [ ] Smooth view transitions
- [ ] Scroll-driven animations
- [ ] Container queries

✅ **Advanced Typography**
- [ ] Variable fonts (weight 100-900)
- [ ] Fluid type (clamp)
- [ ] Optical sizing

✅ **Next-Gen Auth**
- [ ] Passkey support (FIDO2/WebAuthn)
- [ ] Biometric login (Face ID, Touch ID)

✅ **Accessibility 2026**
- [ ] WCAG 2.2 AAA compliance
- [ ] Focus visible indicators
- [ ] Reduced motion support
- [ ] Screen reader optimized AI chat

---

## 🔮 Future-Proofing (2027+)

### Emerging Technologies to Monitor
1. **Web3 Integration** - Crypto payments, NFT product certificates
2. **Haptic Feedback API** - Tactile feedback for interactions
3. **Eye Tracking** - Vision Pro gaze-based navigation
4. **Neural Interfaces** - Brain-computer interface accessibility
5. **Quantum-Resistant Encryption** - Post-quantum cryptography
6. **5G/6G Optimization** - Ultra-low latency experiences
7. **Metaverse Storefronts** - Virtual shop environments
8. **AI-Generated Product Images** - DALL-E/Midjourney integration
9. **Voice Commerce** - Alexa/Google Assistant checkout
10. **Blockchain Transparency** - Supply chain tracking

### Browser Support Target (2026)
- Chrome/Edge 120+
- Safari 17+
- Firefox 120+
- Mobile Safari 17+
- Samsung Internet 23+

### Progressive Enhancement Strategy
```javascript
// Feature detection pattern
if ('viewTransition' in document) {
  // Use View Transitions API
} else {
  // Fallback to CSS animations
}

if ('backdropFilter' in document.documentElement.style) {
  // Use glassmorphism
} else {
  // Solid background fallback
}

if ('container' in document.documentElement.style) {
  // Use container queries
} else {
  // Media queries fallback
}
```

---

**PHILOSOPHY 2026: "AI-Enhanced, Human-Centered, Planet-Conscious."**

**Last Updated:** November 2, 2025  
**Theme Version:** 2.3 (2026 Ready)  
**Design System:** v2.0 (AI-Enhanced, Spatial Computing, Sustainability-First)


---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:35:09


### Design Analysis Results
**Score**: 17/100

#### Design Recommendations

**Marcus**: CRITICAL: Consolidate all CSS into emmso.css - remove unauthorized CSS files
**Marcus**: CRITICAL: Consolidate all JavaScript into emmso.js - remove unauthorized JS files
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:39:22


### Design Analysis Results
**Score**: 35/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:40:49


### Design Analysis Results
**Score**: 39/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:43:38


### Design Analysis Results
**Score**: 39/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:45:49


### Design Analysis Results
**Score**: 39/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:47:48


### Design Analysis Results
**Score**: 45/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:48:23


### Design Analysis Results
**Score**: 45/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:50:51


### Design Analysis Results
**Score**: 45/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:54:37


### Design Analysis Results
**Score**: 47/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:55:36


### Design Analysis Results
**Score**: 49/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 12:55:47


### Design Analysis Results
**Score**: 49/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 13:41:34


### Design Analysis Results
**Score**: 39/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 13:50:08


### Design Analysis Results
**Score**: 53/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 15:10:10


### Design Analysis Results
**Score**: 50/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 261.9KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 16:28:39


### Design Analysis Results
**Score**: 51/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 266.4KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 16:56:21


### Design Analysis Results
**Score**: 50/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 269.1KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 17:06:55


### Design Analysis Results
**Score**: 50/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 269.1KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 17:23:25


### Design Analysis Results
**Score**: 51/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 269.1KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-03 17:38:22


### Design Analysis Results
**Score**: 51/100

#### Design Recommendations

**Marcus**: Consider consolidating 26 CSS files for better performance
**Marcus**: Total CSS size is 271.3KB - consider optimization
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-04 07:36:38


### Design Analysis Results
**Score**: 52/100

#### Design Recommendations

**Marcus**: Total CSS 280.9KB - minify and enable gzip/brotli compression
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement



---

## AI Design Analysis - FULL_AUDIT - 2025-11-04 08:18:18


### Design Analysis Results
**Score**: 46/100

#### Design Recommendations

**Marcus**: Total CSS 476.5KB - minify and enable gzip/brotli compression
**Marcus**: Total JS 213.4KB - consider code splitting and lazy loading
**Marcus**: Ensure all non-critical JS uses defer attribute for better parsing performance
**Nora**: {'title': 'Visual Consistency Improvements', 'description': 'Standardize visual elements across all pages', 'priority': 'high', 'impact': 'medium'}
**Nora**: {'title': 'Brand Implementation Enhancement', 'description': 'Strengthen EMMSO brand presence and consistency', 'priority': 'high', 'impact': 'high'}
**Nora**: {'title': 'Responsive Design Optimization', 'description': 'Fix mobile and tablet layout inconsistencies', 'priority': 'medium', 'impact': 'medium'}

#### Implementation Priority
1. Critical (Score < 40): Immediate action required
2. High (Score < 70): Plan within this sprint
3. Medium (Score < 85): Next sprint
4. Low (Score >= 85): Future enhancement

