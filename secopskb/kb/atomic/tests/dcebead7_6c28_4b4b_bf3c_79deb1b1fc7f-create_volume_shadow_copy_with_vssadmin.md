---
atomic_guid: "dcebead7-6c28-4b4b-bf3c-79deb1b1fc7f"
title: "Create Volume Shadow Copy with vssadmin"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "dcebead7-6c28-4b4b-bf3c-79deb1b1fc7f"
  - "Create Volume Shadow Copy with vssadmin"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create Volume Shadow Copy with vssadmin

This test is intended to be run on a domain Controller.

The Active Directory database NTDS.dit may be dumped by copying it from a Volume Shadow Copy.

## Metadata

- Atomic GUID: dcebead7-6c28-4b4b-bf3c-79deb1b1fc7f
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

## Dependencies

Target must be a Domain Controller

### Prerequisite Check

```text
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ProductOptions  /v ProductType | findstr LanmanNT
```

### Get Prerequisite

```text
echo Sorry, Promoting this machine to a Domain Controller must be done manually
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
vssadmin.exe create shadow /for=#{drive_letter}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
