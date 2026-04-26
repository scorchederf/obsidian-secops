---
atomic_guid: "8707a805-2b76-4f32-b1c0-14e558205772"
title: "Mshta used to Execute PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.005"
attack_technique_name: "Signed Binary Proxy Execution: Mshta"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "8707a805-2b76-4f32-b1c0-14e558205772"
  - "Mshta used to Execute PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Mshta used to Execute PowerShell

Use Mshta to execute arbitrary PowerShell. Example is from the 2021 Threat Detection Report by Red Canary.

## Metadata

- Atomic GUID: 8707a805-2b76-4f32-b1c0-14e558205772
- Technique: T1218.005: Signed Binary Proxy Execution: Mshta
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1218.005/T1218.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Input Arguments

### message

- description: Encoded message to include
- type: string
- default: Hello,%20MSHTA!

### seconds_to_sleep

- description: How many seconds to sleep/wait
- type: integer
- default: 5

## Executor

- name: command_prompt

### Command

```commandprompt
mshta.exe "about:<hta:application><script language="VBScript">Close(Execute("CreateObject(""Wscript.Shell"").Run%20""powershell.exe%20-nop%20-Command%20Write-Host%20#{message};Start-Sleep%20-Seconds%20#{seconds_to_sleep}"""))</script>'"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml)
