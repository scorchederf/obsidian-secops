---
atomic_guid: "3244697d-5a3a-4dfc-941c-550f69f91a4d"
title: "Netsh Helper DLL Registration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.007"
attack_technique_name: "Event Triggered Execution: Netsh Helper DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.007/T1546.007.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "3244697d-5a3a-4dfc-941c-550f69f91a4d"
  - "Netsh Helper DLL Registration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

You can register a "helper dll" with Netsh as a persistance mechanism. The code in the dll is executed every time netsh.exe is called.
The NetshHelper.dll provided with the atomic will simply launch notepad when netsh.exe is run.

[Blog](https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html)
[Sample DLL code](https://github.com/outflanknl/NetshHelperBeacon)

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546007-netsh-helper-dll|T1546.007: Netsh Helper DLL]]

## Input Arguments

### helper_file

- description: Path to DLL
- type: path
- default: PathToAtomicsFolder\T1546.007\bin\NetshHelper.dll

## Dependencies

Helper DLL must exist on disk at specified location (#{helper_file})

### Prerequisite Check

```powershell
if (Test-Path "#{helper_file}") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{helper_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.007/bin/NetshHelper.dll" -OutFile "#{helper_file}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
netsh.exe add helper "#{helper_file}"
taskkill /im notepad.exe /t /f > NUL 2>&1
```

### Cleanup

```cmd
netsh.exe delete helper "#{helper_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.007/T1546.007.yaml)
