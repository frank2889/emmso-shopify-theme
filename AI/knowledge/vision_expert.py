"""
Vision Expert Knowledge Base
============================
Expert knowledge for GPT-4 Vision analysis of e-commerce websites
Focus: UX/UI best practices, conversion optimization, visual accessibility

This knowledge base provides comprehensive expertise for visual analysis of 
e-commerce websites through automated screenshot analysis.
"""

# UX/UI Best Practices for E-commerce
UX_UI_PRINCIPLES = """
E-COMMERCE UX/UI BEST PRACTICES
================================

VISUAL HIERARCHY:
- F-Pattern Reading: Most important content in top-left, navigation top, product images left
- Z-Pattern Layout: Homepage/landing pages follow Z-pattern for scan path
- Size & Scale: Larger elements draw more attention (use for CTA, hero products)
- Color Contrast: High contrast for CTAs (3:1 minimum), critical actions stand out
- White Space: Generous spacing improves comprehension (minimum 16px between elements)
- Typography Hierarchy: Clear distinction between H1 (32-48px), H2 (24-32px), body (16-18px)

ABOVE-THE-FOLD CRITICAL ELEMENTS:
- Logo (top-left, clickable to homepage)
- Navigation menu (persistent, accessible)
- Search bar (prominent, autocomplete enabled)
- Cart icon with item count (top-right)
- Hero message/value proposition (within 1200px width, 600px height)
- Primary CTA visible without scrolling
- Trust signals (free shipping, returns, certifications)

CONVERSION OPTIMIZATION:
- CTA Buttons: Minimum 44x44px (touch targets), action-oriented text ("Add to Cart" not "Submit")
- Color Psychology: Green (go, success), Red (urgency, sale), Blue (trust), Orange (action)
- Visual Consistency: Repeated UI patterns reduce cognitive load
- Scarcity Indicators: "Only 3 left", "Limited time" with visual emphasis
- Social Proof: Customer photos, ratings visible on product cards
- Progress Indicators: Multi-step checkout shows current step + total steps

MOBILE-FIRST DESIGN:
- Touch Targets: Minimum 48x48px for interactive elements
- Thumb Zone: Primary actions in bottom 1/3 of screen (easy reach)
- Single Column Layout: Stack elements vertically on mobile
- Hamburger Menu: 3-line icon (24x24px minimum) top-right or top-left
- Sticky Elements: Fixed header with cart/search, sticky Add to Cart
- Mobile Viewport: Optimize for 375px width (iPhone standard)
"""

# Visual Accessibility (WCAG AAA where possible)
VISUAL_ACCESSIBILITY = """
VISUAL ACCESSIBILITY STANDARDS
===============================

COLOR CONTRAST (WCAG 2.1):
- WCAG AA (Minimum): 4.5:1 for normal text, 3:1 for large text (18pt+)
- WCAG AAA (Enhanced): 7:1 for normal text, 4.5:1 for large text
- Non-text Contrast: 3:1 for UI components (buttons, form borders, icons)
- Disable-state: 3:1 contrast for disabled elements (maintain visibility)

TEXT READABILITY:
- Line Length: 50-75 characters per line (optimal reading)
- Line Height: 1.5x font size minimum (improves scanability)
- Font Size: 16px minimum body text, 14px absolute minimum
- Font Weight: 400 (regular) for body, 600-700 (semibold/bold) for headings
- Letter Spacing: 0.12em for all caps text
- Avoid: Full justification (creates rivers), light text on light backgrounds

FOCUS INDICATORS:
- Visible Focus: 2px solid outline, 3:1 contrast with background
- Focus Order: Logical tab order (top-to-bottom, left-to-right)
- Skip Links: "Skip to main content" link at page top
- Keyboard Navigation: All interactive elements accessible via Tab/Shift+Tab
- Focus Trap: Modal dialogs trap focus until closed

COLOR-BLIND CONSIDERATIONS:
- Never use color alone to convey information (add icons, labels)
- Deuteranopia (green-blind): Avoid green/red combinations
- Protanopia (red-blind): Avoid red/brown combinations
- Tritanopia (blue-blind): Avoid blue/yellow combinations
- Test Tools: Color Oracle, Coblis, browser DevTools color vision simulators

RESPONSIVE IMAGES:
- Alt Text: Descriptive (not "image.jpg"), <125 characters, conveys same info as image
- Decorative Images: Use empty alt="" or CSS background images
- Complex Images: Provide long descriptions via aria-describedby or adjacent text
- Responsive Sizing: Use srcset for multiple resolutions, sizes attribute for layout
- Loading Strategy: loading="eager" above fold, loading="lazy" below fold
"""

