---
atomic_guid: "c59f246a-34f8-4e4d-9276-c295ef9ba0dd"
title: "Register Portable Virtualbox"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.006"
attack_technique_name: "Run Virtual Instance"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.006/T1564.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "c59f246a-34f8-4e4d-9276-c295ef9ba0dd"
  - "Register Portable Virtualbox"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

ransomware payloads via virtual machines (VM). 
[Maze ransomware](https://threatpost.com/maze-ransomware-ragnar-locker-virtual-machine/159350/)

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564006-run-virtual-instance|T1564.006: Run Virtual Instance]]

## Input Arguments

### cab_file_path

- description: Path to the CAB file
- type: path
- default: PathToAtomicsFolder\T1564.006\bin\common.cab

### msi_file_path

- description: Path to the MSI file
- type: path
- default: PathToAtomicsFolder\T1564.006\bin\Virtualbox_52.msi

## Dependencies

MSI file must exist on disk at specified location (#{msi_file_path})

### Prerequisite Check

```powershell
if (Test-Path "#{msi_file_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{msi_file_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1564.006/bin/Virtualbox_52.msi" -OutFile "#{msi_file_path}"
```

CAB file must exist on disk at specified location (#{cab_file_path})

### Prerequisite Check

```powershell
if (Test-Path "#{cab_file_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{cab_file_path}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1564.006/bin/common.cab" -OutFile "#{cab_file_path}"
```

Old version of Virtualbox must be installed

### Prerequisite Check

```powershell
if (Test-Path "C:\Program Files\Oracle\VirtualBox\VboxC.dll") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
msiexec /i "#{msi_file_path}" /qn
```

## Executor

- name: command_prompt

### Command

```cmd
"C:\Program Files\Oracle\VirtualBox\VBoxSVC.exe" /reregserver
regsvr32 /S "C:\Program Files\Oracle\VirtualBox\VboxC.dll"
rundll32 "C:\Program Files\Oracle\VirtualBox\VBoxRT.dll,RTR3Init"
sc create VBoxDRV binpath= "C:\Program Files\Oracle\VirtualBox\drivers\VboxDrv.sys" type= kernel start= auto error= normal displayname= PortableVBoxDRV
sc start VBoxDRV
```

### Cleanup

```cmd
sc stop VBoxDRV
sc delete VBoxDRV
regsvr32 /u /S "C:\Program Files\Oracle\VirtualBox\VboxC.dll"
msiexec /x "#{msi_file_path}" /qn
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.006/T1564.006.yaml)
