---
sigma_id: "d4a11f63-2390-411c-9adf-d791fd152830"
title: "Windows Screen Capture with CopyFromScreen"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_capture_screenshots.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_capture_screenshots.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "d4a11f63-2390-411c-9adf-d791fd152830"
  - "Windows Screen Capture with CopyFromScreen"
attack_technique_ids:
  - "T1113"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Screen Capture with CopyFromScreen

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation.
Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations

## Metadata

- Rule ID: d4a11f63-2390-411c-9adf-d791fd152830
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-28
- Modified: 2022-07-07
- Source Path: rules/windows/powershell/powershell_script/posh_ps_capture_screenshots.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1113-screen_capture|T1113]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: .CopyFromScreen
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1113/T1113.md#atomic-test-6---windows-screen-capture-copyfromscreen

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_capture_screenshots.yml)
