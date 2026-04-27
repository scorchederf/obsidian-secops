---
atomic_guid: "09147b61-40f6-4b2a-b6fb-9e73a3437c96"
title: "Disabling ShowUI Settings of Windows Error Reporting (WER)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "09147b61-40f6-4b2a-b6fb-9e73a3437c96"
  - "Disabling ShowUI Settings of Windows Error Reporting (WER)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disabling ShowUI Settings of Windows Error Reporting (WER)

A modification registry to disable ShowUI settings of Windows Error Report. This registry setting can influence the behavior of error reporting dialogs or prompt box. 
This technique was seen in DarkGate malware as part of its installation.

## Metadata

- Atomic GUID: 09147b61-40f6-4b2a-b6fb-9e73a3437c96
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKCU\Software\Microsoft\Windows\Windows Error Reporting" /v DontShowUI /t REG_DWORD /d 1 /f
```

### Cleanup

```cmd
reg add "HKCU\Software\Microsoft\Windows\Windows Error Reporting" /v DontShowUI /t REG_DWORD /d 0 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
