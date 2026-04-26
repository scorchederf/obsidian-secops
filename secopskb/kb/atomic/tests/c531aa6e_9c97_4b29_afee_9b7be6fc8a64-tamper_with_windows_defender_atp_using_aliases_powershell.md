---
atomic_guid: "c531aa6e-9c97-4b29-afee-9b7be6fc8a64"
title: "Tamper with Windows Defender ATP using Aliases - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "c531aa6e-9c97-4b29-afee-9b7be6fc8a64"
  - "Tamper with Windows Defender ATP using Aliases - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper with Windows Defender ATP using Aliases - PowerShell

Attempting to disable scheduled scanning and other parts of Windows Defender ATP using set-MpPreference aliases. Upon execution Virus and Threat Protection will show as disabled
in Windows settings.

## Metadata

- Atomic GUID: c531aa6e-9c97-4b29-afee-9b7be6fc8a64
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
Set-MpPreference -drtm $True
Set-MpPreference -dbm $True
Set-MpPreference -dscrptsc $True
Set-MpPreference -dbaf $True
```

### Cleanup

```powershell
Set-MpPreference -drtm 0
Set-MpPreference -dbm 0
Set-MpPreference -dscrptsc 0
Set-MpPreference -dbaf 0
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
