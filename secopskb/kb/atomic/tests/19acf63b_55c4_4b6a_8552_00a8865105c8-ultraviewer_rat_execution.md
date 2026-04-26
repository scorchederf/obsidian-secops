---
atomic_guid: "19acf63b-55c4-4b6a-8552-00a8865105c8"
title: "UltraViewer - RAT Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "19acf63b-55c4-4b6a-8552-00a8865105c8"
  - "UltraViewer - RAT Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UltraViewer - RAT Execution

A recent trend by threat actors, once a foothold is established, maintain long term persistence using third party remote services such as UltraViewer to provide the operator with access to the network using legitimate services.

## Metadata

- Atomic GUID: 19acf63b-55c4-4b6a-8552-00a8865105c8
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Input Arguments

### UltraViewer_Path

- description: Path to the UltraViewer executable.
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1219_UltraViewer.exe

## Dependencies

Ultraviewer installer must be downloaded and exist on the disk at the specified location. (#{UltraViewer_Path})

### Prerequisite Check

```text
if (Test-Path "#{UltraViewer_Path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
(New-Object Net.WebClient).DownloadFile("https://www.ultraviewer.net/en/UltraViewer_setup_6.5_en.exe","#{UltraViewer_Path}")
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process -Wait -FilePath "#{UltraViewer_Path}" -Argument "/silent" -PassThru
Start-Process 'C:\Program Files (x86)\UltraViewer\UltraViewer_Desktop.exe'
```

### Cleanup

```powershell
Stop-Process -Name "UltraViewer_Desktop" -Force -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
