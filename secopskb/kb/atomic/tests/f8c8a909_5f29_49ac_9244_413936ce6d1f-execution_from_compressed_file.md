---
atomic_guid: "f8c8a909-5f29-49ac-9244-413936ce6d1f"
title: "Execution from Compressed File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "f8c8a909-5f29-49ac-9244-413936ce6d1f"
  - "Execution from Compressed File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Execution from Compressed File

Mimic execution of compressed executable. When successfully executed, calculator.exe will open.

## Metadata

- Atomic GUID: f8c8a909-5f29-49ac-9244-413936ce6d1f
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Input Arguments

### url_path

- description: url to download Exe
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027/bin/T1027.zip

## Dependencies

T1027.exe must exist on disk at PathToAtomicsFolder\..\ExternalPayloads\temp_T1027.zip\T1027.exe

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\temp_T1027.zip\T1027.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "#{url_path}" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\T1027.zip"
Expand-Archive -path "PathToAtomicsFolder\..\ExternalPayloads\T1027.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\temp_T1027.zip\" -Force
```

## Executor

- name: command_prompt

### Command

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\temp_T1027.zip\T1027.exe"
```

### Cleanup

```cmd
taskkill /f /im calculator.exe >nul 2>nul
taskkill /f /im CalculatorApp.exe >nul 2>nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
