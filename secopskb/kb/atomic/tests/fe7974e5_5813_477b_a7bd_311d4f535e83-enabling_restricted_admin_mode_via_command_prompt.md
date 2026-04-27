---
atomic_guid: "fe7974e5-5813-477b-a7bd-311d4f535e83"
title: "Enabling Restricted Admin Mode via Command_Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "fe7974e5-5813-477b-a7bd-311d4f535e83"
  - "Enabling Restricted Admin Mode via Command_Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enabling Restricted Admin Mode via Command_Prompt

Enabling Restricted Admin Mode via Command_Prompt,enables an attacker to perform a pass-the-hash attack using RDP.

See [Passing the Hash with Remote Desktop](https://www.kali.org/blog/passing-hash-remote-desktop/)

## Metadata

- Atomic GUID: fe7974e5-5813-477b-a7bd-311d4f535e83
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "hklm\system\currentcontrolset\control\lsa" /f /v DisableRestrictedAdmin /t REG_DWORD /d 0
```

### Cleanup

```cmd
reg delete "hklm\system\currentcontrolset\control\lsa" /f /v DisableRestrictedAdmin >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
