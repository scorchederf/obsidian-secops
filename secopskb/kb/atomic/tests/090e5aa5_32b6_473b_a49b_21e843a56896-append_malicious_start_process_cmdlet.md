---
atomic_guid: "090e5aa5-32b6-473b-a49b-21e843a56896"
title: "Append malicious start-process cmdlet"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.013"
attack_technique_name: "Event Triggered Execution: PowerShell Profile"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.013/T1546.013.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "090e5aa5-32b6-473b-a49b-21e843a56896"
  - "Append malicious start-process cmdlet"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Append malicious start-process cmdlet

Appends a start process cmdlet to the current user's powershell profile pofile that points to a malicious executable. Upon execution, calc.exe will be launched.

## Metadata

- Atomic GUID: 090e5aa5-32b6-473b-a49b-21e843a56896
- Technique: T1546.013: Event Triggered Execution: PowerShell Profile
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1546.013/T1546.013.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.013]]

## Input Arguments

### exe_path

- description: Path the malicious executable
- type: path
- default: calc.exe

### ps_profile

- description: Powershell profile to use
- type: string
- default: $profile

## Dependencies

Ensure a powershell profile exists for the current user

### Prerequisite Check

```text
if (Test-Path #{ps_profile}) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Path #{ps_profile} -Type File -Force
```

## Executor

- name: powershell

### Command

```powershell
Add-Content #{ps_profile} -Value ""
Add-Content #{ps_profile} -Value "Start-Process #{exe_path}"
powershell -Command exit
```

### Cleanup

```powershell
$oldprofile = cat $profile | Select-Object -skiplast 1
Set-Content $profile -Value $oldprofile
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.013/T1546.013.yaml)
