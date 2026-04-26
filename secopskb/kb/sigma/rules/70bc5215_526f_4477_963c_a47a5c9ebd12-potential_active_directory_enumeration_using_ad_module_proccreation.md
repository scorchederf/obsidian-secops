---
sigma_id: "70bc5215-526f-4477-963c-a47a5c9ebd12"
title: "Potential Active Directory Enumeration Using AD Module - ProcCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_active_directory_module_dll_import.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_active_directory_module_dll_import.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "70bc5215-526f-4477-963c-a47a5c9ebd12"
  - "Potential Active Directory Enumeration Using AD Module - ProcCreation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Active Directory Enumeration Using AD Module - ProcCreation

Detects usage of the "Import-Module" cmdlet to load the "Microsoft.ActiveDirectory.Management.dl" DLL. Which is often used by attackers to perform AD enumeration.

## Metadata

- Rule ID: 70bc5215-526f-4477-963c-a47a5c9ebd12
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-01-22
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_active_directory_module_dll_import.yml

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
  - 'Import-Module '
  - 'ipmo '
selection_dll:
  CommandLine|contains: Microsoft.ActiveDirectory.Management.dll
condition: all of selection_*
```

## False Positives

- Legitimate use of the library for administrative activity

## References

- https://github.com/samratashok/ADModule
- https://twitter.com/cyb3rops/status/1617108657166061568?s=20
- https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/active-directory-enumeration-with-ad-module-without-rsat-or-admin-privileges

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_active_directory_module_dll_import.yml)
