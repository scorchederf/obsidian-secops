---
sigma_id: "0a4f6091-223b-41f6-8743-f322ec84930b"
title: "Suspicious GUP Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gup_suspicious_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_suspicious_execution.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0a4f6091-223b-41f6-8743-f322ec84930b"
  - "Suspicious GUP Usage"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious GUP Usage

Detects execution of the Notepad++ updater in a suspicious directory, which is often used in DLL side-loading attacks

## Metadata

- Rule ID: 0a4f6091-223b-41f6-8743-f322ec84930b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-02-06
- Modified: 2022-08-13
- Source Path: rules/windows/process_creation/proc_creation_win_gup_suspicious_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith: \GUP.exe
filter_programfiles:
  Image|endswith:
  - \Program Files\Notepad++\updater\GUP.exe
  - \Program Files (x86)\Notepad++\updater\GUP.exe
filter_user:
  Image|contains: \Users\
  Image|endswith:
  - \AppData\Local\Notepad++\updater\GUP.exe
  - \AppData\Roaming\Notepad++\updater\GUP.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Execution of tools named GUP.exe and located in folders different than Notepad++\updater

## References

- https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gup_suspicious_execution.yml)
