"""
Design & Accessibility Expert Knowledge Base - Complete WCAG Certification
=========================================================================
Everything needed to pass: WCAG 2.1 Level AA/AAA, Material Design certification,
and perform professional accessibility audits.

Based on: WCAG 2.1, Material Design, Apple HIG, Inclusive Design Principles
"""

# ============================================================================
# WCAG 2.1 - Complete Level AA & AAA Requirements
# ============================================================================

WCAG_COMPLETE = """
WCAG 2.1 (Web Content Accessibility Guidelines) - Complete Guide:

FOUR PRINCIPLES (POUR):
1. Perceivable: Information must be presentable to users
2. Operable: Interface components must be operable
3. Understandable: Information and operation must be understandable
4. Robust: Content must work with current and future technologies

CONFORMANCE LEVELS:
- Level A: Minimum accessibility (basic)
- Level AA: Acceptable accessibility (REQUIRED for most regulations)
- Level AAA: Optimal accessibility (recommended but not always achievable)

═══════════════════════════════════════════════════════════════════════════
1. PERCEIVABLE - Make content available to senses
═══════════════════════════════════════════════════════════════════════════

1.1 TEXT ALTERNATIVES (Level A):
   Provide text alternatives for non-text content
   
   Images:
   - Informative images: <img src="chart.png" alt="Sales increased 25% in Q4">
   - Decorative images: <img src="decoration.png" alt="">
   - Functional images: <img src="search.png" alt="Search">
   - Complex images: Long description via aria-describedby or longdesc
   
   Icons:
   - With text: aria-hidden="true" on icon, visible text for screen readers
   - Icon-only: <button aria-label="Close">X</button>
   
   Form inputs:
   - Always pair with <label>: <label for="email">Email</label><input id="email">
   - Or use aria-label: <input aria-label="Search products">

1.3 ADAPTABLE (Level A):
   Content can be presented in different ways without losing information
   
   Semantic HTML:
   - Use proper elements: <nav>, <main>, <article>, <aside>, <footer>
   - Heading hierarchy: <h1> → <h2> → <h3> (don't skip levels)
   - Lists: <ul>, <ol>, <dl> for actual lists
   - Tables: <table> with <thead>, <tbody>, <th scope="col">
   
   Reading Order:
   - DOM order = visual order = reading order
   - Don't use CSS to drastically change visual order
   - Tab order should be logical

1.4 DISTINGUISHABLE (Level AA/AAA):
   Make it easy to see and hear content
   
   COLOR CONTRAST (Level AA - CRITICAL):
   Normal Text (< 18pt):
   - Contrast ratio: 4.5:1 minimum
   - Example: #595959 on #FFFFFF = 4.51:1 (PASS)
   - Example: #777777 on #FFFFFF = 4.48:1 (FAIL)
   
   Large Text (≥ 18pt or 14pt bold):
   - Contrast ratio: 3:1 minimum
   - Example: #767676 on #FFFFFF = 4.54:1 (PASS)
   
   UI Components (borders, icons, states):
   - Contrast ratio: 3:1 minimum
   - Example: Button border, form field outline
   
   COLOR CONTRAST (Level AAA):
   Normal Text: 7:1
   Large Text: 4.5:1
   
   Testing Tools:
   - Chrome DevTools: Inspect > Accessibility > Contrast
   - WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
   - Stark plugin for Figma/Sketch
   
   Don't Rely on Color Alone:
   Bad: "Required fields are red"
   Good: "Required fields are marked with * and red border"
   
   Bad: <span style="color: red">Error</span>
   Good: <span class="error" role="alert">⚠️ Error: Invalid email format</span>
   
   Text Sizing:
   - User can resize text to 200% without loss of content/functionality
   - Use relative units (rem, em) not pixels
   - Don't disable zoom: <meta name="viewport" content="user-scalable=yes">

═══════════════════════════════════════════════════════════════════════════
2. OPERABLE - User interface components must be operable
═══════════════════════════════════════════════════════════════════════════

2.1 KEYBOARD ACCESSIBLE (Level A):
   All functionality available via keyboard
   
   Keyboard Navigation:
   - Tab: Move forward through interactive elements
   - Shift+Tab: Move backward
   - Enter: Activate buttons/links
   - Space: Activate buttons, toggle checkboxes
   - Arrow keys: Navigate menus, radio groups, sliders
   
   Focus Indicators (Level AA):
   - Visible focus indicator required
   - Minimum: 2px outline with 3:1 contrast
   
   CSS Example:
   button:focus {
     outline: 3px solid #0066CC;
     outline-offset: 2px;
   }
   
   /* NEVER do this unless providing alternative */
   button:focus {
     outline: none; /* WCAG VIOLATION */
   }
   
   Skip Links (Level A):
   - Bypass repetitive navigation
   <a href="#main-content" class="skip-link">Skip to main content</a>
   
   .skip-link {
     position: absolute;
     top: -40px;
     left: 0;
     background: #000;
     color: #fff;
     padding: 8px;
     z-index: 100;
   }
   .skip-link:focus {
     top: 0;
   }

2.4 NAVIGABLE (Level AA):
   Help users navigate and find content
   
   Page Titles (Level A):
   - Descriptive and unique per page
   - Format: [Page Name] | [Site Name]
   <title>Hardwax Oil Classic - Premium Floor Protection | EMMSO</title>
   
   Link Purpose (Level A):
   Bad: <a href="/products">Click here</a>
   Good: <a href="/products">View all floor care products</a>
   
   Multiple Ways to Find Content (Level AA):
   - Search function
   - Site map
   - Breadcrumb navigation
   - Main navigation menu
   
   Focus Order (Level A):
   - Tab order should match visual order
   - Use tabindex="0" to add to natural tab order
   - Use tabindex="-1" to remove from tab order (still focusable via JS)
   - AVOID tabindex > 0 (creates confusing tab order)

2.5 INPUT MODALITIES (Level A):
   Support various input methods
   
   Touch Target Size (Level AAA, but best practice):
   - Minimum: 44x44 CSS pixels (iOS HIG)
   - Recommended: 48x48 CSS pixels (Material Design)
   
   CSS Example:
   button, a, input, select {
     min-height: 48px;
     min-width: 48px;
     padding: 12px 16px;
   }
   
   /* Mobile-specific */
   @media (max-width: 768px) {
     button {
       min-height: 48px;
       padding: 14px 20px;
     }
   }
   
   Spacing Between Targets:
   - Minimum: 8px spacing between interactive elements
   - Prevents accidental activation

═══════════════════════════════════════════════════════════════════════════
3. UNDERSTANDABLE - Information and operation must be clear
═══════════════════════════════════════════════════════════════════════════

3.1 READABLE (Level A):
   Make text content readable and understandable
   
   Language of Page (Level A):
   <html lang="en">
   
   Language of Parts (Level AA):
   <p>The French phrase <span lang="fr">Bonjour</span> means hello.</p>
   
   Reading Level (Level AAA):
   - Target: 9th grade reading level or lower
   - Use clear, simple language
   - Define jargon and abbreviations
   - Tools: Hemingway Editor, Readable.com

3.2 PREDICTABLE (Level A/AA):
   Web pages appear and operate in predictable ways
   
   Consistent Navigation (Level AA):
   - Navigation in same place on every page
   - Same order of navigation items
   
   Consistent Identification (Level AA):
   - Same icons/labels for same functions
   - Example: Shopping cart icon always means shopping cart
   
   On Focus (Level A):
   - Don't trigger automatic actions on focus
   Bad: Dropdown auto-submits when item receives focus
   Good: Dropdown requires Enter or click to submit

3.3 INPUT ASSISTANCE (Level A/AA):
   Help users avoid and correct mistakes
   
   Error Identification (Level A):
   <div role="alert">
     Error: Email address is required
   </div>
   
   Labels or Instructions (Level A):
   <label for="email">
     Email address *
     <span class="hint">We'll never share your email</span>
   </label>
   <input 
     id="email" 
     type="email" 
     required 
     aria-describedby="email-hint">
   <span id="email-hint" class="hint">
     Format: name@example.com
   </span>
   
   Error Suggestion (Level AA):
   Bad: "Invalid input"
   Good: "Email format is invalid. Example: name@example.com"
   
   Error Prevention (Level AA):
   For legal/financial/data deletion:
   - Reversible: Allow undo
   - Checked: Validate input
   - Confirmed: Require confirmation step
   
   Example:
   <form>
     <button type="submit">Delete Account</button>
   </form>
   
   <!-- Confirmation dialog -->
   <dialog role="alertdialog">
     <h2>Confirm Account Deletion</h2>
     <p>This action cannot be undone. Delete your account?</p>
     <button>Cancel</button>
     <button>Delete Account</button>
   </dialog>

═══════════════════════════════════════════════════════════════════════════
4. ROBUST - Content works with assistive technologies
═══════════════════════════════════════════════════════════════════════════

4.1 COMPATIBLE (Level A):
   Maximize compatibility with current and future tools
   
   Valid HTML (Level A):
   - Use valid, well-formed markup
   - Close all tags properly
   - Unique IDs
   - Proper nesting
   
   Name, Role, Value (Level A):
   All UI components must have:
   - Accessible name (via label, aria-label, aria-labelledby)
   - Role (native HTML or ARIA role)
   - State/value (checked, selected, expanded, etc.)
   
   Example:
   <button 
     aria-label="Close dialog"
     aria-pressed="false"
     role="button">
     X
   </button>
   
   Custom Components:
   <div 
     role="checkbox"
     aria-checked="false"
     aria-labelledby="agree-label"
     tabindex="0">
     <span id="agree-label">I agree to terms</span>
   </div>
"""

