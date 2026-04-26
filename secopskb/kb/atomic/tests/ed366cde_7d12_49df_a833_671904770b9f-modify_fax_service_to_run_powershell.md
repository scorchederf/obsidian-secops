---
atomic_guid: "ed366cde-7d12-49df-a833-671904770b9f"
title: "Modify Fax service to run PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.003"
attack_technique_name: "Create or Modify System Process: Windows Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "ed366cde-7d12-49df-a833-671904770b9f"
  - "Modify Fax service to run PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Modify Fax service to run PowerShell

This test will temporarily modify the service Fax by changing the binPath to PowerShell
and will then revert the binPath change, restoring Fax to its original state.
Upon successful execution, cmd will modify the binpath for `Fax` to spawn powershell. Powershell will then spawn.

## Metadata

- Atomic GUID: ed366cde-7d12-49df-a833-671904770b9f
- Technique: T1543.003: Create or Modify System Process: Windows Service
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1543.003/T1543.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Input Arguments

### service_binpath

- description: The default value for the binary path of the service
- type: string
- default: C:\WINDOWS\system32\fxssvc.exe

### service_name

- description: The name of the service that will be modified
- type: string
- default: Fax

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc config #{service_name} binPath= "C:\windows\system32\WindowsPowerShell\v1.0\powershell.exe -noexit -c \"write-host 'T1543.003 Test'\""
sc start #{service_name}
```

### Cleanup

```cmd
sc config #{service_name} binPath= "#{service_binpath}" >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml)
