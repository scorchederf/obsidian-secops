---
atomic_guid: "6683baf0-6e77-4f58-b114-814184ea8150"
title: "Obfuscated PowerShell Command via Character Array"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "6683baf0-6e77-4f58-b114-814184ea8150"
  - "Obfuscated PowerShell Command via Character Array"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Obfuscated PowerShell Command via Character Array

Spawns a child PowerShell process using character array obfuscation. 
Both the PowerShell binary name and executed command are constructed 
from ASCII values at runtime to evade string-based detection.

## Metadata

- Atomic GUID: 6683baf0-6e77-4f58-b114-814184ea8150
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Executor

- name: powershell

### Command

```powershell
$ps = [char[]](112,111,119,101,114,115,104,101,108,108)
$cmd = [char[]](83,116,97,114,116,45,80,114,111,99,101,115,115,32,99,97,108,99,46,101,120,101)
& (-join $ps) "-Command" (-join $cmd)
```

### Cleanup

```powershell
taskkill /f /im calculator.exe >nul 2>nul
taskkill /f /im CalculatorApp.exe >nul 2>nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
