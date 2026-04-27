---
sigma_id: "6f156c48-3894-4952-baf0-16193e9067d2"
title: "CodeIntegrity - Blocked Image Load With Revoked Certificate"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_revoked_image_blocked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_revoked_image_blocked.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "6f156c48-3894-4952-baf0-16193e9067d2"
  - "CodeIntegrity - Blocked Image Load With Revoked Certificate"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CodeIntegrity - Blocked Image Load With Revoked Certificate

Detects blocked image load events with revoked certificates by code integrity.

## Metadata

- Rule ID: 6f156c48-3894-4952-baf0-16193e9067d2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-06
- Source Path: rules/windows/builtin/code_integrity/win_codeintegrity_revoked_image_blocked.yml

## Logsource

- product: windows
- service: codeintegrity-operational

## Detection

```yaml
selection:
  EventID: 3036
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-tag-explanations
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_revoked_image_blocked.yml)
