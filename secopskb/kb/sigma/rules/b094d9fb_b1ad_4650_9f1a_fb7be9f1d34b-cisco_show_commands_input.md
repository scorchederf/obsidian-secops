---
sigma_id: "b094d9fb-b1ad-4650-9f1a-fb7be9f1d34b"
title: "Cisco Show Commands Input"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_input_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_input_capture.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "cisco / aaa"
aliases:
  - "b094d9fb-b1ad-4650-9f1a-fb7be9f1d34b"
  - "Cisco Show Commands Input"
attack_technique_ids:
  - "T1552.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco Show Commands Input

See what commands are being input into the device by other people, full credentials can be in the history

## Metadata

- Rule ID: b094d9fb-b1ad-4650-9f1a-fb7be9f1d34b
- Status: test
- Level: medium
- Author: Austin Clark
- Date: 2019-08-11
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_input_capture.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.003]]

## Detection

```yaml
keywords:
- show history
- show history all
- show logging
condition: keywords
```

## False Positives

- Not commonly run by administrators, especially if remote logging is configured

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_input_capture.yml)
