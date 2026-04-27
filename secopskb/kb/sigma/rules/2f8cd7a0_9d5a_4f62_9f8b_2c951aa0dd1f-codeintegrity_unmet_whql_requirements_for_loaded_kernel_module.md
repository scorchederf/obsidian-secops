---
sigma_id: "2f8cd7a0-9d5a-4f62-9f8b-2c951aa0dd1f"
title: "CodeIntegrity - Unmet WHQL Requirements For Loaded Kernel Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_whql_failure.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_whql_failure.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "2f8cd7a0-9d5a-4f62-9f8b-2c951aa0dd1f"
  - "CodeIntegrity - Unmet WHQL Requirements For Loaded Kernel Module"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# CodeIntegrity - Unmet WHQL Requirements For Loaded Kernel Module

Detects loaded kernel modules that did not meet the WHQL signing requirements.

## Metadata

- Rule ID: 2f8cd7a0-9d5a-4f62-9f8b-2c951aa0dd1f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-06
- Modified: 2023-06-14
- Source Path: rules/windows/builtin/code_integrity/win_codeintegrity_whql_failure.yml

## Logsource

- product: windows
- service: codeintegrity-operational

## Detection

```yaml
selection:
  EventID:
  - 3082
  - 3083
filter_optional_vmware:
  FileNameBuffer:
  - system32\drivers\vsock.sys
  - System32\drivers\vmci.sys
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-tag-explanations
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_whql_failure.yml)
