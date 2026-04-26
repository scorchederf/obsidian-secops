---
sigma_id: "f64b6e9a-5d9d-48a5-8289-e1dd2b3876e1"
title: "Suspicious Log Entries"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_shell_susp_log_entries.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shell_susp_log_entries.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux"
aliases:
  - "f64b6e9a-5d9d-48a5-8289-e1dd2b3876e1"
  - "Suspicious Log Entries"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Log Entries

Detects suspicious log entries in Linux log files

## Metadata

- Rule ID: f64b6e9a-5d9d-48a5-8289-e1dd2b3876e1
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-25
- Modified: 2021-11-27
- Source Path: rules/linux/builtin/lnx_shell_susp_log_entries.yml

## Logsource

- product: linux

## Detection

```yaml
keywords:
- entered promiscuous mode
- Deactivating service
- Oversized packet received from
- imuxsock begins to drop messages
condition: keywords
```

## False Positives

- Unknown

## References

- https://github.com/ossec/ossec-hids/blob/f6502012b7380208db81f82311ad4a1994d39905/etc/rules/syslog_rules.xml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shell_susp_log_entries.yml)
