---
sigma_id: "590a5f4c-6c8c-4f10-8307-89afe9453a9d"
title: "Suspicious Child Process Created as System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_child_process_as_system_.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_child_process_as_system_.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "590a5f4c-6c8c-4f10-8307-89afe9453a9d"
  - "Suspicious Child Process Created as System"
attack_technique_ids:
  - "T1134.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Child Process Created as System

Detection of child processes spawned with SYSTEM privileges by parents with LOCAL SERVICE or NETWORK SERVICE accounts

## Metadata

- Rule ID: 590a5f4c-6c8c-4f10-8307-89afe9453a9d
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, Roberto Rodriguez (@Cyb3rWard0g), Open Threat Research (OTR)
- Date: 2019-10-26
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_susp_child_process_as_system_.yml

## Logsource

- category: process_creation
- definition: Requirements: ParentUser field needs sysmon >= 13.30
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.002]]

## Detection

```yaml
selection:
  ParentUser|contains:
  - AUTHORI
  - AUTORI
  ParentUser|endswith:
  - \NETWORK SERVICE
  - \LOCAL SERVICE
  User|contains:
  - AUTHORI
  - AUTORI
  User|endswith:
  - \SYSTEM
  - \Système
  - \СИСТЕМА
  IntegrityLevel:
  - System
  - S-1-16-16384
filter_rundll32:
  Image|endswith: \rundll32.exe
  CommandLine|contains: DavSetCookie
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment
- https://foxglovesecurity.com/2016/09/26/rotten-potato-privilege-escalation-from-service-accounts-to-system/
- https://github.com/antonioCoco/RogueWinRM
- https://twitter.com/Cyb3rWard0g/status/1453123054243024897

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_child_process_as_system_.yml)
