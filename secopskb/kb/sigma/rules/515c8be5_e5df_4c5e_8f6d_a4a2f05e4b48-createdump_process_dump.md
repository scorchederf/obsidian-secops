---
sigma_id: "515c8be5-e5df-4c5e-8f6d-a4a2f05e4b48"
title: "CreateDump Process Dump"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_createdump_lolbin_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_createdump_lolbin_execution.yml"
build_date: "2026-04-26 17:03:18"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CreateDump Process Dump

Detects uses of the createdump.exe LOLOBIN utility to dump process memory

## Metadata

- Rule ID: 515c8be5-e5df-4c5e-8f6d-a4a2f05e4b48
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-04
- Modified: 2022-08-19
- Source Path: rules/windows/process_creation/proc_creation_win_createdump_lolbin_execution.yml

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
