---
sigma_id: "0fcd1c79-4eeb-4746-aba9-1b458f7a79cb"
title: "Remote Schedule Task Lateral Movement via ATSvc"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_atsvc_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_atsvc_lateral_movement.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "0fcd1c79-4eeb-4746-aba9-1b458f7a79cb"
  - "Remote Schedule Task Lateral Movement via ATSvc"
attack_technique_ids:
  - "T1053"
  - "T1053.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote Schedule Task Lateral Movement via ATSvc

Detects remote RPC calls to create or execute a scheduled task via ATSvc

## Metadata

- Rule ID: 0fcd1c79-4eeb-4746-aba9-1b458f7a79cb
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_atsvc_lateral_movement.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:1ff70682-0a51-30e8-076d-740be8cee98b"
- product: rpc_firewall

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 1ff70682-0a51-30e8-076d-740be8cee98b
  OpNum:
  - 0
  - 1
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/d1058a28-7e02-4948-8b8d-4a347fa64931
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-TSCH.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_atsvc_lateral_movement.yml)
