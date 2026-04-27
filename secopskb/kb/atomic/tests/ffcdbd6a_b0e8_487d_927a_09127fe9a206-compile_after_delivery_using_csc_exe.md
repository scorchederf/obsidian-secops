---
atomic_guid: "ffcdbd6a-b0e8-487d-927a-09127fe9a206"
title: "Compile After Delivery using csc.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.004"
attack_technique_name: "Obfuscated Files or Information: Compile After Delivery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "ffcdbd6a-b0e8-487d-927a-09127fe9a206"
  - "Compile After Delivery using csc.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Compile After Delivery using csc.exe

Compile C# code using csc.exe binary used by .NET
Upon execution an exe named T1027.004.exe will be placed in the temp folder

## Metadata

- Atomic GUID: ffcdbd6a-b0e8-487d-927a-09127fe9a206
- Technique: T1027.004: Obfuscated Files or Information: Compile After Delivery
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1027.004/T1027.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.004]]

## Input Arguments

### input_file

- description: C# code that launches calc.exe from a hidden cmd.exe Window
- type: path
- default: PathToAtomicsFolder\T1027.004\src\calc.cs

### output_file

- description: Output compiled binary
- type: path
- default: C:\Windows\Temp\T1027.004.exe

## Dependencies

C# file must exist on disk at specified location (#{input_file})

### Prerequisite Check

```powershell
if (Test-Path "#{input_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{input_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027.004/src/calc.cs" -OutFile "#{input_file}"
```

## Executor

- name: command_prompt

### Command

```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /out:#{output_file} "#{input_file}"
```

### Cleanup

```cmd
del #{output_file} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml)
