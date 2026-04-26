---
sigma_id: "91903aba-1088-42ee-b680-d6d94fe002b0"
title: "Windows Defender Submit Sample Feature Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_config_change_sample_submission_consent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_config_change_sample_submission_consent.yml"
build_date: "2026-04-26 14:14:40"
status: "stable"
level: "low"
logsource: "windows / windefend"
aliases:
  - "91903aba-1088-42ee-b680-d6d94fe002b0"
  - "Windows Defender Submit Sample Feature Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Submit Sample Feature Disabled

Detects disabling of the "Automatic Sample Submission" feature of Windows Defender.

## Metadata

- Rule ID: 91903aba-1088-42ee-b680-d6d94fe002b0
- Status: stable
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-06
- Source Path: rules/windows/builtin/windefend/win_defender_config_change_sample_submission_consent.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID: 5007
  NewValue|contains: \Real-Time Protection\SubmitSamplesConsent = 0x0
condition: selection
```

## False Positives

- Administrator activity (must be investigated)

## References

- https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide
- https://bidouillesecurity.com/disable-windows-defender-in-powershell/#DisableAntiSpyware

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_config_change_sample_submission_consent.yml)
