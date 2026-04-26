---
sigma_id: "f305fd62-beca-47da-ad95-7690a0620084"
title: "Potential Bucket Enumeration on AWS"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_enum_buckets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_enum_buckets.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "f305fd62-beca-47da-ad95-7690a0620084"
  - "Potential Bucket Enumeration on AWS"
attack_technique_ids:
  - "T1580"
  - "T1619"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Bucket Enumeration on AWS

Looks for potential enumeration of AWS buckets via ListBuckets.

## Metadata

- Rule ID: f305fd62-beca-47da-ad95-7690a0620084
- Status: test
- Level: low
- Author: Christopher Peacock @securepeacock, SCYTHE @scythe_io
- Date: 2023-01-06
- Modified: 2024-07-10
- Source Path: rules/cloud/aws/cloudtrail/aws_enum_buckets.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1580-cloud_infrastructure_discovery|T1580]]
- [[kb/attack/techniques/T1619-cloud_storage_object_discovery|T1619]]

## Detection

```yaml
selection:
  eventSource: s3.amazonaws.com
  eventName: ListBuckets
filter:
  userIdentity.type: AssumedRole
condition: selection and not filter
```

## False Positives

- Administrators listing buckets, it may be necessary to filter out users who commonly conduct this activity.

## References

- https://github.com/Lifka/hacking-resources/blob/c2ae355d381bd0c9f0b32c4ead049f44e5b1573f/cloud-hacking-cheat-sheets.md
- https://jamesonhacking.blogspot.com/2020/12/pivoting-to-private-aws-s3-buckets.html
- https://securitycafe.ro/2022/12/14/aws-enumeration-part-ii-practical-enumeration/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_enum_buckets.yml)
