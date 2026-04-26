---
sigma_id: "99c8be4f-3087-4f9f-9c24-8c7e257b442e"
title: "Setup16.EXE Execution With Custom .Lst File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_setup16_custom_lst_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_setup16_custom_lst_execution.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "99c8be4f-3087-4f9f-9c24-8c7e257b442e"
  - "Setup16.EXE Execution With Custom .Lst File"
attack_technique_ids:
  - "T1574.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Setup16.EXE Execution With Custom .Lst File

Detects the execution of "Setup16.EXE" and old installation utility with a custom ".lst" file.
These ".lst" file can contain references to external program that "Setup16.EXE" will execute.
Attackers and adversaries might leverage this as a living of the land utility.

## Metadata

- Rule ID: 99c8be4f-3087-4f9f-9c24-8c7e257b442e
- Status: test
- Level: medium
- Author: frack113
- Date: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_setup16_custom_lst_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.005]]

## Detection

```yaml
selection:
  ParentImage: C:\Windows\SysWOW64\setup16.exe
  ParentCommandLine|contains: ' -m '
filter_optional_valid_path:
  Image|startswith: C:\~MSSETUP.T\
condition: selection and not 1 of filter_optional_*
```

## False Positives

- On modern Windows system, the "Setup16" utility is practically never used, hence false positive should be very rare.

## References

- https://www.hexacorn.com/blog/2024/10/12/the-sweet16-the-oldbin-lolbin-called-setup16-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_setup16_custom_lst_execution.yml)
