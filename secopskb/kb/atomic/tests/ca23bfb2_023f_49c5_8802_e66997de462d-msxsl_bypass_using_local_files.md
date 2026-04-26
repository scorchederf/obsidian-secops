---
atomic_guid: "ca23bfb2-023f-49c5-8802-e66997de462d"
title: "MSXSL Bypass using local files"
framework: "atomic"
generated: "true"
attack_technique_id: "T1220"
attack_technique_name: "XSL Script Processing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "ca23bfb2-023f-49c5-8802-e66997de462d"
  - "MSXSL Bypass using local files"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MSXSL Bypass using local files

Executes the code specified within a XSL script tag during XSL transformation using a local payload. 
Requires download of MSXSL. No longer available from Microsoft.
(Available via Internet Archive https://web.archive.org/web/20200825011623/https://www.microsoft.com/en-us/download/details.aspx?id=21714 ) 
Open Calculator.exe when test successfully executed, while AV turned off.

## Metadata

- Atomic GUID: ca23bfb2-023f-49c5-8802-e66997de462d
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

- description: Location of the test XML file on the local filesystem.
- type: path
- default: PathToAtomicsFolder\T1220\src\msxslxmlfile.xml

### xslfile

- description: Location of the test XSL script file on the local filesystem.
- type: path
- default: PathToAtomicsFolder\T1220\src\msxslscript.xsl

## Dependencies

XML file must exist on disk at specified location (#{xmlfile})

### Prerequisite Check

```powershell
if (Test-Path "#{xmlfile}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{xmlfile}") -ErrorAction Ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1220/src/msxslxmlfile.xml" -OutFile "#{xmlfile}"
```

XSL file must exist on disk at specified location (#{xslfile})

### Prerequisite Check

```powershell
if (Test-Path "#{xslfile}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{xslfile}") -ErrorAction Ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1220/src/msxslscript.xsl" -OutFile "#{xslfile}"
```

msxsl.exe must exist on disk at specified location (#{msxsl_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{msxsl_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
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
del "#{msxsl_exe}" >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1220/T1220.yaml)
