---
sigma_id: "c8e35e96-19ce-4f16-aeb6-fd5588dc5365"
title: "Suspicious Named Error"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/syslog/lnx_syslog_susp_named.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/syslog/lnx_syslog_susp_named.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "linux / syslog"
aliases:
  - "c8e35e96-19ce-4f16-aeb6-fd5588dc5365"
  - "Suspicious Named Error"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Named Error

Detects suspicious DNS error messages that indicate a fatal or suspicious error that could be caused by exploiting attempts

## Metadata

- Rule ID: c8e35e96-19ce-4f16-aeb6-fd5588dc5365
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2018-02-20
- Modified: 2022-10-05
- Source Path: rules/linux/builtin/syslog/lnx_syslog_susp_named.yml

## Logsource

- product: linux
- service: syslog

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
keywords:
- ' dropping source port zero packet from '
- ' denied AXFR from '
- ' exiting (due to fatal error)'
condition: keywords
```

## False Positives

- Unknown

## References

- https://github.com/ossec/ossec-hids/blob/1ecffb1b884607cb12e619f9ab3c04f530801083/etc/rules/named_rules.xml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/syslog/lnx_syslog_susp_named.yml)
