---
sigma_id: "10018e73-06ec-46ec-8107-9172f1e04ff2"
title: "Remote Server Service Abuse for Lateral Movement"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_remote_service_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_service_lateral_movement.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "10018e73-06ec-46ec-8107-9172f1e04ff2"
  - "Remote Server Service Abuse for Lateral Movement"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Server Service Abuse for Lateral Movement

Detects remote RPC calls to possibly abuse remote encryption service via MS-EFSR

## Metadata

- Rule ID: 10018e73-06ec-46ec-8107-9172f1e04ff2
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_remote_service_lateral_movement.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:367abb81-9844-35f1-ad32-98f038001003
- product: rpc_firewall

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 367abb81-9844-35f1-ad32-98f038001003
condition: selection
```

## False Positives

- Administrative tasks on remote services

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-srvs/accf23b0-0f57-441c-9185-43041f1b0ee9
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-SCMR.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_service_lateral_movement.yml)
