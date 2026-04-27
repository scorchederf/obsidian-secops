---
atomic_guid: "8d73c7b0-c2b1-4ac1-881a-4aa644f76064"
title: "Msiexec.exe - Execute Local MSI file with embedded VBScript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.007"
attack_technique_name: "Signed Binary Proxy Execution: Msiexec"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "8d73c7b0-c2b1-4ac1-881a-4aa644f76064"
  - "Msiexec.exe - Execute Local MSI file with embedded VBScript"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Msiexec.exe - Execute Local MSI file with embedded VBScript

Executes an MSI containing embedded VBScript code using msiexec.exe

## Metadata

- Atomic GUID: 8d73c7b0-c2b1-4ac1-881a-4aa644f76064
- Technique: T1218.007: Signed Binary Proxy Execution: Msiexec
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.007/T1218.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Input Arguments

### action

- description: Specifies the MSI action to perform: i (install), a (admin), j (advertise). The included MSI is designed to support all three action types.

- type: string
- default: i

### msi_exe

- description: MSIExec File Path
- type: path
- default: c:\windows\system32\msiexec.exe

### msi_payload

- description: MSI file to execute
- type: path
- default: PathToAtomicsFolder\T1218.007\bin\T1218.007_VBScript.msi

## Dependencies

The MSI file must exist on disk at specified location (#{msi_payload})

### Prerequisite Check

```powershell
if (Test-Path "#{msi_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{msi_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.007/bin/T1218.007_VBScript.msi" -OutFile "#{msi_payload}"
```

## Executor

- name: command_prompt

### Command

```cmd
#{msi_exe} /q /#{action} "#{msi_payload}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml)
