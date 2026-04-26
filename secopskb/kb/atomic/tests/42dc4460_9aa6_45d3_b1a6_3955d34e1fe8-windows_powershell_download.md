---
atomic_guid: "42dc4460-9aa6-45d3-b1a6-3955d34e1fe8"
title: "Windows - PowerShell Download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "42dc4460-9aa6-45d3-b1a6-3955d34e1fe8"
  - "Windows - PowerShell Download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - PowerShell Download

This test uses PowerShell to download a payload.
This technique is used by multiple adversaries and malware families.

## Metadata

- Atomic GUID: 42dc4460-9aa6-45d3-b1a6-3955d34e1fe8
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### destination_path

- description: Destination path to file
- type: path
- default: $env:TEMP\Atomic-license.txt

### remote_file

- description: URL of file to copy
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Executor

- name: powershell

### Command

```powershell
(New-Object System.Net.WebClient).DownloadFile("#{remote_file}", "#{destination_path}")
```

### Cleanup

```powershell
Remove-Item #{destination_path} -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
