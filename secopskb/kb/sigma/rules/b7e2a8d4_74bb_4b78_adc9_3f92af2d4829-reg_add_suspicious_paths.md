---
sigma_id: "b7e2a8d4-74bb-4b78-adc9-3f92af2d4829"
title: "Reg Add Suspicious Paths"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_susp_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_susp_paths.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b7e2a8d4-74bb-4b78-adc9-3f92af2d4829"
  - "Reg Add Suspicious Paths"
attack_technique_ids:
  - "T1112"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Reg Add Suspicious Paths

Detects when an adversary uses the reg.exe utility to add or modify new keys or subkeys

## Metadata

- Rule ID: b7e2a8d4-74bb-4b78-adc9-3f92af2d4829
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Modified: 2022-10-10
- Source Path: rules/windows/process_creation/proc_creation_win_reg_susp_paths.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_reg:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_path:
  CommandLine|contains:
  - \AppDataLow\Software\Microsoft\
  - \Policies\Microsoft\Windows\OOBE
  - \Policies\Microsoft\Windows NT\CurrentVersion\Winlogon
  - \SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon
  - \CurrentControlSet\Control\SecurityProviders\WDigest
  - \Microsoft\Windows Defender\
condition: all of selection_*
```

## False Positives

- Rare legitimate add to registry via cli (to these locations)

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1112/T1112.md
- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1562.001/T1562.001.md
- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_susp_paths.yml)
