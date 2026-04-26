---
sigma_id: "686c0b4b-9dd3-4847-9077-d6c1bbe36fcb"
title: "Windows Defender Virus Scanning Feature Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_virus_scan_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_virus_scan_disabled.yml"
build_date: "2026-04-26 15:01:55"
status: "stable"
level: "high"
logsource: "windows / windefend"
aliases:
  - "686c0b4b-9dd3-4847-9077-d6c1bbe36fcb"
  - "Windows Defender Virus Scanning Feature Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Defender Virus Scanning Feature Disabled

Detects disabling of the Windows Defender virus scanning feature

## Metadata

- Rule ID: 686c0b4b-9dd3-4847-9077-d6c1bbe36fcb
- Status: stable
- Level: high
- Author: Ján Trenčanský, frack113
- Date: 2020-07-28
- Modified: 2023-11-22
- Source Path: rules/windows/builtin/windefend/win_defender_virus_scan_disabled.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 5012
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide#event-id-5012
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://craigclouditpro.wordpress.com/2020/03/04/hunting-malicious-windows-defender-activity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_virus_scan_disabled.yml)
