---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SDA"
d3fend_name: "Session Duration Analysis"
d3fend_ontology_id: "d3f:SessionDurationAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASessionDurationAnalysis/"
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

Analyzing the duration of user sessions in order to detect unauthorized  activity.

## Workspace

- [[workspaces/defend/techniques/D3-SDA-session_duration_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SDA-session_duration_analysis-note]]

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works
Detecting unauthorized user sessions by comparing the duration of a user logon session with a baseline behavior model. The behavior model comprises historical user session duration times.  Abnormalities between session duration and the behavior model may indicate suspicious activity.

## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers may not differentiate their session duration enough to trigger an alert.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

