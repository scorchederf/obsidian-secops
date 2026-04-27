---
sigma_id: "9b72b82d-f1c5-4632-b589-187159bc6ec1"
title: "CodeIntegrity - Blocked Driver Load With Revoked Certificate"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_revoked_driver_blocked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_revoked_driver_blocked.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "9b72b82d-f1c5-4632-b589-187159bc6ec1"
  - "CodeIntegrity - Blocked Driver Load With Revoked Certificate"
attack_technique_ids:
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects blocked load attempts of revoked drivers

## Logsource

- product: windows
- service: codeintegrity-operational

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]

## Detection

```yaml
selection:
  EventID: 3023
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-tag-explanations
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_revoked_driver_blocked.yml)
