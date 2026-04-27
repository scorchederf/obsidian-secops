---
atomic_guid: "8dd61a55-44c6-43cc-af0c-8bdda276860c"
title: "Compress Data and lock with password for Exfiltration with winrar"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-27 19:12:28"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Note: Requires winrar installation
rar a -p"blue" hello.rar (VARIANT)

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

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

```untitled
if not exist "#{rar_exe}" (exit /b 1)
```

### Get Prerequisite

```untitled
echo Downloading Winrar installer
bitsadmin /transfer myDownloadJob /download /priority normal "https://www.win-rar.com/fileadmin/winrar-versions/winrar/th/winrar-x64-580.exe" #{rar_installer}
#{rar_installer} /S
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
mkdir .\tmp\victim-files
cd .\tmp\victim-files
echo "This file will be encrypted" > .\encrypted_file.txt
"#{rar_exe}" a -hp"blue" hello.rar
dir
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
