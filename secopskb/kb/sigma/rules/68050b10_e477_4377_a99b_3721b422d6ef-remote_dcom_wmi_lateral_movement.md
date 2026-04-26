---
sigma_id: "68050b10-e477-4377-a99b-3721b422d6ef"
title: "Remote DCOM/WMI Lateral Movement"
framework: "sigma"
generated: "true"
source_path: "rules/application/rpc_firewall/rpc_firewall_remote_dcom_or_wmi.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_dcom_or_wmi.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "rpc_firewall / application"
aliases:
  - "68050b10-e477-4377-a99b-3721b422d6ef"
  - "Remote DCOM/WMI Lateral Movement"
attack_technique_ids:
  - "T1021.003"
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote DCOM/WMI Lateral Movement

Detects remote RPC calls that performs remote DCOM operations. These could be abused for lateral movement via DCOM or WMI.

## Metadata

- Rule ID: 68050b10-e477-4377-a99b-3721b422d6ef
- Status: test
- Level: high
- Author: Sagie Dulce, Dekel Paz
- Date: 2022-01-01
- Source Path: rules/application/rpc_firewall/rpc_firewall_remote_dcom_or_wmi.yml

## Logsource

- category: application
- definition: Requirements: install and apply the RPC Firewall to all processes with "audit:true action:block uuid:367abb81-9844-35f1-ad32-98f038001003
- product: rpc_firewall

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.003]]
- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
  EventLog: RPCFW
  EventID: 3
  InterfaceUuid:
  - 4d9f4ab8-7d1c-11cf-861e-0020af6e7c57
  - 99fcfec4-5260-101b-bbcb-00aa0021347a
  - 000001a0-0000-0000-c000-000000000046
  - 00000131-0000-0000-c000-000000000046
  - 00000143-0000-0000-c000-000000000046
  - 00000000-0000-0000-c000-000000000046
condition: selection
```

## False Positives

- Some administrative tasks on remote host

## References

- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-srvs/accf23b0-0f57-441c-9185-43041f1b0ee9
- https://github.com/zeronetworks/rpcfirewall
- https://zeronetworks.com/blog/stopping-lateral-movement-via-the-rpc-firewall/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/rpc_firewall/rpc_firewall_remote_dcom_or_wmi.yml)
