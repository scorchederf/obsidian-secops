---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RAPA"
d3fend_name: "Resource Access Pattern Analysis"
d3fend_ontology_id: "d3f:ResourceAccessPatternAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AResourceAccessPatternAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-RAPA: Resource Access Pattern Analysis

Analyzing the resources accessed by a user to identify unauthorized activity.

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works
This technique analyzes a user's resource accesses by comparing the user's recent activity against a baseline activity model. Major differences between the current activity and the baseline model might indicate unauthorized activity if they are severe enough.


## Considerations
* Potential for false positives from anomalies that are not associated with malicious activity.
* Attackers that move low and slow may not differentiate their resource access activity behavior enough to trigger an alert.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-rapa-notes|Open workspace note]]

