---
sigma_id: "05c36dd6-79d6-4a9a-97da-3db20298ab2d"
title: "XSL Script Execution Via WMIC.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "05c36dd6-79d6-4a9a-97da-3db20298ab2d"
  - "XSL Script Execution Via WMIC.EXE"
attack_technique_ids:
  - "T1047"
  - "T1220"
  - "T1059.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# XSL Script Execution Via WMIC.EXE

Detects the execution of WMIC with the "format" flag to potentially load local XSL files.
Adversaries abuse this functionality to execute arbitrary files while potentially bypassing application whitelisting defenses.
Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML files.

## Metadata

- Rule ID: 05c36dd6-79d6-4a9a-97da-3db20298ab2d
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community, Swachchhanda Shrawan Poudel
- Date: 2019-10-21
- Modified: 2026-01-24
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
- Hashes|contains:
  - IMPHASH=1B1A3F43BF37B5BFE60751F2EE2F326E
  - IMPHASH=37777A96245A3C74EB217308F3546F4C
  - IMPHASH=9D87C9D67CE724033C0B40CC4CA1B206
  - IMPHASH=B12619881D79C3ACADF45E752A58554A
  - IMPHASH=16A48C3CABF98A9DC1BF02C07FE1EA00
selection_cmd:
  CommandLine|contains|windash: '-format:'
filter_main_known_format:
  CommandLine|contains:
  - Format:List
  - Format:htable
  - Format:hform
  - Format:table
  - Format:mof
  - Format:value
  - Format:rawxml
  - Format:xml
  - Format:csv
filter_main_remote_operation:
  CommandLine|contains:
  - ://
  - \\\\
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- WMIC.exe FP depend on scripts and administrative methods used in the monitored environment.
- Static format arguments - https://petri.com/command-line-wmi-part-3

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1220/T1220.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml)
