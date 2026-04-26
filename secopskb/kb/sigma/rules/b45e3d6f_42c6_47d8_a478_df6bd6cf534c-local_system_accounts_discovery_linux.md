---
sigma_id: "b45e3d6f-42c6-47d8-a478-df6bd6cf534c"
title: "Local System Accounts Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_local_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_local_account.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "b45e3d6f-42c6-47d8-a478-df6bd6cf534c"
  - "Local System Accounts Discovery - Linux"
attack_technique_ids:
  - "T1087.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local System Accounts Discovery - Linux

Detects enumeration of local system accounts. This information can help adversaries determine which local accounts exist on a system to aid in follow-on behavior.

## Metadata

- Rule ID: b45e3d6f-42c6-47d8-a478-df6bd6cf534c
- Status: test
- Level: low
- Author: Alejandro Ortuno, oscd.community, CheraghiMilad
- Date: 2020-10-08
- Modified: 2024-12-10
- Source Path: rules/linux/process_creation/proc_creation_lnx_local_account.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Detection

```yaml
selection_1:
  Image|endswith: /lastlog
selection_2:
  CommandLine|contains: '''x:0:'''
selection_3:
  Image|endswith:
  - /cat
  - /ed
  - /head
  - /more
  - /nano
  - /tail
  - /vi
  - /vim
  - /less
  - /emacs
  - /sqlite3
  - /makemap
  CommandLine|contains:
  - /etc/passwd
  - /etc/shadow
  - /etc/sudoers
  - /etc/spwd.db
  - /etc/pwd.db
  - /etc/master.passwd
selection_4:
  Image|endswith: /id
selection_5:
  Image|endswith: /lsof
  CommandLine|contains: -u
condition: 1 of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1087.001/T1087.001.md
- https://my.f5.com/manage/s/article/K589
- https://man.freebsd.org/cgi/man.cgi?pwd_mkdb

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_local_account.yml)
