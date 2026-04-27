---
sigma_id: "6d580420-ff3f-4e0e-b6b0-41b90c787e28"
title: "SharpHound Recon Sessions"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_sharphound_recon_sessions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_sharphound_recon_sessions.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "6d580420-ff3f-4e0e-b6b0-41b90c787e28"
  - "SharpHound Recon Sessions"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# SharpHound Recon Sessions

Detects remote RPC calls useb by SharpHound to map remote connections and local group membership.

## Metadata

- Rule ID: 6d580420-ff3f-4e0e-b6b0-41b90c787e28
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_sharphound_recon_sessions.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:4b324fc8-1670-01d3-1278-5a47bf6ee188 opnum:12
- product: rpc_firewall

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 4b324fc8-1670-01d3-1278-5a47bf6ee188
  OpNum: 12
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-srvs/02b1f559-fda2-4ba3-94c2-806eb2777183
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-SRVS.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_sharphound_recon_sessions.yml)
