---
sigma_id: "86157017-c2b1-4d4a-8c33-93b8e67e4af4"
title: "Potential Suspicious Change To Sensitive/Critical Files"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_sensitive_file_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_sensitive_file_access.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "86157017-c2b1-4d4a-8c33-93b8e67e4af4"
  - "Potential Suspicious Change To Sensitive/Critical Files"
attack_technique_ids:
  - "T1565.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious Change To Sensitive/Critical Files

Detects changes of sensitive and critical files. Monitors files that you don't expect to change without planning on Linux system.

## Metadata

- Rule ID: 86157017-c2b1-4d4a-8c33-93b8e67e4af4
- Status: test
- Level: medium
- Author: @d4ns4n_ (Wuerth-Phoenix)
- Date: 2023-05-30
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_sensitive_file_access.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1565-data_manipulation|T1565.001]]

## Detection

```yaml
selection_img_1:
  Image|endswith:
  - /cat
  - /echo
  - /grep
  - /head
  - /more
  - /tail
  CommandLine|contains: '>'
selection_img_2:
  Image|endswith:
  - /emacs
  - /nano
  - /sed
  - /vi
  - /vim
selection_paths:
  CommandLine|contains:
  - /bin/login
  - /bin/passwd
  - /boot/
  - /etc/*.conf
  - /etc/cron.
  - /etc/crontab
  - /etc/hosts
  - /etc/init.d
  - /etc/sudoers
  - /opt/bin/
  - /sbin
  - /usr/bin/
  - /usr/local/bin/
condition: 1 of selection_img_* and selection_paths
```

## False Positives

- Some false positives are to be expected on user or administrator machines. Apply additional filters as needed.

## References

- https://learn.microsoft.com/en-us/azure/defender-for-cloud/file-integrity-monitoring-overview#which-files-should-i-monitor

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_sensitive_file_access.yml)
