---
sigma_id: "e80273e1-9faf-40bc-bd85-dbaff104c4e9"
title: "ESXi System Information Discovery Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_system_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_system_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "e80273e1-9faf-40bc-bd85-dbaff104c4e9"
  - "ESXi System Information Discovery Via ESXCLI"
attack_technique_ids:
  - "T1033"
  - "T1007"
  - "T1059.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ESXi System Information Discovery Via ESXCLI

Detects execution of the "esxcli" command with the "system" flag in order to retrieve information about the different component of the system. Such as accounts, modules, NTP, etc.

## Metadata

- Rule ID: e80273e1-9faf-40bc-bd85-dbaff104c4e9
- Status: test
- Level: medium
- Author: Cedric Maurugeon
- Date: 2023-09-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_system_discovery.yml

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
  CommandLine|contains: system
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
- https://developer.broadcom.com/xapis/esxcli-command-reference/7.0.0/namespace/esxcli_system.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_system_discovery.yml)
