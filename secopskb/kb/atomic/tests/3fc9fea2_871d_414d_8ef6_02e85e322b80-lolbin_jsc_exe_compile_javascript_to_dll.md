---
atomic_guid: "3fc9fea2-871d-414d-8ef6-02e85e322b80"
title: "Lolbin Jsc.exe compile javascript to dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1127"
attack_technique_name: "Trusted Developer Utilities Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127/T1127.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "3fc9fea2-871d-414d-8ef6-02e85e322b80"
  - "Lolbin Jsc.exe compile javascript to dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Lolbin Jsc.exe compile javascript to dll

Use jsc.exe to compile javascript code stored in Library.js and output Library.dll.
https://lolbas-project.github.io/lolbas/Binaries/Jsc/
https://www.phpied.com/make-your-javascript-a-windows-exe/

## Metadata

- Atomic GUID: 3fc9fea2-871d-414d-8ef6-02e85e322b80
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
- default: PathToAtomicsFolder\T1127\src\LibHello.js

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

```text
if (Test-Path "#{filename}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "#{filename}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1127/src/LibHello.js" -OutFile "#{filename}"
```

## Executor

- name: command_prompt

### Command

```commandprompt
copy "#{filename}" %TEMP%\LibHello.js
#{jscpath}\#{jscname} /t:library %TEMP%\LibHello.js
```

### Cleanup

```commandprompt
del %TEMP%\LibHello.js
del %TEMP%\LibHello.dll
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127/T1127.yaml)
