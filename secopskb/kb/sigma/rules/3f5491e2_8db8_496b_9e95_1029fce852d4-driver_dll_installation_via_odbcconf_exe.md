---
sigma_id: "3f5491e2-8db8-496b-9e95-1029fce852d4"
title: "Driver/DLL Installation Via Odbcconf.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_driver_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_driver_install.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3f5491e2-8db8-496b-9e95-1029fce852d4"
  - "Driver/DLL Installation Via Odbcconf.EXE"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Driver/DLL Installation Via Odbcconf.EXE

Detects execution of "odbcconf" with "INSTALLDRIVER" which installs a new ODBC driver. Attackers abuse this to install and run malicious DLLs.

## Metadata

- Rule ID: 3f5491e2-8db8-496b-9e95-1029fce852d4
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-22
- Source Path: rules/windows/process_creation/proc_creation_win_odbcconf_driver_install.yml

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
  - 'INSTALLDRIVER '
  - .dll
condition: all of selection_*
```

## False Positives

- Legitimate driver DLLs being registered via "odbcconf" will generate false positives. Investigate the path of the DLL and its contents to determine if the action is authorized.

## References

- https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/
- https://web.archive.org/web/20191023232753/https://twitter.com/Hexacorn/status/1187143326673330176
- https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_driver_install.yml)
