---
sigma_id: "78b3756a-7804-4ef7-8555-7b9024a02e2d"
title: "AWS S3 Data Management Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_s3_data_management_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_s3_data_management_tampering.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "78b3756a-7804-4ef7-8555-7b9024a02e2d"
  - "AWS S3 Data Management Tampering"
attack_technique_ids:
  - "T1537"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS S3 Data Management Tampering

Detects when a user tampers with S3 data management in Amazon Web Services.

## Metadata

- Rule ID: 78b3756a-7804-4ef7-8555-7b9024a02e2d
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-07-24
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_s3_data_management_tampering.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1537-transfer_data_to_cloud_account|T1537]]

## Detection

```yaml
selection:
  eventSource: s3.amazonaws.com
  eventName:
  - PutBucketLogging
  - PutBucketWebsite
  - PutEncryptionConfiguration
  - PutLifecycleConfiguration
  - PutReplicationConfiguration
  - ReplicateObject
  - RestoreObject
condition: selection
```

## False Positives

- A S3 configuration change may be done by a system or network administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment. S3 configuration change from unfamiliar users or hosts should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://github.com/elastic/detection-rules/pull/1145/files
- https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html
- https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html
- https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html
- https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html
- https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_s3_data_management_tampering.yml)
