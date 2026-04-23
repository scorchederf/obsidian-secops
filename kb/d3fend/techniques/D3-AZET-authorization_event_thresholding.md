---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-AZET"
d3fend_name: "Authorization Event Thresholding"
d3fend_ontology_id: "d3f:AuthorizationEventThresholding"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AAuthorizationEventThresholding/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-AZET: Authorization Event Thresholding

Collecting authorization events, creating a baseline user profile, and determining whether authorization events are consistent with the baseline profile.

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works

Authorization event data is collected to create a baseline user profile. Authorization events that deviate from the baseline and exceed a static or dynamic threshold are identified for further action. Authorization events can include successful and failed authorization attempts as well as events related to permissions including viewing, editing, deleting, creating files, databases etc.

## Considerations

Depending on the complexity of the data considered, outliers may not be obvious to a human analyst reviewing events in simplistic analytic views. If malicious activity is not statistically different from benign activity, an alert threshold will not be met.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-azet-notes|Open workspace note]]

