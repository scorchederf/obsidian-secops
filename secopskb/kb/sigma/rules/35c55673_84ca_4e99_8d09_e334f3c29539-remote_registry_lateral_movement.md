---
sigma_id: "35c55673-84ca-4e99-8d09-e334f3c29539"
title: "Remote Registry Lateral Movement"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_remote_registry_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_registry_lateral_movement.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "35c55673-84ca-4e99-8d09-e334f3c29539"
  - "Remote Registry Lateral Movement"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote Registry Lateral Movement

Detects remote RPC calls to modify the registry and possible execute code

## Metadata

- Rule ID: 35c55673-84ca-4e99-8d09-e334f3c29539
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_remote_registry_lateral_movement.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:338cd001-2244-31f1-aaaa-900038001003"
- product: rpc_firewall

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 338cd001-2244-31f1-aaaa-900038001003
  OpNum:
  - 6
  - 7
  - 8
  - 13
  - 18
  - 19
  - 21
  - 22
  - 23
  - 35
condition: selection
```

## False Positives

- Remote administration of registry values

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/0fa3191d-bb79-490a-81bd-54c2601b7a78
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-RRP.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_registry_lateral_movement.yml)
