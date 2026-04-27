---
atomic_guid: "89422c87-b57b-4a04-a8ca-802bb9d06121"
title: "AWS - CloudWatch Log Group Deletes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "89422c87-b57b-4a04-a8ca-802bb9d06121"
  - "AWS - CloudWatch Log Group Deletes"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AWS - CloudWatch Log Group Deletes

Creates a new cloudWatch log group in AWS, Upon successful creation it will Delete the group. Attackers can use this technique to evade defenses by 
deleting the log stream. Once it is deleted, the logs created by the attackers will not be logged. https://www.elastic.co/guide/en/security/current/aws-cloudwatch-log-group-deletion.html#aws-cloudwatch-log-group-deletion

## Metadata

- Atomic GUID: 89422c87-b57b-4a04-a8ca-802bb9d06121
- Technique: T1562.008: Impair Defenses: Disable Cloud Logs
- Platforms: iaas:aws
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1562.008/T1562.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Input Arguments

### cloudwatch_log_group_name

- description: Name of the cloudWatch log group
- type: string
- default: log-test

### region

- description: Name of the region
- type: string
- default: us-east-1

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
aws logs create-log-group --log-group-name #{cloudwatch_log_group_name} --region #{region} --output json
echo "*** Log Group Created ***"
aws logs delete-log-group --log-group-name #{cloudwatch_log_group_name} --region #{region} --output json
echo "*** Log Group Deleted ***"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
