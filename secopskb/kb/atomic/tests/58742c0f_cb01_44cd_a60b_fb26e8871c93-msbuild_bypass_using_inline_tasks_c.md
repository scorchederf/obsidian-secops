---
atomic_guid: "58742c0f-cb01-44cd-a60b-fb26e8871c93"
title: "MSBuild Bypass Using Inline Tasks (C#)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1127.001"
attack_technique_name: "Trusted Developer Utilities Proxy Execution: MSBuild"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127.001/T1127.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "58742c0f-cb01-44cd-a60b-fb26e8871c93"
  - "MSBuild Bypass Using Inline Tasks (C#)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MSBuild Bypass Using Inline Tasks (C#)

Executes the code in a project file using msbuild.exe. The default C# project example file (T1127.001.csproj) will simply print "Hello From a Code Fragment" and "Hello From a Class." to the screen.

## Metadata

- Atomic GUID: 58742c0f-cb01-44cd-a60b-fb26e8871c93
- Technique: T1127.001: Trusted Developer Utilities Proxy Execution: MSBuild
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1127.001/T1127.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127.001]]

## Input Arguments

### filename

- description: Location of the project file
- type: path
- default: PathToAtomicsFolder\T1127.001\src\T1127.001.csproj

### msbuildname

- description: Default name of MSBuild
- type: path
- default: msbuild.exe

### msbuildpath

- description: Default location of MSBuild
- type: path
- default: C:\Windows\Microsoft.NET\Framework\v4.0.30319

## Dependencies

Project file must exist on disk at specified location (#{filename})

### Prerequisite Check

```powershell
if (Test-Path "#{filename}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{filename}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1127.001/src/T1127.001.csproj" -OutFile "#{filename}"
```

## Executor

- name: command_prompt

### Command

```cmd
#{msbuildpath}\#{msbuildname} "#{filename}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127.001/T1127.001.yaml)
