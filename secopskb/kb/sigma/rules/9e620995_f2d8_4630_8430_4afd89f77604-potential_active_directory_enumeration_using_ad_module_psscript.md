---
sigma_id: "9e620995-f2d8-4630-8430-4afd89f77604"
title: "Potential Active Directory Enumeration Using AD Module - PsScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_active_directory_module_dll_import.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_active_directory_module_dll_import.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "9e620995-f2d8-4630-8430-4afd89f77604"
  - "Potential Active Directory Enumeration Using AD Module - PsScript"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Active Directory Enumeration Using AD Module - PsScript

Detects usage of the "Import-Module" cmdlet to load the "Microsoft.ActiveDirectory.Management.dl" DLL. Which is often used by attackers to perform AD enumeration.

## Metadata

- Rule ID: 9e620995-f2d8-4630-8430-4afd89f77604
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali
- Date: 2023-01-22
- Source Path: rules/windows/powershell/powershell_script/posh_ps_active_directory_module_dll_import.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enable
- product: windows

## Detection

```yaml
selection_generic:
  ScriptBlockText|contains|all:
  - 'Import-Module '
  - Microsoft.ActiveDirectory.Management.dll
selection_specific:
  ScriptBlockText|contains: ipmo Microsoft.ActiveDirectory.Management.dll
condition: 1 of selection_*
```

## False Positives

- Legitimate use of the library for administrative activity

## References

- https://github.com/samratashok/ADModule
- https://twitter.com/cyb3rops/status/1617108657166061568?s=20
- https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-enumeration-with-ad-module-without-rsat-or-admin-privileges

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_active_directory_module_dll_import.yml)
