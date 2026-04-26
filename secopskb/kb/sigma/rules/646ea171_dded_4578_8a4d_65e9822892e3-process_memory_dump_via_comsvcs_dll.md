---
sigma_id: "646ea171-dded-4578-8a4d-65e9822892e3"
title: "Process Memory Dump Via Comsvcs.DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_process_dump_via_comsvcs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_process_dump_via_comsvcs.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "646ea171-dded-4578-8a4d-65e9822892e3"
  - "Process Memory Dump Via Comsvcs.DLL"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Memory Dump Via Comsvcs.DLL

Detects a process memory dump via "comsvcs.dll" using rundll32, covering multiple different techniques (ordinal, minidump function, etc.)

## Metadata

- Rule ID: 646ea171-dded-4578-8a4d-65e9822892e3
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Modexp, Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2020-02-18
- Modified: 2025-02-23
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_process_dump_via_comsvcs.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
- CommandLine|contains: rundll32
selection_cli_1:
  CommandLine|contains|all:
  - comsvcs
  - full
  CommandLine|contains:
  - '#-'
  - '#+'
  - '#24'
  - '24 '
  - MiniDump
  - '#65560'
selection_generic:
  CommandLine|contains|all:
  - '24'
  - comsvcs
  - full
  CommandLine|contains:
  - ' #'
  - ',#'
  - ', #'
  - '"#'
condition: (selection_img and 1 of selection_cli_*) or selection_generic
```

## False Positives

- Unlikely

## References

- https://twitter.com/shantanukhande/status/1229348874298388484
- https://twitter.com/pythonresponder/status/1385064506049630211?s=21
- https://twitter.com/Hexacorn/status/1224848930795552769
- https://modexp.wordpress.com/2019/08/30/minidumpwritedump-via-com-services-dll/
- https://twitter.com/SBousseaden/status/1167417096374050817
- https://twitter.com/Wietze/status/1542107456507203586
- https://github.com/Hackndo/lsassy/blob/14d8f8ae596ecf22b449bfe919829173b8a07635/lsassy/dumpmethod/comsvcs.py
- https://www.youtube.com/watch?v=52tAmVLg1KM&t=2070s

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_process_dump_via_comsvcs.yml)
