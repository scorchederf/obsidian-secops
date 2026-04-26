---
sigma_id: "6c4e2f43-d94d-4ead-b64d-97e53fa2bd05"
title: "Persistence Via Cron Files"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_persistence_cron_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_persistence_cron_files.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "linux / file_event"
aliases:
  - "6c4e2f43-d94d-4ead-b64d-97e53fa2bd05"
  - "Persistence Via Cron Files"
attack_technique_ids:
  - "T1053.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Persistence Via Cron Files

Detects creation of cron file or files in Cron directories which could indicates potential persistence.

## Metadata

- Rule ID: 6c4e2f43-d94d-4ead-b64d-97e53fa2bd05
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
- Date: 2021-10-15
- Modified: 2022-12-31
- Source Path: rules/linux/file_event/file_event_lnx_persistence_cron_files.yml

## Logsource

- category: file_event
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Detection

```yaml
selection1:
  TargetFilename|startswith:
  - /etc/cron.d/
  - /etc/cron.daily/
  - /etc/cron.hourly/
  - /etc/cron.monthly/
  - /etc/cron.weekly/
  - /var/spool/cron/crontabs/
selection2:
  TargetFilename|contains:
  - /etc/cron.allow
  - /etc/cron.deny
  - /etc/crontab
condition: 1 of selection*
```

## False Positives

- Any legitimate cron file.

## References

- https://github.com/microsoft/MSTIC-Sysmon/blob/f1477c0512b0747c1455283069c21faec758e29d/linux/configs/attack-based/persistence/T1053.003_Cron_Activity.xml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_persistence_cron_files.yml)
