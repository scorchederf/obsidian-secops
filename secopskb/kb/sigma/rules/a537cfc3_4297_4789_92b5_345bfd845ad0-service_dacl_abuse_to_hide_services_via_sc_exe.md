---
sigma_id: "a537cfc3-4297-4789-92b5-345bfd845ad0"
title: "Service DACL Abuse To Hide Services Via Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_sdset_hide_sevices.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_hide_sevices.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a537cfc3-4297-4789-92b5-345bfd845ad0"
  - "Service DACL Abuse To Hide Services Via Sc.EXE"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service DACL Abuse To Hide Services Via Sc.EXE

Detects usage of the "sc.exe" utility adding a new service with special permission seen used by threat actors which makes the service hidden and unremovable.

## Metadata

- Rule ID: a537cfc3-4297-4789-92b5-345bfd845ad0
- Status: test
- Level: high
- Author: Andreas Hunkeler (@Karneades)
- Date: 2021-12-20
- Modified: 2022-08-08
- Source Path: rules/windows/process_creation/proc_creation_win_sc_sdset_hide_sevices.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \sc.exe
- OriginalFileName: sc.exe
selection_cli:
  CommandLine|contains|all:
  - sdset
  - DCLCWPDTSD
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blog.talosintelligence.com/2021/10/threat-hunting-in-large-datasets-by.html
- https://www.sans.org/blog/red-team-tactics-hiding-windows-services/
- https://twitter.com/Alh4zr3d/status/1580925761996828672
- https://itconnect.uw.edu/tools-services-support/it-systems-infrastructure/msinf/other-help/understanding-sddl-syntax/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_hide_sevices.yml)
