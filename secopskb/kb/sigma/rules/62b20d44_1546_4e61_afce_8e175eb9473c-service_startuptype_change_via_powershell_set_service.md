---
sigma_id: "62b20d44-1546-4e61-afce-8e175eb9473c"
title: "Service StartupType Change Via PowerShell Set-Service"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_set_service_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_set_service_disabled.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "62b20d44-1546-4e61-afce-8e175eb9473c"
  - "Service StartupType Change Via PowerShell Set-Service"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service StartupType Change Via PowerShell Set-Service

Detects the use of the PowerShell "Set-Service" cmdlet to change the startup type of a service to "disabled" or "manual"

## Metadata

- Rule ID: 62b20d44-1546-4e61-afce-8e175eb9473c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-04
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_set_service_disabled.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \powershell.exe
- OriginalFileName: PowerShell.EXE
selection_cli:
  CommandLine|contains|all:
  - Set-Service
  - -StartupType
  CommandLine|contains:
  - Disabled
  - Manual
condition: all of selection_*
```

## False Positives

- False positives may occur with troubleshooting scripts

## References

- https://www.virustotal.com/gui/file/38283b775552da8981452941ea74191aa0d203edd3f61fb2dee7b0aea3514955

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_set_service_disabled.yml)
