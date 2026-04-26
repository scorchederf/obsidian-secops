---
sigma_id: "84f52741-8834-4a8c-a413-2eb2269aa6c8"
title: "DllUnregisterServer Function Call Via Msiexec.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msiexec_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_dll.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "84f52741-8834-4a8c-a413-2eb2269aa6c8"
  - "DllUnregisterServer Function Call Via Msiexec.EXE"
attack_technique_ids:
  - "T1218.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DllUnregisterServer Function Call Via Msiexec.EXE

Detects MsiExec loading a DLL and calling its DllUnregisterServer function

## Metadata

- Rule ID: 84f52741-8834-4a8c-a413-2eb2269aa6c8
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-24
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_msiexec_dll.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Detection

```yaml
selection_img:
- Image|endswith: \msiexec.exe
- OriginalFileName: \msiexec.exe
selection_flag:
  CommandLine|contains|windash: ' -z '
selection_dll:
  CommandLine|contains: .dll
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.007/T1218.007.md
- https://lolbas-project.github.io/lolbas/Binaries/Msiexec/
- https://twitter.com/_st0pp3r_/status/1583914515996897281

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_dll.yml)
