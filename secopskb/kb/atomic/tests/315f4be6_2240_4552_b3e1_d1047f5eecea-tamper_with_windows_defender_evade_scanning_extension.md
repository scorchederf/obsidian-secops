---
atomic_guid: "315f4be6-2240-4552-b3e1-d1047f5eecea"
title: "Tamper with Windows Defender Evade Scanning -Extension"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "315f4be6-2240-4552-b3e1-d1047f5eecea"
  - "Tamper with Windows Defender Evade Scanning -Extension"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Tamper with Windows Defender Evade Scanning -Extension

Malware can exclude specific extensions from being scanned and evading detection. 
Upon successful execution, the extension(s) should be on the list of excluded extensions.
To check the exclusion list using poweshell  (Get-MpPreference).ExclusionExtension.

## Metadata

- Atomic GUID: 315f4be6-2240-4552-b3e1-d1047f5eecea
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### excluded_exts

- description: A list of extension to exclude from scanning
- type: string
- default: .exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$excludedExts= "#{excluded_exts}"
Add-MpPreference -ExclusionExtension  $excludedExts
```

### Cleanup

```powershell
$excludedExts= "#{excluded_exts}"
Remove-MpPreference -ExclusionExtension  $excludedExts -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
