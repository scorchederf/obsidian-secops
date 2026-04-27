---
atomic_guid: "54782d65-12f0-47a5-b4c1-b70ee23de6df"
title: "Lolbas replace.exe use to copy file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "54782d65-12f0-47a5-b4c1-b70ee23de6df"
  - "Lolbas replace.exe use to copy file"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Lolbas replace.exe use to copy file

Copy file.cab to destination
Reference: https://lolbas-project.github.io/lolbas/Binaries/Replace/

## Metadata

- Atomic GUID: 54782d65-12f0-47a5-b4c1-b70ee23de6df
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### Path_replace

- description: Path to replace.exe
- type: path
- default: C:\Windows\System32\replace.exe

### replace_cab

- description: Path to the cab file
- type: path
- default: PathToAtomicsFolder\T1105\src\redcanary.cab

## Dependencies

#{replace_cab} must exist on system.

### Prerequisite Check

```powershell
if (Test-Path "#{replace_cab}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{replace_cab}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1105/src/redcanary.cab" -OutFile "#{replace_cab}"
```

## Executor

- name: command_prompt

### Command

```cmd
del %TEMP%\redcanary.cab >nul 2>&1
#{Path_replace} "#{replace_cab}" %TEMP% /A
```

### Cleanup

```cmd
del %TEMP%\redcanary.cab >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
