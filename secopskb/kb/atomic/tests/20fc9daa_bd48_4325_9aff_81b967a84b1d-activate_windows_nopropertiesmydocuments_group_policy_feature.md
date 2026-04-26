---
atomic_guid: "20fc9daa-bd48-4325-9aff-81b967a84b1d"
title: "Activate Windows NoPropertiesMyDocuments Group Policy Feature"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "20fc9daa-bd48-4325-9aff-81b967a84b1d"
  - "Activate Windows NoPropertiesMyDocuments Group Policy Feature"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Activate Windows NoPropertiesMyDocuments Group Policy Feature

Modify the registry of the currently logged in user using reg.exe via cmd console to hide Properties from "My Documents icon" Group Policy. 
Take note that some Group Policy changes might require a restart to take effect.
See how ransomware abuses this technique- https://www.virustotal.com/gui/file/2d7855bf6470aa323edf2949b54ce2a04d9e38770f1322c3d0420c2303178d91/details

## Metadata

- Atomic GUID: 20fc9daa-bd48-4325-9aff-81b967a84b1d
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
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoPropertiesMyDocuments /t REG_DWORD /d 1 /f
```

### Cleanup

```cmd
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoPropertiesMyDocuments /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
