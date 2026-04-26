---
atomic_guid: "28104f8a-4ff1-4582-bcf6-699dce156608"
title: "Bypass UAC using SilentCleanup task"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "28104f8a-4ff1-4582-bcf6-699dce156608"
  - "Bypass UAC using SilentCleanup task"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC using SilentCleanup task

Bypass UAC using SilentCleanup task on Windows 8-10 using bat file from https://www.reddit.com/r/hacking/comments/ajtrws/bypassing_highest_uac_level_windows_810/

There is an auto-elevated task called SilentCleanup located in %windir%\system32\cleanmgr.exe This can be abused to elevate any file with Administrator privileges without prompting UAC (even highest level).

For example, we can set the windir registry kye to: "cmd /k REM "

And forcefully run SilentCleanup task:

schtasks /run /tn \Microsoft\Windows\DiskCleanup\SilentCleanup /I

REM will tell it to ignore everything after %windir% and treat it just as a NOTE. Therefore just executing cmd with admin privs.

## Metadata

- Atomic GUID: 28104f8a-4ff1-4582-bcf6-699dce156608
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### file_path

- description: Path to the bat file
- type: string
- default: PathToAtomicsFolder\T1548.002\src\T1548.002.bat

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
"#{file_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
