---
sigma_id: "fd877b94-9bb5-4191-bb25-d79cbd93c167"
title: "Dumping of Sensitive Hives Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fd877b94-9bb5-4191-bb25-d79cbd93c167"
  - "Dumping of Sensitive Hives Via Reg.EXE"
attack_technique_ids:
  - "T1003.002"
  - "T1003.004"
  - "T1003.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dumping of Sensitive Hives Via Reg.EXE

Detects the usage of "reg.exe" in order to dump sensitive registry hives. This includes SAM, SYSTEM and SECURITY hives.

## Metadata

- Rule ID: fd877b94-9bb5-4191-bb25-d79cbd93c167
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, Endgame, JHasenbusch, Daniil Yugoslavskiy, oscd.community, frack113
- Date: 2019-10-22
- Modified: 2023-12-13
- Source Path: rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_cli_flag:
  CommandLine|contains:
  - ' save '
  - ' export '
  - ' ˢave '
  - ' eˣport '
selection_cli_hklm:
  CommandLine|contains:
  - hklm
  - hk˪m
  - hkey_local_machine
  - hkey_˪ocal_machine
  - hkey_loca˪_machine
  - hkey_˪oca˪_machine
selection_cli_hive:
  CommandLine|contains:
  - \system
  - \sam
  - \security
  - \ˢystem
  - \syˢtem
  - \ˢyˢtem
  - \ˢam
  - \ˢecurity
condition: all of selection_*
```

## False Positives

- Dumping hives for legitimate purpouse i.e. backup or forensic investigation

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment
- https://eqllib.readthedocs.io/en/latest/analytics/aed95fc6-5e3f-49dc-8b35-06508613f979.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003/T1003.md
- https://www.wietzebeukema.nl/blog/windows-command-line-obfuscation
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/T1003.002.md#atomic-test-1---registry-dump-of-sam-creds-and-secrets

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_dumping_sensitive_hives.yml)
