
class TestSarahSEOAnalyst:
    def __init__(self):
        self.name = "Sarah"
        self.specialty = "SEO"
    
    def analyze(self, site_data):
        from datetime import datetime
        
        # Simulate analysis with d.9.d deliverable
        score = 45  # Low score to trigger urgent deliverable
        
        return {
            "analyst": self.name,
            "specialty": self.specialty,
            "timestamp": datetime.now().isoformat(),
            "score": score,
            "findings": {
                "performance_issues": ["Slow loading", "Large CSS files"],
                "seo_issues": ["Missing meta tags", "No structured data"]
            },
            "recommendations": [
                "CRITICAL: Optimize CSS performance",
                "HIGH: Add structured data markup",
                "TECHNICAL: Implement proper meta tags"
            ],
            "deliverable": {
                "format": "d.o.d",
                "analyst": "Sarah (SEO)",
                "deliverable_type": "SEO_OPTIMIZATION_PACKAGE",
                "urgency": "HIGH",
                "implementation_timeline": "72 hours",
                "target_files": [
                    {"file": "assets/emmso.css", "action": "Optimize and minify CSS", "priority": "HIGH"},
                    {"file": "templates/theme.liquid", "action": "Add meta tags", "priority": "HIGH"},
                    {"file": "snippets/seo-meta.liquid", "action": "Create SEO snippet", "priority": "MEDIUM"}
                ],
                "specific_actions": {
                    "WHAT": ["Optimize CSS performance", "Add structured data", "Implement meta tags"],
                    "WHERE": {
                        "assets/emmso.css": "CSS optimization",
                        "templates/theme.liquid": "Meta tag implementation"
                    },
                    "WHEN": "72 hours",
                    "WHY": "SEO optimization can generate €5,000/month additional revenue"
                },
                "business_context": {
                    "okr_impact": "AI Quality Score ≥ 90/100",
                    "revenue_potential": "€5,000/month",
                    "market_coverage": "Nederland, Denemarken, België"
                }
            }
        }
