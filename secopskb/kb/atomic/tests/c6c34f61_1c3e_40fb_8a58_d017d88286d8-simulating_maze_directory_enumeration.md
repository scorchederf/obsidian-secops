---
atomic_guid: "c6c34f61-1c3e-40fb-8a58-d017d88286d8"
title: "Simulating MAZE Directory Enumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c6c34f61-1c3e-40fb-8a58-d017d88286d8"
  - "Simulating MAZE Directory Enumeration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Simulating MAZE Directory Enumeration

This test emulates MAZE ransomware's ability to enumerate directories using Powershell.
Upon successful execution, this test will output the directory enumeration results to a specified file, as well as display them in the active window.
See https://www.mandiant.com/resources/tactics-techniques-procedures-associated-with-maze-ransomware-incidents

## Metadata

- Atomic GUID: c6c34f61-1c3e-40fb-8a58-d017d88286d8
- Technique: T1083: File and Directory Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Input Arguments

### File_to_output

- description: File to output results to
- type: string
- default: $env:temp\T1083Test5.txt

## Executor

- name: powershell

### Command

```powershell
$folderarray = @("Desktop", "Downloads", "Documents", "AppData/Local", "AppData/Roaming")
Get-ChildItem -Path $env:homedrive -ErrorAction SilentlyContinue | Out-File -append #{File_to_output}
Get-ChildItem -Path $env:programfiles -erroraction silentlycontinue | Out-File -append #{File_to_output}
Get-ChildItem -Path "${env:ProgramFiles(x86)}" -erroraction silentlycontinue | Out-File -append #{File_to_output}
$UsersFolder = "$env:homedrive\Users\"
foreach ($directory in Get-ChildItem -Path $UsersFolder -ErrorAction SilentlyContinue)
{
foreach ($secondarydirectory in $folderarray)
 {Get-ChildItem -Path "$UsersFolder/$directory/$secondarydirectory" -ErrorAction SilentlyContinue | Out-File -append #{File_to_output}}
}
cat #{File_to_output}
```

### Cleanup

```powershell
remove-item #{File_to_output} -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
