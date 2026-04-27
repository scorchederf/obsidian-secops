---
sigma_id: "515c8be5-e5df-4c5e-8f6d-a4a2f05e4b48"
title: "CreateDump Process Dump"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_createdump_lolbin_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_createdump_lolbin_execution.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "515c8be5-e5df-4c5e-8f6d-a4a2f05e4b48"
  - "CreateDump Process Dump"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects uses of the createdump.exe LOLOBIN utility to dump process memory

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036: Masquerading]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection_img:
- Image|endswith: \createdump.exe
- OriginalFileName: FX_VER_INTERNALNAME_STR
selection_cli:
  CommandLine|contains:
  - ' -u '
  - ' --full '
  - ' -f '
  - ' --name '
  - '.dmp '
condition: all of selection_*
```

## False Positives

- Command lines that use the same flags

## References

- https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/
- https://twitter.com/bopin2020/status/1366400799199272960

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_createdump_lolbin_execution.yml)
