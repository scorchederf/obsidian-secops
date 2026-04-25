---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-WSAA"
d3fend_name: "Web Session Activity Analysis"
d3fend_ontology_id: "d3f:WebSessionActivityAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AWebSessionActivityAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Monitoring changes in user web session behavior by comparing current web session activity to a baseline behavior profile or a catalog of predetermined malicious behavior.

## Workspace

- [[notes/defend/techniques/D3-WSAA-web_session_activity_analysis-note|Open workspace note]]

![[notes/defend/techniques/D3-WSAA-web_session_activity_analysis-note]]

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works
User web session data is collected over a period of time to create a user behavior profile. Data collected includes clicks made on a website, average time between clicks, filling out web forms, order in which pages are viewed, and downloading files. Current user web session behavior is then compared against the use behavior profile to identify anomalies and a likelihood that the current user web session is malicious. Current user web session behavior can also be compared to predetermined known malicious behavior profiles that are developed through analysis of malware in run time at a threat research facility.

## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers may not differentiate their web session activity enough to trigger an alert.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

