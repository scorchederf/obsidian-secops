---
car_id: "CAR-2019-04-004"
title: "Credential Dumping via Mimikatz"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2019-04-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-004.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2019-04-004"
  - "Credential Dumping via Mimikatz"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
platforms:
  - "Windows"
implementation_types:
  - "splunk"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Credential dumpers like Mimikatz can be loaded into memory and from there read data from another processes. This analytic looks for instances where processes are requesting specific permissions to read parts of the LSASS process in order to detect when credential dumping is occurring. One weakness is that all current implementations are “overtuned” to look for common access patterns used by Mimikatz.

*This requires information about process access, e.g. Sysmon Event ID 10. That currently doesn’t have a CAR data model mapping, since we currently lack any open/access actions for Processes. If this changes, we will update the data model requirements.*

## ATT&CK Coverage

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Implementations

### splunk

This is specific to the way Mimikatz works currently, and thus is fragile to both future updates and non-default configurations of Mimikatz.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_data__ EventCode=10
TargetImage="C:\\WINDOWS\\system32\\lsass.exe"
(GrantedAccess=0x1410 OR GrantedAccess=0x1010 OR GrantedAccess=0x1438 OR GrantedAccess=0x143a OR GrantedAccess=0x1418)
CallTrace="C:\\windows\\SYSTEM32\\ntdll.dll+*|C:\\windows\\System32\\KERNELBASE.dll+20edd|UNKNOWN(*)"
| table _time hostname user SourceImage GrantedAccess
```

### splunk

This is an outlier version of the above without including the specific call trace. This should work in more (but not all) situations however runs more slowly and will have more false positives - typically installers.

- Data Model: Sysmon native

```splunk
earliest=-d@d latest=now() index=__your_sysmon_data__
  EventCode=10
  TargetImage="C:\\WINDOWS\\system32\\lsass.exe"
  (GrantedAccess=0x1410 OR GrantedAccess=0x1010 OR GrantedAccess=0x1438 OR GrantedAccess=0x143a OR GrantedAccess=0x1418)
| search NOT [ search earliest=-7d@d latest=-2d@d index=__your_sysmon_data__ EventCode=10 TargetImage="C:\\WINDOWS\\system32\\lsass.exe" (GrantedAccess=0x1410 OR GrantedAccess=0x1010 OR GrantedAccess=0x1438 OR GrantedAccess=0x143a OR GrantedAccess=0x1418)
  | dedup SourceImage
  | fields SourceImage ]
| table  _time hostname user SourceImage GrantedAccess
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=10 image="C:\Windows\system32\lsass.exe" (access="0x1410" OR access="0x1010" OR access="0x1438" OR access="0x143a" OR access="0x1418") call_trace="C:\windows\SYSTEM32\ntdll.dll+*|C:\windows\System32\KERNELBASE.dll+20edd|UNKNOWN(*)"
| fields log_ts, host, user, source_image, access
```

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2019-04-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-04-004.yaml)
