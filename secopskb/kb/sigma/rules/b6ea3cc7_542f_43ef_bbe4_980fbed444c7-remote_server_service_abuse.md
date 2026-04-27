---
sigma_id: "b6ea3cc7-542f-43ef-bbe4-980fbed444c7"
title: "Remote Server Service Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_remote_server_service_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_server_service_abuse.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "b6ea3cc7-542f-43ef-bbe4-980fbed444c7"
  - "Remote Server Service Abuse"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote RPC calls to possibly abuse remote encryption service via MS-SRVS

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:4b324fc8-1670-01d3-1278-5a47bf6ee188
- product: rpc_firewall

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 4b324fc8-1670-01d3-1278-5a47bf6ee188
condition: selection
```

## False Positives

- Legitimate remote share creation

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-srvs/accf23b0-0f57-441c-9185-43041f1b0ee9
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-SRVS.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_server_service_abuse.yml)
