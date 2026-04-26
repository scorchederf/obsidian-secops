---
atomic_guid: "a768aaa2-2442-475c-8990-69cf33af0f4e"
title: "Disable ConsentPromptBehaviorAdmin via registry keys"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "a768aaa2-2442-475c-8990-69cf33af0f4e"
  - "Disable ConsentPromptBehaviorAdmin via registry keys"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable ConsentPromptBehaviorAdmin via registry keys

This atomic regarding setting ConsentPromptBehaviorAdmin to 0 configures the UAC so that it does not prompt for consent or credentials when actions requiring elevated privileges are performed by users in the administrators group. This means that any operation that would normally trigger a UAC prompt will proceed automatically without user interaction.

## Metadata

- Atomic GUID: a768aaa2-2442-475c-8990-69cf33af0f4e
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 5 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
