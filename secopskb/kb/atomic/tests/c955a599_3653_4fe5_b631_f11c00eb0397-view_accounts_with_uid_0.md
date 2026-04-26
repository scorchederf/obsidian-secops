---
atomic_guid: "c955a599-3653-4fe5-b631-f11c00eb0397"
title: "View accounts with UID 0"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "c955a599-3653-4fe5-b631-f11c00eb0397"
  - "View accounts with UID 0"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# View accounts with UID 0

View accounts with UID 0

## Metadata

- Atomic GUID: c955a599-3653-4fe5-b631-f11c00eb0397
- Technique: T1087.001: Account Discovery: Local Account
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1087.001/T1087.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Input Arguments

### output_file

- description: Path where captured results will be placed
- type: path
- default: /tmp/T1087.001.txt

## Executor

- name: sh

### Command

```bash
grep 'x:0:' /etc/passwd > #{output_file}
grep '*:0:' /etc/passwd >> #{output_file}
cat #{output_file} 2>/dev/null
```

### Cleanup

```bash
rm -f #{output_file} 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
