---
sigma_id: "f239b326-2f41-4d6b-9dfa-c846a60ef505"
title: "Password Dumper Remote Thread in LSASS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_susp_password_dumper_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_susp_password_dumper_lsass.yml"
build_date: "2026-04-26 15:01:47"
status: "stable"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "f239b326-2f41-4d6b-9dfa-c846a60ef505"
  - "Password Dumper Remote Thread in LSASS"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Dumper Remote Thread in LSASS

Detects password dumper activity by monitoring remote thread creation EventID 8 in combination with the lsass.exe process as TargetImage.
The process in field Process is the malicious program. A single execution can lead to hundreds of events.

## Metadata

- Rule ID: f239b326-2f41-4d6b-9dfa-c846a60ef505
- Status: stable
- Level: high
- Author: Thomas Patzke
- Date: 2017-02-19
- Modified: 2021-06-21
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_susp_password_dumper_lsass.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### Software Tags

- S0005

## Detection

```yaml
selection:
  TargetImage|endswith: \lsass.exe
  StartModule: ''
condition: selection
```

## False Positives

- Antivirus products

## References

- https://jpcertcc.github.io/ToolAnalysisResultSheet/details/WCE.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_susp_password_dumper_lsass.yml)
