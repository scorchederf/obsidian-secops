---
sigma_id: "de41232e-12e8-49fa-86bc-c05c7e722df9"
title: "Suspicious PowerShell Download - PoshModule"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_susp_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_download.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_module"
aliases:
  - "de41232e-12e8-49fa-86bc-c05c7e722df9"
  - "Suspicious PowerShell Download - PoshModule"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Download - PoshModule

Detects suspicious PowerShell download command

## Metadata

- Rule ID: de41232e-12e8-49fa-86bc-c05c7e722df9
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-05
- Modified: 2023-01-20
- Source Path: rules/windows/powershell/powershell_module/posh_pm_susp_download.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_webclient_:
  ContextInfo|contains: System.Net.WebClient
selection_function:
  ContextInfo|contains:
  - .DownloadFile(
  - .DownloadString(
condition: all of selection_*
```

## False Positives

- PowerShell scripts that download content from the Internet

## References

- https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient.downloadfile?view=net-8.0
- https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient.downloadstring?view=net-8.0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_download.yml)
