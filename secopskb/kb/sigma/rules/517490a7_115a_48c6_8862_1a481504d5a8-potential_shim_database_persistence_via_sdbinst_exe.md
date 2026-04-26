---
sigma_id: "517490a7-115a-48c6-8862-1a481504d5a8"
title: "Potential Shim Database Persistence via Sdbinst.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sdbinst_shim_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sdbinst_shim_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "517490a7-115a-48c6-8862-1a481504d5a8"
  - "Potential Shim Database Persistence via Sdbinst.EXE"
attack_technique_ids:
  - "T1546.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Shim Database Persistence via Sdbinst.EXE

Detects installation of a new shim using sdbinst.exe.
Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by application shims

## Metadata

- Rule ID: 517490a7-115a-48c6-8862-1a481504d5a8
- Status: test
- Level: medium
- Author: Markus Neis
- Date: 2019-01-16
- Modified: 2023-12-06
- Source Path: rules/windows/process_creation/proc_creation_win_sdbinst_shim_persistence.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \sdbinst.exe
- OriginalFileName: sdbinst.exe
selection_cli:
  CommandLine|contains: .sdb
filter_optional_iis:
  ParentImage|endswith: \msiexec.exe
  CommandLine|contains:
  - :\Program Files (x86)\IIS Express\iisexpressshim.sdb
  - :\Program Files\IIS Express\iisexpressshim.sdb
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.mandiant.com/resources/blog/fin7-shim-databases-persistence

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sdbinst_shim_persistence.yml)
