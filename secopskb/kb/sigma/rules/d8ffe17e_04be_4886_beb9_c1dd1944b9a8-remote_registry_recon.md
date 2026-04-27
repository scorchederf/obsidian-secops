---
sigma_id: "d8ffe17e-04be-4886-beb9-c1dd1944b9a8"
title: "Remote Registry Recon"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_remote_registry_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_registry_recon.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "d8ffe17e-04be-4886-beb9-c1dd1944b9a8"
  - "Remote Registry Recon"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote RPC calls to collect information

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:338cd001-2244-31f1-aaaa-900038001003"
- product: rpc_firewall

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 338cd001-2244-31f1-aaaa-900038001003
filter:
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
condition: selection and not filter
```

## False Positives

- Remote administration of registry values

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/0fa3191d-bb79-490a-81bd-54c2601b7a78
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-RRP.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_registry_recon.yml)
