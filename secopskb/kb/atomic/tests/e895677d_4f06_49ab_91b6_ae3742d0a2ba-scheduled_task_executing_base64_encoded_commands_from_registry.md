---
atomic_guid: "e895677d-4f06-49ab-91b6-ae3742d0a2ba"
title: "Scheduled Task Executing Base64 Encoded Commands From Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "e895677d-4f06-49ab-91b6-ae3742d0a2ba"
  - "Scheduled Task Executing Base64 Encoded Commands From Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Scheduled Task Executing Base64 Encoded Commands From Registry

A Base64 Encoded command will be stored in the registry (ping 127.0.0.1) and then a scheduled task will be created.
The scheduled task will launch powershell to decode and run the command in the registry daily.
This is a persistence mechanism recently seen in use by Qakbot.  

[Additiona Information](https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/)

## Metadata

- Atomic GUID: e895677d-4f06-49ab-91b6-ae3742d0a2ba
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Input Arguments

### time

- description: Daily scheduled task execution time
- type: string
- default: 07:45

## Executor

- name: command_prompt

### Command

```cmd
reg add HKCU\SOFTWARE\ATOMIC-T1053.005 /v test /t REG_SZ /d cGluZyAxMjcuMC4wLjE= /f
schtasks.exe /Create /F /TN "ATOMIC-T1053.005" /TR "cmd /c start /min \"\" powershell.exe -Command IEX([System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String((Get-ItemProperty -Path HKCU:\\SOFTWARE\\ATOMIC-T1053.005).test)))" /sc daily /st #{time}
```

### Cleanup

```cmd
schtasks /delete /tn "ATOMIC-T1053.005" /F >nul 2>&1
reg delete HKCU\SOFTWARE\ATOMIC-T1053.005 /F >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
