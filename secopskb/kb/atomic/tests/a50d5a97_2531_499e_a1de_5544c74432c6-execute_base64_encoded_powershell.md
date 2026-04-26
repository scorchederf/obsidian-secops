---
atomic_guid: "a50d5a97-2531-499e-a1de-5544c74432c6"
title: "Execute base64-encoded PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a50d5a97-2531-499e-a1de-5544c74432c6"
  - "Execute base64-encoded PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute base64-encoded PowerShell

Creates base64-encoded PowerShell code and executes it. This is used by numerous adversaries and malicious tools.

Upon successful execution, powershell will execute an encoded command and stdout default is "Write-Host "Hey, Atomic!"

## Metadata

- Atomic GUID: a50d5a97-2531-499e-a1de-5544c74432c6
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Input Arguments

### powershell_command

- description: PowerShell command to encode
- type: string
- default: Write-Host "Hey, Atomic!"

## Executor

- name: powershell

### Command

```powershell
$OriginalCommand = '#{powershell_command}'
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($OriginalCommand)
$EncodedCommand =[Convert]::ToBase64String($Bytes)
$EncodedCommand
powershell.exe -EncodedCommand $EncodedCommand
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
