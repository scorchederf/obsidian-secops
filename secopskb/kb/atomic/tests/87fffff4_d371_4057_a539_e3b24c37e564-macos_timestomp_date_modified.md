---
atomic_guid: "87fffff4-d371-4057-a539-e3b24c37e564"
title: "MacOS - Timestomp Date Modified"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.006"
attack_technique_name: "Indicator Removal on Host: Timestomp"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "87fffff4-d371-4057-a539-e3b24c37e564"
  - "MacOS - Timestomp Date Modified"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Stomps on the modification timestamp of a file using MacOS's SetFile utility

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070006-timestomp|T1070.006: Timestomp]]

## Input Arguments

### target_date

- description: Date to replace original timestamps with
- type: string
- default: 01/01/1970

### target_filename

- description: Path of file that we are going to stomp on last modified time

- type: path
- default: /tmp/T1070.006-modified.txt

## Dependencies

The file must exist in order to be timestomped

### Prerequisite Check

```untitled
test -e #{target_filename} && exit 0 || exit 1
```

### Get Prerequisite

```untitled
echo 'T1070.006 MacOS file modified timestomp test' > #{target_filename}
```

## Executor

- name: sh

### Command

```bash
SetFile -m #{target_date} #{target_filename}
```

### Cleanup

```bash
rm -f #{target_filename}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.006/T1070.006.yaml)
