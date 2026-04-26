---
sigma_id: "74176142-4684-4d8a-8b0a-713257e7df8e"
title: "Potential Active Directory Enumeration Using AD Module - PsModule"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_active_directory_module_dll_import.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_active_directory_module_dll_import.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / ps_module"
aliases:
  - "74176142-4684-4d8a-8b0a-713257e7df8e"
  - "Potential Active Directory Enumeration Using AD Module - PsModule"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Active Directory Enumeration Using AD Module - PsModule

Detects usage of the "Import-Module" cmdlet to load the "Microsoft.ActiveDirectory.Management.dl" DLL. Which is often used by attackers to perform AD enumeration.

## Metadata

- Rule ID: 74176142-4684-4d8a-8b0a-713257e7df8e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2023-01-22
- Source Path: rules/windows/powershell/powershell_module/posh_pm_active_directory_module_dll_import.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## Detection

```yaml
selection_cmdlet:
  Payload|contains:
  - 'Import-Module '
  - 'ipmo '
selection_dll:
  Payload|contains: Microsoft.ActiveDirectory.Management.dll
condition: all of selection_*
```

## False Positives

- Legitimate use of the library for administrative activity

## References

- https://github.com/samratashok/ADModule
- https://twitter.com/cyb3rops/status/1617108657166061568?s=20
- https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-enumeration-with-ad-module-without-rsat-or-admin-privileges

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_active_directory_module_dll_import.yml)
