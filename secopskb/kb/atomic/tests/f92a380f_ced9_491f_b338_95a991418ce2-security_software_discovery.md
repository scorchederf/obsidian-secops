---
atomic_guid: "f92a380f-ced9-491f-b338-95a991418ce2"
title: "Security Software Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "f92a380f-ced9-491f-b338-95a991418ce2"
  - "Security Software Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Security Software Discovery

Methods to identify Security Software on an endpoint

when sucessfully executed, the test is going to display running processes, firewall configuration on network profiles
and specific security software.

## Metadata

- Atomic GUID: f92a380f-ced9-491f-b338-95a991418ce2
- Technique: T1518.001: Software Discovery: Security Software Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1518.001/T1518.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Executor

- name: command_prompt

### Command

```commandprompt
netsh.exe advfirewall  show allprofiles 
netsh.exe advfirewall firewall dump
netsh.exe advfirewall show currentprofile
netsh.exe advfirewall firewall show rule name=all
netsh.exe firewall show state
netsh.exe firewall show config
sc query windefend
powershell.exe /c "Get-Process | Where-Object { $_.ProcessName -eq 'Sysmon' }"
powershell.exe /c "Get-Service | where-object {$_.DisplayName -like '*sysm*'}"
powershell.exe /c "Get-CimInstance Win32_Service -Filter 'Description = ''System Monitor service'''"
tasklist.exe
tasklist.exe | findstr /i virus
tasklist.exe | findstr /i cb
tasklist.exe | findstr /i defender
tasklist.exe | findstr /i cylance
tasklist.exe | findstr /i mc
tasklist.exe | findstr /i "virus cb defender cylance mc"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
