---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-UDTA"
d3fend_name: "User Data Transfer Analysis"
d3fend_ontology_id: "d3f:UserDataTransferAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AUserDataTransferAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-UDTA: User Data Transfer Analysis

Analyzing the amount of data transferred by a user.

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works
Unusual data transfer activity may indicate unauthorized activity. Data transfers can be analyzed by collecting network traffic or application logs.

## Considerations
* There is a potential for false positives from anomalies that are not associated with unauthorized activity.
* Attackers that move low and slow may not differentiate their data transfer behavior enough for an alert to trigger.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-udta-notes|Open workspace note]]