# ============================================================================
# ARIA (Accessible Rich Internet Applications)
# ============================================================================

ARIA_COMPLETE = """
ARIA (Accessible Rich Internet Applications) - Complete Guide:

FIRST RULE OF ARIA:
"Don't use ARIA if you can use native HTML"

Bad:  <div role="button" tabindex="0">Click me</div>
Good: <button>Click me</button>

ARIA ATTRIBUTES:

1. ROLES:
   Define what an element is
   
   Landmark Roles:
   <nav role="navigation"> (redundant, nav has implicit role)
   <main role="main">
   <aside role="complementary">
   <header role="banner">
   <footer role="contentinfo">
   <form role="search">
   
   Widget Roles:
   role="button"
   role="checkbox"
   role="dialog"
   role="tab"
   role="tabpanel"
   role="menu"
   role="menuitem"
   role="slider"
   role="progressbar"

2. STATES & PROPERTIES:
   
   aria-label: Provide accessible name
   <button aria-label="Close dialog">X</button>
   
   aria-labelledby: Reference another element's text
   <h2 id="dialog-title">Confirm Purchase</h2>
   <dialog aria-labelledby="dialog-title">...</dialog>
   
   aria-describedby: Additional description
   <input 
     id="password" 
     aria-describedby="password-requirements">
   <span id="password-requirements">
     Must be 8+ characters with number and symbol
   </span>
   
   aria-hidden: Hide from screen readers
   <span aria-hidden="true">★</span> <!-- Decorative star -->
   <span class="sr-only">4.5 out of 5 stars</span>
   
   aria-live: Announce dynamic changes
   <div aria-live="polite">
     Items in cart: 3
   </div>
   
   aria-live values:
   - off: No announcements (default)
   - polite: Announce when user is idle
   - assertive: Announce immediately (use sparingly)
   
   aria-expanded: Expandable UI state
   <button aria-expanded="false" aria-controls="menu">
     Menu
   </button>
   <ul id="menu" hidden>...</ul>
   
   aria-current: Current item in navigation
   <a href="/products" aria-current="page">Products</a>
   
   aria-disabled: Disabled but still focusable
   <button aria-disabled="true">Submit</button>
   
   aria-required: Required field
   <input type="text" aria-required="true">
   (Use required attribute instead when possible)
   
   aria-invalid: Invalid input
   <input type="email" aria-invalid="true" aria-describedby="email-error">
   <span id="email-error" role="alert">Invalid email format</span>

3. COMMON PATTERNS:
   
   Modal Dialog:
   <div 
     role="dialog"
     aria-modal="true"
     aria-labelledby="dialog-title">
     <h2 id="dialog-title">Confirm Action</h2>
     <p>Are you sure?</p>
     <button>Cancel</button>
     <button>Confirm</button>
   </div>
   
   Tabs:
   <div role="tablist" aria-label="Product Information">
     <button role="tab" aria-selected="true" aria-controls="panel-1">
       Description
     </button>
     <button role="tab" aria-selected="false" aria-controls="panel-2">
       Specifications
     </button>
   </div>
   <div role="tabpanel" id="panel-1">...</div>
   <div role="tabpanel" id="panel-2" hidden>...</div>
   
   Accordion:
   <div class="accordion">
     <h3>
       <button 
         aria-expanded="false"
         aria-controls="section1">
         Section 1
       </button>
     </h3>
     <div id="section1" hidden>
       Content...
     </div>
   </div>
   
   Alert/Status:
   <div role="alert">
     Form submitted successfully!
   </div>
   
   <div role="status" aria-live="polite">
     Loading... 50% complete
   </div>
"""