# E-commerce Visual Patterns
ECOMMERCE_PATTERNS = """
E-COMMERCE VISUAL PATTERNS
===========================

HOMEPAGE PATTERNS:
- Hero Section: Full-width image/video + headline + CTA (50-70% viewport height)
- Featured Products Grid: 3-4 products per row desktop, 2 per row tablet, 1 per row mobile
- Category Banners: Large clickable images with category name overlay
- Social Proof Section: Customer reviews, Instagram feed, testimonials
- Newsletter Signup: Email capture with benefit ("Get 10% off"), above footer
- Trust Badges: Payment icons, security seals, shipping guarantees in footer area

PRODUCT LISTING PAGE (PLP):
- Filter Sidebar: Left column 250-300px wide, collapsible on mobile
- Sort Options: Dropdown top-right ("Price: Low to High", "Best Selling", "Newest")
- Product Grid: 3-4 columns desktop, 2 tablet, 1 mobile with consistent card heights
- Product Cards: Image (square aspect ratio), title, price, rating, quick-add button
- Pagination: Bottom center with numbered pages + "Previous/Next"
- Active Filters: Removable tags showing current selections

PRODUCT DETAIL PAGE (PDP):
- Image Gallery: Left 50-60% width, thumbnails below or vertical strip
- Product Info: Right 40-50% width with title, price, reviews, description
- Add to Cart: Prominent button (green/orange), quantity selector above
- Product Options: Variant selector (color swatches, size dropdown) before Add to Cart
- Tabs/Accordion: Description, Specs, Reviews, Shipping in collapsed sections
- Related Products: "You May Also Like" carousel at bottom
- Sticky Add to Cart: Mobile sticky bar at bottom when scrolled past main button

CART PAGE:
- Cart Items: Table/list with product image, name, quantity adjuster, price, remove button
- Cart Summary: Right sidebar with subtotal, shipping estimate, total, checkout CTA
- Continue Shopping: Link back to store
- Upsells: "Frequently Bought Together" or "Complete the Look" suggestions
- Progress Indicator: Visual steps (Cart → Shipping → Payment → Complete)

CHECKOUT FLOW:
- Single Column Form: 600px max width, centered
- Express Checkout: Apple Pay, Shop Pay buttons at top (one-click checkout)
- Form Labels: Above inputs, not placeholders
- Validation: Inline error messages, red borders on invalid fields
- Trust Signals: Security icons, money-back guarantee, secure checkout badge
- Order Summary: Sticky sidebar or collapsible section showing cart contents

NAVIGATION PATTERNS:
- Mega Menu: Dropdown with categories, subcategories, featured products (900-1200px wide)
- Breadcrumbs: Below header (Home > Category > Product)
- Sticky Header: Header remains visible on scroll with condensed height
- Search Autocomplete: Shows suggested products, categories as you type
- Mobile Menu: Full-screen overlay or slide-in drawer with nested subcategories
"""

