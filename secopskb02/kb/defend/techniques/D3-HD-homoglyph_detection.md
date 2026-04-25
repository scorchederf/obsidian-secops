---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-HD"
d3fend_name: "Homoglyph Detection"
d3fend_ontology_id: "d3f:HomoglyphDetection"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AHomoglyphDetection/"
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
  - "T1189"
  - "T1204"
  - "T1204.001"
  - "T1534"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
  - "T1566.003"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Comparing strings using a variety of techniques to determine if a deceptive or malicious string is being presented to a user.

## Workspace

- [[workspaces/defend/techniques/D3-HD-homoglyph_detection-note|Open workspace note]]

![[workspaces/defend/techniques/D3-HD-homoglyph_detection-note]]

## Parent Technique

- [[D3-ID-identifier_analysis|D3-ID: Identifier Analysis]]

## Related ATT&CK Techniques

- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
- [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
- [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]

## Knowledge Base Article

## How it works
A homoglyph, in this context, is a deceptive string or word which looks like a trusted word, but is composed of different characters, for example: goooogle.com versus google.com. This is commonly found in phishing and typo squatting attacks where a human exploiting through a social engineering campaign.

## Considerations
* In very large environments processing DNS queries can be computationally expensive due to the amount of traffic that is generated
* Legitimate companies and products use non-dictionary words in their names that could result in many false positives

## Ontology Relationships

- [[D3-ID-identifier_analysis|D3-ID: Identifier Analysis]]

