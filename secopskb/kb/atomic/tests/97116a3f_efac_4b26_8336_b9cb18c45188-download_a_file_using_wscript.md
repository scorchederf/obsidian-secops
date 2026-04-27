---
atomic_guid: "97116a3f-efac-4b26-8336-b9cb18c45188"
title: "Download a file using wscript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "97116a3f-efac-4b26-8336-b9cb18c45188"
  - "Download a file using wscript"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Download a file using wscript

Use wscript to run a local VisualBasic file to download a remote file

## Metadata

- Atomic GUID: 97116a3f-efac-4b26-8336-b9cb18c45188
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### vbscript_file

- description: Full path to the VisualBasic downloading the file
- type: string
- default: PathToAtomicsFolder\T1105\src\T1105-download-file.vbs

## Dependencies

#{vbscript_file} must be exist on system.

### Prerequisite Check

```powershell
if (Test-Path "#{vbscript_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{vbscript_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1105/src/T1105-download-file.vbs" -OutFile "#{vbscript_file}"
```

## Executor

- name: command_prompt

### Command

```cmd
wscript.exe "#{vbscript_file}"
```

### Cleanup

```cmd
del Atomic-License.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
