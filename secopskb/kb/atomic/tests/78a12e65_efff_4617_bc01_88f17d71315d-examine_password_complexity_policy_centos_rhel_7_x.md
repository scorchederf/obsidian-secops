---
atomic_guid: "78a12e65-efff-4617-bc01-88f17d71315d"
title: "Examine password complexity policy - CentOS/RHEL 7.x"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 14:38:40"
executor: "bash"
aliases:
  - "78a12e65-efff-4617-bc01-88f17d71315d"
  - "Examine password complexity policy - CentOS/RHEL 7.x"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Examine password complexity policy - CentOS/RHEL 7.x

Lists the password complexity policy to console on CentOS/RHEL 7.x Linux.

## Metadata

- Atomic GUID: 78a12e65-efff-4617-bc01-88f17d71315d
- Technique: T1201: Password Policy Discovery
- Platforms: linux
- Executor: bash
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Dependencies

System must be CentOS or RHEL v7

### Prerequisite Check

```text
if [ $(uname -a | grep -ioP 'el[0-9]' | grep -oP '[0-9]') -eq "7" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
echo Please run from CentOS or RHEL v7
```

## Executor

- name: bash

### Command

```bash
cat /etc/security/pwquality.conf
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
