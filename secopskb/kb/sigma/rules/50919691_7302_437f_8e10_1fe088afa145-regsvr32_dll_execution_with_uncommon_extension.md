---
sigma_id: "50919691-7302-437f-8e10-1fe088afa145"
title: "Regsvr32 DLL Execution With Uncommon Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_uncommon_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_uncommon_extension.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "50919691-7302-437f-8e10-1fe088afa145"
  - "Regsvr32 DLL Execution With Uncommon Extension"
attack_technique_ids:
  - "T1574"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Regsvr32 DLL Execution With Uncommon Extension

Detects a "regsvr32" execution where the DLL doesn't contain a common file extension.

## Metadata

- Rule ID: 50919691-7302-437f-8e10-1fe088afa145
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2019-07-17
- Modified: 2023-05-24
- Source Path: rules/windows/process_creation/proc_creation_win_regsvr32_uncommon_extension.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]]

## Detection

```yaml
selection:
- Image|endswith: \regsvr32.exe
- OriginalFileName: REGSVR32.EXE
filter_main_legit_ext:
  CommandLine|contains:
  - .ax
  - .cpl
  - .dll
  - .ocx
filter_optional_pascal:
  CommandLine|contains: .ppl
filter_optional_avg:
  CommandLine|contains: .bav
filter_main_null_4688:
  CommandLine: null
filter_main_empty_4688:
  CommandLine: ''
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Other legitimate extensions currently not in the list either from third party or specific Windows components.

## References

- https://app.any.run/tasks/34221348-072d-4b70-93f3-aa71f6ebecad/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_uncommon_extension.yml)
