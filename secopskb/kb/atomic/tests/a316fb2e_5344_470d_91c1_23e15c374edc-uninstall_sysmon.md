---
atomic_guid: "a316fb2e-5344-470d-91c1-23e15c374edc"
title: "Uninstall Sysmon"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "a316fb2e-5344-470d-91c1-23e15c374edc"
  - "Uninstall Sysmon"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uninstall Sysinternals Sysmon for Defense Evasion

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Input Arguments

### sysmon_exe

- description: The location of the Sysmon executable from Sysinternals (ignored if sysmon.exe is found in your PATH)
- type: path
- default: PathToAtomicsFolder\T1562.001\bin\sysmon.exe

## Dependencies

Sysmon executable must be available

### Prerequisite Check

```powershell
if(cmd /c where sysmon) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
$parentpath = Split-Path "#{sysmon_exe}"; $zippath = "$parentpath\Sysmon.zip"
New-Item -ItemType Directory $parentpath -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/Sysmon.zip" -OutFile "$zippath"
Expand-Archive $zippath $parentpath -Force; Remove-Item $zippath
if(-not ($Env:Path).contains($parentpath)){$Env:Path += ";$parentpath"}
```

Sysmon must be installed

### Prerequisite Check

```powershell
if(cmd /c sc query sysmon) { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
cmd /c sysmon -i -accepteula
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sysmon -u
```

### Cleanup

```cmd
sysmon -i -accepteula >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
