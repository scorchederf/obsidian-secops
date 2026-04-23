---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SDM"
d3fend_name: "System Daemon Monitoring"
d3fend_ontology_id: "d3f:SystemDaemonMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemDaemonMonitoring/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1053"
  - "T1053.002"
  - "T1053.003"
  - "T1053.005"
  - "T1053.006"
  - "T1053.007"
  - "T1562"
  - "T1562.001"
---

# D3-SDM: System Daemon Monitoring

Tracking changes to the state or configuration of critical system level processes.

## Parent Technique

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Related ATT&CK Techniques

- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
- [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
- [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
- [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Knowledge Base Article

## How it works
Attackers may manipulate system settings or services to disable system logging or monitoring of security tools and events. Firewall and antivirus services are popular targets for attackers. Disabling system logs will also allow an attacker's actions to go unnoticed. Analysis of logs, registries, and process monitoring help defenders locate signs of tampering. Two possible approaches are to monitor hardened system services or to monitor registry updates for modifications to security settings.

## Ontology Relationships

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-sdm-notes|Open workspace note]]

