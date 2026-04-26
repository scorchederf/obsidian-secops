---
atomic_guid: "49845fc1-7961-4590-a0f0-3dbcf065ae7e"
title: "Printer Migration Command-Line Tool UNC share folder into a zip file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "49845fc1-7961-4590-a0f0-3dbcf065ae7e"
  - "Printer Migration Command-Line Tool UNC share folder into a zip file"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Printer Migration Command-Line Tool UNC share folder into a zip file

Create a ZIP file from a folder in a remote drive

## Metadata

- Atomic GUID: 49845fc1-7961-4590-a0f0-3dbcf065ae7e
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### Path_PrintBrm

- description: Path to PrintBrm.exe
- type: path
- default: C:\Windows\System32\spool\tools\PrintBrm.exe

### Path_unc

- description: Path to the UNC folder
- type: path
- default: \\127.0.0.1\c$\AtomicRedTeam\atomics\T1105\src\

## Executor

- name: command_prompt

### Command

```cmd
del %TEMP%\PrintBrm.zip >nul 2>&1 
#{Path_PrintBrm} -b -d #{Path_unc}  -f %TEMP%\PrintBrm.zip -O FORCE
```

### Cleanup

```cmd
del %TEMP%\PrintBrm.zip >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
