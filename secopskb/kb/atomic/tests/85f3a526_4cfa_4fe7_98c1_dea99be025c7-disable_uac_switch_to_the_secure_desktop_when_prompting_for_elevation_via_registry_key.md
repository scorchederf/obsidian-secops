---
atomic_guid: "85f3a526-4cfa-4fe7-98c1-dea99be025c7"
title: "Disable UAC - Switch to the secure desktop when prompting for elevation via registry key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "85f3a526-4cfa-4fe7-98c1-dea99be025c7"
  - "Disable UAC - Switch to the secure desktop when prompting for elevation via registry key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable UAC - Switch to the secure desktop when prompting for elevation via registry key

User Account Control (UAC) is a security mechanism for limiting the elevation of privileges, including administrative accounts, unless authorized. 
This setting ensures that the elevation prompt is only used in secure desktop mode.
Disable User Account Conrol (UAC) for secure desktop by setting the registry key HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\PromptOnSecureDesktop to 0.

## Metadata

- Atomic GUID: 85f3a526-4cfa-4fe7-98c1-dea99be025c7
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name PromptOnSecureDesktop -Value 0 -Type Dword -Force
```

### Cleanup

```powershell
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name PromptOnSecureDesktop -Value 1 -Type Dword -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
