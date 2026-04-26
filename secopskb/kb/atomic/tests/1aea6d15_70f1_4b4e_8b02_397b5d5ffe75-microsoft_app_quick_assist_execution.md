---
atomic_guid: "1aea6d15-70f1-4b4e-8b02-397b5d5ffe75"
title: "Microsoft App Quick Assist Execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1aea6d15-70f1-4b4e-8b02-397b5d5ffe75"
  - "Microsoft App Quick Assist Execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Microsoft App Quick Assist Execution

An adversary may attempt to trick a user into executing Microsoft Quick Assist Microsoft Store app and connect to the user's machine.

## Metadata

- Atomic GUID: 1aea6d15-70f1-4b4e-8b02-397b5d5ffe75
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process "shell:AppsFolder\MicrosoftCorporationII.QuickAssist_8wekyb3d8bbwe!App"
```

### Cleanup

```powershell
Stop-Process -Name quickassist
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
