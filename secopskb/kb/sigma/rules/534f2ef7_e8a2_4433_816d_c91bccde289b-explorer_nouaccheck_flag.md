---
sigma_id: "534f2ef7-e8a2-4433-816d-c91bccde289b"
title: "Explorer NOUACCHECK Flag"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_explorer_nouaccheck.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_explorer_nouaccheck.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "534f2ef7-e8a2-4433-816d-c91bccde289b"
  - "Explorer NOUACCHECK Flag"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Explorer NOUACCHECK Flag

Detects suspicious starts of explorer.exe that use the /NOUACCHECK flag that allows to run all sub processes of that newly started explorer.exe without any UAC checks

## Metadata

- Rule ID: 534f2ef7-e8a2-4433-816d-c91bccde289b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-23
- Modified: 2022-04-21
- Source Path: rules/windows/process_creation/proc_creation_win_explorer_nouaccheck.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  Image|endswith: \explorer.exe
  CommandLine|contains: /NOUACCHECK
filter_dc_logon:
- ParentCommandLine: C:\Windows\system32\svchost.exe -k netsvcs -p -s Schedule
- ParentImage: C:\Windows\System32\svchost.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Domain Controller User Logon
- Unknown how many legitimate software products use that method

## References

- https://twitter.com/ORCA6665/status/1496478087244095491

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_explorer_nouaccheck.yml)
