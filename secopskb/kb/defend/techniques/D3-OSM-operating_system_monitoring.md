---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-OSM"
d3fend_name: "Operating System Monitoring"
d3fend_ontology_id: "d3f:OperatingSystemMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AOperatingSystemMonitoring/"
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

The operating system software, for D3FEND's purposes, includes the kernel and its process management functions, hardware drivers, initialization or boot logic. It also includes and other key system daemons and their configuration. The monitoring or analysis of these components for unauthorized activity constitute **Operating System Monitoring**.

## Workspace

- [[workspaces/defend/techniques/D3-OSM-operating_system_monitoring-note|Open workspace note]]

![[workspaces/defend/techniques/D3-OSM-operating_system_monitoring-note]]

## Parent Technique

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

## Child Techniques

- [[D3-EHB-endpoint_health_beacon|D3-EHB: Endpoint Health Beacon]]
- [[D3-IDA-input_device_analysis|D3-IDA: Input Device Analysis]]
- [[D3-MBT-memory_boundary_tracking|D3-MBT: Memory Boundary Tracking]]
- [[D3-SDM-system_daemon_monitoring|D3-SDM: System Daemon Monitoring]]
- [[D3-SFA-system_file_analysis|D3-SFA: System File Analysis]]
- [[D3-SICA-system_init_config_analysis|D3-SICA: System Init Config Analysis]]
- [[D3-SJA-scheduled_job_analysis|D3-SJA: Scheduled Job Analysis]]
- [[D3-USICA-user_session_init_config_analysis|D3-USICA: User Session Init Config Analysis]]

## Knowledge Base Article

## Technique Overview

"An operating system (OS) is system software that manages computer hardware and software resources and provides common services for computer programs." [1]

Operating System Monitoring Techniques have varied implementations including built-in kernel modules, third-party privileged system daemons, or even standard systems administration tools included with an operating system.

1. http://dbpedia.org/resource/Operating_system

## Ontology Relationships

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

