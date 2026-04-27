---
atomic_guid: "1602ff76-ed7f-4c94-b550-2f727b4782d4"
title: "Overwrite Linux Mail Spool"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.002"
attack_technique_name: "Indicator Removal on Host: Clear FreeBSD, Linux or Mac System Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "1602ff76-ed7f-4c94-b550-2f727b4782d4"
  - "Overwrite Linux Mail Spool"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test overwrites the Linux mail spool of a specified user. This technique was used by threat actor Rocke during the exploitation of Linux web servers.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]

## Input Arguments

### username

- description: Username of mail spool
- type: string
- default: root

## Dependencies

target files must exist

### Prerequisite Check

```bash
stat /var/spool/mail/#{username}
```

### Get Prerequisite

```bash
touch /var/spool/mail/#{username}
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo 0> /var/spool/mail/#{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.002/T1070.002.yaml)
