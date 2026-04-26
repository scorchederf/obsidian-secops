---
atomic_guid: "4b81bcfa-fb0a-45e9-90c2-e3efe5160140"
title: "Disable Remote Desktop Security Settings Through Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "4b81bcfa-fb0a-45e9-90c2-e3efe5160140"
  - "Disable Remote Desktop Security Settings Through Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Remote Desktop Security Settings Through Registry

A modification registry to disable RDP security settings. This technique was seen in DarkGate malware as part of its installation

## Metadata

- Atomic GUID: 4b81bcfa-fb0a-45e9-90c2-e3efe5160140
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: command_prompt

### Command

```commandprompt
reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\Terminal Services" /v "DisableSecuritySettings" /t REG_DWORD /d 1 /f
```

### Cleanup

```commandprompt
reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\Terminal Services" /v "DisableSecuritySettings" /t REG_DWORD /d 0 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
