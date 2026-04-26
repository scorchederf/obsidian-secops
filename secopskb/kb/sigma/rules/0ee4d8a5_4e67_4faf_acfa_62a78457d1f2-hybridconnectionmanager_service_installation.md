---
sigma_id: "0ee4d8a5-4e67-4faf-acfa-62a78457d1f2"
title: "HybridConnectionManager Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_hybridconnectionmgr_svc_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hybridconnectionmgr_svc_installation.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "0ee4d8a5-4e67-4faf-acfa-62a78457d1f2"
  - "HybridConnectionManager Service Installation"
attack_technique_ids:
  - "T1554"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HybridConnectionManager Service Installation

Rule to detect the Hybrid Connection Manager service installation.

## Metadata

- Rule ID: 0ee4d8a5-4e67-4faf-acfa-62a78457d1f2
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2021-04-12
- Modified: 2022-10-09
- Source Path: rules/windows/builtin/security/win_security_hybridconnectionmgr_svc_installation.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1554-compromise_host_software_binary|T1554]]

## Detection

```yaml
selection:
  EventID: 4697
  ServiceName: HybridConnectionManager
  ServiceFileName|contains: HybridConnectionManager
condition: selection
```

## False Positives

- Legitimate use of Hybrid Connection Manager via Azure function apps.

## References

- https://twitter.com/Cyb3rWard0g/status/1381642789369286662

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hybridconnectionmgr_svc_installation.yml)