# ============================================================================
# MATERIAL DESIGN 3 - Complete Design System
# ============================================================================

MATERIAL_DESIGN = """
Material Design 3 (2025) - Complete Design System:

CORE PRINCIPLES:
1. Material is the metaphor
2. Bold, graphic, intentional
3. Motion provides meaning

═══════════════════════════════════════════════════════════════════════════
1. COLOR SYSTEM
═══════════════════════════════════════════════════════════════════════════

Dynamic Color (Material You):
- Generated from single seed color
- Adapts to user preferences
- Light and dark theme support

Color Roles:
- Primary: Main brand color (buttons, active states)
- Secondary: Accent color (FABs, highlights)
- Tertiary: Contrasting accent
- Error: Error states, destructive actions
- Surface: Backgrounds, cards
- On-Surface: Text on surfaces

Tonal Palette (0-100):
0: Black
10: Very dark
20: Dark
30: Medium dark
40: Medium
50: Base color
60: Medium light
70: Light
80: Very light
90: Extremely light
95: Near white
99: Almost white
100: White

Example CSS:
:root {
  /* Primary */
  --md-sys-color-primary: #6750A4;
  --md-sys-color-on-primary: #FFFFFF;
  --md-sys-color-primary-container: #EADDFF;
  --md-sys-color-on-primary-container: #21005E;
  
  /* Secondary */
  --md-sys-color-secondary: #625B71;
  --md-sys-color-on-secondary: #FFFFFF;
  
  /* Surface */
  --md-sys-color-surface: #FFFBFE;
  --md-sys-color-on-surface: #1C1B1F;
  
  /* Error */
  --md-sys-color-error: #B3261E;
  --md-sys-color-on-error: #FFFFFF;
}

[data-theme="dark"] {
  --md-sys-color-primary: #D0BCFF;
  --md-sys-color-on-primary: #381E72;
  --md-sys-color-surface: #1C1B1F;
  --md-sys-color-on-surface: #E6E1E5;
}

═══════════════════════════════════════════════════════════════════════════
2. TYPOGRAPHY
═══════════════════════════════════════════════════════════════════════════

Type Scale (Material Design 3):

Display Large:
- Size: 57px / 3.5625rem
- Line height: 64px
- Weight: 400 (Regular)
- Use: Large, short, important text

Display Medium: 45px / 2.8125rem
Display Small: 36px / 2.25rem

Headline Large: 32px / 2rem
Headline Medium: 28px / 1.75rem
Headline Small: 24px / 1.5rem

Title Large: 22px / 1.375rem (page titles)
Title Medium: 16px / 1rem
Title Small: 14px / 0.875rem

Body Large: 16px / 1rem (default body text)
Body Medium: 14px / 0.875rem
Body Small: 12px / 0.75rem

Label Large: 14px / 0.875rem (buttons)
Label Medium: 12px / 0.75rem
Label Small: 11px / 0.6875rem

CSS Example:
.display-large {
  font-size: 3.5625rem;
  line-height: 4rem;
  font-weight: 400;
  letter-spacing: -0.25px;
}

.headline-medium {
  font-size: 1.75rem;
  line-height: 2.25rem;
  font-weight: 400;
  letter-spacing: 0;
}

.body-large {
  font-size: 1rem;
  line-height: 1.5rem;
  font-weight: 400;
  letter-spacing: 0.5px;
}

Font Recommendations:
- Roboto (Google's default)
- Roboto Flex (variable font)
- Custom brand fonts allowed

═══════════════════════════════════════════════════════════════════════════
3. SPACING & LAYOUT
═══════════════════════════════════════════════════════════════════════════

8px Grid System:
Base unit: 8px (0.5rem)

Spacing Scale:
4px   (0.25rem) - Tight spacing
8px   (0.5rem)  - Default spacing
12px  (0.75rem) - Comfortable spacing
16px  (1rem)    - Section spacing
24px  (1.5rem)  - Large spacing
32px  (2rem)    - Very large spacing
48px  (3rem)    - Page sections
64px  (4rem)    - Major sections

CSS Variables:
:root {
  --spacing-xs: 0.25rem;  /* 4px */
  --spacing-sm: 0.5rem;   /* 8px */
  --spacing-md: 1rem;     /* 16px */
  --spacing-lg: 1.5rem;   /* 24px */
  --spacing-xl: 2rem;     /* 32px */
  --spacing-2xl: 3rem;    /* 48px */
}

Responsive Breakpoints:
- Compact: 0-599px (phone)
- Medium: 600-839px (tablet portrait)
- Expanded: 840-1199px (tablet landscape, small laptop)
- Large: 1200-1599px (desktop)
- Extra Large: 1600px+ (large desktop)

@media (max-width: 599px) {  /* Compact */
  .container { padding: 1rem; }
}

@media (min-width: 600px) and (max-width: 839px) {  /* Medium */
  .container { padding: 1.5rem; }
}

@media (min-width: 840px) {  /* Expanded+ */
  .container { padding: 2rem; }
}

═══════════════════════════════════════════════════════════════════════════
4. COMPONENTS
═══════════════════════════════════════════════════════════════════════════

Buttons:
Filled Button (primary action):
.md-filled-button {
  background: var(--md-sys-color-primary);
  color: var(--md-sys-color-on-primary);
  padding: 10px 24px;
  height: 40px;
  border-radius: 20px; /* Fully rounded */
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.1px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.3);
}

.md-filled-button:hover {
  box-shadow: 0 1px 3px rgba(0,0,0,0.4);
}

Outlined Button (secondary action):
.md-outlined-button {
  background: transparent;
  color: var(--md-sys-color-primary);
  border: 1px solid var(--md-sys-color-outline);
  padding: 10px 24px;
  height: 40px;
  border-radius: 20px;
}

Text Button (low priority):
.md-text-button {
  background: transparent;
  color: var(--md-sys-color-primary);
  padding: 10px 12px;
  height: 40px;
}

Cards:
.md-card {
  background: var(--md-sys-color-surface);
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12),
              0 1px 2px rgba(0,0,0,0.24);
}

.md-card:hover {
  box-shadow: 0 3px 6px rgba(0,0,0,0.16),
              0 3px 6px rgba(0,0,0,0.23);
}

Elevation (Shadows):
Level 0: none
Level 1: 0 1px 2px rgba(0,0,0,0.3)
Level 2: 0 1px 3px rgba(0,0,0,0.4)
Level 3: 0 4px 8px rgba(0,0,0,0.3)
Level 4: 0 6px 10px rgba(0,0,0,0.3)
Level 5: 0 8px 12px rgba(0,0,0,0.3)
"""

