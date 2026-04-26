---
sigma_id: "02b18447-ea83-4b1b-8805-714a8a34546a"
title: "Potential Mpclient.DLL Sideloading Via OfflineScannerShell.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_offlinescannershell_mpclient_sideloading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_offlinescannershell_mpclient_sideloading.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "02b18447-ea83-4b1b-8805-714a8a34546a"
  - "Potential Mpclient.DLL Sideloading Via OfflineScannerShell.EXE Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Mpclient.DLL Sideloading Via OfflineScannerShell.EXE Execution

Detects execution of Windows Defender "OfflineScannerShell.exe" from its non standard directory.
The "OfflineScannerShell.exe" binary is vulnerable to DLL side loading and will load any DLL named "mpclient.dll" from the current working directory.

## Metadata

- Rule ID: 02b18447-ea83-4b1b-8805-714a8a34546a
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-06
- Modified: 2023-08-03
- Source Path: rules/windows/process_creation/proc_creation_win_offlinescannershell_mpclient_sideloading.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
- Image|endswith: \OfflineScannerShell.exe
- OriginalFileName: OfflineScannerShell.exe
filter_main_legit_dir:
  CurrentDirectory: C:\Program Files\Windows Defender\Offline\
filter_main_empty:
  CurrentDirectory: ''
filter_main_null:
  CurrentDirectory: null
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/OfflineScannerShell/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_offlinescannershell_mpclient_sideloading.yml)
