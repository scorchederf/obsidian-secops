---
sigma_id: "79df3f68-dccb-48e9-9171-b75cbc37c51d"
title: "Potential Lateral Movement via Windows Remote Shell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrshost_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrshost_command_execution.yml"
build_date: "2026-04-26 14:14:32"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "79df3f68-dccb-48e9-9171-b75cbc37c51d"
  - "Potential Lateral Movement via Windows Remote Shell"
attack_technique_ids:
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Lateral Movement via Windows Remote Shell

Detects a child process spawned by 'winrshost.exe', which suggests remote command execution through Windows Remote Shell (WinRs) and may indicate potential lateral movement activity.

## Metadata

- Rule ID: 79df3f68-dccb-48e9-9171-b75cbc37c51d
- Status: experimental
- Level: medium
- Author: Liran Ravich
- Date: 2025-10-22
- Source Path: rules/windows/process_creation/proc_creation_win_winrshost_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection:
  ParentImage|endswith: \winrshost.exe
filter_main_conhost:
  Image: C:\Windows\System32\conhost.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate use of WinRM within the organization

## References

- https://cardinalops.com/blog/living-off-winrm-abusing-complexity-in-remote-management/
- https://www.ired.team/offensive-security/lateral-movement/winrs-for-lateral-movement

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrshost_command_execution.yml)
