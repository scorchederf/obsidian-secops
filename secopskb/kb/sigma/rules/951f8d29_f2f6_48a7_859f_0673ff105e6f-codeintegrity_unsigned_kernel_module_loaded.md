---
sigma_id: "951f8d29-f2f6-48a7-859f-0673ff105e6f"
title: "CodeIntegrity - Unsigned Kernel Module Loaded"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_driver_loaded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_driver_loaded.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "951f8d29-f2f6-48a7-859f-0673ff105e6f"
  - "CodeIntegrity - Unsigned Kernel Module Loaded"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CodeIntegrity - Unsigned Kernel Module Loaded

Detects the presence of a loaded unsigned kernel module on the system.

## Metadata

- Rule ID: 951f8d29-f2f6-48a7-859f-0673ff105e6f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-06
- Source Path: rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_driver_loaded.yml

## Logsource

- product: windows
- service: codeintegrity-operational

## Detection

```yaml
selection:
  EventID: 3001
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-tag-explanations
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_unsigned_driver_loaded.yml)
