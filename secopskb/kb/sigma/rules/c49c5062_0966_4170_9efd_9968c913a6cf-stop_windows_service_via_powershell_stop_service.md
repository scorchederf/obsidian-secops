---
sigma_id: "c49c5062-0966-4170-9efd-9968c913a6cf"
title: "Stop Windows Service Via PowerShell Stop-Service"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_stop_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_stop_service.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "c49c5062-0966-4170-9efd-9968c913a6cf"
  - "Stop Windows Service Via PowerShell Stop-Service"
attack_technique_ids:
  - "T1489"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Stop Windows Service Via PowerShell Stop-Service

Detects the stopping of a Windows service via the PowerShell Cmdlet "Stop-Service"

## Metadata

- Rule ID: c49c5062-0966-4170-9efd-9968c913a6cf
- Status: test
- Level: low
- Author: Jakob Weinzettl, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_stop_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1489-service_stop|T1489]]

## Detection

```yaml
selection_sc_net_img:
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
selection_cli:
  CommandLine|contains: 'Stop-Service '
condition: all of selection_*
```

## False Positives

- There are many legitimate reasons to stop a service. This rule isn't looking for any suspicious behaviour in particular. Filter legitimate activity accordingly

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/stop-service?view=powershell-7.4

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_stop_service.yml)
