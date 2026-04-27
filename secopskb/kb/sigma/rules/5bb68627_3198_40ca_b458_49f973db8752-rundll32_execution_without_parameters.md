---
sigma_id: "5bb68627-3198-40ca-b458-49f973db8752"
title: "Rundll32 Execution Without Parameters"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_without_parameters.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_without_parameters.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5bb68627-3198-40ca-b458-49f973db8752"
  - "Rundll32 Execution Without Parameters"
attack_technique_ids:
  - "T1021.002"
  - "T1570"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Rundll32 Execution Without Parameters

Detects rundll32 execution without parameters as observed when running Metasploit windows/smb/psexec exploit module

## Metadata

- Rule ID: 5bb68627-3198-40ca-b458-49f973db8752
- Status: test
- Level: high
- Author: Bartlomiej Czyz, Relativity
- Date: 2021-01-31
- Modified: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_without_parameters.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  CommandLine:
  - rundll32.exe
  - rundll32
condition: selection
```

## False Positives

- False positives may occur if a user called rundll32 from CLI with no options

## References

- https://bczyz1.github.io/2021/01/30/psexec.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_without_parameters.yml)
