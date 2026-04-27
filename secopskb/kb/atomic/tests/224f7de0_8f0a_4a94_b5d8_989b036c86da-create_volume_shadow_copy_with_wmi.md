---
atomic_guid: "224f7de0-8f0a-4a94-b5d8-989b036c86da"
title: "Create Volume Shadow Copy with WMI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "224f7de0-8f0a-4a94-b5d8-989b036c86da"
  - "Create Volume Shadow Copy with WMI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test is intended to be run on a domain Controller.

The Active Directory database NTDS.dit may be dumped by copying it from a Volume Shadow Copy.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

## Input Arguments

### drive_letter

- description: Drive letter to source VSC (including colon and backslash)
- type: string
- default: C:\

## Dependencies

Target must be a Domain Controller

### Prerequisite Check

```untitled
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ProductOptions  /v ProductType | findstr LanmanNT
```

### Get Prerequisite

```untitled
echo Sorry, Promoting this machine to a Domain Controller must be done manually
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
wmic shadowcopy call create Volume=#{drive_letter}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