# ============================================================================
# MOBILE-FIRST DESIGN - Complete Guide
# ============================================================================

MOBILE_FIRST_COMPLETE = """
Mobile-First Design - Complete Implementation (2025):

WHY MOBILE-FIRST:
- 60%+ of web traffic is mobile
- Google uses mobile version for ranking (Mobile-First Indexing)
- Easier to enhance than to simplify
- Forces focus on core content/features

═══════════════════════════════════════════════════════════════════════════
1. TOUCH TARGETS & THUMB ZONES
═══════════════════════════════════════════════════════════════════════════

Minimum Touch Target Size:
- Apple HIG: 44x44pt (44x44px @ 1x)
- Material Design: 48x48dp (48x48px)
- WCAG 2.1 AAA: 44x44px
- Recommended: 48x48px minimum

CSS:
button, a, input[type="checkbox"], input[type="radio"] {
  min-width: 48px;
  min-height: 48px;
  /* or */
  padding: 12px 16px; /* Ensures 48px height */
}

Touch Target Spacing:
- Minimum: 8px between targets
- Recommended: 12-16px between critical actions

.button-group button {
  margin: 0 8px;
}

Thumb Zones (One-Handed Use):
Easy to Reach (Natural Thumb Arc):
- Bottom 1/3 of screen
- Center horizontally
- Place primary actions here

Hard to Reach:
- Top corners
- Opposite side from thumb
- Place secondary/less important actions

Example Layout:
┌─────────────────┐
│  Secondary Nav  │ ← Hard to reach
│                 │
│                 │
│  Content Area   │ ← Comfortable
│                 │
│                 │
│ [Primary Btn]   │ ← Easy to reach (thumb zone)
│ Bottom Nav ▼    │ ← Easy to reach
└─────────────────┘

Navigation Placement:
Bottom Navigation (Modern):
<nav class="bottom-nav">
  <a href="/">Home</a>
  <a href="/search">Search</a>
  <a href="/cart">Cart</a>
  <a href="/account">Account</a>
</nav>

.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 56px;
  display: flex;
  justify-content: space-around;
  background: var(--surface);
  box-shadow: 0 -2px 4px rgba(0,0,0,0.1);
}

.bottom-nav a {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-width: 48px;
  padding: 8px;
}

═══════════════════════════════════════════════════════════════════════════
2. RESPONSIVE TYPOGRAPHY
═══════════════════════════════════════════════════════════════════════════

Fluid Typography (clamp):
h1 {
  font-size: clamp(1.75rem, 5vw, 3rem);
  /* Min: 28px, Scales with viewport, Max: 48px */
}

body {
  font-size: clamp(1rem, 2.5vw, 1.125rem);
  /* Min: 16px, Max: 18px */
}

Mobile-Specific Font Sizes:
- Minimum body text: 16px (prevents zoom on iOS)
- Headings: Scale appropriately for screen size
- Line height: 1.5-1.6 for readability

/* Base (Mobile) */
body { font-size: 16px; line-height: 1.5; }
h1 { font-size: 1.75rem; }
h2 { font-size: 1.5rem; }

/* Tablet */
@media (min-width: 768px) {
  body { font-size: 17px; }
  h1 { font-size: 2.25rem; }
  h2 { font-size: 1.875rem; }
}

/* Desktop */
@media (min-width: 1024px) {
  body { font-size: 18px; }
  h1 { font-size: 3rem; }
  h2 { font-size: 2.25rem; }
}

═══════════════════════════════════════════════════════════════════════════
3. MOBILE PERFORMANCE
═══════════════════════════════════════════════════════════════════════════

Critical Rendering Path:
1. Inline critical CSS in <head>
2. Defer non-critical CSS
3. Defer JavaScript
4. Lazy load images below fold

<head>
  <style>
    /* Critical CSS: Above-fold styles */
    .header { ... }
    .hero { ... }
  </style>
  
  <!-- Async load non-critical CSS -->
  <link rel="preload" href="non-critical.css" as="style" 
        onload="this.onload=null;this.rel='stylesheet'">
</head>

Touch-Friendly Interactions:
- Instant visual feedback on tap
- No :hover-dependent functionality
- Use :active for touch feedback

button:active {
  transform: scale(0.95);
  background: var(--primary-dark);
}

Avoid Horizontal Scrolling:
- Max width: 100vw
- Images: max-width: 100%
- Tables: overflow-x: auto wrapper

.table-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

═══════════════════════════════════════════════════════════════════════════
4. MOBILE FORMS
═══════════════════════════════════════════════════════════════════════════

Input Types (triggers appropriate keyboard):
<input type="email">       <!-- @ key prominent -->
<input type="tel">         <!-- Number pad -->
<input type="number">      <!-- Number keyboard -->
<input type="url">         <!-- .com key -->
<input type="search">      <!-- Search/go button -->
<input type="date">        <!-- Date picker -->

Input Mode (finer control):
<input inputmode="numeric">     <!-- Numbers only -->
<input inputmode="decimal">     <!-- Numbers + decimal -->
<input inputmode="email">       <!-- Email keyboard -->
<input inputmode="tel">         <!-- Phone keyboard -->

Form Best Practices:
- Large input fields: min 48px height
- Clear labels above inputs (not placeholders)
- Inline validation with helpful errors
- Autofocus first field (mobile: use sparingly)
- Autocomplete attributes

<form>
  <label for="email">Email</label>
  <input 
    id="email"
    type="email"
    autocomplete="email"
    required>
  
  <label for="phone">Phone</label>
  <input 
    id="phone"
    type="tel"
    autocomplete="tel"
    inputmode="tel">
  
  <button type="submit">Submit</button>
</form>

input {
  width: 100%;
  height: 48px;
  padding: 12px 16px;
  font-size: 16px; /* Prevents iOS zoom */
  border: 2px solid var(--border);
  border-radius: 4px;
}
"""


