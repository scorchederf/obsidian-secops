---
atomic_guid: "aa875ed4-8935-47e2-b2c5-6ec00ab220d2"
title: "Tamper with Windows Defender Command Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "aa875ed4-8935-47e2-b2c5-6ec00ab220d2"
  - "Tamper with Windows Defender Command Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attempting to disable scheduled scanning and other parts of windows defender atp. These commands must be run as System, so they still fail as administrator.
However, adversaries do attempt to perform this action so monitoring for these command lines can help alert to other bad things going on. Upon execution, "Access Denied"
will be displayed twice and the WinDefend service status will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc stop WinDefend
sc config WinDefend start=disabled
sc query WinDefend
```

### Cleanup

```cmd
sc start WinDefend >nul 2>&1
sc config WinDefend start=enabled >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
