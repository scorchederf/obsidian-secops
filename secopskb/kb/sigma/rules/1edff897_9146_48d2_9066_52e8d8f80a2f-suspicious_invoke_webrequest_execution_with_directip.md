---
sigma_id: "1edff897-9146-48d2-9066-52e8d8f80a2f"
title: "Suspicious Invoke-WebRequest Execution With DirectIP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_invoke_webrequest_direct_ip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_invoke_webrequest_direct_ip.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1edff897-9146-48d2-9066-52e8d8f80a2f"
  - "Suspicious Invoke-WebRequest Execution With DirectIP"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Invoke-WebRequest Execution With DirectIP

Detects calls to PowerShell with Invoke-WebRequest cmdlet using direct IP access

## Metadata

- Rule ID: 1edff897-9146-48d2-9066-52e8d8f80a2f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-21
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_invoke_webrequest_direct_ip.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - powershell_ise.EXE
  - PowerShell.EXE
  - pwsh.dll
selection_commands:
  CommandLine|contains:
  - 'curl '
  - Invoke-RestMethod
  - Invoke-WebRequest
  - ' irm '
  - 'iwr '
  - 'wget '
selection_ip:
  CommandLine|contains:
  - ://1
  - ://2
  - ://3
  - ://4
  - ://5
  - ://6
  - ://7
  - ://8
  - ://9
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.huntress.com/blog/critical-vulnerabilities-in-papercut-print-management-software

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_invoke_webrequest_direct_ip.yml)
