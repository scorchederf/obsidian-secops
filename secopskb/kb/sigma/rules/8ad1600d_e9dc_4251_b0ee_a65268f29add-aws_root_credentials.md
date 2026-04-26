---
sigma_id: "8ad1600d-e9dc-4251-b0ee-a65268f29add"
title: "AWS Root Credentials"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_root_account_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_root_account_usage.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "8ad1600d-e9dc-4251-b0ee-a65268f29add"
  - "AWS Root Credentials"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Root Credentials

Detects AWS root account usage

## Metadata

- Rule ID: 8ad1600d-e9dc-4251-b0ee-a65268f29add
- Status: test
- Level: medium
- Author: vitaliy0x1
- Date: 2020-01-21
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_root_account_usage.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection_usertype:
  userIdentity.type: Root
selection_eventtype:
  eventType: AwsServiceEvent
condition: selection_usertype and not selection_eventtype
```

## False Positives

- AWS Tasks That Require AWS Account Root User Credentials https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html

## References

- https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_root_account_usage.yml)
