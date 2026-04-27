---
sigma_id: "5f92fff9-82e2-48eb-8fc1-8b133556a551"
title: "Remote Encrypting File System Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_efs_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_efs_abuse.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "5f92fff9-82e2-48eb-8fc1-8b133556a551"
  - "Remote Encrypting File System Abuse"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote Encrypting File System Abuse

Detects remote RPC calls to possibly abuse remote encryption service via MS-EFSR

## Metadata

- Rule ID: 5f92fff9-82e2-48eb-8fc1-8b133556a551
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_efs_abuse.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:df1941c5-fe89-4e79-bf10-463657acf44d or c681d488-d850-11d0-8c52-00c04fd90f7e
- product: rpc_firewall

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid:
  - df1941c5-fe89-4e79-bf10-463657acf44d
  - c681d488-d850-11d0-8c52-00c04fd90f7e
condition: selection
```

## False Positives

- Legitimate usage of remote file encryption

## References

- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36942
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-EFSR.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_efs_abuse.yml)
