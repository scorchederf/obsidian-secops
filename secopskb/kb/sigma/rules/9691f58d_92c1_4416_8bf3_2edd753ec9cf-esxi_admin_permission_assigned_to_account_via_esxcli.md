---
sigma_id: "9691f58d-92c1-4416-8bf3-2edd753ec9cf"
title: "ESXi Admin Permission Assigned To Account Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_permission_change_admin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_permission_change_admin.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "9691f58d-92c1-4416-8bf3-2edd753ec9cf"
  - "ESXi Admin Permission Assigned To Account Via ESXCLI"
attack_technique_ids:
  - "T1059.012"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ESXi Admin Permission Assigned To Account Via ESXCLI

Detects execution of the "esxcli" command with the "system" and "permission" flags in order to assign admin permissions to an account.

## Metadata

- Rule ID: 9691f58d-92c1-4416-8bf3-2edd753ec9cf
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_permission_change_admin.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.012]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  Image|endswith: /esxcli
  CommandLine|contains: system
  CommandLine|contains|all:
  - ' permission '
  - ' set'
  - Admin
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://developer.broadcom.com/xapis/esxcli-command-reference/7.0.0/namespace/esxcli_system.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_permission_change_admin.yml)
