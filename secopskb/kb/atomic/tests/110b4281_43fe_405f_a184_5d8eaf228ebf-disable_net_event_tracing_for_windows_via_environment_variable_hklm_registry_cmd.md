---
atomic_guid: "110b4281-43fe-405f-a184-5d8eaf228ebf"
title: "Disable .NET Event Tracing for Windows Via Environment Variable HKLM Registry - Cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "110b4281-43fe-405f-a184-5d8eaf228ebf"
  - "Disable .NET Event Tracing for Windows Via Environment Variable HKLM Registry - Cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables ETW for the .NET Framework by setting the COMPlus_ETWEnabled environment variable to 0 in the HKLM registry using the reg.exe utility. In order for changes to take effect a reboot might be required.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v COMPlus_ETWEnabled /t REG_SZ /d 0 /f
```

### Cleanup

```cmd
REG DELETE "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v COMPlus_ETWEnabled /f > nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
