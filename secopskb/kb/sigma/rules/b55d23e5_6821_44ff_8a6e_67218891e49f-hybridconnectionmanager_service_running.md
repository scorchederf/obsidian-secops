---
sigma_id: "b55d23e5-6821-44ff-8a6e-67218891e49f"
title: "HybridConnectionManager Service Running"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/servicebus/win_hybridconnectionmgr_svc_running.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/servicebus/win_hybridconnectionmgr_svc_running.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / microsoft-servicebus-client"
aliases:
  - "b55d23e5-6821-44ff-8a6e-67218891e49f"
  - "HybridConnectionManager Service Running"
attack_technique_ids:
  - "T1554"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HybridConnectionManager Service Running

Rule to detect the Hybrid Connection Manager service running on an endpoint.

## Metadata

- Rule ID: b55d23e5-6821-44ff-8a6e-67218891e49f
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2021-04-12
- Modified: 2024-08-05
- Source Path: rules/windows/builtin/servicebus/win_hybridconnectionmgr_svc_running.yml

## Logsource

- product: windows
- service: microsoft-servicebus-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1554-compromise_host_software_binary|T1554]]

## Detection

```yaml
selection:
  EventID:
  - 40300
  - 40301
  - 40302
keywords:
- HybridConnection
- sb://
- servicebus.windows.net
- HybridConnectionManage
condition: selection and keywords
```

## False Positives

- Legitimate use of Hybrid Connection Manager via Azure function apps.

## References

- https://twitter.com/Cyb3rWard0g/status/1381642789369286662

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/servicebus/win_hybridconnectionmgr_svc_running.yml)
