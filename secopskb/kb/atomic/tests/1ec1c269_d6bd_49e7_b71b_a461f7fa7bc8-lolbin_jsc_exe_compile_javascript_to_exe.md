---
atomic_guid: "1ec1c269-d6bd-49e7-b71b-a461f7fa7bc8"
title: "Lolbin Jsc.exe compile javascript to exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1127"
attack_technique_name: "Trusted Developer Utilities Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127/T1127.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "1ec1c269-d6bd-49e7-b71b-a461f7fa7bc8"
  - "Lolbin Jsc.exe compile javascript to exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Lolbin Jsc.exe compile javascript to exe

Use jsc.exe to compile javascript code stored in scriptfile.js and output scriptfile.exe.
https://lolbas-project.github.io/lolbas/Binaries/Jsc/
https://www.phpied.com/make-your-javascript-a-windows-exe/

## Metadata

- Atomic GUID: 1ec1c269-d6bd-49e7-b71b-a461f7fa7bc8
- Technique: T1127: Trusted Developer Utilities Proxy Execution
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1127/T1127.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Input Arguments

### filename

- description: Location of the project file
- type: path
- default: PathToAtomicsFolder\T1127\src\hello.js

### jscname

- description: Default name of jsc
- type: path
- default: jsc.exe

### jscpath

- description: Default location of jsc.exe
- type: path
- default: C:\Windows\Microsoft.NET\Framework\v4.0.30319

## Dependencies

JavaScript code file must exist on disk at specified location (#{filename})

### Prerequisite Check

```powershell
if (Test-Path "#{filename}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{filename}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1127/src/hello.js" -OutFile "#{filename}"
```

## Executor

- name: command_prompt

### Command

```cmd
copy "#{filename}" %TEMP%\hello.js
#{jscpath}\#{jscname} %TEMP%\hello.js
```

### Cleanup

```cmd
del %TEMP%\hello.js
del %TEMP%\hello.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127/T1127.yaml)
