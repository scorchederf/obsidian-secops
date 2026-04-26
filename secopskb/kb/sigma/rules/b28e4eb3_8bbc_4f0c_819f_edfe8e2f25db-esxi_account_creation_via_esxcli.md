---
sigma_id: "b28e4eb3-8bbc-4f0c-819f-edfe8e2f25db"
title: "ESXi Account Creation Via ESXCLI"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_esxcli_user_account_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_user_account_creation.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "b28e4eb3-8bbc-4f0c-819f-edfe8e2f25db"
  - "ESXi Account Creation Via ESXCLI"
attack_technique_ids:
  - "T1136"
  - "T1059.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ESXi Account Creation Via ESXCLI

Detects user account creation on ESXi system via esxcli

## Metadata

- Rule ID: b28e4eb3-8bbc-4f0c-819f-edfe8e2f25db
- Status: test
- Level: medium
- Author: Cedric Maurugeon
- Date: 2023-08-22
- Source Path: rules/linux/process_creation/proc_creation_lnx_esxcli_user_account_creation.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.012]]

## Detection

```yaml
selection:
  Image|endswith: /esxcli
  CommandLine|contains|all:
  - 'system '
  - 'account '
  - 'add '
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://developer.broadcom.com/xapis/esxcli-command-reference/7.0.0/namespace/esxcli_system.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_esxcli_user_account_creation.yml)
