---
atomic_guid: "15f44ea9-4571-4837-be9e-802431a7bfae"
title: "Javascript in registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "15f44ea9-4571-4837-be9e-802431a7bfae"
  - "Javascript in registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Javascript in registry

Upon execution, a javascript block will be placed in the registry for persistence.
Additionally, open Registry Editor to view the modified entry in HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings.

## Metadata

- Atomic GUID: 15f44ea9-4571-4837-be9e-802431a7bfae
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- name: powershell

### Command

```powershell
New-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name T1112 -Value "<script>"
```

### Cleanup

```powershell
Remove-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name T1112 -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
