---
atomic_guid: "01d1c6c0-faf0-408e-b368-752a02285cb2"
title: "Disable NLA for RDP via Command Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.001"
attack_technique_name: "Remote Services: Remote Desktop Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "01d1c6c0-faf0-408e-b368-752a02285cb2"
  - "Disable NLA for RDP via Command Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables network-level authentication (NLA) for RDP by changing a registry key via Command Prompt
Disabling NLA for RDP can allow remote user interaction with the Windows sign-in screen prior to authentication. According to Microsoft, Flax Typhoon actors used this technique implementation to achieve persistence on victim systems: https://www.microsoft.com/en-us/security/blog/2023/08/24/flax-typhoon-using-legitimate-software-to-quietly-access-taiwanese-organizations/
See also: https://github.com/EmpireProject/Empire/blob/master/lib/modules/powershell/management/enable_rdp.py

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Input Arguments

### Default_UserAuthentication

- description: Default UserAuthentication registry value
- type: string
- default: 1

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /d 0 /t REG_DWORD /f
```

### Cleanup

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /d #{Default_UserAuthentication} /t REG_DWORD -f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml)
