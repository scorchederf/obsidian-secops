---
sigma_id: "8de1cbe8-d6f5-496d-8237-5f44a721c7a0"
title: "Whoami.EXE Execution Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_whoami_parent_anomaly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_parent_anomaly.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8de1cbe8-d6f5-496d-8237-5f44a721c7a0"
  - "Whoami.EXE Execution Anomaly"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Whoami.EXE Execution Anomaly

Detects the execution of whoami.exe with suspicious parent processes.

## Metadata

- Rule ID: 8de1cbe8-d6f5-496d-8237-5f44a721c7a0
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2021-08-12
- Modified: 2025-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_whoami_parent_anomaly.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
- Image|endswith: \whoami.exe
- OriginalFileName: whoami.exe
filter_main_known_parents:
  ParentImage|endswith:
  - \cmd.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
filter_optional_ms_monitoring_agent:
  ParentImage|endswith: :\Program Files\Microsoft Monitoring Agent\Agent\MonitoringHost.exe
filter_main_parent_null:
  ParentImage: null
filter_main_parent_empty:
  ParentImage:
  - ''
  - '-'
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Admin activity
- Scripts and administrative tools used in the monitored environment
- Monitoring activity

## References

- https://brica.de/alerts/alert/public/1247926/agent-tesla-keylogger-delivered-inside-a-power-iso-daa-archive/
- https://app.any.run/tasks/7eaba74e-c1ea-400f-9c17-5e30eee89906/
- https://www.youtube.com/watch?v=DsJ9ByX84o4&t=6s

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_parent_anomaly.yml)
