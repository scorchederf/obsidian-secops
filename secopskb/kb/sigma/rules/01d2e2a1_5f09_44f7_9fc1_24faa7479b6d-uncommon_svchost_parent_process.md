---
sigma_id: "01d2e2a1-5f09-44f7-9fc1-24faa7479b6d"
title: "Uncommon Svchost Parent Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_svchost_uncommon_parent_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_uncommon_parent_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "01d2e2a1-5f09-44f7-9fc1-24faa7479b6d"
  - "Uncommon Svchost Parent Process"
attack_technique_ids:
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Svchost Parent Process

Detects an uncommon svchost parent process

## Metadata

- Rule ID: 01d2e2a1-5f09-44f7-9fc1-24faa7479b6d
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-08-15
- Modified: 2022-06-28
- Source Path: rules/windows/process_creation/proc_creation_win_svchost_uncommon_parent_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
  Image|endswith: \svchost.exe
filter_main_generic:
  ParentImage|endswith:
  - \Mrt.exe
  - \MsMpEng.exe
  - \ngen.exe
  - \rpcnet.exe
  - \services.exe
  - \TiWorker.exe
filter_main_parent_null:
  ParentImage: null
filter_main_parent_empty:
  ParentImage:
  - '-'
  - ''
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_uncommon_parent_process.yml)
