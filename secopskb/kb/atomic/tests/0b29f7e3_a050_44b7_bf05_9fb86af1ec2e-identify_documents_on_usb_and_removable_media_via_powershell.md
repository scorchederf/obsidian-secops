---
atomic_guid: "0b29f7e3-a050-44b7-bf05-9fb86af1ec2e"
title: "Identify Documents on USB and Removable Media via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1025"
attack_technique_name: "Data from Removable Media"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1025/T1025.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "0b29f7e3-a050-44b7-bf05-9fb86af1ec2e"
  - "Identify Documents on USB and Removable Media via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Identify Documents on USB and Removable Media via PowerShell

This test simulates an attack where PowerShell is used to detect connected USB or other removable storage devices and gather a list of specific document files 
(e.g., .docx, .xls, .txt, .pdf). The command works by first identifying removable drives on the system and then recursively searching through each one for files 
matching the targeted extensions. If no removable drives are present, the script will return a message stating that no media is detected. This behavior mimics 
how adversaries might scan for sensitive documents on removable devices for exfiltration or analysis.

## Metadata

- Atomic GUID: 0b29f7e3-a050-44b7-bf05-9fb86af1ec2e
- Technique: T1025: Data from Removable Media
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1025/T1025.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1025-data_from_removable_media|T1025]]

## Executor

- name: command_prompt

### Command

```commandprompt
powershell.exe -c "Get-Volume | Where-Object {$_.DriveType -eq 'Removable'} | ForEach-Object { Get-ChildItem -Path ($_.DriveLetter + ':\*') -Recurse -Include '*.doc*','*.xls*','*.txt','*.pdf' -ErrorAction SilentlyContinue | ForEach-Object {Write-Output $_.FullName} } ; if (-not (Get-Volume | Where-Object {$_.DriveType -eq 'Removable'})) { Write-Output 'No removable media.' }"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1025/T1025.yaml)
