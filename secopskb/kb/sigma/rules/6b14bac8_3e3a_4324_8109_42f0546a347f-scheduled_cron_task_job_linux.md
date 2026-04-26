---
sigma_id: "6b14bac8-3e3a-4324-8109-42f0546a347f"
title: "Scheduled Cron Task/Job - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_schedule_task_job_cron.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_schedule_task_job_cron.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "6b14bac8-3e3a-4324-8109-42f0546a347f"
  - "Scheduled Cron Task/Job - Linux"
attack_technique_ids:
  - "T1053.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Cron Task/Job - Linux

Detects abuse of the cron utility to perform task scheduling for initial or recurring execution of malicious code. Detection will focus on crontab jobs uploaded from the tmp folder.

## Metadata

- Rule ID: 6b14bac8-3e3a-4324-8109-42f0546a347f
- Status: test
- Level: medium
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-06
- Modified: 2022-11-27
- Source Path: rules/linux/process_creation/proc_creation_lnx_schedule_task_job_cron.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Detection

```yaml
selection:
  Image|endswith: crontab
  CommandLine|contains: /tmp/
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1053.003/T1053.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_schedule_task_job_cron.yml)
