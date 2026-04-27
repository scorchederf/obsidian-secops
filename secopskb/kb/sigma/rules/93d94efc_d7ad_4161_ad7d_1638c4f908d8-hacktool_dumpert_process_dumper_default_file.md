---
sigma_id: "93d94efc-d7ad-4161-ad7d-1638c4f908d8"
title: "HackTool - Dumpert Process Dumper Default File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_dumpert.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_dumpert.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "critical"
logsource: "windows / file_event"
aliases:
  - "93d94efc-d7ad-4161-ad7d-1638c4f908d8"
  - "HackTool - Dumpert Process Dumper Default File"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - Dumpert Process Dumper Default File

Detects the creation of the default dump file used by Outflank Dumpert tool. A process dumper, which dumps the lsass process memory

## Metadata

- Rule ID: 93d94efc-d7ad-4161-ad7d-1638c4f908d8
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2020-02-04
- Modified: 2023-05-09
- Source Path: rules/windows/file/file_event/file_event_win_hktl_dumpert.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  TargetFilename|endswith: dumpert.dmp
condition: selection
```

## False Positives

- Very unlikely

## References

- https://github.com/outflanknl/Dumpert
- https://unit42.paloaltonetworks.com/actors-still-exploiting-sharepoint-vulnerability/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_dumpert.yml)
