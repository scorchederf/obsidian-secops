---
sigma_id: "6f3e2987-db24-4c78-a860-b4f4095a7095"
title: "Files Added To An Archive Using Rar.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rar_compress_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rar_compress_data.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "6f3e2987-db24-4c78-a860-b4f4095a7095"
  - "Files Added To An Archive Using Rar.EXE"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Files Added To An Archive Using Rar.EXE

Detects usage of "rar" to add files to an archive for potential compression. An adversary may compress data (e.g. sensitive documents) that is collected prior to exfiltration in order to make it portable and minimize the amount of data sent over the network.

## Metadata

- Rule ID: 6f3e2987-db24-4c78-a860-b4f4095a7095
- Status: test
- Level: low
- Author: Timur Zinniatullin, E.M. Anhaus, oscd.community
- Date: 2019-10-21
- Modified: 2023-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_rar_compress_data.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection:
  Image|endswith: \rar.exe
  CommandLine|contains: ' a '
condition: selection
```

## False Positives

- Highly likely if rar is a default archiver in the monitored environment.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001.md
- https://eqllib.readthedocs.io/en/latest/analytics/1ec33c93-3d0b-4a28-8014-dbdaae5c60ae.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rar_compress_data.yml)
