---
sigma_id: "1a1ed54a-2ba4-4221-94d5-01dee560d71e"
title: "Renamed CreateDump Utility Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_createdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_createdump.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1a1ed54a-2ba4-4221-94d5-01dee560d71e"
  - "Renamed CreateDump Utility Execution"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed CreateDump Utility Execution

Detects uses of a renamed legitimate createdump.exe LOLOBIN utility to dump process memory

## Metadata

- Rule ID: 1a1ed54a-2ba4-4221-94d5-01dee560d71e
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-09-20
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_createdump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_pe:
  OriginalFileName: FX_VER_INTERNALNAME_STR
selection_cli:
- CommandLine|contains|all:
  - ' -u '
  - ' -f '
  - .dmp
- CommandLine|contains|all:
  - ' --full '
  - ' --name '
  - .dmp
filter:
  Image|endswith: \createdump.exe
condition: 1 of selection_* and not filter
```

## False Positives

- Command lines that use the same flags

## References

- https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/
- https://twitter.com/bopin2020/status/1366400799199272960

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_createdump.yml)
