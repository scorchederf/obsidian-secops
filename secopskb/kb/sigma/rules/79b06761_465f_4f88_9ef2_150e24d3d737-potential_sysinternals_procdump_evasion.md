---
sigma_id: "79b06761-465f-4f88-9ef2-150e24d3d737"
title: "Potential SysInternals ProcDump Evasion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_procdump_evasion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_procdump_evasion.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "79b06761-465f-4f88-9ef2-150e24d3d737"
  - "Potential SysInternals ProcDump Evasion"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential SysInternals ProcDump Evasion

Detects uses of the SysInternals ProcDump utility in which ProcDump or its output get renamed, or a dump file is moved or copied to a different name

## Metadata

- Rule ID: 79b06761-465f-4f88-9ef2-150e24d3d737
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-11
- Modified: 2023-05-09
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_procdump_evasion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_1:
  CommandLine|contains:
  - copy procdump
  - move procdump
selection_2:
  CommandLine|contains|all:
  - 'copy '
  - '.dmp '
  CommandLine|contains:
  - 2.dmp
  - lsass
  - out.dmp
selection_3:
  CommandLine|contains:
  - copy lsass.exe_
  - move lsass.exe_
condition: 1 of selection_*
```

## False Positives

- False positives are expected in cases in which ProcDump just gets copied to a different directory without any renaming

## References

- https://twitter.com/mrd0x/status/1480785527901204481

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_procdump_evasion.yml)
