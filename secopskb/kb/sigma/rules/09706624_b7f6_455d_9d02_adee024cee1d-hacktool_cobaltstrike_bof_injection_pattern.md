---
sigma_id: "09706624-b7f6-455d-9d02-adee024cee1d"
title: "HackTool - CobaltStrike BOF Injection Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_hktl_cobaltstrike_bof_injection_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_cobaltstrike_bof_injection_pattern.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "09706624-b7f6-455d-9d02-adee024cee1d"
  - "HackTool - CobaltStrike BOF Injection Pattern"
attack_technique_ids:
  - "T1106"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a typical pattern of a CobaltStrike BOF which inject into other processes

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106: Native API]]
- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  CallTrace|re: ^C:\\Windows\\SYSTEM32\\ntdll\.dll\+[a-z0-9]{4,6}\|C:\\Windows\\System32\\KERNELBASE\.dll\+[a-z0-9]{4,6}\|UNKNOWN\([A-Z0-9]{16}\)$
  GrantedAccess:
  - '0x1028'
  - '0x1fffff'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/boku7/injectAmsiBypass
- https://github.com/boku7/spawn

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_cobaltstrike_bof_injection_pattern.yml)