# ============================================================================
# DARK MODE - Complete Implementation
# ============================================================================

DARK_MODE = """
Dark Mode Implementation - Best Practices (2025):

WHY DARK MODE:
- Reduces eye strain in low light
- Saves battery (OLED screens)
- User preference (accessibility)
- Modern expectation

═══════════════════════════════════════════════════════════════════════════
1. COLOR ADAPTATIONS
═══════════════════════════════════════════════════════════════════════════

Don't Just Invert:
Bad: Use pure black (#000) backgrounds
Good: Use dark gray (#121212) - easier on eyes

Material Design Dark Theme:
Surface colors:
- Surface: #121212 (base background)
- Surface +1dp: #1E1E1E
- Surface +2dp: #232323
- Surface +4dp: #272727
- Surface +8dp: #2C2C2C

Higher elevation = lighter surface

Text colors:
- High emphasis: White 87% opacity (#FFFFFF DE)
- Medium emphasis: White 60% opacity (#FFFFFF 99)
- Disabled: White 38% opacity (#FFFFFF 61)

CSS Implementation:
:root {
  --surface: #FFFFFF;
  --on-surface: #000000;
  --primary: #6200EE;
  --on-primary: #FFFFFF;
}

[data-theme="dark"] {
  --surface: #121212;
  --on-surface: rgba(255, 255, 255, 0.87);
  --primary: #BB86FC; /* Lighter primary for dark mode */
  --on-primary: #000000;
}

Color Adjustments for Dark Mode:
- Use desaturated colors (avoid pure saturated colors)
- Increase color contrast
- Test with color blindness simulators

═══════════════════════════════════════════════════════════════════════════
2. IMPLEMENTATION METHODS
═══════════════════════════════════════════════════════════════════════════

A) CSS Variables (Recommended):
<html data-theme="light">

[data-theme="light"] {
  --bg: #FFFFFF;
  --text: #000000;
}

[data-theme="dark"] {
  --bg: #121212;
  --text: rgba(255,255,255,0.87);
}

body {
  background: var(--bg);
  color: var(--text);
}

B) Prefers-Color-Scheme (Auto-detect):
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #121212;
    --text: rgba(255,255,255,0.87);
  }
}

C) Combined Approach (Best):
:root {
  color-scheme: light dark; /* Tells browser about support */
}

/* Default (Light) */
:root {
  --bg: #FFFFFF;
  --text: #000000;
}

/* Auto dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #121212;
    --text: rgba(255,255,255,0.87);
  }
}

/* User override */
[data-theme="dark"] {
  --bg: #121212;
  --text: rgba(255,255,255,0.87);
}

Toggle JavaScript:
<button id="theme-toggle" aria-label="Toggle dark mode">
  🌙
</button>

<script>
const toggle = document.getElementById('theme-toggle');
const htmlElement = document.documentElement;

// Check saved preference
const savedTheme = localStorage.getItem('theme') || 'auto';
if (savedTheme !== 'auto') {
  htmlElement.setAttribute('data-theme', savedTheme);
}

toggle.addEventListener('click', () => {
  const current = htmlElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  
  htmlElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
});
</script>

═══════════════════════════════════════════════════════════════════════════
3. IMAGES & MEDIA
═══════════════════════════════════════════════════════════════════════════

Picture Element for Dark Mode:
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="logo-light.svg" alt="Logo">
</picture>

SVG with CSS Variables:
<svg>
  <rect fill="var(--primary)" />
</svg>

Image Adjustments in CSS:
@media (prefers-color-scheme: dark) {
  img {
    opacity: 0.8; /* Slightly dim images */
    filter: brightness(0.9);
  }
  
  img.product-photo {
    opacity: 1; /* Keep product images bright */
  }
}
"""

