---
sigma_id: "c443012c-7928-43bf-ac20-7eda5efe61ad"
title: "Suspicious Uninstall of Windows Defender Feature via PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_uninstall_defender_feature.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_uninstall_defender_feature.yml"
build_date: "2026-04-27 19:13:57"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c443012c-7928-43bf-ac20-7eda5efe61ad"
  - "Suspicious Uninstall of Windows Defender Feature via PowerShell"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of PowerShell with Uninstall-WindowsFeature or Remove-WindowsFeature cmdlets to disable or remove the Windows Defender GUI feature, a common technique used by adversaries to evade defenses.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell_ISE.EXE
  - PowerShell.EXE
  - pwsh.dll
selection_cli_uninstall:
  CommandLine|contains:
  - Uninstall-WindowsFeature
  - Remove-WindowsFeature
selection_cli_defender_feature:
  CommandLine|contains: Windows-Defender
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/powershell/module/microsoft.windows.servermanager.migration/uninstall-windowsfeature
- https://thedfirreport.com/2023/04/03/malicious-iso-file-leads-to-domain-wide-ransomware

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_uninstall_defender_feature.yml)
