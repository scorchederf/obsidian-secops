---
atomic_guid: "5e46a58e-cbf6-45ef-a289-ed7754603df9"
title: "Rundll32 ieadvpack.dll Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.011"
attack_technique_name: "Signed Binary Proxy Execution: Rundll32"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "5e46a58e-cbf6-45ef-a289-ed7754603df9"
  - "Rundll32 ieadvpack.dll Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Rundll32 ieadvpack.dll Execution

Test execution of a command using rundll32.exe with ieadvpack.dll.
Upon execution calc.exe will be launched

Reference: https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Ieadvpack.yml

## Metadata

- Atomic GUID: 5e46a58e-cbf6-45ef-a289-ed7754603df9
- Technique: T1218.011: Signed Binary Proxy Execution: Rundll32
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.011/T1218.011.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Input Arguments

### inf_to_execute

- description: Local location of inf file
- type: string
- default: PathToAtomicsFolder\T1218.011\src\T1218.011.inf

## Dependencies

Inf file must exist on disk at specified location ("#{inf_to_execute}")

### Prerequisite Check

```powershell
if (Test-Path "#{inf_to_execute}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{inf_to_execute}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.011/src/T1218.011.inf" -OutFile "#{inf_to_execute}"
```

## Executor

- name: command_prompt

### Command

```cmd
rundll32.exe ieadvpack.dll,LaunchINFSection "#{inf_to_execute}",DefaultInstall_SingleUser,1,
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.011/T1218.011.yaml)
