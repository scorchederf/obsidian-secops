---
atomic_guid: "34557863-344a-468f-808b-a1bfb89b4fa9"
title: "DNS Server Discovery Using nslookup"
framework: "atomic"
generated: "true"
attack_technique_id: "T1016"
attack_technique_name: "System Network Configuration Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "34557863-344a-468f-808b-a1bfb89b4fa9"
  - "DNS Server Discovery Using nslookup"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DNS Server Discovery Using nslookup

Identify System domain dns controller on an endpoint using nslookup ldap query. This tool is being abused by qakbot malware to gather information on the domain
controller of the targeted or compromised host. reference https://securelist.com/qakbot-technical-analysis/103931/

## Metadata

- Atomic GUID: 34557863-344a-468f-808b-a1bfb89b4fa9
- Technique: T1016: System Network Configuration Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1016/T1016.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Executor

- name: command_prompt

### Command

```commandprompt
nslookup -querytype=ALL -timeout=12 _ldap._tcp.dc._msdcs.%USERDNSDOMAIN%
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1016/T1016.yaml)
