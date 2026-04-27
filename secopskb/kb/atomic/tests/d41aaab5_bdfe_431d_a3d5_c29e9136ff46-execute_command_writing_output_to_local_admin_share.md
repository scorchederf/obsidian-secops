---
atomic_guid: "d41aaab5-bdfe-431d-a3d5-c29e9136ff46"
title: "Execute command writing output to local Admin Share"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.002"
attack_technique_name: "Remote Services: SMB/Windows Admin Shares"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "d41aaab5-bdfe-431d-a3d5-c29e9136ff46"
  - "Execute command writing output to local Admin Share"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Execute command writing output to local Admin Share

Executes a command, writing the output to a local Admin Share.
This technique is used by post-exploitation frameworks.

## Metadata

- Atomic GUID: d41aaab5-bdfe-431d-a3d5-c29e9136ff46
- Technique: T1021.002: Remote Services: SMB/Windows Admin Shares
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1021.002/T1021.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Input Arguments

### command_to_execute

- description: Command to execute for output.
- type: string
- default: hostname

### output_file

- description: Remote computer to receive the copy and execute the file
- type: string
- default: output.txt

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
cmd.exe /Q /c #{command_to_execute} 1> \\127.0.0.1\ADMIN$\#{output_file} 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.002/T1021.002.yaml)
