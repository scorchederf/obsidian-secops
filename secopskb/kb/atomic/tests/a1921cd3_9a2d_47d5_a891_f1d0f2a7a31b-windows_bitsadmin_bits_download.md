---
atomic_guid: "a1921cd3-9a2d-47d5-a891-f1d0f2a7a31b"
title: "Windows - BITSAdmin BITS Download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "a1921cd3-9a2d-47d5-a891-f1d0f2a7a31b"
  - "Windows - BITSAdmin BITS Download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test uses BITSAdmin.exe to schedule a BITS job for the download of a file.
This technique is used by Qbot malware to download payloads.

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### bits_job_name

- description: Name of the created BITS job
- type: string
- default: qcxjb7

### local_path

- description: Local path to place file
- type: path
- default: %temp%\Atomic-license.txt

### remote_file

- description: URL of file to copy
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Executor

- name: command_prompt

### Command

```cmd
C:\Windows\System32\bitsadmin.exe /transfer #{bits_job_name} /Priority HIGH #{remote_file} #{local_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
