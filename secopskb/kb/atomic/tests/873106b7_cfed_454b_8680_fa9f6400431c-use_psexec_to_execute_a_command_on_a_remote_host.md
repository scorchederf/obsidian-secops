---
atomic_guid: "873106b7-cfed-454b-8680-fa9f6400431c"
title: "Use PsExec to execute a command on a remote host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.002"
attack_technique_name: "System Services: Service Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "873106b7-cfed-454b-8680-fa9f6400431c"
  - "Use PsExec to execute a command on a remote host"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Use PsExec to execute a command on a remote host

Requires having Sysinternals installed, path to sysinternals is one of the input input_arguments
Will start a process on a remote host.

Upon successful execution, cmd will utilize psexec.exe to spawn calc.exe on a remote endpoint (default:localhost).

## Metadata

- Atomic GUID: 873106b7-cfed-454b-8680-fa9f6400431c
- Technique: T1569.002: System Services: Service Execution
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
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
- default: DOMAIN\Administrator

## Dependencies

PsExec tool from Sysinternals must exist in the ExternalPayloads directory

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" -Force
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" \\#{remote_host} -i -u #{user_name} -p #{password} -accepteula "C:\Windows\System32\calc.exe"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml)
