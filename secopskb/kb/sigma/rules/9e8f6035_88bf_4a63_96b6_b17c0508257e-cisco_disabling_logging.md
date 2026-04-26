---
sigma_id: "9e8f6035-88bf-4a63-96b6-b17c0508257e"
title: "Cisco Disabling Logging"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_disable_logging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_disable_logging.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "cisco / aaa"
aliases:
  - "9e8f6035-88bf-4a63-96b6-b17c0508257e"
  - "Cisco Disabling Logging"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cisco Disabling Logging

Turn off logging locally or remote

## Metadata

- Rule ID: 9e8f6035-88bf-4a63-96b6-b17c0508257e
- Status: test
- Level: high
- Author: Austin Clark
- Date: 2019-08-11
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_disable_logging.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
keywords:
- no logging
- no aaa new-model
condition: keywords
```

## False Positives

- Unknown

## References

- https://www.cisco.com/en/US/docs/ios/security/command/reference/sec_a2.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_disable_logging.yml)
