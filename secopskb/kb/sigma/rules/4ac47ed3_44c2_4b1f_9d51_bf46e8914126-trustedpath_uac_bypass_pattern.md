---
sigma_id: "4ac47ed3-44c2-4b1f-9d51-bf46e8914126"
title: "TrustedPath UAC Bypass Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_uac_bypass_trustedpath.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_trustedpath.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "4ac47ed3-44c2-4b1f-9d51-bf46e8914126"
  - "TrustedPath UAC Bypass Pattern"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# TrustedPath UAC Bypass Pattern

Detects indicators of a UAC bypass method by mocking directories

## Metadata

- Rule ID: 4ac47ed3-44c2-4b1f-9d51-bf46e8914126
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-08-27
- Modified: 2025-06-17
- Source Path: rules/windows/process_creation/proc_creation_win_uac_bypass_trustedpath.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  Image|contains:
  - C:\Windows \System32\
  - C:\Windows \SysWOW64\
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/tenable-techblog/uac-bypass-by-mocking-trusted-directories-24a96675f6e
- https://www.wietzebeukema.nl/blog/hijacking-dlls-in-windows
- https://github.com/netero1010/TrustedPath-UACBypass-BOF
- https://x.com/Wietze/status/1933495426952421843

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_uac_bypass_trustedpath.yml)
