---
sigma_id: "2d32dd6f-3196-4093-b9eb-1ad8ab088ca5"
title: "Suspicious Response File Execution Via Odbcconf.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_response_file_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_response_file_susp.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2d32dd6f-3196-4093-b9eb-1ad8ab088ca5"
  - "Suspicious Response File Execution Via Odbcconf.EXE"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of "odbcconf" with the "-f" flag in order to load a response file with a non-".rsp" extension.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218008-odbcconf|T1218.008: Odbcconf]]

## Detection

```yaml
selection_img:
- Image|endswith: \odbcconf.exe
- OriginalFileName: odbcconf.exe
selection_cli:
  CommandLine|contains|windash: ' -f '
filter_main_rsp_ext:
  CommandLine|contains: .rsp
filter_main_runonce_odbc:
  ParentImage: C:\Windows\System32\runonce.exe
  Image: C:\Windows\System32\odbcconf.exe
  CommandLine|contains: .exe /E /F "C:\WINDOWS\system32\odbcconf.tmp"
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/sql/odbc/odbcconf-exe?view=sql-server-ver16
- https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/
- https://www.trendmicro.com/en_us/research/17/h/backdoor-carrying-emails-set-sights-on-russian-speaking-businesses.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_response_file_susp.yml)
