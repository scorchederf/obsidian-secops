---
sigma_id: "9525dc73-0327-438c-8c04-13c0e037e9da"
title: "Regsvr32 Execution From Potential Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9525dc73-0327-438c-8c04-13c0e037e9da"
  - "Regsvr32 Execution From Potential Suspicious Location"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Regsvr32 Execution From Potential Suspicious Location

Detects execution of regsvr32 where the DLL is located in a potentially suspicious location.

## Metadata

- Rule ID: 9525dc73-0327-438c-8c04-13c0e037e9da
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-26
- Source Path: rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml

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
selection_cli:
  CommandLine|contains:
  - :\ProgramData\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
  - \AppData\Roaming\
condition: all of selection_*
```

## False Positives

- Some installers might execute "regsvr32" with DLLs located in %TEMP% or in %PROGRAMDATA%. Apply additional filters if necessary.

## References

- https://web.archive.org/web/20171001085340/https://subt0x10.blogspot.com/2017/04/bypass-application-whitelisting-script.html
- https://app.any.run/tasks/34221348-072d-4b70-93f3-aa71f6ebecad/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_exec_path_1.yml)
