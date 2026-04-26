---
atomic_guid: "f8aab3dd-5990-4bf8-b8ab-2226c951696f"
title: "Enumerate all accounts (Local)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.001"
attack_technique_name: "Account Discovery: Local Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "f8aab3dd-5990-4bf8-b8ab-2226c951696f"
  - "Enumerate all accounts (Local)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate all accounts (Local)

Enumerate all accounts by copying /etc/passwd to another file

## Metadata

- Atomic GUID: f8aab3dd-5990-4bf8-b8ab-2226c951696f
- Technique: T1087.001: Account Discovery: Local Account
- Platforms: linux
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

```sh
cat /etc/passwd > #{output_file}
cat #{output_file}
```

### Cleanup

```sh
rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.001/T1087.001.yaml)
