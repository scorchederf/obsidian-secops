---
sigma_id: "af491bca-e752-4b44-9c86-df5680533dbc"
title: "Finger.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_finger_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_finger_execution.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "af491bca-e752-4b44-9c86-df5680533dbc"
  - "Finger.EXE Execution"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Finger.EXE Execution

Detects execution of the "finger.exe" utility.
Finger.EXE or "TCPIP Finger Command" is an old utility that is still present on modern Windows installation. It Displays information about users on a specified remote computer (typically a UNIX computer) that is running the finger service or daemon.
Due to the old nature of this utility and the rareness of machines having the finger service. Any execution of "finger.exe" can be considered "suspicious" and worth investigating.

## Metadata

- Rule ID: af491bca-e752-4b44-9c86-df5680533dbc
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), omkar72, oscd.community
- Date: 2021-02-24
- Modified: 2024-06-27
- Source Path: rules/windows/process_creation/proc_creation_win_finger_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
- OriginalFileName: finger.exe
- Image|endswith: \finger.exe
condition: selection
```

## False Positives

- Admin activity (unclear what they do nowadays with finger.exe)

## References

- https://twitter.com/bigmacjpg/status/1349727699863011328?s=12
- https://app.any.run/tasks/40115012-a919-4208-bfed-41e82cb3dadf/
- http://hyp3rlinx.altervista.org/advisories/Windows_TCPIP_Finger_Command_C2_Channel_and_Bypassing_Security_Software.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_finger_execution.yml)
