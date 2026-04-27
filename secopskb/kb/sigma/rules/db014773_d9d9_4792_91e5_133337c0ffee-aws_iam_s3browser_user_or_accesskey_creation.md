---
sigma_id: "db014773-d9d9-4792-91e5-133337c0ffee"
title: "AWS IAM S3Browser User or AccessKey Creation"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_iam_s3browser_user_or_accesskey_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_iam_s3browser_user_or_accesskey_creation.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "db014773-d9d9-4792-91e5-133337c0ffee"
  - "AWS IAM S3Browser User or AccessKey Creation"
attack_technique_ids:
  - "T1059.009"
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects S3 Browser utility creating IAM User or AccessKey.

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]]
- [[kb/attack/techniques/T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]

## Detection

```yaml
selection:
  eventSource: iam.amazonaws.com
  eventName:
  - CreateUser
  - CreateAccessKey
  userAgent|contains: S3 Browser
condition: selection
```

## False Positives

- Valid usage of S3 Browser for IAM User and/or AccessKey creation

## References

- https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_iam_s3browser_user_or_accesskey_creation.yml)
