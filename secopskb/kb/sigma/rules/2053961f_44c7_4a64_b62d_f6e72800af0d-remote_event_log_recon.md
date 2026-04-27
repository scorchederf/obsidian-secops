---
sigma_id: "2053961f-44c7-4a64-b62d-f6e72800af0d"
title: "Remote Event Log Recon"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_eventlog_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_eventlog_recon.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "2053961f-44c7-4a64-b62d-f6e72800af0d"
  - "Remote Event Log Recon"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote RPC calls to get event log information via EVEN or EVEN6

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:82273fdc-e32a-18c3-3f78-827929dc23ea and uuid:f6beaff7-1e19-4fbb-9f8f-b89e2018337c"
- product: rpc_firewall

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid:
  - 82273fdc-e32a-18c3-3f78-827929dc23ea
  - f6beaff7-1e19-4fbb-9f8f-b89e2018337c
condition: selection
```

## False Positives

- Remote administrative tasks on Windows Events

## References

- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_eventlog_recon.yml)
