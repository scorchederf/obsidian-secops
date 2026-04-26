---
atomic_guid: "fad04df1-5229-4185-b016-fb6010cd87ac"
title: "Execution from Compressed JScript File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027"
attack_technique_name: "Obfuscated Files or Information"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "fad04df1-5229-4185-b016-fb6010cd87ac"
  - "Execution from Compressed JScript File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execution from Compressed JScript File

Mimic execution of compressed JavaScript file. When successfully executed, calculator.exe will open. This test is meant to help emulate Gootloader as per https://redcanary.com/blog/gootloader/

## Metadata

- Atomic GUID: fad04df1-5229-4185-b016-fb6010cd87ac
- Technique: T1027: Obfuscated Files or Information
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1027/T1027.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Input Arguments

### url_path

- description: url to download JScript file
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1027/bin/t1027js.zip

## Dependencies

T1027.js must exist on disk at PathToAtomicsFolder\..\ExternalPayloads\temp_T1027js.zip\T1027js.js

### Prerequisite Check

```text
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\temp_T1027js.zip\T1027js.js") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest "#{url_path}" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\T1027js.zip"
Expand-Archive -path "PathToAtomicsFolder\..\ExternalPayloads\T1027js.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\temp_T1027js.zip\" -Force
```

## Executor

- name: command_prompt

### Command

```commandprompt
"PathToAtomicsFolder\..\ExternalPayloads\temp_T1027js.zip\T1027js.js"
```

### Cleanup

```commandprompt
taskkill /f /im calculator.exe >nul 2>nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027/T1027.yaml)
