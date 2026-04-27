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
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Analyzing the amount of data transferred by a user.

## Workspace

- [[workspaces/defend/techniques/D3-UDTA-user_data_transfer_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-UDTA-user_data_transfer_analysis-note]]

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

