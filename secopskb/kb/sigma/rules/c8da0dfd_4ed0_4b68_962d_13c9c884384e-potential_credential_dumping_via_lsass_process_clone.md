---
sigma_id: "c8da0dfd-4ed0-4b68-962d-13c9c884384e"
title: "Potential Credential Dumping Via LSASS Process Clone"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lsass_process_clone.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lsass_process_clone.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "c8da0dfd-4ed0-4b68-962d-13c9c884384e"
  - "Potential Credential Dumping Via LSASS Process Clone"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Credential Dumping Via LSASS Process Clone

Detects a suspicious LSASS process process clone that could be a sign of credential dumping activity

## Metadata

- Rule ID: c8da0dfd-4ed0-4b68-962d-13c9c884384e
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems), Samir Bousseaden
- Date: 2021-11-27
- Modified: 2023-03-02
- Source Path: rules/windows/process_creation/proc_creation_win_lsass_process_clone.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  ParentImage|endswith: \Windows\System32\lsass.exe
  Image|endswith: \Windows\System32\lsass.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.matteomalvica.com/blog/2019/12/02/win-defender-atp-cred-bypass/
- https://twitter.com/Hexacorn/status/1420053502554951689
- https://twitter.com/SBousseaden/status/1464566846594691073?s=20

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lsass_process_clone.yml)
