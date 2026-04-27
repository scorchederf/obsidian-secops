---
sigma_id: "1af57a4b-460a-4738-9034-db68b880c665"
title: "PowerShell SAM Copy"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_sam_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_sam_access.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1af57a4b-460a-4738-9034-db68b880c665"
  - "PowerShell SAM Copy"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell SAM Copy

Detects suspicious PowerShell scripts accessing SAM hives

## Metadata

- Rule ID: 1af57a4b-460a-4738-9034-db68b880c665
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-07-29
- Modified: 2023-01-06
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_sam_access.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection_1:
  CommandLine|contains|all:
  - \HarddiskVolumeShadowCopy
  - System32\config\sam
selection_2:
  CommandLine|contains:
  - Copy-Item
  - cp $_.
  - cpi $_.
  - copy $_.
  - .File]::Copy(
condition: all of selection*
```

## False Positives

- Some rare backup scenarios
- PowerShell scripts fixing HiveNightmare / SeriousSAM ACLs

## References

- https://twitter.com/splinter_code/status/1420546784250769408

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_sam_access.yml)
