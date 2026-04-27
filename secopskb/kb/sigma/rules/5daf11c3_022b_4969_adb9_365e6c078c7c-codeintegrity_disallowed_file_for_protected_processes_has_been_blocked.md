---
sigma_id: "5daf11c3-022b-4969-adb9-365e6c078c7c"
title: "CodeIntegrity - Disallowed File For Protected Processes Has Been Blocked"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/code_integrity/win_codeintegrity_blocked_protected_process_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_blocked_protected_process_file.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / codeintegrity-operational"
aliases:
  - "5daf11c3-022b-4969-adb9-365e6c078c7c"
  - "CodeIntegrity - Disallowed File For Protected Processes Has Been Blocked"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects block events for files that are disallowed by code integrity for protected processes

## Logsource

- product: windows
- service: codeintegrity-operational

## Detection

```yaml
selection:
  EventID: 3104
condition: selection
```

## False Positives

- Unlikely

## References

- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-id-explanations
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/operations/event-tag-explanations
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/code_integrity/win_codeintegrity_blocked_protected_process_file.yml)
