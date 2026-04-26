---
sigma_id: "3761e026-f259-44e6-8826-719ed8079408"
title: "Linux Network Service Scanning - Auditd"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_network_service_scanning.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_network_service_scanning.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "3761e026-f259-44e6-8826-719ed8079408"
  - "Linux Network Service Scanning - Auditd"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Network Service Scanning - Auditd

Detects enumeration of local or remote network services.

## Metadata

- Rule ID: 3761e026-f259-44e6-8826-719ed8079408
- Status: test
- Level: low
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-21
- Modified: 2023-09-26
- Source Path: rules/linux/auditd/syscall/lnx_auditd_network_service_scanning.yml

## Logsource

- definition: Configure these rules https://github.com/Neo23x0/auditd/blob/e181243a7c708e9d579557d6f80e0ed3d3483b89/audit.rules#L182-L183
- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
  type: SYSCALL
  exe|endswith:
  - /telnet
  - /nmap
  - /netcat
  - /nc
  - /ncat
  - /nc.openbsd
  key: network_connect_4
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1046/T1046.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_network_service_scanning.yml)
