---
sigma_id: "18b042f0-2ecd-4b6e-9f8d-aa7a7e7de781"
title: "Buffer Overflow Attempts"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_buffer_overflows.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_buffer_overflows.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "18b042f0-2ecd-4b6e-9f8d-aa7a7e7de781"
  - "Buffer Overflow Attempts"
attack_technique_ids:
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Buffer Overflow Attempts

Detects buffer overflow attempts in Unix system log files

## Metadata

- Rule ID: 18b042f0-2ecd-4b6e-9f8d-aa7a7e7de781
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-01
- Modified: 2025-03-17
- Source Path: rules/linux/builtin/lnx_buffer_overflows.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

## Detection

```yaml
keywords:
- attempt to execute code on stack by
- 0bin0sh1
- AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
- stack smashing detected
condition: keywords
```

## False Positives

- Base64 encoded data in log entries

## References

- https://github.com/ossec/ossec-hids/blob/1ecffb1b884607cb12e619f9ab3c04f530801083/etc/rules/attack_rules.xml
- https://docs.oracle.com/cd/E19683-01/816-4883/6mb2joatd/index.html
- https://www.giac.org/paper/gcih/266/review-ftp-protocol-cyber-defense-initiative/102802
- https://blu.org/mhonarc/discuss/2001/04/msg00285.php
- https://rapid7.com/blog/post/2019/02/19/stack-based-buffer-overflow-attacks-what-you-need-to-know/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_buffer_overflows.yml)
