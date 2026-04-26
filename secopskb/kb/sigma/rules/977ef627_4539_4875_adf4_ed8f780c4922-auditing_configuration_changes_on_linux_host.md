---
sigma_id: "977ef627-4539-4875-adf4-ed8f780c4922"
title: "Auditing Configuration Changes on Linux Host"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_auditing_config_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_auditing_config_change.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "977ef627-4539-4875-adf4-ed8f780c4922"
  - "Auditing Configuration Changes on Linux Host"
attack_technique_ids:
  - "T1562.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Auditing Configuration Changes on Linux Host

Detect changes in auditd configuration files

## Metadata

- Rule ID: 977ef627-4539-4875-adf4-ed8f780c4922
- Status: test
- Level: high
- Author: Mikhail Larin, oscd.community
- Date: 2019-10-25
- Modified: 2021-11-27
- Source Path: rules/linux/auditd/path/lnx_auditd_auditing_config_change.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Detection

```yaml
selection:
  type: PATH
  name:
  - /etc/audit/*
  - /etc/libaudit.conf
  - /etc/audisp/*
condition: selection
```

## False Positives

- Legitimate administrative activity

## References

- https://github.com/Neo23x0/auditd/blob/master/audit.rules
- Self Experience

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_auditing_config_change.yml)
