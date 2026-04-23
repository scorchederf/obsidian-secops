---
mitre_id: "DC0052"
mitre_name: "Social Media"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--8fb2f315-1aca-4cef-ae0d-8105e1f95985"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

# DC0052: Social Media

Established, compromised, or otherwise acquired by adversaries to conduct reconnaissance, influence operations, social engineering, or other cyber threats.

*Data Collection Measures:*

- API Monitoring	
    - Social media APIs (e.g., Twitter API, Facebook Graph API) can extract behavioral patterns of accounts.
- Web Scraping
    - Extracts public profile data, friend lists, or interactions to identify impersonation attempts.
- Threat Intelligence Feeds	
    - External feeds track malicious personas linked to disinformation campaigns or phishing.
- OSINT Tools
    - Maltego, SpiderFoot, and OpenCTI can map social media persona relationships.
- Endpoint Detection	
    - EDR logs user behavior and alerts on suspicious social media interactions.
- SIEM Logging
    - Detects access to known phishing pages or social media abuse via proxy logs.
- Dark Web Monitoring	
    - Identifies compromised social media credentials being sold.

## Workspace

- [[kb/notes/attack/data-components/dc0052-notes|Open workspace note]]

