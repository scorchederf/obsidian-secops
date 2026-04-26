---
sigma_id: "7f7c49eb-2977-4ac8-8ab0-ab1bae14730e"
title: "Remote Schedule Task Recon via ITaskSchedulerService"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_recon.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "7f7c49eb-2977-4ac8-8ab0-ab1bae14730e"
  - "Remote Schedule Task Recon via ITaskSchedulerService"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Schedule Task Recon via ITaskSchedulerService

Detects remote RPC calls to read information about scheduled tasks

## Metadata

- Rule ID: 7f7c49eb-2977-4ac8-8ab0-ab1bae14730e
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_recon.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:86d35949-83c9-4044-b424-db363231fd0c"
- product: rpc_firewall

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid: 86d35949-83c9-4044-b424-db363231fd0c
filter:
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
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tsch/d1058a28-7e02-4948-8b8d-4a347fa64931
- https://github.com/jsecurity101/MSRPC-to-ATTACK/blob/ddd4608fe8684fcf2fcf9b48c5f0b3c28097f8a3/documents/MS-TSCH.md
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_itaskschedulerservice_recon.yml)
