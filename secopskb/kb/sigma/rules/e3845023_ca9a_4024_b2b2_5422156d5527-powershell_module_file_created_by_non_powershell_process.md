---
sigma_id: "e3845023-ca9a-4024-b2b2-5422156d5527"
title: "PowerShell Module File Created By Non-PowerShell Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_powershell_module_uncommon_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_module_uncommon_creation.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "e3845023-ca9a-4024-b2b2-5422156d5527"
  - "PowerShell Module File Created By Non-PowerShell Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Module File Created By Non-PowerShell Process

Detects the creation of a new PowerShell module ".psm1", ".psd1", ".dll", ".ps1", etc. by a non-PowerShell process

## Metadata

- Rule ID: e3845023-ca9a-4024-b2b2-5422156d5527
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-09
- Modified: 2025-10-07
- Source Path: rules/windows/file/file_event/file_event_win_powershell_module_uncommon_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|contains:
  - \WindowsPowerShell\Modules\
  - \PowerShell\7\Modules\
filter_main_pwsh:
  Image|endswith:
  - :\Program Files\PowerShell\7-preview\pwsh.exe
  - :\Program Files\PowerShell\7\pwsh.exe
  - :\Windows\System32\poqexec.exe
  - :\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe
  - :\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
  - :\Windows\SysWOW64\poqexec.exe
  - :\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell_ise.exe
  - :\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
filter_main_msiexec:
  Image:
  - C:\Windows\System32\msiexec.exe
  - C:\Windows\SysWOW64\msiexec.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://learn.microsoft.com/en-us/powershell/scripting/developer/module/understanding-a-windows-powershell-module?view=powershell-7.3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_module_uncommon_creation.yml)
