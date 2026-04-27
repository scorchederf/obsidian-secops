---
atomic_guid: "4c4959bf-addf-4b4a-be86-8d09cc1857aa"
title: "System Owner/User Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1033"
attack_technique_name: "System Owner/User Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "4c4959bf-addf-4b4a-be86-8d09cc1857aa"
  - "System Owner/User Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# System Owner/User Discovery

Identify System owner or users on an endpoint.

Upon successful execution, cmd.exe will spawn multiple commands against a target host to identify usernames. Output will be via stdout. 
Additionally, two files will be written to disk - computers.txt and usernames.txt.

## Metadata

- Atomic GUID: 4c4959bf-addf-4b4a-be86-8d09cc1857aa
- Technique: T1033: System Owner/User Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1033/T1033.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Input Arguments

### computer_name

- description: Name of remote computer
- type: string
- default: localhost

## Executor

- name: command_prompt

### Command

```cmd
cmd.exe /C whoami
wmic useraccount get /ALL
quser /SERVER:"#{computer_name}"
quser
qwinsta.exe /server:#{computer_name}
qwinsta.exe
for /F "tokens=1,2" %i in ('qwinsta /server:#{computer_name} ^| findstr "Active Disc"') do @echo %i | find /v "#" | find /v "console" || echo %j > computers.txt
@FOR /F %n in (computers.txt) DO @FOR /F "tokens=1,2" %i in ('qwinsta /server:%n ^| findstr "Active Disc"') do @echo %i | find /v "#" | find /v "console" || echo %j > usernames.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml)
