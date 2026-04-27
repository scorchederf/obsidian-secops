---
sigma_id: "ace3ff54-e7fd-46bd-8ea0-74b49a0aca1d"
title: "Remote Schedule Task Lateral Movement via ITaskSchedulerService"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_lateral_movement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_lateral_movement.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "ace3ff54-e7fd-46bd-8ea0-74b49a0aca1d"
  - "Remote Schedule Task Lateral Movement via ITaskSchedulerService"
attack_technique_ids:
  - "T1053"
  - "T1053.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote Schedule Task Lateral Movement via ITaskSchedulerService

Detects remote RPC calls to create or execute a scheduled task

## Metadata

- Rule ID: ace3ff54-e7fd-46bd-8ea0-74b49a0aca1d
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_lateral_movement.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:86d35949-83c9-4044-b424-db363231fd0c"
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
  InterfaceUuid: 86d35949-83c9-4044-b424-db363231fd0c
  OpNum:
  - 1
  - 3
  - 4
  - 10
  - 11
  - 12
  - 13
  - 14
  - 15
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_lateral_movement.yml)
