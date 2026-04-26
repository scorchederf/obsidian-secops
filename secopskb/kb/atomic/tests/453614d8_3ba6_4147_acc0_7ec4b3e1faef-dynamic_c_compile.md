---
atomic_guid: "453614d8-3ba6-4147-acc0-7ec4b3e1faef"
title: "Dynamic C# Compile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.004"
attack_technique_name: "Obfuscated Files or Information: Compile After Delivery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "453614d8-3ba6-4147-acc0-7ec4b3e1faef"
  - "Dynamic C# Compile"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dynamic C# Compile

When C# is compiled dynamically, a .cmdline file will be created as a part of the process. 
Certain processes are not typically observed compiling C# code, but can do so without touching disk. This can be used to unpack a payload for execution.
The exe file that will be executed is named as T1027.004_DynamicCompile.exe is contained in the 'bin' folder of this atomic, and the source code to the file is in the 'src' folder.
Upon execution, the exe will print 'T1027.004 Dynamic Compile'.

## Metadata

- Atomic GUID: 453614d8-3ba6-4147-acc0-7ec4b3e1faef
- Technique: T1027.004: Obfuscated Files or Information: Compile After Delivery
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1027.004/T1027.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.004]]

## Input Arguments

### input_file

- description: exe program containing dynamically compiled C# code
- type: path
- default: PathToAtomicsFolder\T1027.004\bin\T1027.004_DynamicCompile.exe

## Dependencies

exe file must exist on disk at specified location (#{input_file})

### Prerequisite Check

```text
if (Test-Path "#{input_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Invoke-WebRequest https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027.004/bin/T1027.004_DynamicCompile.exe -OutFile "#{input_file}"
```

## Executor

- name: powershell

### Command

```powershell
Invoke-Expression "#{input_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.004/T1027.004.yaml)
