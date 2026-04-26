---
sigma_id: "f91ed517-a6ba-471d-9910-b3b4a398c0f3"
title: "Potentially Suspicious Windows App Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_appx_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_appx_execution.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f91ed517-a6ba-471d-9910-b3b4a398c0f3"
  - "Potentially Suspicious Windows App Activity"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Windows App Activity

Detects potentially suspicious child process of applications launched from inside the WindowsApps directory. This could be a sign of a rogue ".appx" package installation/execution

## Metadata

- Rule ID: f91ed517-a6ba-471d-9910-b3b4a398c0f3
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-12
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_susp_appx_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|contains: C:\Program Files\WindowsApps\
selection_susp_img:
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \powershell_ise.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
selection_susp_cli:
  CommandLine|contains:
  - cmd /c
  - Invoke-
  - Base64
filter_optional_terminal:
  ParentImage|contains: :\Program Files\WindowsApps\Microsoft.WindowsTerminal
  ParentImage|endswith: \WindowsTerminal.exe
  Image|endswith:
  - \powershell.exe
  - \cmd.exe
  - \pwsh.exe
filter_optional_sysinternals:
  ParentImage|startswith: C:\Program Files\WindowsApps\Microsoft.SysinternalsSuite
  Image|endswith: \cmd.exe
condition: selection_parent and 1 of selection_susp_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate packages that make use of external binaries such as Windows Terminal

## References

- https://news.sophos.com/en-us/2021/11/11/bazarloader-call-me-back-attack-abuses-windows-10-apps-mechanism/
- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_appx_execution.yml)
