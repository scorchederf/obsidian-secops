---
sigma_id: "d94a35f0-7a29-45f6-90a0-80df6159967c"
title: "Cisco Denial of Service"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_dos.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_dos.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "cisco / aaa"
aliases:
  - "d94a35f0-7a29-45f6-90a0-80df6159967c"
  - "Cisco Denial of Service"
attack_technique_ids:
  - "T1495"
  - "T1529"
  - "T1565.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco Denial of Service

Detect a system being shutdown or put into different boot mode

## Metadata

- Rule ID: d94a35f0-7a29-45f6-90a0-80df6159967c
- Status: test
- Level: medium
- Author: Austin Clark
- Date: 2019-08-15
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_dos.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1495-firmware_corruption|T1495]]
- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]
- [[kb/attack/techniques/T1565-data_manipulation|T1565.001]]

## Detection

```yaml
keywords:
- shutdown
- config-register 0x2100
- config-register 0x2142
condition: keywords
```

## False Positives

- Legitimate administrators may run these commands, though rarely.

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_dos.yml)
