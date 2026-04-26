---
atomic_guid: "02ea31cb-3b4c-4a2d-9bf1-e4e70ebcf5d0"
title: "Compress Data for Exfiltration With Rar"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "02ea31cb-3b4c-4a2d-9bf1-e4e70ebcf5d0"
  - "Compress Data for Exfiltration With Rar"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Compress Data for Exfiltration With Rar

An adversary may compress data (e.g., sensitive documents) that is collected prior to exfiltration.
When the test completes you should find the txt files from the %USERPROFILE% directory compressed in a file called T1560.001-data.rar in the %USERPROFILE% directory

## Metadata

- Atomic GUID: 02ea31cb-3b4c-4a2d-9bf1-e4e70ebcf5d0
- Technique: T1560.001: Archive Collected Data: Archive via Utility
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1560.001/T1560.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Input Arguments

### file_extension

- description: Extension of files to compress
- type: string
- default: .txt

### input_path

- description: Path that should be compressed into our output file
- type: path
- default: %USERPROFILE%

### output_file

- description: Path where resulting compressed data should be placed
- type: path
- default: %USERPROFILE%\T1560.001-data.rar

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
"#{rar_exe}" a -r #{output_file} #{input_path}\*#{file_extension}
```

### Cleanup

```cmd
del /f /q /s #{output_file} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
