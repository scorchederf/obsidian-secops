---
sigma_id: "b8fd0e93-ff58-4cbd-8f48-1c114e342e62"
title: "Windows Binaries Write Suspicious Extensions"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_shell_write_susp_files_extensions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_shell_write_susp_files_extensions.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "b8fd0e93-ff58-4cbd-8f48-1c114e342e62"
  - "Windows Binaries Write Suspicious Extensions"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Binaries Write Suspicious Extensions

Detects Windows executables that write files with suspicious extensions

## Metadata

- Rule ID: b8fd0e93-ff58-4cbd-8f48-1c114e342e62
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-12
- Modified: 2025-10-07
- Source Path: rules/windows/file/file_event/file_event_win_shell_write_susp_files_extensions.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_generic:
  Image|endswith:
  - \csrss.exe
  - \lsass.exe
  - \RuntimeBroker.exe
  - \sihost.exe
  - \smss.exe
  - \wininit.exe
  - \winlogon.exe
  TargetFilename|endswith:
  - .bat
  - .dll
  - .exe
  - .hta
  - .iso
  - .ps1
  - .txt
  - .vbe
  - .vbs
selection_special:
  Image|endswith:
  - \dllhost.exe
  - \rundll32.exe
  - \svchost.exe
  TargetFilename|endswith:
  - .bat
  - .hta
  - .iso
  - .ps1
  - .vbe
  - .vbs
filter_main_AppLockerPolicyTest:
  Image: C:\Windows\System32\dllhost.exe
  TargetFilename|contains|all:
  - :\Users\
  - \AppData\Local\Temp\__PSScriptPolicyTest_
  TargetFilename|endswith: .ps1
filter_main_script_gpo_machine:
  Image: C:\Windows\system32\svchost.exe
  TargetFilename|contains|all:
  - C:\Windows\System32\GroupPolicy\DataStore\
  - \sysvol\
  - \Policies\
  - \Machine\Scripts\Startup\
  TargetFilename|endswith:
  - .ps1
  - .bat
filter_main_clipchamp:
  Image: C:\Windows\system32\svchost.exe
  TargetFilename|contains|all:
  - C:\Program Files\WindowsApps\Clipchamp
  - .ps1
filter_main_powershell_preview:
  Image:
  - C:\Windows\system32\svchost.exe
  - C:\Windows\SysWOW64\svchost.exe
  TargetFilename|startswith:
  - C:\Program Files\WindowsApps\Microsoft.PowerShellPreview
  - C:\Program Files (x86)\WindowsApps\Microsoft.PowerShellPreview
  TargetFilename|endswith: .ps1
condition: 1 of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_shell_write_susp_files_extensions.yml)
