---
atomic_guid: "0330a5d2-a45a-4272-a9ee-e364411c4b18"
title: "Maldoc choice flags command execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "0330a5d2-a45a-4272-a9ee-e364411c4b18"
  - "Maldoc choice flags command execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Maldoc choice flags command execution

This Test uses a VBA macro to execute cmd with flags observed in recent maldoc and 2nd stage downloaders. Upon execution, CMD will be launched.
Execution is handled by [Invoke-MalDoc](https://github.com/redcanaryco/invoke-atomicredteam/blob/master/Public/Invoke-MalDoc.ps1) to load and execute VBA code into Excel or Word documents.

## Metadata

- Atomic GUID: 0330a5d2-a45a-4272-a9ee-e364411c4b18
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Input Arguments

### ms_product

- description: Maldoc application Word or Excel
- type: string
- default: Word

## Dependencies

Microsoft #{ms_product} must be installed

### Prerequisite Check

```text
try {
  New-Object -COMObject "#{ms_product}.Application" | Out-Null
  $process = "#{ms_product}"; if ( $process -eq "Word") {$process = "winword"}
  Stop-Process -Name $process
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```text
Write-Host "You will need to install Microsoft #{ms_product} manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
$macrocode = "  a = Shell(`"cmd.exe /c choice /C Y /N /D Y /T 3`", vbNormalFocus)"
Invoke-MalDoc -macroCode $macrocode -officeProduct "#{ms_product}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
