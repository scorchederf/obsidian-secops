---
sigma_id: "b36d01a3-ddaf-4804-be18-18a6247adfcd"
title: "Add Windows Capability Via PowerShell Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_add_windows_capability.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_add_windows_capability.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b36d01a3-ddaf-4804-be18-18a6247adfcd"
  - "Add Windows Capability Via PowerShell Cmdlet"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Add Windows Capability Via PowerShell Cmdlet

Detects usage of the "Add-WindowsCapability" cmdlet to add Windows capabilities. Notable capabilities could be "OpenSSH" and others.

## Metadata

- Rule ID: b36d01a3-ddaf-4804-be18-18a6247adfcd
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-22
- Modified: 2023-05-09
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_add_windows_capability.yml

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
  CommandLine|contains: Add-WindowsCapability
selection_capa:
  CommandLine|contains: OpenSSH.
condition: all of selection_*
```

## False Positives

- Legitimate usage of the capabilities by administrators or users. Add additional filters accordingly.

## References

- https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell
- https://www.virustotal.com/gui/file/af1c82237b6e5a3a7cdbad82cc498d298c67845d92971bada450023d1335e267/content

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_add_windows_capability.yml)
