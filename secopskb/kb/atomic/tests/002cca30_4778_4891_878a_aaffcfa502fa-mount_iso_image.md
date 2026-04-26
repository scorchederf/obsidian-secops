---
atomic_guid: "002cca30-4778-4891-878a-aaffcfa502fa"
title: "Mount ISO image"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.005"
attack_technique_name: "Subvert Trust Controls: Mark-of-the-Web Bypass"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "002cca30-4778-4891-878a-aaffcfa502fa"
  - "Mount ISO image"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mount ISO image

Mounts ISO image downloaded from internet to evade Mark-of-the-Web. Upon successful execution, powershell will download the .iso from the Atomic Red Team repo, and mount the image. The provided sample ISO simply has a Reports shortcut file in it. Reference: https://www.microsoft.com/security/blog/2021/05/27/new-sophisticated-email-based-attack-from-nobelium/

## Metadata

- Atomic GUID: 002cca30-4778-4891-878a-aaffcfa502fa
- Technique: T1553.005: Subvert Trust Controls: Mark-of-the-Web Bypass
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1553.005/T1553.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.005]]

## Input Arguments

### path_of_iso

- description: Path to ISO file
- type: path
- default: PathToAtomicsFolder\T1553.005\bin\T1553.005.iso

## Dependencies

T1553.005.iso must exist on disk at specified location (#{path_of_iso})

### Prerequisite Check

```powershell
if (Test-Path "#{path_of_iso}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{path_of_iso}") -ErrorAction ignore | Out-Null
Invoke-WebRequest https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1553.005/bin/T1553.005.iso -OutFile "#{path_of_iso}"
```

## Executor

- name: powershell

### Command

```powershell
Mount-DiskImage -ImagePath "#{path_of_iso}"
```

### Cleanup

```powershell
Dismount-DiskImage -ImagePath "#{path_of_iso}" | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml)
