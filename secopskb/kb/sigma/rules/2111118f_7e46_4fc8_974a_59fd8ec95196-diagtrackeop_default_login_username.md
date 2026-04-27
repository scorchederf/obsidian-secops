---
sigma_id: "2111118f-7e46-4fc8-974a-59fd8ec95196"
title: "DiagTrackEoP Default Login Username"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_diagtrack_eop_default_login_username.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_diagtrack_eop_default_login_username.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "critical"
logsource: "windows / security"
aliases:
  - "2111118f-7e46-4fc8-974a-59fd8ec95196"
  - "DiagTrackEoP Default Login Username"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the default "UserName" used by the DiagTrackEoP POC

## Logsource

- product: windows
- service: security

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 9
  TargetOutboundUserName: thisisnotvaliduser
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/Wh04m1001/DiagTrackEoP/blob/3a2fc99c9700623eb7dc7d4b5f314fd9ce5ef51f/main.cpp#L46

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_diagtrack_eop_default_login_username.yml)
