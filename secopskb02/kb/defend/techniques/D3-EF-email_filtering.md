---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-EF"
d3fend_name: "Email Filtering"
d3fend_ontology_id: "d3f:EmailFiltering"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AEmailFiltering/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
attack_technique_ids:
  - "T1114"
  - "T1114.001"
  - "T1534"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Filtering incoming email traffic based on specific criteria.

## Workspace

- [[workspaces/defend/techniques/D3-EF-email_filtering-note|Open workspace note]]

![[workspaces/defend/techniques/D3-EF-email_filtering-note]]

## Parent Technique

- [[D3-ITF-inbound_traffic_filtering|D3-ITF: Inbound Traffic Filtering]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
- [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]

## Knowledge Base Article

## How it works

Mail filters can be implemented to scan inbound email messages at the initial SMTP connection stage to detect and reject email containing spam and malware.

This technique is distinct from d3f:EmailDeletion because it prevents an email from reaching an user's inbox. This technique can also be used for outbound email traffic.

## Considerations
* The effectiveness of mail filters depend on the completeness of the filter policies

## Ontology Relationships

- [[D3-ITF-inbound_traffic_filtering|D3-ITF: Inbound Traffic Filtering]]

