---
sigma_id: "055fb148-60f8-462d-ad16-26926ce050f1"
title: "AWS User Login Profile Was Modified"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_update_login_profile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_update_login_profile.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "055fb148-60f8-462d-ad16-26926ce050f1"
  - "AWS User Login Profile Was Modified"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS User Login Profile Was Modified

Detects activity when someone is changing passwords on behalf of other users.
An attacker with the "iam:UpdateLoginProfile" permission on other users can change the password used to login to the AWS console on any user that already has a login profile setup.

## Metadata

- Rule ID: 055fb148-60f8-462d-ad16-26926ce050f1
- Status: test
- Level: high
- Author: toffeebr33k
- Date: 2021-08-09
- Modified: 2024-04-26
- Source Path: rules/cloud/aws/cloudtrail/aws_update_login_profile.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  eventSource: iam.amazonaws.com
  eventName: UpdateLoginProfile
filter_main_user_identity:
  userIdentity.arn|fieldref: requestParameters.userName
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate user account administration

## References

- https://github.com/RhinoSecurityLabs/AWS-IAM-Privilege-Escalation

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_update_login_profile.yml)
