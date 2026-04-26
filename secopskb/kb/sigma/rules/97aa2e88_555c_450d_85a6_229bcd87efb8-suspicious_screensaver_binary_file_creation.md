---
sigma_id: "97aa2e88-555c-450d-85a6-229bcd87efb8"
title: "Suspicious Screensaver Binary File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_creation_scr_binary_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_scr_binary_file.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "97aa2e88-555c-450d-85a6-229bcd87efb8"
  - "Suspicious Screensaver Binary File Creation"
attack_technique_ids:
  - "T1546.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Screensaver Binary File Creation

Adversaries may establish persistence by executing malicious content triggered by user inactivity.
Screensavers are programs that execute after a configurable time of user inactivity and consist of Portable Executable (PE) files with a .scr file extension

## Metadata

- Rule ID: 97aa2e88-555c-450d-85a6-229bcd87efb8
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-29
- Modified: 2022-11-08
- Source Path: rules/windows/file/file_event/file_event_win_creation_scr_binary_file.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.002]]

## Detection

```yaml
selection:
  TargetFilename|endswith: .scr
filter_generic:
  Image|endswith:
  - \Kindle.exe
  - \Bin\ccSvcHst.exe
filter_tiworker:
  Image|endswith: \TiWorker.exe
  TargetFilename|endswith: \uwfservicingscr.scr
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.002/T1546.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_creation_scr_binary_file.yml)
