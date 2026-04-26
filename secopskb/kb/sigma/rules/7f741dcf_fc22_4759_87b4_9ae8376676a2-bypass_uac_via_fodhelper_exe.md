---
sigma_id: "7f741dcf-fc22-4759-87b4-9ae8376676a2"
title: "Bypass UAC via Fodhelper.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_fodhelper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_fodhelper.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7f741dcf-fc22-4759-87b4-9ae8376676a2"
  - "Bypass UAC via Fodhelper.exe"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bypass UAC via Fodhelper.exe

Identifies use of Fodhelper.exe to bypass User Account Control. Adversaries use this technique to execute privileged processes.

## Metadata

- Rule ID: 7f741dcf-fc22-4759-87b4-9ae8376676a2
- Status: test
- Level: high
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Tony Lambert), oscd.community
- Date: 2019-10-24
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_fodhelper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  ParentImage|endswith: \fodhelper.exe
condition: selection
```

## False Positives

- Legitimate use of fodhelper.exe utility by legitimate user

## References

- https://eqllib.readthedocs.io/en/latest/analytics/e491ce22-792f-11e9-8f5c-d46d6d62a49e.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1548.002/T1548.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_fodhelper.yml)
