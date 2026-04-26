---
atomic_guid: "8d1c2368-b503-40c9-9057-8e42f21c58ad"
title: "AWS - Create a new IAM user"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.003"
attack_technique_name: "Create Account: Cloud Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml"
build_date: "2026-04-26 14:38:40"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS - Create a new IAM user

Creates a new IAM user in AWS. Upon successful creation, a new user will be created. Adversaries create new IAM users so that their malicious activity do not interupt the normal functions of the compromised users and can remain undetected for a long time

## Metadata

- Atomic GUID: 8d1c2368-b503-40c9-9057-8e42f21c58ad
- Technique: T1136.003: Create Account: Cloud Account
- Platforms: iaas:aws
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1136.003/T1136.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.003]]

## Input Arguments

### username

- description: Username of the IAM user to create in AWS
- type: string
- default: atomicredteam

## Dependencies

Check if ~/.aws/credentials file has a default stanza is configured

### Prerequisite Check

```text
cat ~/.aws/credentials | grep "default"
```

### Get Prerequisite

```text
echo Please install the aws-cli and configure your AWS defult profile using: aws configure
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
aws iam create-user --user-name #{username}
```

### Cleanup

```sh
aws iam delete-user --user-name #{username}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.003/T1136.003.yaml)
