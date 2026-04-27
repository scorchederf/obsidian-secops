---
sigma_id: "51e33403-2a37-4d66-a574-1fda1782cc31"
title: "RDP Login from Localhost"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_rdp_localhost_login.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_rdp_localhost_login.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "51e33403-2a37-4d66-a574-1fda1782cc31"
  - "RDP Login from Localhost"
attack_technique_ids:
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

RDP login with localhost source address may be a tunnelled login

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Detection

```yaml
selection:
  EventID: 4624
  LogonType: 10
  IpAddress:
  - ::1
  - 127.0.0.1
condition: selection
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2019/01/bypassing-network-restrictions-through-rdp-tunneling.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_rdp_localhost_login.yml)
