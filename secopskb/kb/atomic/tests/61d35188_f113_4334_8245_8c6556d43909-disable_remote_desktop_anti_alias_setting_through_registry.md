---
atomic_guid: "61d35188-f113-4334-8245-8c6556d43909"
title: "Disable Remote Desktop Anti-Alias Setting Through Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "61d35188-f113-4334-8245-8c6556d43909"
  - "Disable Remote Desktop Anti-Alias Setting Through Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Remote Desktop Anti-Alias Setting Through Registry

A modification registry to disable RDP anti-alias settings. This technique was seen in DarkGate malware as part of its installation

## Metadata

- Atomic GUID: 61d35188-f113-4334-8245-8c6556d43909
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
reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\Terminal Services" /v "DisableRemoteDesktopAntiAlias" /t REG_DWORD /d 1 /f
```

### Cleanup

```commandprompt
reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\Terminal Services" /v "DisableRemoteDesktopAntiAlias" /t REG_DWORD /d 0 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
