---
sigma_id: "c830f15d-6f6e-430f-8074-6f73d6807841"
title: "Logging Configuration Changes on Linux Host"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_logging_config_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_logging_config_change.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "c830f15d-6f6e-430f-8074-6f73d6807841"
  - "Logging Configuration Changes on Linux Host"
attack_technique_ids:
  - "T1562.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect changes of syslog daemons configuration files

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]

## Detection

```yaml
selection:
  type: PATH
  name:
  - /etc/syslog.conf
  - /etc/rsyslog.conf
  - /etc/syslog-ng/syslog-ng.conf
condition: selection
```

## False Positives

- Legitimate administrative activity

## References

- self experience

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_logging_config_change.yml)
