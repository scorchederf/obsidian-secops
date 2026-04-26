---
sigma_id: "1cb0c6ce-3d00-44fc-ab9c-6d6d577bf20b"
title: "DNS Query To Devtunnels Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_devtunnels_communication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "1cb0c6ce-3d00-44fc-ab9c-6d6d577bf20b"
  - "DNS Query To Devtunnels Domain"
attack_technique_ids:
  - "T1071.001"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query To Devtunnels Domain

Detects DNS query requests to Devtunnels domains. Attackers can abuse that feature to establish a reverse shell or persistence on a machine.

## Metadata

- Rule ID: 1cb0c6ce-3d00-44fc-ab9c-6d6d577bf20b
- Status: test
- Level: medium
- Author: citron_ninja
- Date: 2023-10-25
- Modified: 2023-11-20
- Source Path: rules/windows/dns_query/dns_query_win_devtunnels_communication.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection:
  QueryName|endswith: .devtunnels.ms
condition: selection
```

## False Positives

- Legitimate use of Devtunnels will also trigger this.

## References

- https://blueteamops.medium.com/detecting-dev-tunnels-16f0994dc3e2
- https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/security
- https://cydefops.com/devtunnels-unleashed

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_devtunnels_communication.yml)
