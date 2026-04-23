---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SJA"
d3fend_name: "Scheduled Job Analysis"
d3fend_ontology_id: "d3f:ScheduledJobAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AScheduledJobAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1036"
  - "T1036.004"
  - "T1053"
  - "T1053.002"
  - "T1053.003"
  - "T1053.005"
  - "T1053.006"
  - "T1053.007"
---

# D3-SJA: Scheduled Job Analysis

Analysis of source files, processes, destination files, or destination servers associated with a scheduled job to detect unauthorized use of job scheduling.

## Parent Technique

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Related ATT&CK Techniques

- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading#^t1036004-masquerade-task-or-service|T1036.004: Masquerade Task or Service]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
- [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
- [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
- [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
- [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]

## Knowledge Base Article

## How it works
Scheduled job execution can be utilized by adversaries for the purpose of persistence, conducting remote execution, or gaining privileges. Details of a scheduled job such as associated source files, processes, destination files, or destination servers are first identified and analyzed and then compared against an anti-malware signature database, whitelist, or reputation server. For example, a file associated with a scheduled job to be executed at a specified time or a remote server that is accessed as part of a scheduled task is compared against an anti-malware signature database, whitelist, or reputation server, and if a match is found, execution is denied and an alert is generated.

In addition to traditional scheduled jobs, triggers can be set to execute a specific command after detecting a specific event in the system, such as with WMI Event Subscriptions in Windows.

## Considerations
Jobs can be scheduled in many different and sometimes creative ways through operating system capabilities.

## Ontology Relationships

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-sja-notes|Open workspace note]]

