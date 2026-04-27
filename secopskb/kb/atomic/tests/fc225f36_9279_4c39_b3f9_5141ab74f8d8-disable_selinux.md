---
atomic_guid: "fc225f36-9279-4c39-b3f9-5141ab74f8d8"
title: "Disable SELinux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "fc225f36-9279-4c39-b3f9-5141ab74f8d8"
  - "Disable SELinux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables SELinux enforcement

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Dependencies

SELinux must be installed

### Prerequisite Check

```untitled
which setenforce
```

### Get Prerequisite

```untitled
echo "SELinux is not installed"; exit 1
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
setenforce 0
```

### Cleanup

```bash
setenforce 1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
