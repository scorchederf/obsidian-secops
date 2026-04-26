---
sigma_id: "9f0a8bf3-a65b-440a-8c1e-5cb1547c8e70"
title: "New DLL Registered Via Odbcconf.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_register_dll_regsvr.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_register_dll_regsvr.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9f0a8bf3-a65b-440a-8c1e-5cb1547c8e70"
  - "New DLL Registered Via Odbcconf.EXE"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New DLL Registered Via Odbcconf.EXE

Detects execution of "odbcconf" with "REGSVR" in order to register a new DLL (equivalent to running regsvr32). Attackers abuse this to install and run malicious DLLs.

## Metadata

- Rule ID: 9f0a8bf3-a65b-440a-8c1e-5cb1547c8e70
- Status: test
- Level: medium
- Author: Kirill Kiryanov, Beyu Denis, Daniil Yugoslavskiy, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-22
- Source Path: rules/windows/process_creation/proc_creation_win_odbcconf_register_dll_regsvr.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.008]]

## Detection

```yaml
selection_img:
- Image|endswith: \odbcconf.exe
- OriginalFileName: odbcconf.exe
selection_cli:
  CommandLine|contains|all:
  - 'REGSVR '
  - .dll
condition: all of selection_*
```

## False Positives

- Legitimate DLLs being registered via "odbcconf" will generate false positives. Investigate the path of the DLL and its content to determine if the action is authorized.

## References

- https://learn.microsoft.com/en-us/sql/odbc/odbcconf-exe?view=sql-server-ver16
- https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/
- https://redcanary.com/blog/raspberry-robin/
- https://web.archive.org/web/20191023232753/https://twitter.com/Hexacorn/status/1187143326673330176
- https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/
- https://www.trendmicro.com/en_us/research/17/h/backdoor-carrying-emails-set-sights-on-russian-speaking-businesses.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_register_dll_regsvr.yml)
