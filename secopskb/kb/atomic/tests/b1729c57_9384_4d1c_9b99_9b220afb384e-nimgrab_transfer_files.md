---
atomic_guid: "b1729c57-9384-4d1c-9b99-9b220afb384e"
title: "Nimgrab - Transfer Files"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "b1729c57-9384-4d1c-9b99-9b220afb384e"
  - "Nimgrab - Transfer Files"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Nimgrab - Transfer Files

Use nimgrab.exe to download a file from the web.

## Metadata

- Atomic GUID: b1729c57-9384-4d1c-9b99-9b220afb384e
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### destination_path

- description: Destination path to file
- type: path
- default: $env:TEMP\Atomic-license.txt

### remote_file

- description: URL of file to copy
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Dependencies

NimGrab must be installed on system.

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\nimgrab.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://nim-lang.org/download/nim-1.6.6_x64.zip" -Outfile "PathToAtomicsFolder\..\ExternalPayloads\nim.zip"
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\nim.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\nim" -Force
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\nim\nim-1.6.6\bin\nimgrab.exe" "PathToAtomicsFolder\..\ExternalPayloads\nimgrab.exe"
```

## Executor

- name: command_prompt

### Command

```cmd
cmd /c "PathToAtomicsFolder\..\ExternalPayloads\nimgrab.exe" #{remote_file} #{destination_path}
```

### Cleanup

```cmd
del #{destination_path} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
