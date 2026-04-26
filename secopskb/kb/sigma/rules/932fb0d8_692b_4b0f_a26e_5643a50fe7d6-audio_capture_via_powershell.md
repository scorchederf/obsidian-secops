---
sigma_id: "932fb0d8-692b-4b0f-a26e-5643a50fe7d6"
title: "Audio Capture via PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_audio_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_audio_capture.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "932fb0d8-692b-4b0f-a26e-5643a50fe7d6"
  - "Audio Capture via PowerShell"
attack_technique_ids:
  - "T1123"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Audio Capture via PowerShell

Detects audio capture via PowerShell Cmdlet.

## Metadata

- Rule ID: 932fb0d8-692b-4b0f-a26e-5643a50fe7d6
- Status: test
- Level: medium
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-24
- Modified: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_audio_capture.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1123-audio_capture|T1123]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - WindowsAudioDevice-Powershell-Cmdlet
  - Toggle-AudioDevice
  - 'Get-AudioDevice '
  - 'Set-AudioDevice '
  - 'Write-AudioDevice '
condition: selection
```

## False Positives

- Legitimate audio capture by legitimate user.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1123/T1123.md
- https://eqllib.readthedocs.io/en/latest/analytics/ab7a6ef4-0983-4275-a4f1-5c6bd3c31c23.html
- https://github.com/frgnca/AudioDeviceCmdlets

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_audio_capture.yml)
