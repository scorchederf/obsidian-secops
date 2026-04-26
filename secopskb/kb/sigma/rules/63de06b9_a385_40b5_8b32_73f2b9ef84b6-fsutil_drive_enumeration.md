---
sigma_id: "63de06b9-a385-40b5-8b32-73f2b9ef84b6"
title: "Fsutil Drive Enumeration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_fsutil_drive_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsutil_drive_enumeration.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "63de06b9-a385-40b5-8b32-73f2b9ef84b6"
  - "Fsutil Drive Enumeration"
attack_technique_ids:
  - "T1120"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Fsutil Drive Enumeration

Attackers may leverage fsutil to enumerated connected drives.

## Metadata

- Rule ID: 63de06b9-a385-40b5-8b32-73f2b9ef84b6
- Status: test
- Level: low
- Author: Christopher Peacock '@securepeacock', SCYTHE '@scythe_io'
- Date: 2022-03-29
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_fsutil_drive_enumeration.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1120-peripheral_device_discovery|T1120]]

## Detection

```yaml
selection_img:
- Image|endswith: \fsutil.exe
- OriginalFileName: fsutil.exe
selection_cli:
  CommandLine|contains: drives
condition: all of selection_*
```

## False Positives

- Certain software or administrative tasks may trigger false positives.

## References

- Turla has used fsutil fsinfo drives to list connected drives.
- https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/discovery_peripheral_device.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_fsutil_drive_enumeration.yml)
