---
sigma_id: "7f43c430-5001-4f8b-aaa9-c3b88f18fa5c"
title: "Execute From Alternate Data Streams"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7f43c430-5001-4f8b-aaa9-c3b88f18fa5c"
  - "Execute From Alternate Data Streams"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execute From Alternate Data Streams

Detects execution from an Alternate Data Stream (ADS). Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection

## Metadata

- Rule ID: 7f43c430-5001-4f8b-aaa9-c3b88f18fa5c
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-09-01
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection_stream:
  CommandLine|contains: 'txt:'
selection_tools_type:
  CommandLine|contains|all:
  - 'type '
  - ' > '
selection_tools_makecab:
  CommandLine|contains|all:
  - 'makecab '
  - .cab
selection_tools_reg:
  CommandLine|contains|all:
  - 'reg '
  - ' export '
selection_tools_regedit:
  CommandLine|contains|all:
  - 'regedit '
  - ' /E '
selection_tools_esentutl:
  CommandLine|contains|all:
  - 'esentutl '
  - ' /y '
  - ' /d '
  - ' /o '
condition: selection_stream and (1 of selection_tools_*)
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.004/T1564.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml)
