---
sigma_id: "1816994b-42e1-4fb1-afd2-134d88184f71"
title: "PowerShell Base64 Encoded WMI Classes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_wmi_classes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_wmi_classes.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1816994b-42e1-4fb1-afd2-134d88184f71"
  - "PowerShell Base64 Encoded WMI Classes"
attack_technique_ids:
  - "T1059.001"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects calls to base64 encoded WMI class such as "Win32_ShadowCopy", "Win32_ScheduledJob", etc.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_cli_shadowcopy:
  CommandLine|contains:
  - VwBpAG4AMwAyAF8AUwBoAGEAZABvAHcAYwBvAHAAeQ
  - cAaQBuADMAMgBfAFMAaABhAGQAbwB3AGMAbwBwAHkA
  - XAGkAbgAzADIAXwBTAGgAYQBkAG8AdwBjAG8AcAB5A
  - V2luMzJfU2hhZG93Y29we
  - dpbjMyX1NoYWRvd2NvcH
  - XaW4zMl9TaGFkb3djb3B5
selection_cli_scheduledJob:
  CommandLine|contains:
  - VwBpAG4AMwAyAF8AUwBjAGgAZQBkAHUAbABlAGQASgBvAGIA
  - cAaQBuADMAMgBfAFMAYwBoAGUAZAB1AGwAZQBkAEoAbwBiA
  - XAGkAbgAzADIAXwBTAGMAaABlAGQAdQBsAGUAZABKAG8AYg
  - V2luMzJfU2NoZWR1bGVkSm9i
  - dpbjMyX1NjaGVkdWxlZEpvY
  - XaW4zMl9TY2hlZHVsZWRKb2
selection_cli_process:
  CommandLine|contains:
  - VwBpAG4AMwAyAF8AUAByAG8AYwBlAHMAcw
  - cAaQBuADMAMgBfAFAAcgBvAGMAZQBzAHMA
  - XAGkAbgAzADIAXwBQAHIAbwBjAGUAcwBzA
  - V2luMzJfUHJvY2Vzc
  - dpbjMyX1Byb2Nlc3
  - XaW4zMl9Qcm9jZXNz
selection_cli_useraccount:
  CommandLine|contains:
  - VwBpAG4AMwAyAF8AVQBzAGUAcgBBAGMAYwBvAHUAbgB0A
  - cAaQBuADMAMgBfAFUAcwBlAHIAQQBjAGMAbwB1AG4AdA
  - XAGkAbgAzADIAXwBVAHMAZQByAEEAYwBjAG8AdQBuAHQA
  - V2luMzJfVXNlckFjY291bn
  - dpbjMyX1VzZXJBY2NvdW50
  - XaW4zMl9Vc2VyQWNjb3Vud
selection_cli_loggedonuser:
  CommandLine|contains:
  - VwBpAG4AMwAyAF8ATABvAGcAZwBlAGQATwBuAFUAcwBlAHIA
  - cAaQBuADMAMgBfAEwAbwBnAGcAZQBkAE8AbgBVAHMAZQByA
  - XAGkAbgAzADIAXwBMAG8AZwBnAGUAZABPAG4AVQBzAGUAcg
  - V2luMzJfTG9nZ2VkT25Vc2Vy
  - dpbjMyX0xvZ2dlZE9uVXNlc
  - XaW4zMl9Mb2dnZWRPblVzZX
condition: selection_img and 1 of selection_cli_*
```

## False Positives

- Unknown

## References

- https://github.com/Neo23x0/Raccine/blob/20a569fa21625086433dcce8bb2765d0ea08dcb6/yara/mal_revil.yar

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_wmi_classes.yml)
