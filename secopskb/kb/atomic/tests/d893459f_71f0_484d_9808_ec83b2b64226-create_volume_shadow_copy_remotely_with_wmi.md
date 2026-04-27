---
atomic_guid: "d893459f-71f0-484d-9808-ec83b2b64226"
title: "Create Volume Shadow Copy remotely with WMI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "d893459f-71f0-484d-9808-ec83b2b64226"
  - "Create Volume Shadow Copy remotely with WMI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create Volume Shadow Copy remotely with WMI

This test is intended to be run from a remote workstation with domain admin context.
The Active Directory database NTDS.dit may be dumped by copying it from a Volume Shadow Copy.

## Metadata

- Atomic GUID: d893459f-71f0-484d-9808-ec83b2b64226
- Technique: T1003.003: OS Credential Dumping: NTDS
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1003.003/T1003.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Input Arguments

### drive_letter

- description: Drive letter to source VSC (including colon and backslash)
- type: string
- default: C:\

### target_host

- description: IP Address / Hostname you want to target
- type: string
- default: localhost

## Dependencies

Target must be a reachable Domain Controller, and current context must be domain admin

### Prerequisite Check

```untitled
wmic /node:"#{target_host}" shadowcopy list brief
```

### Get Prerequisite

```untitled
echo Sorry, can't connect to target host, check: network, firewall or permissions (must be admin on target)
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
wmic /node:"#{target_host}" shadowcopy call create Volume=#{drive_letter}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
