---
sigma_id: "352a918a-34d8-4882-8470-44830c507aa3"
title: "Malicious Usage Of IMDS Credentials Outside Of AWS Infrastructure"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_imds_malicious_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_imds_malicious_usage.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "352a918a-34d8-4882-8470-44830c507aa3"
  - "Malicious Usage Of IMDS Credentials Outside Of AWS Infrastructure"
attack_technique_ids:
  - "T1078"
  - "T1078.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Malicious Usage Of IMDS Credentials Outside Of AWS Infrastructure

Detects when an instance identity has taken an action that isn't inside SSM.
This can indicate that a compromised EC2 instance is being used as a pivot point.

## Metadata

- Rule ID: 352a918a-34d8-4882-8470-44830c507aa3
- Status: test
- Level: high
- Author: jamesc-grafana
- Date: 2024-07-11
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_imds_malicious_usage.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]

## Detection

```yaml
selection:
  userIdentity.arn|re: .+:assumed-role/aws:.+
filter_main_generic:
- eventSource: ssm.amazonaws.com
- eventName: RegisterManagedInstance
- sourceIPAddress: AWS Internal
condition: selection and not 1 of filter_main_*
```

## False Positives

- A team has configured an EC2 instance to use instance profiles that grant the option for the EC2 instance to talk to other AWS Services

## References

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-identity-roles.html
- https://ermetic.com/blog/aws/aws-ec2-imds-what-you-need-to-know/
- https://www.packetmischief.ca/2023/07/31/amazon-ec2-credential-exfiltration-how-it-happens-and-how-to-mitigate-it/#lifting-credentials-from-imds-this-is-why-we-cant-have-nice-things

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_imds_malicious_usage.yml)
