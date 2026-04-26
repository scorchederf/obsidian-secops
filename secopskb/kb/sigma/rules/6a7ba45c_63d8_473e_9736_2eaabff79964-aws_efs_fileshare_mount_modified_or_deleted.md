---
sigma_id: "6a7ba45c-63d8-473e-9736-2eaabff79964"
title: "AWS EFS Fileshare Mount Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_efs_fileshare_mount_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_efs_fileshare_mount_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "6a7ba45c-63d8-473e-9736-2eaabff79964"
  - "AWS EFS Fileshare Mount Modified or Deleted"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS EFS Fileshare Mount Modified or Deleted

Detects when a EFS Fileshare Mount is modified or deleted. An adversary breaking any file system using the mount target that is being deleted, which might disrupt instances or applications using those mounts.

## Metadata

- Rule ID: 6a7ba45c-63d8-473e-9736-2eaabff79964
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-15
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_efs_fileshare_mount_modified_or_deleted.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Detection

```yaml
selection:
  eventSource: elasticfilesystem.amazonaws.com
  eventName: DeleteMountTarget
condition: selection
```

## False Positives

- Unknown

## References

- https://docs.aws.amazon.com/efs/latest/ug/API_DeleteMountTarget.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_efs_fileshare_mount_modified_or_deleted.yml)
