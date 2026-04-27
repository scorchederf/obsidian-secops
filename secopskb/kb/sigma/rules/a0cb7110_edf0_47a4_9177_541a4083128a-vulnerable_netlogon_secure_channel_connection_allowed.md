---
sigma_id: "a0cb7110-edf0-47a4-9177-541a4083128a"
title: "Vulnerable Netlogon Secure Channel Connection Allowed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/netlogon/win_system_vul_cve_2020_1472.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/netlogon/win_system_vul_cve_2020_1472.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "a0cb7110-edf0-47a4-9177-541a4083128a"
  - "Vulnerable Netlogon Secure Channel Connection Allowed"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects that a vulnerable Netlogon secure channel connection was allowed, which could be an indicator of CVE-2020-1472.

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]

## Detection

```yaml
selection:
  Provider_Name: NetLogon
  EventID: 5829
condition: selection
```

## False Positives

- Unknown

## References

- https://support.microsoft.com/en-us/help/4557222/how-to-manage-the-changes-in-netlogon-secure-channel-connections-assoc

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/netlogon/win_system_vul_cve_2020_1472.yml)
