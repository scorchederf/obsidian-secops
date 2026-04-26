---
sigma_id: "c30fb093-1109-4dc8-88a8-b30d11c95a5d"
title: "Whoami.EXE Execution With Output Option"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_whoami_output.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_output.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c30fb093-1109-4dc8-88a8-b30d11c95a5d"
  - "Whoami.EXE Execution With Output Option"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Whoami.EXE Execution With Output Option

Detects the execution of "whoami.exe" with the "/FO" flag to choose CSV as output format or with redirection options to export the results to a file for later use.

## Metadata

- Rule ID: c30fb093-1109-4dc8-88a8-b30d11c95a5d
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-28
- Modified: 2023-12-04
- Source Path: rules/windows/process_creation/proc_creation_win_whoami_output.yml

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
  CommandLine|contains:
  - ' /FO CSV'
  - ' -FO CSV'
selection_special:
  CommandLine|contains: whoami*>
condition: all of selection_main_* or selection_special
```

## False Positives

- Unknown

## References

- https://brica.de/alerts/alert/public/1247926/agent-tesla-keylogger-delivered-inside-a-power-iso-daa-archive/
- https://app.any.run/tasks/7eaba74e-c1ea-400f-9c17-5e30eee89906/
- https://www.youtube.com/watch?v=DsJ9ByX84o4&t=6s

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_output.yml)
