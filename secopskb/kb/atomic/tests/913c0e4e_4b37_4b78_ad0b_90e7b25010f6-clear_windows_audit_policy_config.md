---
atomic_guid: "913c0e4e-4b37-4b78-ad0b-90e7b25010f6"
title: "Clear Windows Audit Policy Config"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "913c0e4e-4b37-4b78-ad0b-90e7b25010f6"
  - "Clear Windows Audit Policy Config"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Clear the Windows audit policy using auditpol utility. This action would stop certain audit events from being recorded in the security log.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
auditpol /clear /y
auditpol /remove /allusers
```

### Cleanup

```cmd
auditpol /set /category:"Account Logon" /success:enable /failure:enable
auditpol /set /category:"Detailed Tracking" /success:enable
auditpol /set /category:"Logon/Logoff" /success:enable /failure:enable
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
