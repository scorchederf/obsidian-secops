---
sigma_id: "7530cd3d-7671-43e3-b209-976966f6ea48"
title: "Renamed CURL.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_curl.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_curl.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7530cd3d-7671-43e3-b209-976966f6ea48"
  - "Renamed CURL.EXE Execution"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed CURL.EXE Execution

Detects the execution of a renamed "CURL.exe" binary based on the PE metadata fields

## Metadata

- Rule ID: 7530cd3d-7671-43e3-b209-976966f6ea48
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-09-11
- Modified: 2023-10-12
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_curl.yml

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
- OriginalFileName: curl.exe
- Description: The curl executable
filter_main_img:
  Image|contains: \curl
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/Kostastsale/status/1700965142828290260

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_curl.yml)
