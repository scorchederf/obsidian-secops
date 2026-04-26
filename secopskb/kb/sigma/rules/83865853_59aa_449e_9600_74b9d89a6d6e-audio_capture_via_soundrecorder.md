---
sigma_id: "83865853-59aa-449e-9600-74b9d89a6d6e"
title: "Audio Capture via SoundRecorder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_soundrecorder_audio_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_soundrecorder_audio_capture.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "83865853-59aa-449e-9600-74b9d89a6d6e"
  - "Audio Capture via SoundRecorder"
attack_technique_ids:
  - "T1123"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Audio Capture via SoundRecorder

Detect attacker collecting audio via SoundRecorder application.

## Metadata

- Rule ID: 83865853-59aa-449e-9600-74b9d89a6d6e
- Status: test
- Level: medium
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community
- Date: 2019-10-24
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_soundrecorder_audio_capture.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1123-audio_capture|T1123]]

## Detection

```yaml
selection:
  Image|endswith: \SoundRecorder.exe
  CommandLine|contains: /FILE
condition: selection
```

## False Positives

- Legitimate audio capture by legitimate user.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1123/T1123.md
- https://eqllib.readthedocs.io/en/latest/analytics/f72a98cb-7b3d-4100-99c3-a138b6e9ff6e.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_soundrecorder_audio_capture.yml)
