---
sigma_id: "9e8f6035-88bf-4a63-96b6-b17c0508257e"
title: "Cisco Disabling Logging"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_disable_logging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_disable_logging.yml"
build_date: "2026-04-27 19:13:50"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Turn off logging locally or remote

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

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
