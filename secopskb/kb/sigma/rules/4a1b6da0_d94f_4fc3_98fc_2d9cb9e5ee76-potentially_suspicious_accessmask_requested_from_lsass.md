---
sigma_id: "4a1b6da0-d94f-4fc3-98fc-2d9cb9e5ee76"
title: "Potentially Suspicious AccessMask Requested From LSASS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_lsass_dump_generic.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_lsass_dump_generic.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "4a1b6da0-d94f-4fc3-98fc-2d9cb9e5ee76"
  - "Potentially Suspicious AccessMask Requested From LSASS"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious AccessMask Requested From LSASS

Detects process handle on LSASS process with certain access mask

## Metadata

- Rule ID: 4a1b6da0-d94f-4fc3-98fc-2d9cb9e5ee76
- Status: test
- Level: medium
- Author: Roberto Rodriguez, Teymur Kheirkhabarov, Dimitrios Slamaris, Mark Russinovich, Aleksey Potapov, oscd.community (update)
- Date: 2019-11-01
- Modified: 2023-12-19
- Source Path: rules/windows/builtin/security/win_security_susp_lsass_dump_generic.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_1:
  EventID: 4656
  ObjectName|endswith: \lsass.exe
  AccessMask|contains:
  - '0x40'
  - '0x1400'
  - '0x100000'
  - '0x1410'
  - '0x1010'
  - '0x1438'
  - '0x143a'
  - '0x1418'
  - '0x1f0fff'
  - '0x1f1fff'
  - '0x1f2fff'
  - '0x1f3fff'
selection_2:
  EventID: 4663
  ObjectName|endswith: \lsass.exe
  AccessList|contains:
  - '4484'
  - '4416'
filter_main_specific:
  ProcessName|endswith:
  - \csrss.exe
  - \GamingServices.exe
  - \lsm.exe
  - \MicrosoftEdgeUpdate.exe
  - \minionhost.exe
  - \MRT.exe
  - \MsMpEng.exe
  - \perfmon.exe
  - \procexp.exe
  - \procexp64.exe
  - \svchost.exe
  - \taskmgr.exe
  - \thor.exe
  - \thor64.exe
  - \vmtoolsd.exe
  - \VsTskMgr.exe
  - \wininit.exe
  - \wmiprvse.exe
  - RtkAudUService64
  ProcessName|contains:
  - :\Program Files (x86)\
  - :\Program Files\
  - :\ProgramData\Microsoft\Windows Defender\Platform\
  - :\Windows\SysNative\
  - :\Windows\System32\
  - :\Windows\SysWow64\
  - :\Windows\Temp\asgard2-agent\
filter_main_generic:
  ProcessName|contains: :\Program Files
filter_main_exact:
  ProcessName|endswith:
  - :\Windows\System32\taskhostw.exe
  - :\Windows\System32\msiexec.exe
  - :\Windows\CCM\CcmExec.exe
filter_main_sysmon:
  ProcessName|endswith: :\Windows\Sysmon64.exe
  AccessList|contains: '%%4484'
filter_main_aurora:
  ProcessName|contains: :\Windows\Temp\asgard2-agent-sc\aurora\
  ProcessName|endswith: \aurora-agent-64.exe
  AccessList|contains: '%%4484'
filter_main_scenarioengine:
  ProcessName|endswith: \x64\SCENARIOENGINE.EXE
  AccessList|contains: '%%4484'
filter_main_avira1:
  ProcessName|contains|all:
  - :\Users\
  - \AppData\Local\Temp\is-
  ProcessName|endswith: \avira_system_speedup.tmp
  AccessList|contains: '%%4484'
filter_main_avira2:
  ProcessName|contains: :\Windows\Temp\
  ProcessName|endswith: \avira_speedup_setup_update.tmp
  AccessList|contains: '%%4484'
filter_main_snmp:
  ProcessName|endswith: :\Windows\System32\snmp.exe
  AccessList|contains: '%%4484'
filter_main_googleupdate:
  ProcessName|contains: :\Windows\SystemTemp\
  ProcessName|endswith: \GoogleUpdate.exe
  AccessList|contains: '%%4484'
filter_optional_procmon:
  ProcessName|endswith:
  - \procmon64.exe
  - \procmon.exe
  AccessList|contains: '%%4484'
condition: 1 of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate software accessing LSASS process for legitimate reason; update the whitelist with it

## References

- https://web.archive.org/web/20230208123920/https://cyberwardog.blogspot.com/2017/03/chronicles-of-threat-hunter-hunting-for_22.html
- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_lsass_dump_generic.yml)
