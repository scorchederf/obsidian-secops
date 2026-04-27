---
atomic_guid: "6657864e-0323-4206-9344-ac9cd7265a4f"
title: "Create a new user in a command prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "6657864e-0323-4206-9344-ac9cd7265a4f"
  - "Create a new user in a command prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a new user in a command prompt. Upon execution, "The command completed successfully." will be displayed. To verify the
new account, run "net user" in powershell or CMD and observe that there is a new user named "T1136.001_CMD"

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account#^t1136001-local-account|T1136.001: Local Account]]

## Input Arguments

### password

- description: Password of the user to create
- type: string
- default: T1136.001_CMD!

### username

- description: Username of the user to create
- type: string
- default: T1136.001_CMD

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
net user /add "#{username}" "#{password}"
```

### Cleanup

```cmd
net user /del "#{username}" >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
