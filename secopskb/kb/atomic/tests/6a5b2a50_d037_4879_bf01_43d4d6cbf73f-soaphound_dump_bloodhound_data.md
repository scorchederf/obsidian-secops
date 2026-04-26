---
atomic_guid: "6a5b2a50-d037-4879-bf01-43d4d6cbf73f"
title: "SOAPHound - Dump BloodHound Data"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "6a5b2a50-d037-4879-bf01-43d4d6cbf73f"
  - "SOAPHound - Dump BloodHound Data"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SOAPHound - Dump BloodHound Data

Dump BloodHound data using SOAPHound. Upon execution, BloodHound data will be dumped and stored in the specified output directory.
src: https://github.com/FalconForceTeam/SOAPHound

## Metadata

- Atomic GUID: 6a5b2a50-d037-4879-bf01-43d4d6cbf73f
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Input Arguments

### cachefilename

- description: Cache filename
- type: string
- default: c:\temp\cache.txt

### dc

- description: Domain Controller IP
- type: string
- default: 10.0.1.14

### domain

- description: Domain for authentication
- type: string
- default: $env:USERDOMAIN

### outputdirectory

- description: Output directory
- type: string
- default: c:\temp\test2

### password

- description: Password for authentication
- type: string
- default: P@ssword1

### soaphound_path

- description: Path to SOAPHound binary
- type: string
- default: PathToAtomicsFolder\T1059.001\bin\SOAPHound.exe

### user

- description: Username for authentication
- type: string
- default: $env:USERNAME

## Executor

- name: powershell

### Command

```powershell
#{soaphound_path} --user #{user} --password #{password} --domain #{domain} --dc #{dc} --bhdump --cachefilename #{cachefilename} --outputdirectory #{outputdirectory}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
