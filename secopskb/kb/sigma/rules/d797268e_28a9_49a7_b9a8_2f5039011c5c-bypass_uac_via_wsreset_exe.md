---
sigma_id: "d797268e-28a9-49a7-b9a8-2f5039011c5c"
title: "Bypass UAC via WSReset.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d797268e-28a9-49a7-b9a8-2f5039011c5c"
  - "Bypass UAC via WSReset.exe"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC via WSReset.exe

Detects use of WSReset.exe to bypass User Account Control (UAC). Adversaries use this technique to execute privileged processes.

## Metadata

- Rule ID: d797268e-28a9-49a7-b9a8-2f5039011c5c
- Status: test
- Level: high
- Author: E.M. Anhaus (originally from Atomic Blue Detections, Tony Lambert), oscd.community, Florian Roth
- Date: 2019-10-24
- Modified: 2022-05-13
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  ParentImage|endswith: \wsreset.exe
filter:
- Image|endswith: \conhost.exe
- OriginalFileName: CONHOST.EXE
condition: selection and not filter
```

## False Positives

- Unknown sub processes of Wsreset.exe

## References

- https://eqllib.readthedocs.io/en/latest/analytics/532b5ed4-7930-11e9-8f5c-d46d6d62a49e.html
- https://lolbas-project.github.io/lolbas/Binaries/Wsreset/
- https://www.activecyber.us/activelabs/windows-uac-bypass
- https://twitter.com/ReaQta/status/1222548288731217921

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_wsreset.yml)
