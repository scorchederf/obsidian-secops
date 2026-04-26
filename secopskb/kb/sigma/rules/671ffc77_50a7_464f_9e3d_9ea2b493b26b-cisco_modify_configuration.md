---
sigma_id: "671ffc77-50a7-464f-9e3d-9ea2b493b26b"
title: "Cisco Modify Configuration"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_modify_config.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_modify_config.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "cisco / aaa"
aliases:
  - "671ffc77-50a7-464f-9e3d-9ea2b493b26b"
  - "Cisco Modify Configuration"
attack_technique_ids:
  - "T1490"
  - "T1505"
  - "T1565.002"
  - "T1053"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco Modify Configuration

Modifications to a config that will serve an adversary's impacts or persistence

## Metadata

- Rule ID: 671ffc77-50a7-464f-9e3d-9ea2b493b26b
- Status: test
- Level: medium
- Author: Austin Clark
- Date: 2019-08-12
- Modified: 2025-04-28
- Source Path: rules/network/cisco/aaa/cisco_cli_modify_config.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]
- [[kb/attack/techniques/T1505-server_software_component|T1505]]
- [[kb/attack/techniques/T1565-data_manipulation|T1565.002]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053]]

## Detection

```yaml
keywords:
- ip http server
- ip https server
- kron policy-list
- kron occurrence
- policy-list
- access-list
- ip access-group
- archive maximum
- ntp server
condition: keywords
```

## False Positives

- Legitimate administrators may run these commands

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_modify_config.yml)
