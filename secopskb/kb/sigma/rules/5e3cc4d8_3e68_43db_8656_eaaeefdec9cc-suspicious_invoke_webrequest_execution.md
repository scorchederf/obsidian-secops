---
sigma_id: "5e3cc4d8-3e68-43db-8656-eaaeefdec9cc"
title: "Suspicious Invoke-WebRequest Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_invoke_webrequest_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_invoke_webrequest_download.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5e3cc4d8-3e68-43db-8656-eaaeefdec9cc"
  - "Suspicious Invoke-WebRequest Execution"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious call to Invoke-WebRequest cmdlet where the and output is located in a suspicious location

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

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
  - Invoke-WebRequest
  - 'iwr '
  - 'wget '
selection_flags:
  CommandLine|contains:
  - ' -ur'
  - ' -o'
selection_susp_locations:
  CommandLine|contains:
  - \AppData\
  - \Desktop\
  - \Temp\
  - \Users\Public\
  - '%AppData%'
  - '%Public%'
  - '%Temp%'
  - '%tmp%'
  - :\Windows\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.sentinelone.com/blog/living-off-windows-defender-lockbit-ransomware-sideloads-cobalt-strike-through-microsoft-security-tool/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_invoke_webrequest_download.yml)
