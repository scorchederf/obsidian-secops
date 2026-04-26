---
sigma_id: "d22df9cd-2aee-4089-93c7-9dc4eae77f2c"
title: "ISATAP Router Address Was Set"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_Iphlpsvc/win_system_isatap_router_address_set.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_Iphlpsvc/win_system_isatap_router_address_set.yml"
build_date: "2026-04-26 14:14:27"
status: "experimental"
level: "medium"
logsource: "windows / system"
aliases:
  - "d22df9cd-2aee-4089-93c7-9dc4eae77f2c"
  - "ISATAP Router Address Was Set"
attack_technique_ids:
  - "T1557"
  - "T1565.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ISATAP Router Address Was Set

Detects the configuration of a new ISATAP router on a Windows host. While ISATAP is a legitimate Microsoft technology for IPv6 transition, unexpected or unauthorized ISATAP router configurations could indicate a potential IPv6 DNS Takeover attack using tools like mitm6.
In such attacks, adversaries advertise themselves as DHCPv6 servers and set malicious ISATAP routers to intercept traffic.
This detection should be correlated with network baselines and known legitimate ISATAP deployments in your environment.

## Metadata

- Rule ID: d22df9cd-2aee-4089-93c7-9dc4eae77f2c
- Status: experimental
- Level: medium
- Author: hamid
- Date: 2025-10-19
- Source Path: rules/windows/builtin/system/microsoft_windows_Iphlpsvc/win_system_isatap_router_address_set.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557]]
- [[kb/attack/techniques/T1565-data_manipulation|T1565.002]]

## Detection

```yaml
selection:
  EventID: 4100
  Provider_Name: Microsoft-Windows-Iphlpsvc
filter_main_localhost:
  IsatapRouter:
  - 127.0.0.1
  - ::1
filter_optional_null:
  IsatapRouter: null
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate ISATAP router configuration in enterprise environments
- IPv6 transition projects and network infrastructure changes
- Network administrators configuring dual-stack networking
- Automatic ISATAP configuration in some Windows deployments

## References

- https://www.blackhillsinfosec.com/mitm6-strikes-again-the-dark-side-of-ipv6/
- https://redfoxsec.com/blog/ipv6-dns-takeover/
- https://www.securityhq.com/blog/malicious-isatap-tunneling-unearthed-on-windows-server/
- https://medium.com/@ninnesoturan/detecting-ipv6-dns-takeover-a54a6a88be1f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_Iphlpsvc/win_system_isatap_router_address_set.yml)
