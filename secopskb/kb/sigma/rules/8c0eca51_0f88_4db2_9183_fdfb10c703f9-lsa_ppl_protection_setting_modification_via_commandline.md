---
sigma_id: "8c0eca51-0f88-4db2-9183-fdfb10c703f9"
title: "LSA PPL Protection Setting Modification via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lsa_ppl_protection_setting_modification_via_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lsa_ppl_protection_setting_modification_via_cli.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8c0eca51-0f88-4db2-9183-fdfb10c703f9"
  - "LSA PPL Protection Setting Modification via CommandLine"
attack_technique_ids:
  - "T1562.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LSA PPL Protection Setting Modification via CommandLine

Detects modification of LSA PPL protection settings via CommandLine.
It may indicate an attempt to disable protection and enable credential dumping tools to access LSASS process memory.

## Metadata

- Rule ID: 8c0eca51-0f88-4db2-9183-fdfb10c703f9
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2022-03-22
- Modified: 2026-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_lsa_ppl_protection_setting_modification_via_cli.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.010]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \reg.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - reg.exe
  - powershell.exe
  - pwsh.dll
selection_cli_action:
  CommandLine|contains|all:
  - ControlSet
  - \Control\Lsa
  CommandLine|contains:
  - Set-ItemProperty
  - New-ItemProperty
  - ' add '
selection_key:
  CommandLine|contains:
  - IsPplAutoEnabled
  - RunAsPPL
  - RunAsPPLBoot
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell/
- https://github.com/shoober420/windows11-scripts/blob/38d83331738cd713ccb42f2c4557d17a27aefd98/Windows11Tweaks.bat#L1825

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lsa_ppl_protection_setting_modification_via_cli.yml)
