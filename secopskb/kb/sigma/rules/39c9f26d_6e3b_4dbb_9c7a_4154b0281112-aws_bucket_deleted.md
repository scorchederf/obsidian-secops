---
sigma_id: "39c9f26d-6e3b-4dbb-9c7a-4154b0281112"
title: "AWS Bucket Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_bucket_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_bucket_deleted.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "39c9f26d-6e3b-4dbb-9c7a-4154b0281112"
  - "AWS Bucket Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Bucket Deleted

Detects the deletion of S3 buckets in AWS CloudTrail logs.
Monitoring the deletion of S3 buckets is critical for security and data integrity, as it may indicate potential data loss or unauthorized access attempts.

## Metadata

- Rule ID: 39c9f26d-6e3b-4dbb-9c7a-4154b0281112
- Status: experimental
- Level: medium
- Author: Ivan Saakov, Nasreddine Bencherchali
- Date: 2025-10-19
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_bucket_deleted.yml

## Logsource

- product: aws
- service: cloudtrail

## Detection

```yaml
selection_event_name:
  eventName: DeleteBucket
selection_status_success:
  errorCode: Success
selection_status_null:
  errorCode: null
condition: selection_event_name and 1 of selection_status_*
```

## False Positives

- During maintenance operations or testing, authorized administrators may delete S3 buckets as part of routine data management or cleanup activities.

## References

- https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html
- https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_bucket_deleted.yml)
