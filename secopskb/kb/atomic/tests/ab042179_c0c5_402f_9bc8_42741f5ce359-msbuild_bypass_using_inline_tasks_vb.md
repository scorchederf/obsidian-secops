---
atomic_guid: "ab042179-c0c5-402f-9bc8-42741f5ce359"
title: "MSBuild Bypass Using Inline Tasks (VB)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1127.001"
attack_technique_name: "Trusted Developer Utilities Proxy Execution: MSBuild"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127.001/T1127.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "ab042179-c0c5-402f-9bc8-42741f5ce359"
  - "MSBuild Bypass Using Inline Tasks (VB)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes the code in a project file using msbuild.exe. The default Visual Basic example file (vb.xml) will simply print "Hello from a Visual Basic inline task!" to the screen.

## ATT&CK Mapping

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution#^t1127001-msbuild|T1127.001: MSBuild]]

## Input Arguments

### filename

- description: Location of the project file
- type: path
- default: PathToAtomicsFolder\T1127.001\src\vb.xml

### msbuildname

- description: Default name of MSBuild
- type: path
- default: msbuild.exe

### msbuildpath

- description: Default location of MSBuild
- type: path
- default: C:\Windows\Microsoft.NET\Framework\v4.0.30319

## Dependencies

Project file must exist on disk at specified location (#{filename})

### Prerequisite Check

```powershell
if (Test-Path "#{filename}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{filename}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1127.001/src/vb.xml" -OutFile "#{filename}"
```

## Executor

- name: command_prompt

### Command

```cmd
#{msbuildpath}\#{msbuildname} "#{filename}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127.001/T1127.001.yaml)
