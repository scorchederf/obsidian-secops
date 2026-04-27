---
sigma_id: "49f2f17b-b4c8-4172-a68b-d5bf95d05130"
title: "UAC Bypass via ICMLuaUtil"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_icmluautil.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_icmluautil.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "49f2f17b-b4c8-4172-a68b-d5bf95d05130"
  - "UAC Bypass via ICMLuaUtil"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the pattern of UAC Bypass using ICMLuaUtil Elevated COM interface

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detection

```yaml
selection:
  ParentImage|endswith: \dllhost.exe
  ParentCommandLine|contains:
  - /Processid:{3E5FC7F9-9A51-4367-9063-A120244FBEC7}
  - /Processid:{D2E7041B-2927-42FB-8E9F-7CE93B6DC937}
filter:
- Image|endswith: \WerFault.exe
- OriginalFileName: WerFault.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/uac-bypass-via-icmluautil-elevated-com-interface.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_icmluautil.yml)
