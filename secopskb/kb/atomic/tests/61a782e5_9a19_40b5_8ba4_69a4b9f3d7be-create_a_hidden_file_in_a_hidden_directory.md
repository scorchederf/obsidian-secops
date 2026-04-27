---
atomic_guid: "61a782e5-9a19-40b5-8ba4-69a4b9f3d7be"
title: "Create a hidden file in a hidden directory"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "61a782e5-9a19-40b5-8ba4-69a4b9f3d7be"
  - "Create a hidden file in a hidden directory"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a hidden file inside a hidden directory

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564001-hidden-files-and-directories|T1564.001: Hidden Files and Directories]]

## Executor

- name: sh

### Command

```bash
mkdir /var/tmp/.hidden-directory
echo "T1564.001" > /var/tmp/.hidden-directory/.hidden-file
```

### Cleanup

```bash
rm -rf /var/tmp/.hidden-directory/
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
