---
sigma_id: "e4be5675-4a53-426a-8c81-a8bb2387e947"
title: "CodeIntegrity - Blocked Image/Driver Load For Policy Violation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_enforced_policy_block.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_enforced_policy_block.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "e4be5675-4a53-426a-8c81-a8bb2387e947"
  - "CodeIntegrity - Blocked Image/Driver Load For Policy Violation"
attack_technique_ids:
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CodeIntegrity - Blocked Image/Driver Load For Policy Violation

Detects blocked load events that did not meet the authenticode signing level requirements or violated the code integrity policy.

## Metadata

- Rule ID: e4be5675-4a53-426a-8c81-a8bb2387e947
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-10
- Modified: 2023-06-07
- Source Path: rules/windows/builtin/code_integrity/win_codeintegrity_enforced_policy_block.yml

## Logsource

- product: windows
- service: codeintegrity-operational

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]]

## Detection

```yaml
selection:
  EventID: 3077
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/wdormann/status/1590434950335320065
- https://github.com/MicrosoftDocs/windows-itpro-docs/blob/40fe118976734578f83e5e839b9c63ae7a4af82d/windows/security/threat-protection/windows-defender-application-control/event-id-explanations.md#windows-codeintegrity-operational-log
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_enforced_policy_block.yml)
