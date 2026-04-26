---
sigma_id: "b9e8c7d6-a5f4-4e3d-8b1a-9f0c8d7e6a5b"
title: "Windows Defender Context Menu Removed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_defender_remove_context_menu.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_defender_remove_context_menu.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b9e8c7d6-a5f4-4e3d-8b1a-9f0c8d7e6a5b"
  - "Windows Defender Context Menu Removed"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Context Menu Removed

Detects the use of reg.exe or PowerShell to delete the Windows Defender context menu handler registry keys.
This action removes the "Scan with Microsoft Defender" option from the right-click menu for files, directories, and drives.
Attackers may use this technique to hinder manual, on-demand scans and reduce the visibility of the security product.

## Metadata

- Rule ID: b9e8c7d6-a5f4-4e3d-8b1a-9f0c8d7e6a5b
- Status: experimental
- Level: high
- Author: Matt Anderson (Huntress)
- Date: 2025-07-09
- Source Path: rules/windows/process_creation/proc_creation_win_defender_remove_context_menu.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \reg.exe
- OriginalFileName:
  - powershell_ise.EXE
  - PowerShell.EXE
  - pwsh.dll
  - reg.exe
selection_action:
  CommandLine|contains:
  - del
  - Remove-Item
  - 'ri '
selection_reg_path:
  CommandLine|contains: \shellex\ContextMenuHandlers\EPP
condition: all of selection_*
```

## False Positives

- May be part of a system customization or "debloating" script, but this is highly unusual in a managed corporate environment.

## References

- https://research.splunk.com/endpoint/395ed5fe-ad13-4366-9405-a228427bdd91/
- https://winaero.com/how-to-delete-scan-with-windows-defender-from-context-menu-in-windows-10/
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/
- https://blog.malwarebytes.com/malwarebytes-news/2021/02/lazyscripter-from-empire-to-double-rat/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_defender_remove_context_menu.yml)
