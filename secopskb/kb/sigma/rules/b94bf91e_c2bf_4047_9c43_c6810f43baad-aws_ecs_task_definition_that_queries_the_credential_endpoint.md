---
sigma_id: "b94bf91e-c2bf-4047-9c43-c6810f43baad"
title: "AWS ECS Task Definition That Queries The Credential Endpoint"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_ecs_task_definition_cred_endpoint_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ecs_task_definition_cred_endpoint_query.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "b94bf91e-c2bf-4047-9c43-c6810f43baad"
  - "AWS ECS Task Definition That Queries The Credential Endpoint"
attack_technique_ids:
  - "T1525"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS ECS Task Definition That Queries The Credential Endpoint

Detects when an Elastic Container Service (ECS) Task Definition includes a command to query the credential endpoint.
This can indicate a potential adversary adding a backdoor to establish persistence or escalate privileges.

## Metadata

- Rule ID: b94bf91e-c2bf-4047-9c43-c6810f43baad
- Status: test
- Level: medium
- Author: Darin Smith
- Date: 2022-06-07
- Modified: 2023-04-24
- Source Path: rules/cloud/aws/cloudtrail/aws_ecs_task_definition_cred_endpoint_query.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1525-implant_internal_image|T1525]]

## Detection

```yaml
selection:
  eventSource: ecs.amazonaws.com
  eventName:
  - DescribeTaskDefinition
  - RegisterTaskDefinition
  - RunTask
  requestParameters.containerDefinitions.command|contains: $AWS_CONTAINER_CREDENTIALS_RELATIVE_URI
condition: selection
```

## False Positives

- Task Definition being modified to request credentials from the Task Metadata Service for valid reasons

## References

- https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2c5b181/pacu/modules/ecs__backdoor_task_def/main.py
- https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefinition.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ecs_task_definition_cred_endpoint_query.yml)
