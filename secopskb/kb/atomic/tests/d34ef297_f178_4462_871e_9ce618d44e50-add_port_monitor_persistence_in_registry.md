---
atomic_guid: "d34ef297-f178-4462-871e-9ce618d44e50"
title: "Add Port Monitor persistence in Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.010"
attack_technique_name: "Boot or Logon Autostart Execution: Port Monitors"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.010/T1547.010.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "d34ef297-f178-4462-871e-9ce618d44e50"
  - "Add Port Monitor persistence in Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Add Port Monitor persistence in Registry

Add key-value pair to a Windows Port Monitor registry. On the subsequent reboot DLL will be execute under spoolsv with NT AUTHORITY/SYSTEM privilege.

## Metadata

- Atomic GUID: d34ef297-f178-4462-871e-9ce618d44e50
- Technique: T1547.010: Boot or Logon Autostart Execution: Port Monitors
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1547.010/T1547.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.010]]

## Input Arguments

### monitor_dll

- description: Addition to port monitor registry key. Normally refers to a DLL name in C:\Windows\System32 but an arbitrary DLL can be specified with the absolute path.
- type: path
- default: $PathToAtomicsFolder\T1547.010\bin\PortMonitor.dll

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "hklm\system\currentcontrolset\control\print\monitors\AtomicRedTeam" /v "Driver" /d "#{monitor_dll}" /t REG_SZ /f
```

### Cleanup

```cmd
reg delete "hklm\system\currentcontrolset\control\print\monitors\AtomicRedTeam" /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.010/T1547.010.yaml)
