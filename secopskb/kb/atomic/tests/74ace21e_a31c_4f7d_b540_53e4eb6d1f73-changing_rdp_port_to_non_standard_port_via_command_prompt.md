---
atomic_guid: "74ace21e-a31c-4f7d-b540-53e4eb6d1f73"
title: "Changing RDP Port to Non Standard Port via Command_Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.001"
attack_technique_name: "Remote Services: Remote Desktop Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "74ace21e-a31c-4f7d-b540-53e4eb6d1f73"
  - "Changing RDP Port to Non Standard Port via Command_Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Changing RDP Port to Non Standard Port via Command_Prompt

Changing RDP Port to Non Standard Port via Command_Prompt

## Metadata

- Atomic GUID: 74ace21e-a31c-4f7d-b540-53e4eb6d1f73
- Technique: T1021.001: Remote Services: Remote Desktop Protocol
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1021.001/T1021.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Input Arguments

### NEW_Remote_Port

- description: New RDP Listening Port
- type: string
- default: 4489

### OLD_Remote_Port

- description: Default RDP Listening Port
- type: string
- default: 3389

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t REG_DWORD /d #{NEW_Remote_Port} /f
netsh advfirewall firewall add rule name="RDPPORTLatest-TCP-In" dir=in action=allow protocol=TCP localport=#{NEW_Remote_Port}
```

### Cleanup

```cmd
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t REG_DWORD /d #{OLD_Remote_Port} /f >nul 2>&1
netsh advfirewall firewall delete rule name="RDPPORTLatest-TCP-In" >nul 2>&1
net stop TermService /y >nul 2>&1
net start TermService >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.001/T1021.001.yaml)
