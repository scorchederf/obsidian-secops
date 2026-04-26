---
sigma_id: "af202fd3-7bff-4212-a25a-fb34606cfcbe"
title: "Modifying Crontab"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/cron/lnx_cron_crontab_file_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/cron/lnx_cron_crontab_file_modification.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "linux / cron"
aliases:
  - "af202fd3-7bff-4212-a25a-fb34606cfcbe"
  - "Modifying Crontab"
attack_technique_ids:
  - "T1053.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Modifying Crontab

Detects suspicious modification of crontab file.

## Metadata

- Rule ID: af202fd3-7bff-4212-a25a-fb34606cfcbe
- Status: test
- Level: medium
- Author: Pawel Mazur
- Date: 2022-04-16
- Source Path: rules/linux/builtin/cron/lnx_cron_crontab_file_modification.yml

## Logsource

- product: linux
- service: cron

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Detection

```yaml
keywords:
- REPLACE
condition: keywords
```

## False Positives

- Legitimate modification of crontab

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1053.003/T1053.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/cron/lnx_cron_crontab_file_modification.yml)
