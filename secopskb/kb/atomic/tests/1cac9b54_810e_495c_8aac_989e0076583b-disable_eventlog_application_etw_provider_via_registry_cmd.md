---
atomic_guid: "1cac9b54-810e-495c-8aac-989e0076583b"
title: "Disable EventLog-Application ETW Provider Via Registry - Cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "1cac9b54-810e-495c-8aac-989e0076583b"
  - "Disable EventLog-Application ETW Provider Via Registry - Cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable EventLog-Application ETW Provider Via Registry - Cmd

This atomic simulates an activity where an attacker disables a specific ETW provider from the EventLog-Application ETW Auto Logger session using the reg.exe utility to update the Windows registry value "Enabled". This would effectivly remove that provider from the session and cause to not emit any logs of that type. The changes would only take effect after a restart.

## Metadata

- Atomic GUID: 1cac9b54-810e-495c-8aac-989e0076583b
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### ETWProviderGUID

- description: Microsoft-Windows-SenseIR ETW Provider GUID
- type: string
- default: {B6D775EF-1436-4FE6-BAD3-9E436319E218}

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\EventLog-Application\#{ETWProviderGUID}" /v "Enabled" /t REG_DWORD /d "0" /f
```

### Cleanup

```cmd
reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\EventLog-Application\#{ETWProviderGUID}" /v "Enabled" /t REG_DWORD /d "1" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
