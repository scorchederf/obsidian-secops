---
sigma_id: "b28e58e4-2a72-4fae-bdee-0fbe904db642"
title: "Windows Defender Real-time Protection Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_real_time_protection_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_real_time_protection_disabled.yml"
build_date: "2026-04-26 14:14:40"
status: "stable"
level: "high"
logsource: "windows / windefend"
aliases:
  - "b28e58e4-2a72-4fae-bdee-0fbe904db642"
  - "Windows Defender Real-time Protection Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Real-time Protection Disabled

Detects disabling of Windows Defender Real-time Protection. As this event doesn't contain a lot of information on who initiated this action you might want to reduce it to a "medium" level if this occurs too many times in your environment

## Metadata

- Rule ID: b28e58e4-2a72-4fae-bdee-0fbe904db642
- Status: stable
- Level: high
- Author: Ján Trenčanský, frack113
- Date: 2020-07-28
- Modified: 2023-11-22
- Source Path: rules/windows/builtin/windefend/win_defender_real_time_protection_disabled.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 5001
condition: selection
```

## False Positives

- Administrator actions (should be investigated)
- Seen being triggered occasionally during Windows 8 Defender Updates

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide#event-id-5001
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://craigclouditpro.wordpress.com/2020/03/04/hunting-malicious-windows-defender-activity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_real_time_protection_disabled.yml)
