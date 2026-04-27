---
atomic_guid: "35727d9e-7a7f-4d0c-a259-dc3906d6e8b9"
title: "Mimic Ransomware - Allow Multiple RDP Sessions per User"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "35727d9e-7a7f-4d0c-a259-dc3906d6e8b9"
  - "Mimic Ransomware - Allow Multiple RDP Sessions per User"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mimic Ransomware - Allow Multiple RDP Sessions per User

This test emulates Mimic ransomware's ability to enable multiple RDP sessions per user by modifying the fSingleSessionPerUser value within the Terminal Server registry key. 
See [Mimic Ransomware Overview] (https://www.trendmicro.com/en_us/research/23/a/new-mimic-ransomware-abuses-everything-apis-for-its-encryption-p.html)

## Metadata

- Atomic GUID: 35727d9e-7a7f-4d0c-a259-dc3906d6e8b9
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
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fSingleSessionPerUser /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg delete "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fSingleSessionPerUser /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
