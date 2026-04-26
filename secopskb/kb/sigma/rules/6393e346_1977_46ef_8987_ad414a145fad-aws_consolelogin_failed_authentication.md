---
sigma_id: "6393e346-1977-46ef-8987-ad414a145fad"
title: "AWS ConsoleLogin Failed Authentication"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_failed_authentication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_failed_authentication.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "6393e346-1977-46ef-8987-ad414a145fad"
  - "AWS ConsoleLogin Failed Authentication"
attack_technique_ids:
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS ConsoleLogin Failed Authentication

Detects failed AWS console login attempts due to authentication failures. Monitoring these events is crucial for identifying potential brute-force attacks or unauthorized access attempts to AWS accounts.

## Metadata

- Rule ID: 6393e346-1977-46ef-8987-ad414a145fad
- Status: experimental
- Level: medium
- Author: Ivan Saakov, Nasreddine Bencherchali
- Date: 2025-10-19
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_failed_authentication.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  eventName: ConsoleLogin
  errorMessage: Failed authentication
condition: selection
```

## False Positives

- Legitimate failed login attempts by authorized users. Investigate the source of repeated failed login attempts.

## References

- https://naikordian.github.io/blog/posts/brute-force-aws-console/
- https://help.fortinet.com/fsiem/Public_Resource_Access/7_2_1/rules/PH_RULE_AWS_Management_Console_Brute_Force_of_Root_User_Identity.htm
- https://media.githubusercontent.com/media/splunk/attack_data/master/datasets/attack_techniques/T1110.001/aws_login_failure/aws_cloudtrail_events.json

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_console_login_failed_authentication.yml)
