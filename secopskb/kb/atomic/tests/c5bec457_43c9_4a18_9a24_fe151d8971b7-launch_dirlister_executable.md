---
atomic_guid: "c5bec457-43c9-4a18-9a24-fe151d8971b7"
title: "Launch DirLister Executable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c5bec457-43c9-4a18-9a24-fe151d8971b7"
  - "Launch DirLister Executable"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Launch DirLister Executable

Launches the DirLister executable for a short period of time and then exits.

Recently seen used by [BlackCat ransomware](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/) to create a list of accessible directories and files.

## Metadata

- Atomic GUID: c5bec457-43c9-4a18-9a24-fe151d8971b7
- Technique: T1083: File and Directory Discovery
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Input Arguments

### dirlister_path

- description: Path to the DirLister executable 
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\DirLister.exe

## Dependencies

DirLister.exe must exist in the specified path #{dirlister_path}

### Prerequisite Check

```powershell
if (Test-Path "#{dirlister_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
$parentpath = Split-Path "#{dirlister_path}"
New-Item -ItemType Directory -Force -Path $parentpath | Out-Null
Invoke-WebRequest https://github.com/SanderSade/DirLister/releases/download/v2.beta4/DirLister.v2.beta4.zip -OutFile "PathToAtomicsFolder\..\ExternalPayloads\TDirLister.v2.beta4.zip"
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\TDirLister.v2.beta4.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\TDirLister.v2.beta4" -Force
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\TDirLister.v2.beta4\*" "$parentpath" -Recurse
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\TDirLister.v2.beta4.zip","PathToAtomicsFolder\..\ExternalPayloads\TDirLister.v2.beta4" -Recurse -ErrorAction Ignore
```

## Executor

- name: powershell

### Command

```powershell
Start-Process "#{dirlister_path}"
Start-Sleep -Second 4
Stop-Process -Name "DirLister"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
