---
sigma_id: "92f84194-8d9a-4ee0-8699-c30bfac59780"
title: "AWS Key Pair Import Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_ec2_import_key_pair_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_import_key_pair_activity.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "92f84194-8d9a-4ee0-8699-c30bfac59780"
  - "AWS Key Pair Import Activity"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Key Pair Import Activity

Detects the import of SSH key pairs into AWS EC2, which may indicate an attacker attempting to gain unauthorized access to instances. This activity could lead to initial access, persistence, or privilege escalation, potentially compromising sensitive data and operations.

## Metadata

- Rule ID: 92f84194-8d9a-4ee0-8699-c30bfac59780
- Status: experimental
- Level: medium
- Author: Ivan Saakov
- Date: 2024-12-19
- Source Path: rules/cloud/aws/cloudtrail/aws_ec2_import_key_pair_activity.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  eventSource: ec2.amazonaws.com
  eventName: ImportKeyPair
condition: selection
```

## False Positives

- Legitimate administrative actions by authorized users importing keys for valid purposes.
- Automated processes for infrastructure setup may trigger this alert.
- Verify the user identity, user agent, and source IP address to ensure they are expected.

## References

- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_import_key_pair_activity.yml)
