---
atomic_guid: "a9b93f17-31cb-435d-a462-5e838a2a6026"
title: "AutoIt Script Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059"
attack_technique_name: "Command and Scripting Interpreter"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059/T1059.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "a9b93f17-31cb-435d-a462-5e838a2a6026"
  - "AutoIt Script Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AutoIt Script Execution

An adversary may attempt to execute suspicious or malicious script using AutoIt software instead of regular terminal like powershell or cmd. Calculator will popup when the script is executed successfully.

## Metadata

- Atomic GUID: a9b93f17-31cb-435d-a462-5e838a2a6026
- Technique: T1059: Command and Scripting Interpreter
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1059/T1059.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Input Arguments

### autoit_path

- description: AutoIt Executable File Path
- type: path
- default: C:\Program Files (x86)\AutoIt3\AutoIt3.exe

### script_path

- description: AutoIt Script Path
- type: path
- default: PathToAtomicsFolder\T1059\src\calc.au3

## Dependencies

AutoIt executable file must exist on disk at the specified location (#{autoit_path})

### Prerequisite Check

```text
if(Test-Path "#{autoit_path}") {
    exit 0
} else {
    exit 1
}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
$AutoItURL = "https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.exe"
$InstallerPath = "$PathToAtomicsFolder\..\ExternalPayloads\autoit-v3-setup.exe"
Invoke-WebRequest -Uri $AutoItURL -OutFile $InstallerPath
Start-Process -FilePath $InstallerPath -ArgumentList "/S" -Wait
```

## Executor

- name: powershell

### Command

```powershell
Start-Process -FilePath "#{autoit_path}" -ArgumentList "#{script_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059/T1059.yaml)
