---
sigma_id: "264982dc-dbad-4dce-b707-1e0d3e0f73d9"
title: "Renamed NirCmd.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_nircmd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_nircmd.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "264982dc-dbad-4dce-b707-1e0d3e0f73d9"
  - "Renamed NirCmd.EXE Execution"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed NirCmd.EXE Execution

Detects the execution of a renamed "NirCmd.exe" binary based on the PE metadata fields.

## Metadata

- Rule ID: 264982dc-dbad-4dce-b707-1e0d3e0f73d9
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2024-03-11
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_nircmd.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  OriginalFileName: NirCmd.exe
filter_main_img:
  Image|endswith:
  - \nircmd.exe
  - \nircmdc.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-ttps-observed-in-mint-sandstorm-campaign-targeting-high-profile-individuals-at-universities-and-research-orgs/
- https://www.nirsoft.net/utils/nircmd.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_nircmd.yml)
