---
atomic_guid: "64b12afc-18b8-4d3f-9eab-7f6cae7c73f9"
title: "Remove the Zone.Identifier alternate data stream"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.005"
attack_technique_name: "Subvert Trust Controls: Mark-of-the-Web Bypass"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "64b12afc-18b8-4d3f-9eab-7f6cae7c73f9"
  - "Remove the Zone.Identifier alternate data stream"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remove the Zone.Identifier alternate data stream

Remove the Zone.Identifier alternate data stream which identifies the file as downloaded from the internet.
Removing this allows more freedom in executing scripts in PowerShell and avoids opening files in protected view.

## Metadata

- Atomic GUID: 64b12afc-18b8-4d3f-9eab-7f6cae7c73f9
- Technique: T1553.005: Subvert Trust Controls: Mark-of-the-Web Bypass
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1553.005/T1553.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.005]]

## Input Arguments

### file_path

- description: File to have the Zone.Identifier removed.
- type: string
- default: $env:tmp\ReadMe.md

### file_to_download

- description: File that will be downloaded to test against.
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/README.md

## Dependencies

A test file with the Zone.Identifier attribute must be present.

### Prerequisite Check

```powershell
if (Test-Path #{file_path}) { EXIT 0 } else { EXIT 1 }
```

### Get Prerequisite

```powershell
Invoke-WebRequest #{file_to_download} -OutFile #{file_path}
Set-Content -Path #{file_path} -Stream Zone.Identifier -Value '[ZoneTransfer]','ZoneId=3'
```

## Executor

- name: powershell

### Command

```powershell
Unblock-File -Path #{file_path}
```

### Cleanup

```powershell
Set-Content -Path #{file_path} -Stream Zone.Identifier -Value '[ZoneTransfer]','ZoneId=3'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.005/T1553.005.yaml)
