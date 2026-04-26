---
sigma_id: "c2e234de-03a3-41e1-b39a-1e56dc17ba67"
title: "Remove Scheduled Cron Task/Job"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_crontab_removal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_crontab_removal.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "c2e234de-03a3-41e1-b39a-1e56dc17ba67"
  - "Remove Scheduled Cron Task/Job"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remove Scheduled Cron Task/Job

Detects usage of the 'crontab' utility to remove the current crontab.
This is a common occurrence where cryptocurrency miners compete against each other by removing traces of other miners to hijack the maximum amount of resources possible

## Metadata

- Rule ID: c2e234de-03a3-41e1-b39a-1e56dc17ba67
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_crontab_removal.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|endswith: crontab
  CommandLine|contains: ' -r'
condition: selection
```

## False Positives

- Unknown

## References

- https://www.trendmicro.com/en_us/research/22/i/how-malicious-actors-abuse-native-linux-tools-in-their-attacks.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_crontab_removal.yml)
