---
sigma_id: "65f77b1e-8e79-45bf-bb67-5988a8ce45a5"
title: "SharpHound Recon Account Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_sharphound_recon_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_sharphound_recon_account.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "65f77b1e-8e79-45bf-bb67-5988a8ce45a5"
  - "SharpHound Recon Account Discovery"
attack_technique_ids:
  - "T1087"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote RPC calls useb by SharpHound to map remote connections and local group membership.

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:6bffd098-a112-3610-9833-46c3f87e345a opnum:2
- product: rpc_firewall

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087: Account Discovery]]

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 6bffd098-a112-3610-9833-46c3f87e345a
  OpNum: 2
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wkst/55118c55-2122-4ef9-8664-0c1ff9e168f3
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-WKST.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_sharphound_recon_account.yml)
