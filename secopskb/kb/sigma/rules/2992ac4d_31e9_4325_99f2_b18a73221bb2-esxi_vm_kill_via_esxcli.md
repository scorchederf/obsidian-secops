---
sigma_id: "2992ac4d-31e9-4325-99f2-b18a73221bb2"
title: "ESXi VM Kill Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_vm_kill.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_vm_kill.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "2992ac4d-31e9-4325-99f2-b18a73221bb2"
  - "ESXi VM Kill Via ESXCLI"
attack_technique_ids:
  - "T1059.012"
  - "T1529"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ESXi VM Kill Via ESXCLI

Detects execution of the "esxcli" command with the "vm" and "kill" flag in order to kill/shutdown a specific VM.

## Metadata

- Rule ID: 2992ac4d-31e9-4325-99f2-b18a73221bb2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Cedric Maurugeon
- Date: 2023-09-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_vm_kill.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.012]]
- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Detection

```yaml
selection:
  Image|endswith: /esxcli
  CommandLine|contains|all:
  - vm process
  - kill
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_vm_kill.yml)
