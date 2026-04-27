---
atomic_guid: "54ad7d5a-a1b5-472c-b6c4-f8090fb2daef"
title: "InfDefaultInstall.exe .inf Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Test execution of a .inf using InfDefaultInstall.exe

Reference: https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Infdefaultinstall.yml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Input Arguments

### inf_to_execute

- description: Local location of inf file
- type: string
- default: PathToAtomicsFolder\T1218\src\Infdefaultinstall.inf

## Dependencies

INF file must exist on disk at specified location (#{inf_to_execute})

### Prerequisite Check

```powershell
if (Test-Path "#{inf_to_execute}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{inf_to_execute}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218/src/Infdefaultinstall.inf" -OutFile "#{inf_to_execute}"
```

## Executor

- name: command_prompt

### Command

```cmd
InfDefaultInstall.exe "#{inf_to_execute}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
