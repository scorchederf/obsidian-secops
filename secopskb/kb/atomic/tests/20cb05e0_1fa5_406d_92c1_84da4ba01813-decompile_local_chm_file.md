---
atomic_guid: "20cb05e0-1fa5-406d-92c1-84da4ba01813"
title: "Decompile Local CHM File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.001"
attack_technique_name: "Signed Binary Proxy Execution: Compiled HTML File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "20cb05e0-1fa5-406d-92c1-84da4ba01813"
  - "Decompile Local CHM File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Decompile Local CHM File

Uses hh.exe to decompile a local compiled HTML Help file.
Upon successful execution the chm file will decompile to disk.
Reference:https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/

## Metadata

- Atomic GUID: 20cb05e0-1fa5-406d-92c1-84da4ba01813
- Technique: T1218.001: Signed Binary Proxy Execution: Compiled HTML File
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1218.001/T1218.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]

## Input Arguments

### local_chm_file

- description: Local .chm payload
- type: path
- default: PathToAtomicsFolder\T1218.001\src\T1218.001.chm

## Dependencies

The payload must exist on disk at specified location (#{local_chm_file})

### Prerequisite Check

```text
if (Test-Path "#{local_chm_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{local_chm_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.001/src/T1218.001.chm" -OutFile "#{local_chm_file}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
hh.exe -decompile %temp% "#{local_chm_file}"
```

### Cleanup

```commandprompt
del %temp%\T1218.001.html >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.001/T1218.001.yaml)
