---
sigma_id: "327ff235-94eb-4f06-b9de-aaee571324be"
title: "Regsvr32 Execution From Highly Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_2.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_2.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "327ff235-94eb-4f06-b9de-aaee571324be"
  - "Regsvr32 Execution From Highly Suspicious Location"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Regsvr32 Execution From Highly Suspicious Location

Detects execution of regsvr32 where the DLL is located in a highly suspicious locations

## Metadata

- Rule ID: 327ff235-94eb-4f06-b9de-aaee571324be
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-26
- Source Path: rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_2.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection_img:
- Image|endswith: \regsvr32.exe
- OriginalFileName: REGSVR32.EXE
selection_path_1:
  CommandLine|contains:
  - :\PerfLogs\
  - :\Temp\
  - \Windows\Registration\CRMLog
  - \Windows\System32\com\dmp\
  - \Windows\System32\FxsTmp\
  - \Windows\System32\Microsoft\Crypto\RSA\MachineKeys\
  - \Windows\System32\spool\drivers\color\
  - \Windows\System32\spool\PRINTERS\
  - \Windows\System32\spool\SERVERS\
  - \Windows\System32\Tasks_Migrated\
  - \Windows\System32\Tasks\Microsoft\Windows\SyncCenter\
  - \Windows\SysWOW64\com\dmp\
  - \Windows\SysWOW64\FxsTmp\
  - \Windows\SysWOW64\Tasks\Microsoft\Windows\PLA\System\
  - \Windows\SysWOW64\Tasks\Microsoft\Windows\SyncCenter\
  - \Windows\Tasks\
  - \Windows\Tracing\
selection_path_2:
  CommandLine|contains:
  - ' "C:\'
  - ' C:\'
  - ' ''C:\'
  - D:\
selection_exclude_known_dirs:
  CommandLine|contains:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\ProgramData\
  - C:\Users\
  - ' C:\Windows\'
  - ' "C:\Windows\'
  - ' ''C:\Windows\'
filter_main_empty:
  CommandLine: ''
filter_main_null:
  CommandLine: null
condition: selection_img and (selection_path_1 or (selection_path_2 and not selection_exclude_known_dirs))
  and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_2.yml)
