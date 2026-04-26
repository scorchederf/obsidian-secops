---
atomic_guid: "f63b8bc4-07e5-4112-acba-56f646f3f0bc"
title: "Bitsadmin Download (PowerShell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1197"
attack_technique_name: "BITS Jobs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "f63b8bc4-07e5-4112-acba-56f646f3f0bc"
  - "Bitsadmin Download (PowerShell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bitsadmin Download (PowerShell)

This test simulates an adversary leveraging bitsadmin.exe to download
and execute a payload leveraging PowerShell

Upon execution you will find a github markdown file downloaded to the Temp directory

## Metadata

- Atomic GUID: f63b8bc4-07e5-4112-acba-56f646f3f0bc
- Technique: T1197: BITS Jobs
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1197/T1197.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Input Arguments

### local_file

- description: Local file path to save downloaded file
- type: path
- default: $env:TEMP\bitsadmin2_flag.ps1

### remote_file

- description: Remote file to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1197/T1197.md

## Executor

- name: powershell

### Command

```powershell
Start-BitsTransfer -Priority foreground -Source #{remote_file} -Destination #{local_file}
```

### Cleanup

```powershell
Remove-Item #{local_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml)
