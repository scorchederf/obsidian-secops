---
sigma_id: "f177f2bc-5f3e-4453-b599-57eefce9a59c"
title: "Remote Schedule Task Recon via AtScv"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_atsvc_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_atsvc_recon.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "f177f2bc-5f3e-4453-b599-57eefce9a59c"
  - "Remote Schedule Task Recon via AtScv"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote RPC calls to read information about scheduled tasks via AtScv

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:1ff70682-0a51-30e8-076d-740be8cee98b"
- product: rpc_firewall

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 1ff70682-0a51-30e8-076d-740be8cee98b
filter:
  OpNum:
  - 0
  - 1
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/d1058a28-7e02-4948-8b8d-4a347fa64931
- https://github.com/zeronetworks/rpcfirewall
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-TSCH.md
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_atsvc_recon.yml)
