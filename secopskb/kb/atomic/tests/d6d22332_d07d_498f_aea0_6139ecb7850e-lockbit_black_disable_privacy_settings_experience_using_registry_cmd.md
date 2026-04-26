---
atomic_guid: "d6d22332-d07d-498f-aea0-6139ecb7850e"
title: "LockBit Black - Disable Privacy Settings Experience Using Registry -cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "d6d22332-d07d-498f-aea0-6139ecb7850e"
  - "LockBit Black - Disable Privacy Settings Experience Using Registry -cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LockBit Black - Disable Privacy Settings Experience Using Registry -cmd

LockBit Black - Disable Privacy Settings Experience Using Registry

## Metadata

- Atomic GUID: d6d22332-d07d-498f-aea0-6139ecb7850e
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add "HKCU\Software\Policies\Microsoft\Windows\OOBE" /v DisablePrivacyExperience /t REG_DWORD /d 1 /f
```

### Cleanup

```commandprompt
reg delete "HKCU\Software\Policies\Microsoft\Windows\OOBE" /v DisablePrivacyExperience /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
