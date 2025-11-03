# EMMSO Service Account Setup

## Google APIs Access Required

### Service Account Details
- **Email**: emmso-461@positive-karma-475015-h7.iam.gserviceaccount.com
- **Project**: positive-karma-475015-h7
- **GA4 Property**: 460990321

### Required Service Account File
File needed: `/Users/Frank/Documents/EMMSO/AI/config/emmso-service-account.json`

### APIs to Enable
1. Google Analytics Data API v1 (beta)
2. Google Analytics Reporting API v4
3. Google Search Console API
4. PageSpeed Insights API

### Permissions Required
- **GA4 Property 460990321**: Viewer access
- **Search Console**: Verified property access
- **PageSpeed API**: API key access (already configured)

### Setup Instructions
1. Download service account JSON from Google Cloud Console
2. Place in `/Users/Frank/Documents/EMMSO/AI/config/emmso-service-account.json`
3. Verify GA4 property access permissions
4. Test API connectivity

### Python Dependencies
```bash
pip install google-analytics-data google-api-python-client google-auth
```

### Critical for Analyzers
- **Eva (Analytics)**: Needs GA4 API access
- **Jessica (UX)**: Needs GA4 user behavior metrics
- **Sarah (SEO)**: Already has PageSpeed API access
- **Others**: Need respective API integrations