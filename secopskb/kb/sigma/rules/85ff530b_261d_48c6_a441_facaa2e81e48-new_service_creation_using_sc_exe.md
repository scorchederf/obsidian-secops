---
sigma_id: "85ff530b-261d-48c6-a441-facaa2e81e48"
title: "New Service Creation Using Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_create_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_create_service.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "85ff530b-261d-48c6-a441-facaa2e81e48"
  - "New Service Creation Using Sc.EXE"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Service Creation Using Sc.EXE

Detects the creation of a new service using the "sc.exe" utility.

## Metadata

- Rule ID: 85ff530b-261d-48c6-a441-facaa2e81e48
- Status: test
- Level: low
- Author: Timur Zinniatullin, Daniil Yugoslavskiy, oscd.community
- Date: 2023-02-20
- Modified: 2025-09-01
- Source Path: rules/windows/process_creation/proc_creation_win_sc_create_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  Image|endswith: \sc.exe
  CommandLine|contains|all:
  - create
  - binPath
filter_optional_dropbox:
  ParentImage|startswith:
  - C:\Program Files (x86)\Dropbox\Client\
  - C:\Program Files\Dropbox\Client\
  ParentImage|endswith: \Dropbox.exe
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Legitimate administrator or user creates a service for legitimate reasons.
- Software installation

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1543.003/T1543.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_create_service.yml)
