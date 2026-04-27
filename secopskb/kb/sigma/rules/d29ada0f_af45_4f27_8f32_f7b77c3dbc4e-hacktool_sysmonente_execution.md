---
sigma_id: "d29ada0f-af45-4f27-8f32-f7b77c3dbc4e"
title: "HackTool - SysmonEnte Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_hktl_sysmonente.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_sysmonente.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "d29ada0f-af45-4f27-8f32-f7b77c3dbc4e"
  - "HackTool - SysmonEnte Execution"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of SysmonEnte, a tool to attack the integrity of Sysmon

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Detection

```yaml
selection_sysmon:
  TargetImage|contains:
  - :\Windows\Sysmon.exe
  - :\Windows\Sysmon64.exe
  GrantedAccess: '0x1400'
selection_calltrace:
  CallTrace: Ente
filter_main_generic:
  SourceImage|contains:
  - :\Program Files (x86)\
  - :\Program Files\
  - :\Windows\System32\
  - :\Windows\SysWOW64\
filter_main_msdefender:
  SourceImage|contains: :\ProgramData\Microsoft\Windows Defender\Platform\
  SourceImage|endswith: \MsMpEng.exe
condition: ( selection_sysmon and not 1 of filter_main_* ) or selection_calltrace
```

## False Positives

- Unknown

## References

- https://codewhitesec.blogspot.com/2022/09/attacks-on-sysmon-revisited-sysmonente.html
- https://github.com/codewhitesec/SysmonEnte/
- https://github.com/codewhitesec/SysmonEnte/blob/fe267690fcc799fbda15398243615a30451d9099/screens/1.png

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_sysmonente.yml)
