---
sigma_id: "6c8fbee5-dee8-49bc-851d-c3142d02aa47"
title: "Allow Service Access Using Security Descriptor Tampering Via Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_sdset_allow_service_changes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_allow_service_changes.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6c8fbee5-dee8-49bc-851d-c3142d02aa47"
  - "Allow Service Access Using Security Descriptor Tampering Via Sc.EXE"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Allow Service Access Using Security Descriptor Tampering Via Sc.EXE

Detects suspicious DACL modifications to allow access to a service from a suspicious trustee. This can be used to override access restrictions set by previous ACLs.

## Metadata

- Rule ID: 6c8fbee5-dee8-49bc-851d-c3142d02aa47
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-28
- Modified: 2025-10-22
- Source Path: rules/windows/process_creation/proc_creation_win_sc_sdset_allow_service_changes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection_sc:
- Image|endswith: \sc.exe
- OriginalFileName: sc.exe
selection_sdset:
  CommandLine|contains|all:
  - sdset
  - A;
selection_trustee:
  CommandLine|contains:
  - ;IU
  - ;SU
  - ;BA
  - ;SY
  - ;WD
filter_optional_hexnode:
  ParentImage: C:\Hexnode\Hexnode Agent\Current\HexnodeAgent.exe
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1628720819537936386
- https://itconnect.uw.edu/tools-services-support/it-systems-infrastructure/msinf/other-help/understanding-sddl-syntax/
- https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-strings

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_sdset_allow_service_changes.yml)