# Conversion Rate Optimization Visual Cues
CRO_VISUAL_CUES = """
CONVERSION RATE OPTIMIZATION (CRO)
===================================

TRUST BUILDING VISUAL ELEMENTS:
- Customer Photos: Real user-generated content (Instagram grid, reviews)
- Security Badges: SSL certificates, payment provider logos (Visa, Mastercard, PayPal)
- Guarantees: "30-Day Money Back", "Free Returns", "Lifetime Warranty" badges
- Press Mentions: "As Seen In" logos (Forbes, TechCrunch, Vogue)
- Awards: "Best of 2024", "Editor's Choice" badges with recognizable icons
- Live Visitor Count: "127 people viewing this product" (subtle, not intrusive)

URGENCY & SCARCITY TACTICS:
- Stock Counter: "Only 3 left in stock" in orange/red text
- Timer: Countdown clock for sales with contrasting colors
- Limited Edition: Badge on product images ("Limited", "Exclusive")
- Recently Purchased: "John from New York bought this 2 hours ago"
- Fast-Moving: "12 sold in the last 24 hours" indicator
- Sale Badge: Red corner ribbon with "SALE" or "50% OFF"

VISUAL CTA OPTIMIZATION:
- Button Size: Minimum 44x44px, ideally 48-60px height for prominence
- Button Color: Contrasts with background (green on white, orange on blue)
- Button Text: Action verb + benefit ("Add to Cart", "Start Free Trial", "Get My Discount")
- Hover States: Color change, slight elevation (box-shadow), scale increase
- Icon Usage: Cart icon in "Add to Cart", arrow in "Continue", checkmark in "Complete"
- Button Placement: Right-aligned for forward actions, left for back/cancel

PRODUCT IMAGE OPTIMIZATION:
- Primary Image: Square ratio (1:1), white background, product centered
- Hover Effect: Show alternate view on hover (lifestyle shot or back view)
- Zoom Functionality: Magnifying glass icon, click to expand
- Multiple Angles: Minimum 3 images (front, back, detail shot)
- Lifestyle Images: Product in use, shows scale and context
- Video: Autoplay muted video showing product features (15-30 seconds)

TYPOGRAPHY FOR CONVERSION:
- Price Display: Larger font (24-36px), bold weight, contrasting color
- Strike-through Price: Original price with line-through next to sale price
- Savings Calculation: "Save $45 (30%)" in green text
- Product Title: Clear hierarchy (H1, 24-32px), benefit-focused when possible
- Reviews Count: "(247 reviews)" in smaller, secondary color text next to stars
- Urgency Text: Red or orange text for limited offers, slightly larger than body

LAYOUT PATTERNS THAT CONVERT:
- F-Pattern: Logo top-left, menu top, main CTA left column
- Z-Pattern: Hero headline top-left, image top-right, CTA bottom-left
- Grid Symmetry: Even spacing between products builds trust
- Visual Weight: Larger, bolder CTAs draw eye before secondary actions
- Progressive Disclosure: Show essentials first, details in tabs/accordion
- Exit-Intent: Modal popup when mouse moves toward browser close (offer discount)
"""

# Mobile-Specific Visual Patterns
MOBILE_PATTERNS = """
MOBILE-SPECIFIC VISUAL PATTERNS
================================

MOBILE NAVIGATION:
- Hamburger Menu: 3 horizontal lines, 24x24px minimum, top-left or top-right
- Bottom Navigation: 4-5 icons (Home, Search, Cart, Account) sticky at bottom
- Swipe Gestures: Left/right swipe for product image galleries
- Pull-to-Refresh: Drag down to reload page (visual loading indicator)
- Back Button: Always provide in-app back navigation (don't rely on browser back)

MOBILE PRODUCT PAGES:
- Full-Width Images: Edge-to-edge product photos
- Sticky Add to Cart: Fixed bar at bottom with price + CTA
- Thumb-Friendly CTAs: Bottom 1/3 of screen for primary actions
- Collapsible Sections: Accordion for Description, Reviews, Specs (conserve space)
- Quick Add: From PLP, tap product card opens mini-modal with size/color selector
- Image Carousel: Swipeable with dots indicator at bottom

MOBILE FORMS:
- Single Column: Stack all form fields vertically
- Large Input Fields: Minimum 44px height for easy tapping
- Input Types: Use HTML5 types (type="tel", type="email") for optimized keyboards
- Autofill: Enable with autocomplete attributes (autocomplete="shipping street-address")
- Inline Validation: Check as user types, not just on submit
- Show Password: Toggle eye icon to reveal password input

MOBILE CHECKOUT:
- One Field Per Row: Full width for each input
- Mobile Wallets First: Apple Pay, Google Pay buttons at top (50-60% mobile conversions)
- Progress Indicator: Numbered steps at top (1. Shipping → 2. Payment → 3. Review)
- Collapsible Cart: Order summary collapses to single line with expand button
- Fixed CTA: "Place Order" button always visible (sticky to bottom)
- Minimal Distractions: Hide header/footer, focus only on checkout flow

PERFORMANCE INDICATORS:
- Loading Skeletons: Gray placeholders matching layout while content loads
- Image Lazy Loading: Load images as user scrolls (improves initial load)
- Progress Spinners: Centered spinner for async actions (adding to cart, loading more)
- Optimistic UI: Immediately show success state, rollback if error
- Pull-to-Refresh: Visual indicator (arrow, spinner) during refresh
"""

