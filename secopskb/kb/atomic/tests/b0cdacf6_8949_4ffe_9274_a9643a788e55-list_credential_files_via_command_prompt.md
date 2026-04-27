---
atomic_guid: "b0cdacf6-8949-4ffe-9274-a9643a788e55"
title: "List Credential Files via Command Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.001"
attack_technique_name: "Unsecured Credentials: Credentials In Files"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "b0cdacf6-8949-4ffe-9274-a9643a788e55"
  - "List Credential Files via Command Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Via Command Prompt,list files where credentials are stored in Windows Credential Manager

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
dir /a:h C:\Users\%USERNAME%\AppData\Local\Microsoft\Credentials\
dir /a:h C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Credentials\
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.001/T1552.001.yaml)
