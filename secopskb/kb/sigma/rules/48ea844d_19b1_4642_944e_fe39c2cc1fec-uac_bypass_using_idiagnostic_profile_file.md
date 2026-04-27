---
sigma_id: "48ea844d-19b1-4642-944e-fe39c2cc1fec"
title: "UAC Bypass Using IDiagnostic Profile - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_uac_bypass_idiagnostic_profile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_idiagnostic_profile.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "48ea844d-19b1-4642-944e-fe39c2cc1fec"
  - "UAC Bypass Using IDiagnostic Profile - File"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a file by "dllhost.exe" in System32 directory part of "IDiagnosticProfileUAC" UAC bypass technique

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]

## Detection

```yaml
selection:
  Image|endswith: \DllHost.exe
  TargetFilename|startswith: C:\Windows\System32\
  TargetFilename|endswith: .dll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Wh04m1001/IDiagnosticProfileUAC

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_uac_bypass_idiagnostic_profile.yml)
