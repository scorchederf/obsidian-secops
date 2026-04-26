---
sigma_id: "1eeed653-dbc8-4187-ad0c-eeebb20e6599"
title: "Potential SPN Enumeration Via Setspn.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_setspn_spn_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_setspn_spn_enumeration.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1eeed653-dbc8-4187-ad0c-eeebb20e6599"
  - "Potential SPN Enumeration Via Setspn.EXE"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential SPN Enumeration Via Setspn.EXE

Detects service principal name (SPN) enumeration used for Kerberoasting

## Metadata

- Rule ID: 1eeed653-dbc8-4187-ad0c-eeebb20e6599
- Status: test
- Level: medium
- Author: Markus Neis, keepwatch
- Date: 2018-11-14
- Modified: 2023-10-23
- Source Path: rules/windows/process_creation/proc_creation_win_setspn_spn_enumeration.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection_pe:
- Image|endswith: \setspn.exe
- OriginalFileName: setspn.exe
- Description|contains|all:
  - Query or reset the computer
  - SPN attribute
selection_cli:
  CommandLine|contains:
  - ' -q '
  - ' /q '
condition: all of selection_*
```

## False Positives

- Administration activity

## References

- https://web.archive.org/web/20200329173843/https://p16.praetorian.com/blog/how-to-use-kerberoasting-t1208-for-privilege-escalation
- https://www.praetorian.com/blog/how-to-use-kerberoasting-t1208-for-privilege-escalation/?edition=2019

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_setspn_spn_enumeration.yml)
