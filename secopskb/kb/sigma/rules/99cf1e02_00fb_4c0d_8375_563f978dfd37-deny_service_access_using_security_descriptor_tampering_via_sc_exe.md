---
sigma_id: "99cf1e02-00fb-4c0d-8375-563f978dfd37"
title: "Deny Service Access Using Security Descriptor Tampering Via Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_sdset_deny_service_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_deny_service_access.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "99cf1e02-00fb-4c0d-8375-563f978dfd37"
  - "Deny Service Access Using Security Descriptor Tampering Via Sc.EXE"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious DACL modifications to deny access to a service that affects critical trustees. This can be used to hide services or make them unstoppable.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]

## Detection

```yaml
selection_sc:
- Image|endswith: \sc.exe
- OriginalFileName: sc.exe
selection_sdset:
  CommandLine|contains|all:
  - sdset
  - D;
selection_trustee:
  CommandLine|contains:
  - ;IU
  - ;SU
  - ;BA
  - ;SY
  - ;WD
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.sans.org/blog/red-team-tactics-hiding-windows-services/
- https://itconnect.uw.edu/tools-services-support/it-systems-infrastructure/msinf/other-help/understanding-sddl-syntax/
- https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-strings

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_deny_service_access.yml)
