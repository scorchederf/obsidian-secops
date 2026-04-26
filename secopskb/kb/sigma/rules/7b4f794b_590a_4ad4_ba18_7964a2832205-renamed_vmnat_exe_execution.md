---
sigma_id: "7b4f794b-590a-4ad4-ba18-7964a2832205"
title: "Renamed Vmnat.exe Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_vmnat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_vmnat.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7b4f794b-590a-4ad4-ba18-7964a2832205"
  - "Renamed Vmnat.exe Execution"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed Vmnat.exe Execution

Detects renamed vmnat.exe or portable version that can be used for DLL side-loading

## Metadata

- Rule ID: 7b4f794b-590a-4ad4-ba18-7964a2832205
- Status: test
- Level: high
- Author: elhoim
- Date: 2022-09-09
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_vmnat.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  OriginalFileName: vmnat.exe
filter_rename:
  Image|endswith: vmnat.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://twitter.com/malmoeb/status/1525901219247845376

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_vmnat.yml)
