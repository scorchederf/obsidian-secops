---
sigma_id: "c8da0dfd-4ed0-4b68-962d-13c9c884384e"
title: "Potential Credential Dumping Via LSASS Process Clone"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lsass_process_clone.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lsass_process_clone.yml"
build_date: "2026-04-27 19:13:53"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious LSASS process process clone that could be a sign of credential dumping activity

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

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
