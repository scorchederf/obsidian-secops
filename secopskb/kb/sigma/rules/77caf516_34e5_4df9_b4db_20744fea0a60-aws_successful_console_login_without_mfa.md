---
sigma_id: "77caf516-34e5-4df9-b4db-20744fea0a60"
title: "AWS Successful Console Login Without MFA"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_success_without_mfa.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_success_without_mfa.yml"
build_date: "2026-04-26 14:14:20"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "77caf516-34e5-4df9-b4db-20744fea0a60"
  - "AWS Successful Console Login Without MFA"
attack_technique_ids:
  - "T1078.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Successful Console Login Without MFA

Detects successful AWS console logins that were performed without Multi-Factor Authentication (MFA).
This alert can be used to identify potential unauthorized access attempts, as logging in without MFA can indicate compromised credentials or misconfigured security settings.

## Metadata

- Rule ID: 77caf516-34e5-4df9-b4db-20744fea0a60
- Status: experimental
- Level: medium
- Author: Thuya@Hacktilizer, Ivan Saakov
- Date: 2025-10-18
- Modified: 2025-10-21
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_success_without_mfa.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Detection

```yaml
selection:
  eventName: ConsoleLogin
  additionalEventData.MFAUsed: 'NO'
  responseElements.ConsoleLogin: Success
condition: selection
```

## False Positives

- Unlikely

## References

- https://securitylabs.datadoghq.com/cloud-security-atlas/vulnerabilities/iam-user-without-mfa/
- https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_success_without_mfa.yml)