# ============================================================================
# TESTING & VALIDATION
# ============================================================================

ACCESSIBILITY_TESTING = """
Accessibility Testing - Complete Toolkit:

═══════════════════════════════════════════════════════════════════════════
1. AUTOMATED TESTING TOOLS
═══════════════════════════════════════════════════════════════════════════

Browser DevTools:
Chrome Lighthouse:
- Open DevTools > Lighthouse tab
- Select "Accessibility" category
- Run audit
- Shows WCAG violations with fixes

Chrome DevTools Accessibility:
- Inspect element
- Accessibility pane shows:
  * Accessible name
  * Role
  * Contrast ratio
  * ARIA attributes

Firefox Accessibility Inspector:
- DevTools > Accessibility tab
- Visual tree of accessible elements
- Check for issues
- Simulate color blindness

Browser Extensions:
axe DevTools (Free):
- Install from Chrome Web Store
- Run automated accessibility scan
- Detailed violation reports
- Guided fixes

WAVE (WebAIM):
- Visual feedback on page
- Shows errors, alerts, features
- Color contrast checker
- Structure analysis

Online Tools:
WAVE by WebAIM: https://wave.webaim.org
- Enter URL
- Get comprehensive report
- Visual indicators on page

WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Test color combinations
- Meets WCAG AA/AAA?
- Suggestions for passing

Color Safe: http://colorsafe.co
- Generate accessible color palettes
- Based on WCAG contrast ratios

Who Can Use: https://www.whocanuse.com
- Test color combinations
- Shows how different people see colors
- Visual simulations

═══════════════════════════════════════════════════════════════════════════
2. MANUAL TESTING
═══════════════════════════════════════════════════════════════════════════

Keyboard Navigation Test:
1. Unplug mouse/trackpad
2. Navigate using only keyboard:
   - Tab: Forward
   - Shift+Tab: Backward
   - Enter: Activate buttons/links
   - Space: Activate buttons, toggle checkboxes
   - Arrow keys: Menus, radio groups
3. Verify:
   - Can reach all interactive elements?
   - Focus indicator visible?
   - Logical tab order?
   - No keyboard traps?

Screen Reader Test:
macOS: VoiceOver (Cmd+F5)
Windows: NVDA (free) or JAWS
iOS: VoiceOver (Settings > Accessibility)
Android: TalkBack

Basic commands:
- VoiceOver: Control+Option+Arrow keys to navigate
- NVDA: Insert+Arrow keys
- Check:  * All content readable?
  * Images have alt text?
  * Forms have labels?
  * Dynamic content announced?
  * Heading structure logical?

Zoom Test:
1. Zoom browser to 200%
2. Check:
   - Content still visible?
   - No horizontal scrolling?
   - Interactive elements still usable?
   - Text doesn't overlap?

Color Blindness Simulation:
Chrome DevTools:
- Rendering tab > "Emulate vision deficiencies"
- Test: Protanopia, Deuteranopia, Tritanopia
- Verify: All information still accessible?

Mobile Touch Test:
1. Test on real device (emulators not enough)
2. Check:
   - Touch targets 48x48px minimum?
   - Sufficient spacing between targets?
   - No accidental activations?
   - Zoom works properly?

═══════════════════════════════════════════════════════════════════════════
3. CHECKLIST
═══════════════════════════════════════════════════════════════════════════

Visual/Perception:
□ Color contrast 4.5:1 for text (AA)
□ Color contrast 3:1 for UI components (AA)
□ Don't rely on color alone for information
□ Text resizable to 200%
□ Touch targets minimum 48x48px

Keyboard:
□ All functionality keyboard accessible
□ Visible focus indicators (3px, 3:1 contrast)
□ Logical tab order
□ No keyboard traps
□ Skip links present

Content:
□ Page has descriptive title
□ Headings used correctly (H1-H6)
□ Landmark regions (nav, main, etc.)
□ Link text descriptive ("Read more about X", not "Click here")
□ Images have alt text (decorative images alt="")

Forms:
□ All inputs have labels
□ Error messages clear and helpful
□ Required fields indicated
□ Validation errors announced
□ Confirmation for destructive actions

Dynamic Content:
□ Status messages use role="status" or aria-live
□ Loading states communicated
□ Errors use role="alert"
□ Content changes announced to screen readers

ARIA:
□ Prefer native HTML over ARIA
□ ARIA roles used correctly
□ States and properties accurate
□ Dynamic ARIA updates work
"""

