---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-APM"
d3fend_name: "Application Performance Monitoring"
d3fend_ontology_id: "d3f:ApplicationPerformanceMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AApplicationPerformanceMonitoring/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Monitoring the count and duration of the application or program cycle.

## Workspace

- [[workspaces/defend/techniques/D3-APM-application_performance_monitoring-note|Open workspace note]]

![[workspaces/defend/techniques/D3-APM-application_performance_monitoring-note]]

## Parent Technique

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

## Child Techniques

- [[D3-AEM-application_exception_monitoring|D3-AEM: Application Exception Monitoring]]

## Knowledge Base Article

## How it works
Keeping track of the controller cycle time by logging it, setting alarms, and correlating with other events. Changes to cycle time can be indicative of injecting new logic, deleting logic, or system failures.

## Ontology Relationships

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

