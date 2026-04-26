---
atomic_guid: "ffbb407e-7f1d-4c95-b22e-548169db1fbd"
title: "Activate Windows NoFind Group Policy Feature"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "ffbb407e-7f1d-4c95-b22e-548169db1fbd"
  - "Activate Windows NoFind Group Policy Feature"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Activate Windows NoFind Group Policy Feature

Modify the registry of the currently logged in user using reg.exe via cmd console to Remove Search menu from Start Menu Group Policy.
Take note that some Group Policy changes might require a restart to take effect.
See how Trojan abuses this technique- https://www.sophos.com/de-de/threat-center/threat-analyses/viruses-and-spyware/Troj~Krotten-N/detailed-analysis

## Metadata

- Atomic GUID: ffbb407e-7f1d-4c95-b22e-548169db1fbd
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

```commandprompt
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoFind /t REG_DWORD /d 1 /f
```

### Cleanup

```commandprompt
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoFind /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
