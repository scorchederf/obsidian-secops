---
sigma_id: "49f5dfc1-f92e-4d34-96fa-feba3f6acf36"
title: "Disabling Security Tools - Builtin"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/syslog/lnx_syslog_security_tools_disabling_syslog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/syslog/lnx_syslog_security_tools_disabling_syslog.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / syslog"
aliases:
  - "49f5dfc1-f92e-4d34-96fa-feba3f6acf36"
  - "Disabling Security Tools - Builtin"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disabling Security Tools - Builtin

Detects disabling security tools

## Metadata

- Rule ID: 49f5dfc1-f92e-4d34-96fa-feba3f6acf36
- Status: test
- Level: medium
- Author: Ömer Günal, Alejandro Ortuno, oscd.community
- Date: 2020-06-17
- Modified: 2022-11-26
- Source Path: rules/linux/builtin/syslog/lnx_syslog_security_tools_disabling_syslog.yml

## Logsource

- product: linux
- service: syslog

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
keywords:
- stopping iptables
- stopping ip6tables
- stopping firewalld
- stopping cbdaemon
- stopping falcon-sensor
condition: keywords
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/syslog/lnx_syslog_security_tools_disabling_syslog.yml)
