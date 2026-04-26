---
atomic_guid: "54ad7d5a-a1b5-472c-b6c4-f8090fb2daef"
title: "InfDefaultInstall.exe .inf Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "54ad7d5a-a1b5-472c-b6c4-f8090fb2daef"
  - "InfDefaultInstall.exe .inf Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# InfDefaultInstall.exe .inf Execution

Test execution of a .inf using InfDefaultInstall.exe

Reference: https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Infdefaultinstall.yml

## Metadata

- Atomic GUID: 54ad7d5a-a1b5-472c-b6c4-f8090fb2daef
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Input Arguments

### inf_to_execute

- description: Local location of inf file
- type: string
- default: PathToAtomicsFolder\T1218\src\Infdefaultinstall.inf

## Dependencies

INF file must exist on disk at specified location (#{inf_to_execute})

### Prerequisite Check

```text
if (Test-Path "#{inf_to_execute}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{inf_to_execute}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218/src/Infdefaultinstall.inf" -OutFile "#{inf_to_execute}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
InfDefaultInstall.exe "#{inf_to_execute}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
