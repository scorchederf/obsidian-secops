---
sigma_id: "320fccbf-5e32-4101-82b8-2679c5f007c6"
title: "CodeIntegrity - Revoked Kernel Driver Loaded"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_revoked_driver_loaded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_revoked_driver_loaded.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "320fccbf-5e32-4101-82b8-2679c5f007c6"
  - "CodeIntegrity - Revoked Kernel Driver Loaded"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CodeIntegrity - Revoked Kernel Driver Loaded

Detects the load of a revoked kernel driver

## Metadata

- Rule ID: 320fccbf-5e32-4101-82b8-2679c5f007c6
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-06
- Source Path: rules/windows/builtin/code_integrity/win_codeintegrity_revoked_driver_loaded.yml

## Logsource

- product: windows
- service: codeintegrity-operational

## Detection

```yaml
selection:
  EventID:
  - 3021
  - 3022
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-tag-explanations
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_revoked_driver_loaded.yml)
