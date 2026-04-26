---
sigma_id: "dee0a7a3-f200-4112-a99b-952196d81e42"
title: "DumpMinitool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dee0a7a3-f200-4112-a99b-952196d81e42"
  - "DumpMinitool Execution"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DumpMinitool Execution

Detects the use of "DumpMinitool.exe" a tool that allows the dump of process memory via the use of the "MiniDumpWriteDump"

## Metadata

- Rule ID: dee0a7a3-f200-4112-a99b-952196d81e42
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2022-04-06
- Modified: 2023-04-12
- Source Path: rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml

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
- Image|endswith:
  - \DumpMinitool.exe
  - \DumpMinitool.x86.exe
  - \DumpMinitool.arm64.exe
- OriginalFileName:
  - DumpMinitool.exe
  - DumpMinitool.x86.exe
  - DumpMinitool.arm64.exe
selection_cli:
  CommandLine|contains:
  - ' Full'
  - ' Mini'
  - ' WithHeap'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1511415432888131586
- https://twitter.com/mrd0x/status/1511489821247684615
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/DumpMinitool/
- https://gist.github.com/nasbench/6d58c3c125e2fa1b8f7a09754c1b087f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dumpminitool_execution.yml)
