---
atomic_guid: "a5d8cdeb-be90-43a9-8b26-cc618deac1e0"
title: "Use RemCom to execute a command on a remote host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.002"
attack_technique_name: "System Services: Service Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "a5d8cdeb-be90-43a9-8b26-cc618deac1e0"
  - "Use RemCom to execute a command on a remote host"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Use RemCom to execute a command on a remote host

Requires having RemCom installed, path to RemCom is one of the input input_arguments
Will start a process on a remote host.
Upon successful execution, cmd will utilize RemCom.exe to spawn calc.exe on a remote endpoint (default:localhost).

## Metadata

- Atomic GUID: a5d8cdeb-be90-43a9-8b26-cc618deac1e0
- Technique: T1569.002: System Services: Service Execution
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1569.002/T1569.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Input Arguments

### password

- description: Password
- type: string
- default: P@ssw0rd1

### remote_host

- description: Remote hostname or IP address
- type: string
- default: localhost

### user_name

- description: Username
- type: string
- default: Administrator

## Dependencies

RemCom tool must exist on disk in the ExternalPayloads folder

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\remcom.exe") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/kavika13/RemCom/raw/master/bin/Release/RemCom.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\remcom.exe"
```

## Executor

- name: command_prompt

### Command

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\remcom.exe" \\#{remote_host} /user:#{user_name} /pwd:#{password} cmd.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml)
