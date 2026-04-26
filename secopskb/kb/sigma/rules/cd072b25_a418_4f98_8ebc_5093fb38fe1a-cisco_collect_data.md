---
sigma_id: "cd072b25-a418-4f98-8ebc-5093fb38fe1a"
title: "Cisco Collect Data"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_collect_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_collect_data.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "cisco / aaa"
aliases:
  - "cd072b25-a418-4f98-8ebc-5093fb38fe1a"
  - "Cisco Collect Data"
attack_technique_ids:
  - "T1087.001"
  - "T1552.001"
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco Collect Data

Collect pertinent data from the configuration files

## Metadata

- Rule ID: cd072b25-a418-4f98-8ebc-5093fb38fe1a
- Status: test
- Level: low
- Author: Austin Clark
- Date: 2019-08-11
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_collect_data.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]
- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Detection

```yaml
keywords:
- show running-config
- show startup-config
- show archive config
- more
condition: keywords
```

## False Positives

- Commonly run by administrators

## References

- https://blog.router-switch.com/2013/11/show-running-config/
- https://www.cisco.com/E-Learning/bulk/public/tac/cim/cib/using_cisco_ios_software/cmdrefs/show_startup-config.htm
- https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/config-mgmt/configuration/15-sy/config-mgmt-15-sy-book/cm-config-diff.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_collect_data.yml)
