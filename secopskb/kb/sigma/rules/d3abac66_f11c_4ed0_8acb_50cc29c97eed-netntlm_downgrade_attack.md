---
sigma_id: "d3abac66-f11c-4ed0-8acb-50cc29c97eed"
title: "NetNTLM Downgrade Attack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_net_ntlm_downgrade.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_net_ntlm_downgrade.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "d3abac66-f11c-4ed0-8acb-50cc29c97eed"
  - "NetNTLM Downgrade Attack"
attack_technique_ids:
  - "T1562.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects NetNTLM downgrade attack

## Logsource

- definition: Requirements: Audit Policy : Object Access > Audit Registry (Success)
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]
- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  EventID: 4657
  ObjectName|contains|all:
  - \REGISTRY\MACHINE\SYSTEM
  - ControlSet
  - \Control\Lsa
  ObjectValueName:
  - LmCompatibilityLevel
  - NtlmMinClientSec
  - RestrictSendingNTLMTraffic
condition: selection
```

## False Positives

- Unknown

## References

- https://www.optiv.com/blog/post-exploitation-using-netntlm-downgrade-attacks

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_net_ntlm_downgrade.yml)
