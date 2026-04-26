---
sigma_id: "56fda488-113e-4ce9-8076-afc2457922c3"
title: "Possible DCSync Attack"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_dcsync_attack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_dcsync_attack.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "56fda488-113e-4ce9-8076-afc2457922c3"
  - "Possible DCSync Attack"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Possible DCSync Attack

Detects remote RPC calls to MS-DRSR from non DC hosts, which could indicate DCSync / DCShadow attacks.

## Metadata

- Rule ID: 56fda488-113e-4ce9-8076-afc2457922c3
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_dcsync_attack.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes, enable DRSR UUID (e3514235-4b06-11d1-ab04-00c04fc2dcd2) for "dangerous" opcodes (not 0,1 or 12) only from trusted IPs (DCs)
- product: rpc_firewall

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: e3514235-4b06-11d1-ab04-00c04fc2dcd2
filter:
  OpNum:
  - 0
  - 1
  - 12
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-drsr/f977faaa-673e-4f66-b9bf-48c640241d47?redirectedfrom=MSDN
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-DRSR.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_dcsync_attack.yml)
