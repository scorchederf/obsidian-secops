---
atomic_guid: "ac34b0f7-0f85-4ac0-b93e-3ced2bc69bb8"
title: "Disable Windows Registry Tool"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "ac34b0f7-0f85-4ac0-b93e-3ced2bc69bb8"
  - "Disable Windows Registry Tool"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable Windows Registry Tool

Modify the registry of the currently logged in user using reg.exe via cmd console to disable the windows registry tool to prevent user modifying registry entry.
See example how Agent Tesla malware abuses this technique: https://any.run/report/ea4ea08407d4ee72e009103a3b77e5a09412b722fdef67315ea63f22011152af/a866d7b1-c236-4f26-a391-5ae32213dfc4#registry

## Metadata

- Atomic GUID: ac34b0f7-0f85-4ac0-b93e-3ced2bc69bb8
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
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\policies\system /v DisableRegistryTools /t REG_DWORD /d 1 /f
```

### Cleanup

```cmd
powershell Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\policies\system" -Name DisableRegistryTools -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
