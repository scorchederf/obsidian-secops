---
sigma_id: "5e51acb2-bcbe-435b-99c6-0e3cd5e2aa59"
title: "Cisco Stage Data"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_moving_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_moving_data.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "cisco / aaa"
aliases:
  - "5e51acb2-bcbe-435b-99c6-0e3cd5e2aa59"
  - "Cisco Stage Data"
attack_technique_ids:
  - "T1074"
  - "T1105"
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco Stage Data

Various protocols maybe used to put data on the device for exfil or infil

## Metadata

- Rule ID: 5e51acb2-bcbe-435b-99c6-0e3cd5e2aa59
- Status: test
- Level: low
- Author: Austin Clark
- Date: 2019-08-12
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_moving_data.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1074-data_staged|T1074]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
keywords:
- tftp
- rcp
- puts
- copy
- configure replace
- archive tar
condition: keywords
```

## False Positives

- Generally used to copy configs or IOS images

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_moving_data.yml)
