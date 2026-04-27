---
atomic_guid: "e672a340-a933-447c-954c-d68db38a09b1"
title: "Modify EnableNonTPM Registry entry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "e672a340-a933-447c-954c-d68db38a09b1"
  - "Modify EnableNonTPM Registry entry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify EnableNonTPM Registry entry

Allow Bitlocker without TPM for Bitlocker tool

## Metadata

- Atomic GUID: e672a340-a933-447c-954c-d68db38a09b1
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Policies\Microsoft\FVE" /v EnableNonTPM /t REG_DWORD /d 1 /f
```

### Cleanup

```cmd
reg delete "HKLM\SOFTWARE\Policies\Microsoft\FVE" /v EnableNonTPM /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
