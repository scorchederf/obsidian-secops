---
atomic_guid: "0940a971-809a-48f1-9c4d-b1d785e96ee5"
title: "System Network Connections Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1049"
attack_technique_name: "System Network Connections Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "0940a971-809a-48f1-9c4d-b1d785e96ee5"
  - "System Network Connections Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Get a listing of network connections.

Upon successful execution, cmd.exe will execute `netstat`, `net use` and `net sessions`. `net sessions` requires
elevated privileges; on standard user accounts this command may not return results. Results will output via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
netstat -ano
net use
net sessions 2>nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1049/T1049.yaml)
