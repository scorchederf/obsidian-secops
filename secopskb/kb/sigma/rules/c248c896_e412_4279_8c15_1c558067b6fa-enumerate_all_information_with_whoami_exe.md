---
sigma_id: "c248c896-e412-4279-8c15-1c558067b6fa"
title: "Enumerate All Information With Whoami.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_whoami_all_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_all_execution.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c248c896-e412-4279-8c15-1c558067b6fa"
  - "Enumerate All Information With Whoami.EXE"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enumerate All Information With Whoami.EXE

Detects the execution of "whoami.exe" with the "/all" flag

## Metadata

- Rule ID: c248c896-e412-4279-8c15-1c558067b6fa
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-12-04
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_whoami_all_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection_main_img:
- Image|endswith: \whoami.exe
- OriginalFileName: whoami.exe
selection_main_cli:
  CommandLine|contains|windash: ' -all'
condition: all of selection_main_*
```

## False Positives

- Unknown

## References

- https://brica.de/alerts/alert/public/1247926/agent-tesla-keylogger-delivered-inside-a-power-iso-daa-archive/
- https://app.any.run/tasks/7eaba74e-c1ea-400f-9c17-5e30eee89906/
- https://www.youtube.com/watch?v=DsJ9ByX84o4&t=6s

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_all_execution.yml)
