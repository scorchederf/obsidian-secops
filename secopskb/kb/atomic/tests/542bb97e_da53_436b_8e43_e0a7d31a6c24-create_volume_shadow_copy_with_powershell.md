---
atomic_guid: "542bb97e-da53-436b-8e43-e0a7d31a6c24"
title: "Create Volume Shadow Copy with Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-27 19:12:25"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test is intended to be run on a domain Controller.

The Active Directory database NTDS.dit may be dumped by copying it from a Volume Shadow Copy.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

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
