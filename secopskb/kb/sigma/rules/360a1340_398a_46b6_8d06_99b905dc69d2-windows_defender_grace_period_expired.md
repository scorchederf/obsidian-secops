---
sigma_id: "360a1340-398a-46b6-8d06-99b905dc69d2"
title: "Windows Defender Grace Period Expired"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_antimalware_platform_expired.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_antimalware_platform_expired.yml"
build_date: "2026-04-26 14:14:40"
status: "stable"
level: "high"
logsource: "windows / windefend"
aliases:
  - "360a1340-398a-46b6-8d06-99b905dc69d2"
  - "Windows Defender Grace Period Expired"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Grace Period Expired

Detects the expiration of the grace period of Windows Defender. This means protection against viruses, spyware, and other potentially unwanted software is disabled.

## Metadata

- Rule ID: 360a1340-398a-46b6-8d06-99b905dc69d2
- Status: stable
- Level: high
- Author: Ján Trenčanský, frack113
- Date: 2020-07-28
- Modified: 2023-11-22
- Source Path: rules/windows/builtin/windefend/win_defender_antimalware_platform_expired.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 5101
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide#event-id-5101
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://craigclouditpro.wordpress.com/2020/03/04/hunting-malicious-windows-defender-activity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_antimalware_platform_expired.yml)
