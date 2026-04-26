---
sigma_id: "f1086bf7-a0c4-4a37-9102-01e573caf4a0"
title: "Renamed Whoami Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_whoami.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_whoami.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "f1086bf7-a0c4-4a37-9102-01e573caf4a0"
  - "Renamed Whoami Execution"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed Whoami Execution

Detects the execution of whoami that has been renamed to a different name to avoid detection

## Metadata

- Rule ID: f1086bf7-a0c4-4a37-9102-01e573caf4a0
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-08-12
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_whoami.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
  OriginalFileName: whoami.exe
filter:
  Image|endswith: \whoami.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://brica.de/alerts/alert/public/1247926/agent-tesla-keylogger-delivered-inside-a-power-iso-daa-archive/
- https://app.any.run/tasks/7eaba74e-c1ea-400f-9c17-5e30eee89906/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_whoami.yml)
