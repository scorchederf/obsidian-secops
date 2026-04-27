---
sigma_id: "e97d9903-53b2-41fc-8cb9-889ed4093e80"
title: "KrbRelayUp Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_krbrelayup_service_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_krbrelayup_service_installation.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "e97d9903-53b2-41fc-8cb9-889ed4093e80"
  - "KrbRelayUp Service Installation"
attack_technique_ids:
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects service creation from KrbRelayUp tool used for privilege escalation in Windows domain environments where LDAP signing is not enforced (the default settings)

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]

## Detection

```yaml
selection:
  EventID: 7045
  ServiceName: KrbSCM
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Dec0ne/KrbRelayUp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_krbrelayup_service_installation.yml)