# Visual Testing Checklist
VISUAL_TESTING = """
VISUAL TESTING CHECKLIST
=========================

LAYOUT TESTING:
☐ Content fits within viewport (no horizontal scroll on mobile)
☐ Breakpoints work correctly (test 320px, 375px, 768px, 1024px, 1440px)
☐ Images maintain aspect ratio across devices
☐ Text remains readable at all screen sizes (minimum 16px)
☐ Navigation accessible at all breakpoints
☐ Sticky elements don't overlap content
☐ Footer stays at bottom (not floating mid-page)

INTERACTIVE ELEMENT TESTING:
☐ All buttons have visible hover states
☐ Links are distinguishable from regular text
☐ Form inputs have focus indicators
☐ Disabled elements have reduced opacity (0.5-0.6)
☐ Click/tap targets minimum 44x44px (48x48px ideal)
☐ Dropdowns fully visible (not cut off by viewport)
☐ Modals center on screen with backdrop overlay

COLOR & CONTRAST TESTING:
☐ Text contrast meets WCAG AA (4.5:1 normal, 3:1 large)
☐ Button contrast meets WCAG AA (3:1 for UI components)
☐ Focus indicators have 3:1 contrast with background
☐ Color-blind simulator shows distinct elements
☐ Error messages not red-only (include icon or text)
☐ Success messages not green-only (include icon or text)

TYPOGRAPHY TESTING:
☐ Headings have clear hierarchy (H1 > H2 > H3)
☐ Body text line-height 1.5x or greater
☐ Line length 50-75 characters per line
☐ No text smaller than 14px (16px minimum preferred)
☐ Font weights distinguishable (400 vs 700 clearly different)
☐ All text horizontally aligned (not cropped)

IMAGE & MEDIA TESTING:
☐ All images have alt text
☐ Images load progressively (show low-res first)
☐ Broken image icons not visible
☐ Lazy loading works (images load as scrolled)
☐ Videos have play/pause controls
☐ Autoplay videos are muted
☐ Image zoom/lightbox functions correctly

MOBILE-SPECIFIC TESTING:
☐ Hamburger menu opens/closes correctly
☐ Touch targets large enough (48x48px)
☐ Swipe gestures work in galleries
☐ Pinch-to-zoom enabled on product images
☐ Fixed/sticky elements don't overlap content
☐ Keyboard covers input fields (viewport adjusts)
☐ Bottom nav doesn't block content

PERFORMANCE VISUAL TESTING:
☐ Largest Contentful Paint (LCP) < 2.5s
☐ No layout shifts during load (CLS < 0.1)
☐ Skeleton screens shown during loading
☐ Spinners indicate processing states
☐ Optimistic UI updates for instant feedback
☐ Images sized correctly (not scaling down huge images)
"""

