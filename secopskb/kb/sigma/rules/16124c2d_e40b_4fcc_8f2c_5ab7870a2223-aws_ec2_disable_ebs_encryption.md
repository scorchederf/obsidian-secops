---
sigma_id: "16124c2d-e40b-4fcc-8f2c-5ab7870a2223"
title: "AWS EC2 Disable EBS Encryption"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_ec2_disable_encryption.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_disable_encryption.yml"
build_date: "2026-04-26 14:14:19"
status: "stable"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "16124c2d-e40b-4fcc-8f2c-5ab7870a2223"
  - "AWS EC2 Disable EBS Encryption"
attack_technique_ids:
  - "T1486"
  - "T1565"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS EC2 Disable EBS Encryption

Identifies disabling of default Amazon Elastic Block Store (EBS) encryption in the current region.
Disabling default encryption does not change the encryption status of your existing volumes.

## Metadata

- Rule ID: 16124c2d-e40b-4fcc-8f2c-5ab7870a2223
- Status: stable
- Level: medium
- Author: Sittikorn S
- Date: 2021-06-29
- Modified: 2021-08-20
- Source Path: rules/cloud/aws/cloudtrail/aws_ec2_disable_encryption.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]
- [[kb/attack/techniques/T1565-data_manipulation|T1565]]

## Detection

```yaml
selection:
  eventSource: ec2.amazonaws.com
  eventName: DisableEbsEncryptionByDefault
condition: selection
```

## False Positives

- System Administrator Activities
- DEV, UAT, SAT environment. You should apply this rule with PROD account only.

## References

- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableEbsEncryptionByDefault.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_disable_encryption.yml)
