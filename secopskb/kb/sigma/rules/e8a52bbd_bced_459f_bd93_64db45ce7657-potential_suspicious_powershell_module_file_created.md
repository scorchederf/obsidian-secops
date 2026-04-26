---
sigma_id: "e8a52bbd-bced-459f-bd93-64db45ce7657"
title: "Potential Suspicious PowerShell Module File Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_powershell_module_susp_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_module_susp_creation.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "e8a52bbd-bced-459f-bd93-64db45ce7657"
  - "Potential Suspicious PowerShell Module File Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious PowerShell Module File Created

Detects the creation of a new PowerShell module in the first folder of the module directory structure "\WindowsPowerShell\Modules\malware\malware.psm1". This is somewhat an uncommon practice as legitimate modules often includes a version folder.

## Metadata

- Rule ID: e8a52bbd-bced-459f-bd93-64db45ce7657
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-09
- Source Path: rules/windows/file/file_event/file_event_win_powershell_module_susp_creation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \\WindowsPowerShell\\Modules\\*\.ps
  - \\WindowsPowerShell\\Modules\\*\.dll
condition: selection
```

## False Positives

- False positive rate will vary depending on the environments. Additional filters might be required to make this logic usable in production.

## References

- Internal Research
- https://learn.microsoft.com/en-us/powershell/scripting/developer/module/understanding-a-windows-powershell-module?view=powershell-7.3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_powershell_module_susp_creation.yml)
