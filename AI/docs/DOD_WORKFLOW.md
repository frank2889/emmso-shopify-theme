# D.O.D (Directed Output Document) Workflow

## 🎯 Overview

The **d.o.d (directed.output.document)** workflow is EMMSO's structured approach for AI analysts to provide actionable, file-specific deliverables to the Captain for immediate implementation.

## 📋 D.O.D Format Structure

```json
{
  "format": "d.o.d",
  "analyst": "Analyst Name (Specialty)",
  "deliverable_type": "OPTIMIZATION_PACKAGE_TYPE",
  "urgency": "IMMEDIATE|HIGH|MEDIUM|LOW",
  "implementation_timeline": "24 hours|72 hours|1 week|2 weeks",
  "target_files": [
    {
      "file": "exact/file/path.ext",
      "action": "Specific action to take",
      "priority": "HIGH|MEDIUM|LOW"
    }
  ],
  "specific_actions": {
    "WHAT": ["List of specific actions"],
    "WHERE": {"file": "action description"},
    "WHEN": "Timeline",
    "WHY": "Business justification with revenue impact"
  },
  "captain_instructions": {
    "deployment_order": ["Step-by-step implementation"],
    "success_metrics": ["Measurable success criteria"],
    "validation_commands": ["How to verify completion"]
  },
  "business_context": {
    "okr_impact": "Which OKR this impacts",
    "revenue_potential": "€X,XXX/month",
    "market_coverage": "Target markets affected"
  }
}
```

## 🚢 Captain Processing Workflow

### 1. **D.O.D Reception**
```
Analyst → d.o.d Output → Captain Processing Queue
```

### 2. **Priority Calculation**
- **IMMEDIATE** (Score < 30): Priority 10/10
- **HIGH** (Score < 60): Priority 8/10  
- **MEDIUM** (Score < 80): Priority 5/10
- **LOW** (Score ≥ 80): Priority 2/10

### 3. **Execution Sequence Generation**
1. Sort by priority (HIGH → MEDIUM → LOW)
2. Group by file type/location
3. Generate step-by-step deployment plan
4. Calculate estimated timeline

### 4. **Action Plan Generation**
- **File Deployment Map**: Which files need modification
- **Implementation Timeline**: Total hours required
- **Success Validation**: How to verify completion

## 👥 Analyst Implementation

### Required Methods
Each analyst must implement:

```python
def _generate_directed_output_document(self, score, findings, recommendations):
    """Generate d.o.d format output for Captain"""
    return {
        'format': 'd.o.d',
        'analyst': f'{self.name} ({self.specialty})',
        'deliverable_type': 'OPTIMIZATION_PACKAGE',
        # ... complete d.o.d structure
    }
```

### File Targeting Rules
- **Templates**: `templates/*.liquid` - UI/UX changes
- **Assets**: `assets/emmso.css`, `assets/emmso.js` - Performance/visual
- **Snippets**: `snippets/*.liquid` - Reusable components  
- **Config**: `config/settings_schema.json` - Theme settings
- **Sections**: `sections/*.liquid` - Page components

## 🎯 Business Integration

### Revenue Impact Tracking
Each d.o.d must include:
- **Monthly Revenue Potential**: Calculated from real data
- **Implementation Cost**: Estimated development hours
- **ROI Calculation**: Revenue vs implementation cost
- **OKR Alignment**: Which business objective it supports

### Multi-Market Considerations
- **Target Markets**: Nederland, Denemarken, België, Duitsland, Frankrijk, Oostenrijk, Ierland, Italië, Spanje, Portugal
- **Internationalization**: URL structure impacts (/da, /de, /en, /it, /es, /fr)
- **Localization**: Market-specific optimization needs

## 🔄 Complete Workflow Example

### 1. Sarah (SEO) Analysis
```
Score: 45/100 → URGENT d.o.d required
```

### 2. D.O.D Generation
```json
{
  "format": "d.o.d",
  "urgency": "HIGH",
  "target_files": [
    {"file": "assets/emmso.css", "action": "Optimize CSS performance"},
    {"file": "templates/theme.liquid", "action": "Add meta tags"}
  ]
}
```

### 3. Captain Processing
```
Priority: 8/10
Timeline: 72 hours
Files: 2 files affected
Sequence: CSS optimization → Meta tag implementation
```

### 4. Action Plan Output
```
📋 DIRECTED OUTPUT DOCUMENTS ACTION PLAN:
📊 Total d.o.d Outputs: 1
⏱️  Estimated Implementation: 6 hours

🔥 HIGH PRIORITY ACTIONS (1):
• Sarah: SEO_OPTIMIZATION_PACKAGE - 2 files

📁 FILE DEPLOYMENT MAP (2 files affected):
📄 assets/emmso.css:
   → Sarah: Optimize CSS performance (HIGH)
📄 templates/theme.liquid:
   → Sarah: Add meta tags (HIGH)
```

## ✅ Success Metrics

### Analyst Level
- ✅ D.O.D format compliance
- ✅ File targeting accuracy  
- ✅ Revenue impact calculation
- ✅ Timeline estimation

### Captain Level
- ✅ Priority calculation accuracy
- ✅ Execution sequence optimization
- ✅ Multi-analyst coordination
- ✅ Business context integration

### System Level
- ✅ End-to-end workflow completion
- ✅ Revenue tracking accuracy
- ✅ OKR alignment verification
- ✅ Multi-market optimization success

## 🚀 Ready for Production

The d.o.d workflow provides:
- **Structured Output**: Consistent analyst deliverables
- **File-Specific Actions**: Exact implementation guidance
- **Business Justification**: Revenue-driven prioritization
- **Captain Coordination**: Centralized execution planning
- **Multi-Market Awareness**: Global optimization support