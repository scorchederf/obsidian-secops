---
sigma_id: "d4ca7c59-e9e4-42d8-bf57-91a776efcb87"
title: "LOLBIN Execution From Abnormal Drive"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_lolbin_exec_from_non_c_drive.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_lolbin_exec_from_non_c_drive.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d4ca7c59-e9e4-42d8-bf57-91a776efcb87"
  - "LOLBIN Execution From Abnormal Drive"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LOLBIN Execution From Abnormal Drive

Detects LOLBINs executing from an abnormal or uncommon drive such as a mounted ISO.

## Metadata

- Rule ID: d4ca7c59-e9e4-42d8-bf57-91a776efcb87
- Status: test
- Level: medium
- Author: Christopher Peacock '@securepeacock', SCYTHE '@scythe_io', Angelo Violetti - SEC Consult '@angelo_violetti', Aaron Herman
- Date: 2022-01-25
- Modified: 2023-08-29
- Source Path: rules/windows/process_creation/proc_creation_win_susp_lolbin_exec_from_non_c_drive.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image|endswith:
  - \calc.exe
  - \certutil.exe
  - \cmstp.exe
  - \cscript.exe
  - \installutil.exe
  - \mshta.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- OriginalFileName:
  - CALC.EXE
  - CertUtil.exe
  - CMSTP.EXE
  - cscript.exe
  - installutil.exe
  - MSHTA.EXE
  - REGSVR32.EXE
  - RUNDLL32.EXE
  - wscript.exe
filter_main_currentdirectory:
  CurrentDirectory|contains: C:\
filter_main_empty:
  CurrentDirectory: ''
filter_main_null:
  CurrentDirectory: null
condition: selection and not 1 of filter_main_*
```

## False Positives

- Rare false positives could occur on servers with multiple drives.

## References

- https://thedfirreport.com/2021/12/13/diavol-ransomware/
- https://www.scythe.io/library/threat-emulation-qakbot
- https://sec-consult.com/blog/detail/bumblebee-hunting-with-a-velociraptor/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_lolbin_exec_from_non_c_drive.yml)
