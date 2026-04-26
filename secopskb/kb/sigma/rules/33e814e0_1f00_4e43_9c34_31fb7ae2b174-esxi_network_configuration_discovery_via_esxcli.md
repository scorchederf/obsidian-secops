---
sigma_id: "33e814e0-1f00-4e43-9c34-31fb7ae2b174"
title: "ESXi Network Configuration Discovery Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_network_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_network_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "33e814e0-1f00-4e43-9c34-31fb7ae2b174"
  - "ESXi Network Configuration Discovery Via ESXCLI"
attack_technique_ids:
  - "T1033"
  - "T1007"
  - "T1059.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ESXi Network Configuration Discovery Via ESXCLI

Detects execution of the "esxcli" command with the "network" flag in order to retrieve information about the network configuration.

## Metadata

- Rule ID: 33e814e0-1f00-4e43-9c34-31fb7ae2b174
- Status: test
- Level: medium
- Author: Cedric Maurugeon
- Date: 2023-09-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_network_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]
- [[kb/attack/techniques/T1007-system_service_discovery|T1007]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.012]]

## Detection

```yaml
selection_img:
  Image|endswith: /esxcli
  CommandLine|contains: network
selection_cli:
  CommandLine|contains:
  - ' get'
  - ' list'
condition: all of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://www.crowdstrike.com/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/
- https://developer.broadcom.com/xapis/esxcli-command-reference/7.0.0/namespace/esxcli_network.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_network_discovery.yml)
