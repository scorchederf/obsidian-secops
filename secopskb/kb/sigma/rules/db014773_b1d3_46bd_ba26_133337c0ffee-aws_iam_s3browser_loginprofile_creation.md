---
sigma_id: "db014773-b1d3-46bd-ba26-133337c0ffee"
title: "AWS IAM S3Browser LoginProfile Creation"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_iam_s3browser_loginprofile_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_iam_s3browser_loginprofile_creation.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "db014773-b1d3-46bd-ba26-133337c0ffee"
  - "AWS IAM S3Browser LoginProfile Creation"
attack_technique_ids:
  - "T1059.009"
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS IAM S3Browser LoginProfile Creation

Detects S3 Browser utility performing reconnaissance looking for existing IAM Users without a LoginProfile defined then (when found) creating a LoginProfile.

## Metadata

- Rule ID: db014773-b1d3-46bd-ba26-133337c0ffee
- Status: test
- Level: high
- Author: daniel.bohannon@permiso.io (@danielhbohannon)
- Date: 2023-05-17
- Source Path: rules/cloud/aws/cloudtrail/aws_iam_s3browser_loginprofile_creation.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.009]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  eventSource: iam.amazonaws.com
  eventName:
  - GetLoginProfile
  - CreateLoginProfile
  userAgent|contains: S3 Browser
condition: selection
```

## False Positives

- Valid usage of S3 Browser for IAM LoginProfile listing and/or creation

## References

- https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_iam_s3browser_loginprofile_creation.yml)
