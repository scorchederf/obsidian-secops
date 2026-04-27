---
sigma_id: "16f5d8ca-44bd-47c8-acbe-6fc95a16c12f"
title: "RottenPotato Like Attack Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_susp_rottenpotato.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_rottenpotato.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "16f5d8ca-44bd-47c8-acbe-6fc95a16c12f"
  - "RottenPotato Like Attack Pattern"
attack_technique_ids:
  - "T1557.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects logon events that have characteristics of events generated during an attack with RottenPotato and the like

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 3
  TargetUserName: ANONYMOUS LOGON
  WorkstationName: '-'
  IpAddress:
  - 127.0.0.1
  - ::1
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/SBousseaden/status/1195284233729777665

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_rottenpotato.yml)
