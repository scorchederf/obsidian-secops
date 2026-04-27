---
atomic_guid: "8d1c2368-b503-40c9-9057-8e42f21c58ad"
title: "AWS - Create a new IAM user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.003"
attack_technique_name: "Create Account: Cloud Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "8d1c2368-b503-40c9-9057-8e42f21c58ad"
  - "AWS - Create a new IAM user"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a new IAM user in AWS. Upon successful creation, a new user will be created. Adversaries create new IAM users so that their malicious activity do not interupt the normal functions of the compromised users and can remain undetected for a long time

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]

## Input Arguments

### username

- description: Username of the IAM user to create in AWS
- type: string
- default: atomicredteam

## Dependencies

Check if ~/.aws/credentials file has a default stanza is configured

### Prerequisite Check

```untitled
cat ~/.aws/credentials | grep "default"
```

### Get Prerequisite

```untitled
echo Please install the aws-cli and configure your AWS defult profile using: aws configure
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
aws iam create-user --user-name #{username}
```

### Cleanup

```bash
aws iam delete-user --user-name #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml)
