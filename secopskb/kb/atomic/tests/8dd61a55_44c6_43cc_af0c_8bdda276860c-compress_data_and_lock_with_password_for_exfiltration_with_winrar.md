---
atomic_guid: "8dd61a55-44c6-43cc-af0c-8bdda276860c"
title: "Compress Data and lock with password for Exfiltration with winrar"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "8dd61a55-44c6-43cc-af0c-8bdda276860c"
  - "Compress Data and lock with password for Exfiltration with winrar"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Compress Data and lock with password for Exfiltration with winrar

Note: Requires winrar installation
rar a -p"blue" hello.rar (VARIANT)

## Metadata

- Atomic GUID: 8dd61a55-44c6-43cc-af0c-8bdda276860c
- Technique: T1560.001: Archive Collected Data: Archive via Utility
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1560.001/T1560.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Input Arguments

### rar_exe

- description: The RAR executable from Winrar
- type: path
- default: %programfiles%/WinRAR/Rar.exe

### rar_installer

- description: Winrar installer
- type: path
- default: %TEMP%\winrar.exe

## Dependencies

Rar tool must be installed at specified location (#{rar_exe})

### Prerequisite Check

```text
if not exist "#{rar_exe}" (exit /b 1)
```

### Get Prerequisite

```text
echo Downloading Winrar installer
bitsadmin /transfer myDownloadJob /download /priority normal "https://www.win-rar.com/fileadmin/winrar-versions/winrar/th/winrar-x64-580.exe" #{rar_installer}
#{rar_installer} /S
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
mkdir .\tmp\victim-files
cd .\tmp\victim-files
echo "This file will be encrypted" > .\encrypted_file.txt
"#{rar_exe}" a -hp"blue" hello.rar
dir
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
