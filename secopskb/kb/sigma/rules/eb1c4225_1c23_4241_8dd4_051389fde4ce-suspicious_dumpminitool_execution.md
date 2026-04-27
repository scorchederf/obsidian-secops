---
sigma_id: "eb1c4225-1c23-4241-8dd4-051389fde4ce"
title: "Suspicious DumpMinitool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dumpminitool_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dumpminitool_susp_execution.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "eb1c4225-1c23-4241-8dd4-051389fde4ce"
  - "Suspicious DumpMinitool Execution"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious ways to use the "DumpMinitool.exe" binary

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
- Image|endswith:
  - \DumpMinitool.exe
  - \DumpMinitool.x86.exe
  - \DumpMinitool.arm64.exe
- OriginalFileName:
  - DumpMinitool.exe
  - DumpMinitool.x86.exe
  - DumpMinitool.arm64.exe
filter_folder:
  Image|contains:
  - \Microsoft Visual Studio\
  - \Extensions\
susp_flags:
  CommandLine|contains: .txt
cmd_has_flags:
  CommandLine|contains:
  - ' Full'
  - ' Mini'
  - ' WithHeap'
filter_cmd_misses_flags:
  CommandLine|contains: --dumpType
condition: selection and ( ( not filter_folder ) or susp_flags or ( cmd_has_flags
  and not filter_cmd_misses_flags ) )
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1511415432888131586
- https://twitter.com/mrd0x/status/1511489821247684615
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/DumpMinitool/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dumpminitool_susp_execution.yml)
