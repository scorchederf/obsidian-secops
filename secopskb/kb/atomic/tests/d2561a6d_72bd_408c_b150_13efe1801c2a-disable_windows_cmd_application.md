---
atomic_guid: "d2561a6d-72bd-408c-b150-13efe1801c2a"
title: "Disable Windows CMD application"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "d2561a6d-72bd-408c-b150-13efe1801c2a"
  - "Disable Windows CMD application"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Windows CMD application

Modify the registry of the currently logged in user using reg.exe via cmd console to disable the windows CMD application.
See example how Agent Tesla malware abuses this technique: https://any.run/report/ea4ea08407d4ee72e009103a3b77e5a09412b722fdef67315ea63f22011152af/a866d7b1-c236-4f26-a391-5ae32213dfc4#registry

## Metadata

- Atomic GUID: d2561a6d-72bd-408c-b150-13efe1801c2a
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path "HKCU:\Software\Policies\Microsoft\Windows\System" -Name DisableCMD -Value 1
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKCU:\Software\Policies\Microsoft\Windows\System" -Name DisableCMD -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
