---
sigma_id: "8ec2c8b4-557a-4121-b87c-5dfb3a602fae"
title: "JexBoss Command Sequence"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_susp_jexboss.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_susp_jexboss.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "8ec2c8b4-557a-4121-b87c-5dfb3a602fae"
  - "JexBoss Command Sequence"
attack_technique_ids:
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# JexBoss Command Sequence

Detects suspicious command sequence that JexBoss

## Metadata

- Rule ID: 8ec2c8b4-557a-4121-b87c-5dfb3a602fae
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-08-24
- Modified: 2025-11-22
- Source Path: rules/linux/builtin/lnx_susp_jexboss.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
keywords:
  '|all':
  - bash -c /bin/bash
  - '&/dev/tcp/'
condition: keywords
```

## False Positives

- Unknown

## References

- https://www.us-cert.gov/ncas/analysis-reports/AR18-312A

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_susp_jexboss.yml)
