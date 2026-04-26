---
sigma_id: "b640c0b8-87f8-4daa-aef8-95a24261dd1d"
title: "MITRE BZAR Indicators for Execution"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dce_rpc_mitre_bzar_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_mitre_bzar_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "zeek / dce_rpc"
aliases:
  - "b640c0b8-87f8-4daa-aef8-95a24261dd1d"
  - "MITRE BZAR Indicators for Execution"
attack_technique_ids:
  - "T1047"
  - "T1053.002"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MITRE BZAR Indicators for Execution

Windows DCE-RPC functions which indicate an execution techniques on the remote system. All credit for the Zeek mapping of the suspicious endpoint/operation field goes to MITRE

## Metadata

- Rule ID: b640c0b8-87f8-4daa-aef8-95a24261dd1d
- Status: test
- Level: medium
- Author: @neu5ron, SOC Prime
- Date: 2020-03-19
- Modified: 2021-11-27
- Source Path: rules/network/zeek/zeek_dce_rpc_mitre_bzar_execution.yml

## Logsource

- product: zeek
- service: dce_rpc

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
op1:
  endpoint: JobAdd
  operation: atsvc
op2:
  endpoint: ITaskSchedulerService
  operation: SchRpcEnableTask
op3:
  endpoint: ITaskSchedulerService
  operation: SchRpcRegisterTask
op4:
  endpoint: ITaskSchedulerService
  operation: SchRpcRun
op5:
  endpoint: IWbemServices
  operation: ExecMethod
op6:
  endpoint: IWbemServices
  operation: ExecMethodAsync
op7:
  endpoint: svcctl
  operation: CreateServiceA
op8:
  endpoint: svcctl
  operation: CreateServiceW
op9:
  endpoint: svcctl
  operation: StartServiceA
op10:
  endpoint: svcctl
  operation: StartServiceW
condition: 1 of op*
```

## False Positives

- Windows administrator tasks or troubleshooting
- Windows management scripts or software

## References

- https://github.com/mitre-attack/bzar#indicators-for-attck-execution

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dce_rpc_mitre_bzar_execution.yml)
