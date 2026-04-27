---
atomic_guid: "39f1f378-ba8a-42b3-96dc-2a6540cfc1e3"
title: "Mimic Ransomware - Enable Multiple User Sessions"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "39f1f378-ba8a-42b3-96dc-2a6540cfc1e3"
  - "Mimic Ransomware - Enable Multiple User Sessions"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test emulates Mimic ransomware's ability to enable multiple user sessions by modifying the AllowMultipleTSSessions value within the Winlogon registry key. 
See [Mimic Ransomware Overview] (https://www.trendmicro.com/en_us/research/23/a/new-mimic-ransomware-abuses-everything-apis-for-its-encryption-p.html)

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Winlogon /t REG_DWORD /v AllowMultipleTSSessions /d 1 /f
```

### Cleanup

```cmd
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Winlogon /v AllowMultipleTSSessions /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
