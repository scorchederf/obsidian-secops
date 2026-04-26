---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PUM"
d3fend_name: "Platform Uptime Monitoring"
d3fend_ontology_id: "d3f:PlatformUptimeMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3APlatformUptimeMonitoring/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Monitor the amount of time since the last power cycle or restart.

## Workspace

- [[workspaces/defend/techniques/D3-PUM-platform_uptime_monitoring-note|Open workspace note]]

![[workspaces/defend/techniques/D3-PUM-platform_uptime_monitoring-note]]

## Parent Technique

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

## Knowledge Base Article

## How it works
Monitoring the time since the last power cycle or restart alerts operators to unexpected restarts and their frequency. This can indicate potential issues or malicious activity, and provides valuable information for forensic investigations.

## Considerations
The source of the variable may be mutable depending on the platform, and the provenance of the value.

## Ontology Relationships

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

