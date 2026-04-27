---
atomic_guid: "038263cb-00f4-4b0a-98ae-0696c67e1752"
title: "List Windows Firewall Rules"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "038263cb-00f4-4b0a-98ae-0696c67e1752"
  - "List Windows Firewall Rules"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerates Windows Firewall Rules using netsh.

Upon successful execution, cmd.exe will spawn netsh.exe to list firewall rules. Output will be via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
netsh advfirewall firewall show rule name=all
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
