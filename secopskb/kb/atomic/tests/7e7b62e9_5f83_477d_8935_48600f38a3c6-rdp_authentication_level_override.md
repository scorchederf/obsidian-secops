---
atomic_guid: "7e7b62e9-5f83-477d-8935-48600f38a3c6"
title: "RDP Authentication Level Override"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "7e7b62e9-5f83-477d-8935-48600f38a3c6"
  - "RDP Authentication Level Override"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RDP Authentication Level Override

A modification registry to override RDP Authentication Level. This technique was seen in DarkGate malware as part of its installation.

## Metadata

- Atomic GUID: 7e7b62e9-5f83-477d-8935-48600f38a3c6
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
reg add "HKCU\Software\Microsoft\Terminal Server Client" /v AuthenticationLevelOverride /t REG_DWORD /d 0 /f
```

### Cleanup

```commandprompt
reg delete "HKCU\Software\Microsoft\Terminal Server Client" /v AuthenticationLevelOverride
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
