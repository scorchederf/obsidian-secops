---
atomic_guid: "d1334303-59cb-4a03-8313-b3e24d02c198"
title: "Compress Data and lock with password for Exfiltration with 7zip"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "d1334303-59cb-4a03-8313-b3e24d02c198"
  - "Compress Data and lock with password for Exfiltration with 7zip"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Note: This test requires 7zip installation

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]

## Input Arguments

### 7zip_exe

- description: Path to installed 7zip executable
- type: path
- default: %ProgramFiles%\7-zip\7z.exe

### 7zip_installer

- description: 7zip installer
- type: path
- default: %TEMP%\7zip.exe

## Dependencies

7zip tool must be installed at specified location (#{7zip_exe})

### Prerequisite Check

```untitled
if not exist "#{7zip_exe}" (exit /b 1)
```

### Get Prerequisite

```untitled
echo Downloading 7-zip installer
bitsadmin /transfer myDownloadJob /download /priority normal "https://www.7-zip.org/a/7z2301-x64.exe" #{7zip_installer}
#{7zip_installer} /S
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
mkdir $PathToAtomicsFolder\T1560.001\victim-files
cd $PathToAtomicsFolder\T1560.001\victim-files
echo "This file will be encrypted" > .\encrypted_file.txt
"#{7zip_exe}" u archive.7z *txt -pblue
dir
```

### Cleanup

```cmd
rmdir /s /Q $PathToAtomicsFolder\T1560.001\victim-files >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
