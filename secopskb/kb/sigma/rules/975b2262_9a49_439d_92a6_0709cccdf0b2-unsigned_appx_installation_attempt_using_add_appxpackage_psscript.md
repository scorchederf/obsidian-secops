---
sigma_id: "975b2262-9a49-439d-92a6-0709cccdf0b2"
title: "Unsigned AppX Installation Attempt Using Add-AppxPackage - PsScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_install_unsigned_appx_packages.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_install_unsigned_appx_packages.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "975b2262-9a49-439d-92a6-0709cccdf0b2"
  - "Unsigned AppX Installation Attempt Using Add-AppxPackage - PsScript"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unsigned AppX Installation Attempt Using Add-AppxPackage - PsScript

Detects usage of the "Add-AppxPackage" or it's alias "Add-AppPackage" to install unsigned AppX packages

## Metadata

- Rule ID: 975b2262-9a49-439d-92a6-0709cccdf0b2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-31
- Source Path: rules/windows/powershell/powershell_script/posh_ps_install_unsigned_appx_packages.yml

## Logsource

- category: ps_script
- definition: Script Block Logging must be enable
- product: windows

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains:
  - 'Add-AppPackage '
  - 'Add-AppxPackage '
selection_flag:
  ScriptBlockText|contains: ' -AllowUnsigned'
condition: all of selection_*
```

## False Positives

- Installation of unsigned packages for testing purposes

## References

- https://learn.microsoft.com/en-us/windows/msix/package/unsigned-package
- https://twitter.com/WindowsDocs/status/1620078135080325122

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_install_unsigned_appx_packages.yml)
