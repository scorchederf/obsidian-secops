---
sigma_id: "e36941d0-c0f0-443f-bc6f-cb2952eb69ea"
title: "PowerShell Module File Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_powershell_module_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_module_creation.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "e36941d0-c0f0-443f-bc6f-cb2952eb69ea"
  - "PowerShell Module File Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Module File Created

Detects the creation of a new PowerShell module ".psm1", ".psd1", ".dll", ".ps1", etc.

## Metadata

- Rule ID: e36941d0-c0f0-443f-bc6f-cb2952eb69ea
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-09
- Source Path: rules/windows/file/file_event/file_event_win_powershell_module_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  TargetFilename|contains:
  - \WindowsPowerShell\Modules\
  - \PowerShell\7\Modules\
condition: selection
```

## False Positives

- Likely

## References

- Internal Research
- https://learn.microsoft.com/en-us/powershell/scripting/developer/module/understanding-a-windows-powershell-module?view=powershell-7.3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_module_creation.yml)