# ============================================================================
# HELPER FUNCTION
# ============================================================================

def get_recommendation(topic, current_score=None):
    """
    Generate design/accessibility recommendation based on topic and score
    
    Args:
        topic (str): Design aspect (contrast, touch_targets, typography, mobile, etc.)
        current_score (float, optional): Current score/value
    
    Returns:
        list: Prioritized recommendations for improvement
    """
    recommendations = {
        'contrast': [
            'CRITICAL: Increase color contrast to meet WCAG AA (4.5:1 for normal text)',
            'Test with Chrome DevTools contrast checker (Inspect > Accessibility)',
            'Use WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/',
            'Avoid gray text on light backgrounds (common violation)',
            'Test with color blindness simulators (Chrome DevTools > Rendering)'
        ],
        'touch_targets': [
            'CRITICAL: Increase button size to 48x48px minimum (Material Design)',
            'Add sufficient padding around interactive elements (12-16px)',
            'Ensure 8-12px spacing between adjacent touch targets',
            'Test on actual mobile devices (not just emulators)',
            'Use Chrome DevTools mobile view to verify sizes'
        ],
        'typography': [
            'Use minimum 16px base font size (prevents iOS zoom)',
            'Implement clear heading hierarchy (H1 → H2 → H3)',
            'Improve line height (1.5-1.6 for body text)',
            'Limit line length (50-75 characters for readability)',
            'Use relative units (rem, em) instead of pixels'
        ],
        'mobile': [
            'Optimize for thumb-friendly navigation (bottom 1/3 of screen)',
            'Place primary actions in thumb zone (easy to reach)',
            'Increase touch target sizes to 48x48px',
            'Test on multiple device sizes and orientations',
            'Ensure no horizontal scrolling (max-width: 100vw)'
        ],
        'keyboard': [
            'CRITICAL: Ensure all functionality keyboard accessible',
            'Add visible focus indicators (3px outline, 3:1 contrast)',
            'Implement skip links for navigation bypass',
            'Test with keyboard only (unplug mouse)',
            'Verify logical tab order matches visual order'
        ],
        'aria': [
            'Use native HTML elements instead of ARIA when possible',
            'Add aria-label to icon-only buttons',
            'Use role="alert" for error messages',
            'Implement aria-live for dynamic content updates',
            'Test with screen reader (VoiceOver/NVDA)'
        ],
        'dark_mode': [
            'Use dark gray (#121212) not pure black for backgrounds',
            'Adjust colors: lighter primary, desaturated colors',
            'Test contrast ratios in dark mode (higher contrast needed)',
            'Provide theme toggle with localStorage persistence',
            'Use CSS custom properties for easy theme switching'
        ],
        'forms': [
            'Associate all inputs with labels (for/id or aria-label)',
            'Use appropriate input types (email, tel, number)',
            'Provide helpful error messages with suggestions',
            'Indicate required fields clearly (* and aria-required)',
            'Implement inline validation with aria-invalid'
        ],
        'wcag': [
            'Run Lighthouse accessibility audit',
            'Install axe DevTools for automated testing',
            'Test keyboard navigation (Tab, Shift+Tab, Enter, Space)',
            'Test with screen reader (VoiceOver on Mac/iOS)',
            'Check color contrast for all text/UI elements'
        ]
    }
    
    topic_lower = topic.lower()
    
    if topic_lower not in recommendations:
        return [f'Review {topic} against WCAG 2.1 Level AA guidelines']
    
    return recommendations[topic_lower][:5]  # Top 5 recommendations


def get_expert_knowledge():
    """
    Returns complete Design & Accessibility expert knowledge as single string
    
    Use this for AI/LLM context when generating design/accessibility recommendations.
    Contains complete certification-level knowledge covering:
    - WCAG 2.1 (Level A, AA, AAA)
    - ARIA best practices
    - Material Design 3 (Material You)
    - Mobile-first responsive design
    - Dark mode implementation
    - Accessibility testing
    
    Returns:
        str: Complete knowledge base (~50,000 tokens)
    """
    return "\n\n".join([
        "DESIGN & ACCESSIBILITY EXPERT KNOWLEDGE BASE",
        "=" * 80,
        WCAG_COMPLETE,
        ARIA_COMPLETE,
        MATERIAL_DESIGN,
        MOBILE_FIRST_COMPLETE,
        DARK_MODE,
        ACCESSIBILITY_TESTING
    ])


