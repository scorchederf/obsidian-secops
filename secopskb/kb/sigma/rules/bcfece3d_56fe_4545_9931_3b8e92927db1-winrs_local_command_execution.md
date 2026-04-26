---
sigma_id: "bcfece3d-56fe-4545-9931-3b8e92927db1"
title: "Winrs Local Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrs_local_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrs_local_command_execution.yml"
build_date: "2026-04-26 17:03:24"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bcfece3d-56fe-4545-9931-3b8e92927db1"
  - "Winrs Local Command Execution"
attack_technique_ids:
  - "T1021.006"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Winrs Local Command Execution

Detects the execution of Winrs.exe where it is used to execute commands locally.
Commands executed this way are launched under Winrshost.exe and can represent proxy execution used for defense evasion or lateral movement.

## Metadata

- Rule ID: bcfece3d-56fe-4545-9931-3b8e92927db1
- Status: experimental
- Level: high
- Author: Liran Ravich, Nasreddine Bencherchali
- Date: 2025-10-22
- Source Path: rules/windows/process_creation/proc_creation_win_winrs_local_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.006]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \winrs.exe
- OriginalFileName: winrs.exe
selection_local_ip:
  CommandLine|contains|windash:
  - /r:localhost
  - /r:127.0.0.1
  - /r:[::1]
  - /remote:localhost
  - /remote:127.0.0.1
  - /remote:[::1]
filter_main_remote:
  CommandLine|contains|windash:
  - '/r:'
  - '/remote:'
condition: all of selection_* or (selection_img and not 1 of filter_main_*)
```

## False Positives

- Unlikely

## References

- https://cardinalops.com/blog/living-off-winrm-abusing-complexity-in-remote-management/
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/winrs

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrs_local_command_execution.yml)
