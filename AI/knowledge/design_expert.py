"""
Design & Accessibility Expert Knowledge Base
Centralized design expertise for Nora (and other analysts who need design/a11y knowledge)
"""

WCAG_STANDARDS = """
WCAG 2.1 Level AA Requirements:

1. Color Contrast:
   - Normal text: 4.5:1 minimum
   - Large text (18pt+): 3:1 minimum
   - UI components: 3:1 minimum

2. Touch Targets:
   - Minimum size: 44x44px (Level AA)
   - Recommended: 48x48px (Level AAA)
   - Sufficient spacing between targets

3. Keyboard Navigation:
   - All interactive elements keyboard accessible
   - Visible focus indicators
   - Logical tab order

4. Screen Reader Support:
   - Proper ARIA labels
   - Semantic HTML (nav, main, article, etc.)
   - Alt text for images
   - Descriptive link text
"""

DESIGN_TOKENS = """
Design System Best Practices:

1. Color System:
   - Primary: Brand color
   - Secondary: Accent color
   - Neutral: Gray scale (50-900)
   - Semantic: Success, Warning, Error, Info

2. Typography Scale:
   - Base: 16px (1rem)
   - Scale: 1.25 (Major Third)
   - Headings: H1-H6 with clear hierarchy

3. Spacing System:
   - Base unit: 4px or 8px
   - Scale: 0.25, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 12, 16
   - Consistent throughout design

4. Responsive Breakpoints:
   - Mobile: 0-640px
   - Tablet: 641-1024px
   - Desktop: 1025px+
"""

MOBILE_FIRST_DESIGN = """
Mobile-First Design Principles:

1. Touch Zones:
   - Primary actions in thumb zone (bottom 1/3)
   - Navigation at bottom (not top)
   - Large touch targets (48px minimum)

2. Progressive Enhancement:
   - Start with mobile design
   - Add complexity for larger screens
   - Mobile is the baseline experience

3. Performance:
   - Mobile networks slower
   - Optimize images aggressively
   - Lazy load non-critical content
   - Minimize JavaScript payload
"""

def get_recommendation(topic, current_score):
    """
    Generate design recommendation based on topic and score
    """
    recommendations = {
        'contrast': [
            'Increase color contrast to meet WCAG AA (4.5:1)',
            'Test with browser DevTools contrast checker',
            'Use darker text on light backgrounds',
            'Avoid gray text on light backgrounds'
        ],
        'touch_targets': [
            'Increase button size to 48x48px minimum',
            'Add padding around interactive elements',
            'Ensure sufficient spacing between targets',
            'Test on actual mobile devices'
        ],
        'typography': [
            'Use minimum 16px base font size',
            'Implement clear heading hierarchy',
            'Improve line height (1.5-1.6 for body text)',
            'Limit line length (50-75 characters)'
        ],
        'mobile': [
            'Optimize for thumb-friendly navigation',
            'Place primary actions in bottom third',
            'Increase touch target sizes',
            'Test on multiple device sizes'
        ]
    }
    
    return recommendations.get(topic, [])
