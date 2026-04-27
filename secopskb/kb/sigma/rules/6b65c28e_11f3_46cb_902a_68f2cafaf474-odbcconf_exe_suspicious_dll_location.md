---
sigma_id: "6b65c28e-11f3-46cb-902a-68f2cafaf474"
title: "Odbcconf.EXE Suspicious DLL Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_exec_susp_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_exec_susp_locations.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6b65c28e-11f3-46cb-902a-68f2cafaf474"
  - "Odbcconf.EXE Suspicious DLL Location"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of "odbcconf" where the path of the DLL being registered is located in a potentially suspicious location.

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
  CommandLine|contains:
  - :\PerfLogs\
  - :\ProgramData\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\Registration\CRMLog
  - :\Windows\System32\com\dmp\
  - :\Windows\System32\FxsTmp\
  - :\Windows\System32\Microsoft\Crypto\RSA\MachineKeys\
  - :\Windows\System32\spool\drivers\color\
  - :\Windows\System32\spool\PRINTERS\
  - :\Windows\System32\spool\SERVERS\
  - :\Windows\System32\Tasks_Migrated\
  - :\Windows\System32\Tasks\Microsoft\Windows\SyncCenter\
  - :\Windows\SysWOW64\com\dmp\
  - :\Windows\SysWOW64\FxsTmp\
  - :\Windows\SysWOW64\Tasks\Microsoft\Windows\PLA\System\
  - :\Windows\SysWOW64\Tasks\Microsoft\Windows\SyncCenter\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - :\Windows\Tracing\
  - \AppData\Local\Temp\
  - \AppData\Roaming\
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/sql/odbc/odbcconf-exe?view=sql-server-ver16
- https://www.trendmicro.com/en_us/research/17/h/backdoor-carrying-emails-set-sights-on-russian-speaking-businesses.html
- https://securityintelligence.com/posts/raspberry-robin-worm-dridex-malware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_exec_susp_locations.yml)
