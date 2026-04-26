---
atomic_guid: "e7e3a525-7612-4d68-a5d3-c4649181b8af"
title: "Invoke HTML Application - JScript Engine with Rundll32 and Inline Protocol Handler"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.005"
attack_technique_name: "Signed Binary Proxy Execution: Mshta"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "e7e3a525-7612-4d68-a5d3-c4649181b8af"
  - "Invoke HTML Application - JScript Engine with Rundll32 and Inline Protocol Handler"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke HTML Application - JScript Engine with Rundll32 and Inline Protocol Handler

Executes an HTA Application with JScript Engine, Rundll32 and Inline Protocol Handler.

## Metadata

- Atomic GUID: e7e3a525-7612-4d68-a5d3-c4649181b8af
- Technique: T1218.005: Signed Binary Proxy Execution: Mshta
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1218.005/T1218.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.005]]

## Input Arguments

### protocol_handler

- description: Protocol Handler to use
- type: string
- default: About

### rundll32_file_path

- description: Location of rundll32.exe
- type: path
- default: $env:windir\system32\rundll32.exe

### script_engine

- description: Script Engine to use
- type: string
- default: JScript

## Dependencies

The AtomicTestHarnesses module must be installed and Invoke-ATHHTMLApplication must be exported in the module.

### Prerequisite Check

```text
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Invoke-ATHHTMLApplication']) {exit 1} else {exit 0}
```

### Get Prerequisite

```text
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Invoke-ATHHTMLApplication -ScriptEngine #{script_engine} -InlineProtocolHandler #{protocol_handler} -UseRundll32 -Rundll32FilePath #{rundll32_file_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.005/T1218.005.yaml)
