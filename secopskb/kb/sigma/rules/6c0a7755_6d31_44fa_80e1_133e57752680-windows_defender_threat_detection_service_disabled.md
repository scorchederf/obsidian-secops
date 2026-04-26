---
sigma_id: "6c0a7755-6d31-44fa-80e1-133e57752680"
title: "Windows Defender Threat Detection Service Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_defender_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_defender_disabled.yml"
build_date: "2026-04-26 14:14:40"
status: "stable"
level: "medium"
logsource: "windows / system"
aliases:
  - "6c0a7755-6d31-44fa-80e1-133e57752680"
  - "Windows Defender Threat Detection Service Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Threat Detection Service Disabled

Detects when the "Windows Defender Threat Protection" service is disabled.

## Metadata

- Rule ID: 6c0a7755-6d31-44fa-80e1-133e57752680
- Status: stable
- Level: medium
- Author: Ján Trenčanský, frack113
- Date: 2020-07-28
- Modified: 2024-07-02
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_defender_disabled.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 7036
  Provider_Name: Service Control Manager
  param1:
  - Windows Defender Antivirus Service
  - Service antivirus Microsoft Defender
  param2:
  - stopped
  - arrêté
condition: selection
```

## False Positives

- Administrator actions
- Auto updates of Windows Defender causes restarts

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_defender_disabled.yml)
