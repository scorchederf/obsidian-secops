---
atomic_guid: "00682c9f-7df4-4df8-950b-6dcaaa3ad9af"
title: "Command prompt writing script to file then executes it"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.003"
attack_technique_name: "Command and Scripting Interpreter: Windows Command Shell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "00682c9f-7df4-4df8-950b-6dcaaa3ad9af"
  - "Command prompt writing script to file then executes it"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Command prompt writing script to file then executes it

Simulate DarkGate malware's second stage by writing a VBscript to disk directly from the command prompt then executing it.
    The script will execute 'whoami' then exit.

## Metadata

- Atomic GUID: 00682c9f-7df4-4df8-950b-6dcaaa3ad9af
- Technique: T1059.003: Command and Scripting Interpreter: Windows Command Shell
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1059.003/T1059.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Input Arguments

### script_name

- description: Script name (without the extension)
- type: string
- default: AtomicTest

### script_path

- description: Path in which the script will be written.
- type: path
- default: %TEMP%\

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
 c:\windows\system32\cmd.exe /c cd /d #{script_path} & echo Set objShell = CreateObject("WScript.Shell"):Set objExec = objShell.Exec("whoami"):Set objExec = Nothing:Set objShell = Nothing > #{script_name}.vbs & #{script_name}.vbs
```

### Cleanup

```cmd
del "#{script_name}.vbs" >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml)