# Common Visual Issues & Solutions
COMMON_ISSUES = """
COMMON VISUAL ISSUES & SOLUTIONS
=================================

ISSUE: Invisible CTA Buttons
SYMPTOMS: Low contrast, same color as background, no hover state
SOLUTION: Use high-contrast colors (3:1 minimum), add hover state with color change + shadow

ISSUE: Text Over Images Unreadable
SYMPTOMS: White text on light image, no background overlay
SOLUTION: Add semi-transparent dark overlay (rgba(0,0,0,0.5)), use text-shadow, or ensure high-contrast areas

ISSUE: Inconsistent Spacing
SYMPTOMS: Random gaps between elements, cramped sections, uneven margins
SOLUTION: Use 8px grid system (8, 16, 24, 32, 40, 48px spacing), consistent component margins

ISSUE: Poor Mobile Navigation
SYMPTOMS: Hamburger menu not obvious, menu items too small, nested dropdowns hard to use
SOLUTION: Use 24x24px+ hamburger icon, 48px+ menu item height, single-level mobile menu or accordion

ISSUE: Cluttered Product Pages
SYMPTOMS: Too much text above fold, multiple CTAs competing, overwhelming options
SOLUTION: Progressive disclosure (tabs/accordions), single primary CTA, visual hierarchy with size/color

ISSUE: Slow-Loading Images
SYMPTOMS: Blank white boxes, content jumping, slow page renders
SOLUTION: Lazy loading, optimized image formats (WebP, AVIF), correct sizing, skeleton placeholders

ISSUE: Unclear Product Images
SYMPTOMS: Small thumbnails, no zoom, single angle only
SOLUTION: Minimum 600px images, zoom on click, 3-5 images per product, 1:1 aspect ratio

ISSUE: Broken Responsive Layout
SYMPTOMS: Horizontal scroll on mobile, overlapping elements, cut-off text
SOLUTION: Mobile-first CSS, test at 320px width, use flexible grids, max-width: 100% on images

ISSUE: Inaccessible Forms
SYMPTOMS: Placeholder-only labels, no error messages, tiny inputs
SOLUTION: Labels above inputs, inline validation, 44px+ input height, clear error text

ISSUE: Poor Typography Hierarchy
SYMPTOMS: All text same size, hard to scan, wall of text
SOLUTION: 3-4 heading levels, 1.5x line-height, bold headings, adequate white space
"""

# Full expert knowledge export
VISION_EXPERT_KNOWLEDGE = {
    "ux_ui_principles": UX_UI_PRINCIPLES,
    "visual_accessibility": VISUAL_ACCESSIBILITY,
    "ecommerce_patterns": ECOMMERCE_PATTERNS,
    "cro_visual_cues": CRO_VISUAL_CUES,
    "mobile_patterns": MOBILE_PATTERNS,
    "visual_testing": VISUAL_TESTING,
    "common_issues": COMMON_ISSUES
}

def get_analysis_prompt() -> str:
    """
    Generate comprehensive prompt for GPT-4 Vision analysis
    
    Returns:
        Formatted prompt string with all expert knowledge
    """
    return f"""
You are an expert UX/UI analyst specializing in e-commerce website evaluation.
Analyze this screenshot with MEEDOGENLOOS STRENGE (ruthlessly strict) standards.

{UX_UI_PRINCIPLES}

{VISUAL_ACCESSIBILITY}

{ECOMMERCE_PATTERNS}

{CRO_VISUAL_CUES}

{MOBILE_PATTERNS}

ANALYSIS REQUIREMENTS:
1. Identify SPECIFIC visual issues with pixel-level precision
2. Rate severity: CRITICAL (breaks functionality), HIGH (major UX issue), MEDIUM (suboptimal), LOW (minor polish)
3. Provide ACTIONABLE fixes with exact measurements (colors, sizes, positions)
4. Check against ALL testing checklist items
5. No generic feedback - cite specific elements, locations, measurements

OUTPUT FORMAT:
- Issue: [Specific problem with location]
- Severity: [CRITICAL/HIGH/MEDIUM/LOW]
- Standard Violated: [Which guideline from above]
- Current State: [Exact description with measurements if applicable]
- Required Fix: [Exact action with measurements, colors, code if needed]
- Impact: [How this affects user experience or conversion]

Be MEEDOGENLOOS STRENGE - find every visual flaw, no matter how small.
"""

def get_mobile_analysis_prompt() -> str:
    """
    Generate mobile-specific analysis prompt
    
    Returns:
        Mobile-focused prompt string
    """
    return f"""
MOBILE-SPECIFIC VISUAL ANALYSIS (MEEDOGENLOOS STRENGE)

{MOBILE_PATTERNS}

MOBILE TESTING CHECKLIST:
{VISUAL_TESTING}

CRITICAL MOBILE CHECKS:
- Touch targets minimum 48x48px
- Thumb zone optimization (bottom 1/3 for primary actions)
- No horizontal scroll at 375px width
- Sticky elements don't overlap content
- Text readable without zoom (16px+ body text)
- Forms use appropriate input types
- Hamburger menu accessible and functional

Analyze this mobile screenshot against ALL mobile standards above.
Provide pixel-perfect critique with exact fixes.
"""
