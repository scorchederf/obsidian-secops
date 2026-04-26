---
sigma_id: "d54c2f06-aca9-4e2b-81c9-5317858f4b79"
title: "ESXi VSAN Information Discovery Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_vsan_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_vsan_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "d54c2f06-aca9-4e2b-81c9-5317858f4b79"
  - "ESXi VSAN Information Discovery Via ESXCLI"
attack_technique_ids:
  - "T1033"
  - "T1007"
  - "T1059.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ESXi VSAN Information Discovery Via ESXCLI

Detects execution of the "esxcli" command with the "vsan" flag in order to retrieve information about virtual storage. Seen used by malware such as DarkSide.

## Metadata

- Rule ID: d54c2f06-aca9-4e2b-81c9-5317858f4b79
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Cedric Maurugeon
- Date: 2023-09-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_vsan_discovery.yml

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
  CommandLine|contains: vsan
selection_cli:
  CommandLine|contains:
  - ' get'
  - ' list'
condition: all of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://www.trendmicro.com/en_us/research/21/e/darkside-linux-vms-targeted.html
- https://www.trendmicro.com/en_us/research/22/a/analysis-and-Impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant.html
- https://developer.broadcom.com/xapis/esxcli-command-reference/7.0.0/namespace/esxcli_vsan.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_vsan_discovery.yml)
