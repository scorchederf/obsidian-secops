---
sigma_id: "a136ac98-b2bc-4189-a14d-f0d0388e57a7"
title: "AWS S3 Bucket Versioning Disable"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_disable_bucket_versioning.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_disable_bucket_versioning.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "a136ac98-b2bc-4189-a14d-f0d0388e57a7"
  - "AWS S3 Bucket Versioning Disable"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS S3 Bucket Versioning Disable

Detects when S3 bucket versioning is disabled. Threat actors use this technique during AWS ransomware incidents prior to deleting S3 objects.

## Metadata

- Rule ID: a136ac98-b2bc-4189-a14d-f0d0388e57a7
- Status: test
- Level: medium
- Author: Sean Johnstone | Unit 42
- Date: 2023-10-28
- Source Path: rules/cloud/aws/cloudtrail/aws_disable_bucket_versioning.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  eventSource: s3.amazonaws.com
  eventName: PutBucketVersioning
  requestParameters|contains: Suspended
condition: selection
```

## False Positives

- AWS administrator legitimately disabling bucket versioning

## References

- https://invictus-ir.medium.com/ransomware-in-the-cloud-7f14805bbe82

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_disable_bucket_versioning.yml)
