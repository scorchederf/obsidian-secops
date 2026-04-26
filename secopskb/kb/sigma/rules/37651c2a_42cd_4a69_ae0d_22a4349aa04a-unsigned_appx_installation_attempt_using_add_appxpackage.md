---
sigma_id: "37651c2a-42cd-4a69-ae0d-22a4349aa04a"
title: "Unsigned AppX Installation Attempt Using Add-AppxPackage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_install_unsigned_appx_packages.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_install_unsigned_appx_packages.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "37651c2a-42cd-4a69-ae0d-22a4349aa04a"
  - "Unsigned AppX Installation Attempt Using Add-AppxPackage"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unsigned AppX Installation Attempt Using Add-AppxPackage

Detects usage of the "Add-AppxPackage" or it's alias "Add-AppPackage" to install unsigned AppX packages

## Metadata

- Rule ID: 37651c2a-42cd-4a69-ae0d-22a4349aa04a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-31
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_install_unsigned_appx_packages.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_cmdlet:
  CommandLine|contains:
  - 'Add-AppPackage '
  - 'Add-AppxPackage '
selection_flag:
  CommandLine|contains: ' -AllowUnsigned'
condition: all of selection_*
```

## False Positives

- Installation of unsigned packages for testing purposes

## References

- https://learn.microsoft.com/en-us/windows/msix/package/unsigned-package
- https://twitter.com/WindowsDocs/status/1620078135080325122

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_install_unsigned_appx_packages.yml)
