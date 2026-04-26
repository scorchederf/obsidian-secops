---
atomic_guid: "275d963d-3f36-476c-8bef-a2a3960ee6eb"
title: "SyncAppvPublishingServer Signed Script PowerShell Command Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1216"
attack_technique_name: "Signed Script Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1216/T1216.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "275d963d-3f36-476c-8bef-a2a3960ee6eb"
  - "SyncAppvPublishingServer Signed Script PowerShell Command Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SyncAppvPublishingServer Signed Script PowerShell Command Execution

Executes the signed SyncAppvPublishingServer script with options to execute an arbitrary PowerShell command.
Upon execution, calc.exe will be launched.

## Metadata

- Atomic GUID: 275d963d-3f36-476c-8bef-a2a3960ee6eb
- Technique: T1216: Signed Script Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1216/T1216.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Input Arguments

### command_to_execute

- description: A PowerShell command to execute.
- type: string
- default: Start-Process calc

## Executor

- name: command_prompt

### Command

```commandprompt
C:\windows\system32\SyncAppvPublishingServer.vbs "\n;#{command_to_execute}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1216/T1216.yaml)
