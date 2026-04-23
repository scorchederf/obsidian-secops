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
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-SDA: Session Duration Analysis

Analyzing the duration of user sessions in order to detect unauthorized  activity.

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

## Workspace

- [[kb/notes/d3fend/techniques/d3-sda-notes|Open workspace note]]

