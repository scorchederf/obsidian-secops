---
sigma_id: "53389db6-ba46-48e3-a94c-e0f2cefe1583"
title: "MITRE BZAR Indicators for Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dce_rpc_mitre_bzar_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_mitre_bzar_persistence.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "zeek / dce_rpc"
aliases:
  - "53389db6-ba46-48e3-a94c-e0f2cefe1583"
  - "MITRE BZAR Indicators for Persistence"
attack_technique_ids:
  - "T1547.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MITRE BZAR Indicators for Persistence

Windows DCE-RPC functions which indicate a persistence techniques on the remote system. All credit for the Zeek mapping of the suspicious endpoint/operation field goes to MITRE.

## Metadata

- Rule ID: 53389db6-ba46-48e3-a94c-e0f2cefe1583
- Status: test
- Level: medium
- Author: @neu5ron, SOC Prime
- Date: 2020-03-19
- Modified: 2021-11-27
- Source Path: rules/network/zeek/zeek_dce_rpc_mitre_bzar_persistence.yml

## Logsource

- product: zeek
- service: dce_rpc

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.004]]

## Detection

```yaml
op1:
  endpoint: spoolss
  operation: RpcAddMonitor
op2:
  endpoint: spoolss
  operation: RpcAddPrintProcessor
op3:
  endpoint: IRemoteWinspool
  operation: RpcAsyncAddMonitor
op4:
  endpoint: IRemoteWinspool
  operation: RpcAsyncAddPrintProcessor
op5:
  endpoint: ISecLogon
  operation: SeclCreateProcessWithLogonW
op6:
  endpoint: ISecLogon
  operation: SeclCreateProcessWithLogonExW
condition: 1 of op*
```

## False Positives

- Windows administrator tasks or troubleshooting
- Windows management scripts or software

## References

- https://github.com/mitre-attack/bzar#indicators-for-attck-persistence

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_mitre_bzar_persistence.yml)
