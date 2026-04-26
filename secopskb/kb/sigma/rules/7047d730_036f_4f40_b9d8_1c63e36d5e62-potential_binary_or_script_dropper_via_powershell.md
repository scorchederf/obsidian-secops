---
sigma_id: "7047d730-036f-4f40-b9d8-1c63e36d5e62"
title: "Potential Binary Or Script Dropper Via PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_powershell_drop_binary_or_script.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_drop_binary_or_script.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "7047d730-036f-4f40-b9d8-1c63e36d5e62"
  - "Potential Binary Or Script Dropper Via PowerShell"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Binary Or Script Dropper Via PowerShell

Detects PowerShell creating a binary executable or a script file.

## Metadata

- Rule ID: 7047d730-036f-4f40-b9d8-1c63e36d5e62
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-17
- Modified: 2025-07-04
- Source Path: rules/windows/file/file_event/file_event_win_powershell_drop_binary_or_script.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \powershell_ise.exe
  - \pwsh.exe
  TargetFilename|endswith:
  - .bat
  - .chm
  - .cmd
  - .com
  - .dll
  - .exe
  - .hta
  - .jar
  - .js
  - .ocx
  - .scr
  - .sys
  - .vbe
  - .vbs
  - .wsf
filter_main_user_temp:
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains: \AppData\Local\Temp\
  TargetFilename|endswith:
  - .dll
  - .exe
filter_main_other_temp:
  TargetFilename|startswith:
  - C:\Windows\Temp\
  - C:\Windows\SystemTemp\
  TargetFilename|endswith:
  - .dll
  - .exe
filter_main_powershell_module:
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains: \WindowsPowerShell\Modules\
  TargetFilename|endswith: .dll
filter_main_nuget:
  TargetFilename|startswith: C:\Program Files\PackageManagement\ProviderAssemblies\nuget\
  TargetFilename|endswith: \Microsoft.PackageManagement.NuGetProvider.dll
condition: selection and not 1 of filter_main_*
```

## False Positives

- False positives will differ depending on the environment and scripts used. Apply additional filters accordingly.

## References

- https://www.zscaler.com/blogs/security-research/onenote-growing-threat-malware-distribution

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_drop_binary_or_script.yml)
