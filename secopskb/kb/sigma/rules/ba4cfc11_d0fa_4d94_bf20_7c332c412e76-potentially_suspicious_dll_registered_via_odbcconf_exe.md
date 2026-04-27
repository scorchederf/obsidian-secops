---
sigma_id: "ba4cfc11-d0fa-4d94-bf20-7c332c412e76"
title: "Potentially Suspicious DLL Registered Via Odbcconf.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_register_dll_regsvr_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_register_dll_regsvr_susp.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ba4cfc11-d0fa-4d94-bf20-7c332c412e76"
  - "Potentially Suspicious DLL Registered Via Odbcconf.EXE"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of "odbcconf" with the "REGSVR" action where the DLL in question doesn't contain a ".dll" extension. Which is often used as a method to evade defenses.

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
  CommandLine|contains: 'REGSVR '
filter_main_dll_ext:
  CommandLine|contains: .dll
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/sql/odbc/odbcconf-exe?view=sql-server-ver16
- https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/
- https://www.trendmicro.com/en_us/research/17/h/backdoor-carrying-emails-set-sights-on-russian-speaking-businesses.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_register_dll_regsvr_susp.yml)
