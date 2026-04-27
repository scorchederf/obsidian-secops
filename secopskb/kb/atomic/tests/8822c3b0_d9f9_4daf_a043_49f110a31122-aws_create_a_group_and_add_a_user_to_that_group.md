---
atomic_guid: "8822c3b0-d9f9-4daf-a043-49f110a31122"
title: "AWS - Create a group and add a user to that group"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "8822c3b0-d9f9-4daf-a043-49f110a31122"
  - "AWS - Create a group and add a user to that group"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adversaries create AWS group, add users to specific to that group to elevate their privileges to gain more accesss

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098: Account Manipulation]]

## Input Arguments

### username

- description: Name of the AWS group to create
- type: string
- default: atomicredteam

## Dependencies

Check if the user exists, we can only add a user to a group if the user exists.

### Prerequisite Check

```untitled
aws iam list-users | grep #{username}
```

### Get Prerequisite

```untitled
echo Please run atomic test T1136.003, before running this atomic test
```

## Executor

- name: sh

### Command

```bash
aws iam create-group --group-name #{username}
aws iam add-user-to-group --user-name #{username} --group-name #{username}
```

### Cleanup

```bash
aws iam remove-user-from-group --user-name #{username} --group-name #{username}
aws iam delete-group --group-name #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
