---
sigma_id: "1fc0809e-06bf-4de3-ad52-25e5263b7623"
title: "Publicly Accessible RDP Service"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_rdp_public_listener.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_rdp_public_listener.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "zeek / rdp"
aliases:
  - "1fc0809e-06bf-4de3-ad52-25e5263b7623"
  - "Publicly Accessible RDP Service"
attack_technique_ids:
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects connections from routable IPs to an RDP listener. Which is indicative of a publicly-accessible RDP service.

## Logsource

- product: zeek
- service: rdp

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]

## Detection

```yaml
selection:
  id.orig_h|cidr:
  - ::1/128
  - 10.0.0.0/8
  - 127.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 169.254.0.0/16
  - 2620:83:8000::/48
  - fc00::/7
  - fe80::/10
condition: not selection
```

## False Positives

- Although it is recommended to NOT have RDP exposed to the internet, verify that this is a) allowed b) the server has not already been compromised via some brute force or remote exploit since it has been exposed to the internet. Work to secure the server if you are unable to remove it from being exposed to the internet.

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_rdp_public_listener.yml)
