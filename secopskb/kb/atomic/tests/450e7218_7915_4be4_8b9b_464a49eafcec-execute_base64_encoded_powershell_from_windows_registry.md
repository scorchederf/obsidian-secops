---
atomic_guid: "450e7218-7915-4be4-8b9b-464a49eafcec"
title: "Execute base64-encoded PowerShell from Windows Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "450e7218-7915-4be4-8b9b-464a49eafcec"
  - "Execute base64-encoded PowerShell from Windows Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute base64-encoded PowerShell from Windows Registry

Stores base64-encoded PowerShell code in the Windows Registry and deobfuscates it for execution. This is used by numerous adversaries and malicious tools.

Upon successful execution, powershell will execute encoded command and read/write from the registry.

## Metadata

- Atomic GUID: 450e7218-7915-4be4-8b9b-464a49eafcec
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

### registry_entry_storage

- description: Windows Registry entry to store code under key
- type: string
- default: Debug

### registry_key_storage

- description: Windows Registry Key to store code
- type: string
- default: HKCU:Software\Microsoft\Windows\CurrentVersion

## Executor

- name: powershell

### Command

```powershell
$OriginalCommand = '#{powershell_command}'
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($OriginalCommand)
$EncodedCommand =[Convert]::ToBase64String($Bytes)
$EncodedCommand

Set-ItemProperty -Force -Path #{registry_key_storage} -Name #{registry_entry_storage} -Value $EncodedCommand
powershell.exe -Command "IEX ([Text.Encoding]::UNICODE.GetString([Convert]::FromBase64String((gp #{registry_key_storage} #{registry_entry_storage}).#{registry_entry_storage})))"
```

### Cleanup

```powershell
Remove-ItemProperty -Force -ErrorAction Ignore -Path #{registry_key_storage} -Name #{registry_entry_storage}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
