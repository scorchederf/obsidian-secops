---
sigma_id: "9b0b7ac3-6223-47aa-a3fd-e8f211e637db"
title: "Changing Existing Service ImagePath Value Via Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_service_imagepath_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_service_imagepath_change.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9b0b7ac3-6223-47aa-a3fd-e8f211e637db"
  - "Changing Existing Service ImagePath Value Via Reg.EXE"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Changing Existing Service ImagePath Value Via Reg.EXE

Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services.
Adversaries may use flaws in the permissions for registry to redirect from the originally specified executable to one that they control, in order to launch their own code at Service start.
Windows stores local service configuration information in the Registry under HKLM\SYSTEM\CurrentControlSet\Services

## Metadata

- Rule ID: 9b0b7ac3-6223-47aa-a3fd-e8f211e637db
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-30
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_reg_service_imagepath_change.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection:
  Image|endswith: \reg.exe
  CommandLine|contains|all:
  - 'add '
  - SYSTEM\CurrentControlSet\Services\
  - ' ImagePath '
selection_value:
  CommandLine|contains|windash: ' -d '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.011/T1574.011.md#atomic-test-2---service-imagepath-change-with-regexe

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_service_imagepath_change.yml)
