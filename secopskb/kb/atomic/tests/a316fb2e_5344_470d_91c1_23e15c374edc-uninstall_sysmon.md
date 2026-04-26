---
atomic_guid: "a316fb2e-5344-470d-91c1-23e15c374edc"
title: "Uninstall Sysmon"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Uninstall Sysmon

Uninstall Sysinternals Sysmon for Defense Evasion

## Metadata

- Atomic GUID: a316fb2e-5344-470d-91c1-23e15c374edc
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### sysmon_exe

- description: The location of the Sysmon executable from Sysinternals (ignored if sysmon.exe is found in your PATH)
- type: path
- default: PathToAtomicsFolder\T1562.001\bin\sysmon.exe

## Dependencies

Sysmon executable must be available

### Prerequisite Check

```text
if(cmd /c where sysmon) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
$parentpath = Split-Path "#{sysmon_exe}"; $zippath = "$parentpath\Sysmon.zip"
New-Item -ItemType Directory $parentpath -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/Sysmon.zip" -OutFile "$zippath"
Expand-Archive $zippath $parentpath -Force; Remove-Item $zippath
if(-not ($Env:Path).contains($parentpath)){$Env:Path += ";$parentpath"}
```

Sysmon must be installed

### Prerequisite Check

```text
if(cmd /c sc query sysmon) { exit 0} else { exit 1}
```

### Get Prerequisite

```text
cmd /c sysmon -i -accepteula
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
sysmon -u
```

### Cleanup

```commandprompt
sysmon -i -accepteula >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
