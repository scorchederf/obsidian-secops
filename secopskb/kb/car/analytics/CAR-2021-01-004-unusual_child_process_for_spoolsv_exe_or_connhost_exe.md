---
car_id: "CAR-2021-01-004"
title: "Unusual Child Process for Spoolsv.Exe or Connhost.Exe"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-01-004/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-004.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2021-01-004"
  - "Unusual Child Process for Spoolsv.Exe or Connhost.Exe"
attack_technique_ids:
  - "T1068"
platforms:
  - "Windows"
implementation_types:
  - "Splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

After gaining initial access to a system, threat actors attempt to escalate privileges as they may be operating within a lower privileged process which does not allow them to access protected information or carry out tasks which require higher permissions. A common way of escalating privileges in a system is by externally invoking and exploiting spoolsv or connhost executables, both of which are legitimate Windows applications. This query searches for an invocation of either of these executables by a user, thus alerting us of any potentially malicious activity.

## ATT&CK Coverage

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]] (coverage: Low; tactics: TA0004)

## Implementations

### Splunk

This query looks for processes spawned by spoolsv.exe or connhost.exe externally, thus alerting us of potentially malicious activity.

- Data Model: Sysmon native

```splunk
(index=__your_sysmon_index__ EventCode=1) (Image=C:\\Windows\\System32\\spoolsv.exe* OR Image=C:\\Windows\\System32\\conhost.exe) ParentImage = "C:\\Windows\\System32\\cmd.exe"
```

## Data Model References

- process/create/command_line

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-01-004/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-004.yaml)
