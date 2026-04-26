---
sigma_id: "6e968eb1-5f05-4dac-94e9-fd0c5cb49fd6"
title: "Uncommon Link.EXE Parent Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_link_uncommon_parent_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_link_uncommon_parent_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6e968eb1-5f05-4dac-94e9-fd0c5cb49fd6"
  - "Uncommon Link.EXE Parent Process"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Link.EXE Parent Process

Detects an uncommon parent process of "LINK.EXE".
Link.EXE in Microsoft incremental linker. Its a utility usually bundled with Visual Studio installation.
Multiple utilities often found in the same folder (editbin.exe, dumpbin.exe, lib.exe, etc) have a hardcode call to the "LINK.EXE" binary without checking its validity.
This would allow an attacker to sideload any binary with the name "link.exe" if one of the aforementioned tools get executed from a different location.
By filtering the known locations of such utilities we can spot uncommon parent process of LINK.EXE that might be suspicious or malicious.

## Metadata

- Rule ID: 6e968eb1-5f05-4dac-94e9-fd0c5cb49fd6
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-22
- Modified: 2024-06-27
- Source Path: rules/windows/process_creation/proc_creation_win_link_uncommon_parent_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \link.exe
  CommandLine|contains: LINK /
filter_main_visual_studio:
  ParentImage|startswith:
  - C:\Program Files\Microsoft Visual Studio\
  - C:\Program Files (x86)\Microsoft Visual Studio\
  ParentImage|contains:
  - \VC\bin\
  - \VC\Tools\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1560732860935729152

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_link_uncommon_parent_process.yml)
