---
atomic_guid: "33ca84bc-4259-4943-bd36-4655dc420932"
title: "AWS CloudWatch Log Stream Deletes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "33ca84bc-4259-4943-bd36-4655dc420932"
  - "AWS CloudWatch Log Stream Deletes"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a new cloudWatch log stream in AWS, Upon successful creation it will Delete the stream. Attackers can use this technique to evade defenses by 
deleting the log stream. Once it is deleted, the logs created by the attackers will not be logged. https://www.elastic.co/guide/en/security/current/aws-cloudwatch-log-stream-deletion.html

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562008-disable-or-modify-cloud-logs|T1562.008: Disable or Modify Cloud Logs]]

## Input Arguments

### cloudwatch_log_group_name

- description: Name of the cloudWatch log group
- type: string
- default: test-logs

### cloudwatch_log_stream_name

- description: Name of the cloudWatch log stream
- type: string
- default: 20150601

### region

- description: Name of the region
- type: string
- default: us-west-2

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
aws logs create-log-stream --log-group-name #{cloudwatch_log_group_name} --log-stream-name #{cloudwatch_log_stream_name} --region #{region}
echo "*** Log Stream Created ***"
aws logs delete-log-stream --log-group-name #{cloudwatch_log_group_name} --log-stream-name #{cloudwatch_log_stream_name} --region #{region}
echo "*** Log Stream Deleted ***"
aws logs delete-log-group --log-group-name #{cloudwatch_log_group_name} --region #{region} --output json
echo "*** Log Group Deleted ***"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
