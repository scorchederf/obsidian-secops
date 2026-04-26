---
atomic_guid: "15330820-d405-450b-bd08-16b5be5be9f4"
title: "Examine AWS Password Policy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1201"
attack_technique_name: "Password Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "15330820-d405-450b-bd08-16b5be5be9f4"
  - "Examine AWS Password Policy"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Examine AWS Password Policy

This atomic test will display details about the password policy for the current AWS account.

## Metadata

- Atomic GUID: 15330820-d405-450b-bd08-16b5be5be9f4
- Technique: T1201: Password Policy Discovery
- Platforms: iaas:aws
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1201/T1201.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

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
aws iam get-account-password-policy
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1201/T1201.yaml)
