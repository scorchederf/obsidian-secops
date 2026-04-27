---
atomic_guid: "47c96489-2f55-4774-a6df-39faff428f6f"
title: "PowerShell Version 2 Downgrade"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.010"
attack_technique_name: "Impair Defenses: Downgrade Attack"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.010/T1562.010.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "47c96489-2f55-4774-a6df-39faff428f6f"
  - "PowerShell Version 2 Downgrade"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Version 2 Downgrade

Executes outdated PowerShell Version 2 which does not support security features like AMSI. By default the atomic will attempt to execute the cmdlet Invoke-Mimikatz whether it exists or not, as this cmdlet will be blocked by AMSI when active.

## Metadata

- Atomic GUID: 47c96489-2f55-4774-a6df-39faff428f6f
- Technique: T1562.010: Impair Defenses: Downgrade Attack
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1562.010/T1562.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.010]]

## Input Arguments

### v2_command

- description: Specify the command to execute with Version 2
- type: string
- default: Invoke-Mimikatz

## Dependencies

Check if Version 2 is installed.

### Prerequisite Check

```untitled
$v2_installed = PowerShell -version 2 -command '$PSVersionTable.PSVersion.Major'
if (-not $v2_installed) {exit 1} else {exit 0}
```

### Get Prerequisite

```untitled
echo "Manually install PowerShell Version 2"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
PowerShell -version 2 -command '#{v2_command}'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.010/T1562.010.yaml)
