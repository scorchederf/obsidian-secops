---
atomic_guid: "ba38e193-37a6-4c41-b214-61b33277fe36"
title: "System Owner/User Discovery Using Command Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1033"
attack_technique_name: "System Owner/User Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "ba38e193-37a6-4c41-b214-61b33277fe36"
  - "System Owner/User Discovery Using Command Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Identify the system owner or current user using native Windows command prompt utilities.

## ATT&CK Mapping

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]

## Input Arguments

### output_file_path

- description: Location of output file.
- type: string
- default: $env:temp

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
set file=#{output_file_path}\user_info_%random%.tmp
echo Username: %USERNAME% > %file%
echo User Domain: %USERDOMAIN% >> %file%
net users >> %file%
query user >> %file%
```

### Cleanup

```cmd
del #{output_file_path}\\user_info_*.tmp
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1033/T1033.yaml)
