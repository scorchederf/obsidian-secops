---
sigma_id: "0a5177f4-6ca9-44c2-aacf-d3f3d8b6e4d2"
title: "AWS IAM Backdoor Users Keys"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_iam_backdoor_users_keys.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_iam_backdoor_users_keys.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "0a5177f4-6ca9-44c2-aacf-d3f3d8b6e4d2"
  - "AWS IAM Backdoor Users Keys"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS IAM Backdoor Users Keys

Detects AWS API key creation for a user by another user.
Backdoored users can be used to obtain persistence in the AWS environment.
Also with this alert, you can detect a flow of AWS keys in your org.

## Metadata

- Rule ID: 0a5177f4-6ca9-44c2-aacf-d3f3d8b6e4d2
- Status: test
- Level: medium
- Author: faloker
- Date: 2020-02-12
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_iam_backdoor_users_keys.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection_source:
  eventSource: iam.amazonaws.com
  eventName: CreateAccessKey
filter:
  userIdentity.arn|contains: responseElements.accessKey.userName
condition: selection_source and not filter
```

## False Positives

- Adding user keys to their own accounts (the filter cannot cover all possible variants of user naming)
- AWS API keys legitimate exchange workflows

## References

- https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2c5b181/pacu/modules/iam__backdoor_users_keys/main.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_iam_backdoor_users_keys.yml)
