---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-OMM"
d3fend_name: "Operating Mode Monitoring"
d3fend_ontology_id: "d3f:OperatingModeMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AOperatingModeMonitoring/"
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

Detects operating modes such as Program, Run, Remote, or Stop.

## Workspace

- [[workspaces/defend/techniques/D3-OMM-operating_mode_monitoring-note|Open workspace note]]

![[workspaces/defend/techniques/D3-OMM-operating_mode_monitoring-note]]

## Parent Technique

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

## Knowledge Base Article

## How it works
Many OT Controllers have key switches to change the controller into various modes of operation. These modes of operation can include Program, Run, Remote, or Stop.

The key switch position is often available as a system diagnostic function block of the programming logic.

## Considerations
* It is advised to configure a key switch alarm such that an operator is alerted when the controller is put into a programming mode, as this could indicate unintentional or malicious changes to operational code.

## Ontology Relationships

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

