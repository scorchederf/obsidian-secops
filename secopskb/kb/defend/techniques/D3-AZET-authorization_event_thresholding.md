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
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Collecting authorization events, creating a baseline user profile, and determining whether authorization events are consistent with the baseline profile.

## Workspace

- [[workspaces/defend/techniques/D3-AZET-authorization_event_thresholding-note|Open workspace note]]

![[workspaces/defend/techniques/D3-AZET-authorization_event_thresholding-note]]

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works

Authorization event data is collected to create a baseline user profile. Authorization events that deviate from the baseline and exceed a static or dynamic threshold are identified for further action. Authorization events can include successful and failed authorization attempts as well as events related to permissions including viewing, editing, deleting, creating files, databases etc.

## Considerations

Depending on the complexity of the data considered, outliers may not be obvious to a human analyst reviewing events in simplistic analytic views. If malicious activity is not statistically different from benign activity, an alert threshold will not be met.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

