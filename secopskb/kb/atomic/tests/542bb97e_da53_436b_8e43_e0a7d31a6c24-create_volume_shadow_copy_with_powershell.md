---
atomic_guid: "542bb97e-da53-436b-8e43-e0a7d31a6c24"
title: "Create Volume Shadow Copy with Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "542bb97e-da53-436b-8e43-e0a7d31a6c24"
  - "Create Volume Shadow Copy with Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create Volume Shadow Copy with Powershell

This test is intended to be run on a domain Controller.

The Active Directory database NTDS.dit may be dumped by copying it from a Volume Shadow Copy.

## Metadata

- Atomic GUID: 542bb97e-da53-436b-8e43-e0a7d31a6c24
- Technique: T1003.003: OS Credential Dumping: NTDS
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003.003/T1003.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Input Arguments

### drive_letter

- description: Drive letter to source VSC (including colon)
- type: string
- default: C:\

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
(gwmi -list win32_shadowcopy).Create('#{drive_letter}','ClientAccessible')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
