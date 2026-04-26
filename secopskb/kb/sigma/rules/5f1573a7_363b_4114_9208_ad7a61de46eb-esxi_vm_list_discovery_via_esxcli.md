---
sigma_id: "5f1573a7-363b-4114-9208-ad7a61de46eb"
title: "ESXi VM List Discovery Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_vm_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_vm_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "5f1573a7-363b-4114-9208-ad7a61de46eb"
  - "ESXi VM List Discovery Via ESXCLI"
attack_technique_ids:
  - "T1033"
  - "T1007"
  - "T1059.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ESXi VM List Discovery Via ESXCLI

Detects execution of the "esxcli" command with the "vm" flag in order to retrieve information about the installed VMs.

## Metadata

- Rule ID: 5f1573a7-363b-4114-9208-ad7a61de46eb
- Status: test
- Level: medium
- Author: Cedric Maurugeon
- Date: 2023-09-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_vm_discovery.yml

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
selection:
  Image|endswith: /esxcli
  CommandLine|contains: vm process
  CommandLine|endswith: ' list'
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://www.crowdstrike.com/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/
- https://developer.broadcom.com/xapis/esxcli-command-reference/7.0.0/namespace/esxcli_vm.html
- https://www.secuinfra.com/en/techtalk/hide-your-hypervisor-analysis-of-esxiargs-ransomware/
- https://www.trendmicro.com/en_us/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_vm_discovery.yml)
