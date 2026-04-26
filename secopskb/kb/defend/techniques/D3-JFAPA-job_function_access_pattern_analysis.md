---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-JFAPA"
d3fend_name: "Job Function Access Pattern Analysis"
d3fend_ontology_id: "d3f:JobFunctionAccessPatternAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AJobFunctionAccessPatternAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Detecting anomalies in user access patterns by comparing user access activity to behavioral profiles that categorize users by role such as job title, function, department.

## Workspace

- [[workspaces/defend/techniques/D3-JFAPA-job_function_access_pattern_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-JFAPA-job_function_access_pattern_analysis-note]]

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works
Peer group analysis identifies functionally similar groups of actors (users or resources) based on categorizations such as job title, organizational hierarchy, or other attribute that indicates similarity of job function. Current user access activity is then compared to the appropriate peer group behavior profile to identify anomalies.

## Considerations
Potential for false positives from anomalies that are not associated with malicious activity.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

