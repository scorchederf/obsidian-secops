---
sigma_id: "d99b79d2-0a6f-4f46-ad8b-260b6e17f982"
title: "Security Eventlog Cleared"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_audit_log_cleared.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_audit_log_cleared.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "d99b79d2-0a6f-4f46-ad8b-260b6e17f982"
  - "Security Eventlog Cleared"
attack_technique_ids:
  - "T1070.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Security Eventlog Cleared

One of the Windows Eventlogs has been cleared. e.g. caused by "wevtutil cl" command execution

## Metadata

- Rule ID: d99b79d2-0a6f-4f46-ad8b-260b6e17f982
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-01-10
- Modified: 2022-02-24
- Source Path: rules/windows/builtin/security/win_security_audit_log_cleared.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Detection

```yaml
selection_517:
  EventID: 517
  Provider_Name: Security
selection_1102:
  EventID: 1102
  Provider_Name: Microsoft-Windows-Eventlog
condition: 1 of selection_*
```

## False Positives

- Rollout of log collection agents (the setup routine often includes a reset of the local Eventlog)
- System provisioning (system reset before the golden image creation)

## References

- https://twitter.com/deviouspolack/status/832535435960209408
- https://www.hybrid-analysis.com/sample/027cc450ef5f8c5f653329641ec1fed91f694e0d229928963b30f6b0d7d3a745?environmentId=100
- https://github.com/Azure/Azure-Sentinel/blob/f99542b94afe0ad2f19a82cc08262e7ac8e1428e/Detections/SecurityEvent/SecurityEventLogCleared.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_audit_log_cleared.yml)
