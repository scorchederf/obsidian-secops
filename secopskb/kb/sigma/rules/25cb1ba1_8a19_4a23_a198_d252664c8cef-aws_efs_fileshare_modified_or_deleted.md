---
sigma_id: "25cb1ba1-8a19-4a23-a198-d252664c8cef"
title: "AWS EFS Fileshare Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_efs_fileshare_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_efs_fileshare_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "25cb1ba1-8a19-4a23-a198-d252664c8cef"
  - "AWS EFS Fileshare Modified or Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS EFS Fileshare Modified or Deleted

Detects when a EFS Fileshare is modified or deleted.
You can't delete a file system that is in use.
If the file system has any mount targets, the adversary must first delete them, so deletion of a mount will occur before deletion of a fileshare.

## Metadata

- Rule ID: 25cb1ba1-8a19-4a23-a198-d252664c8cef
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-15
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_efs_fileshare_modified_or_deleted.yml

## Logsource

- product: aws
- service: cloudtrail

## Detection

```yaml
selection:
  eventSource: elasticfilesystem.amazonaws.com
  eventName: DeleteFileSystem
condition: selection
```

## False Positives

- Unknown

## References

- https://docs.aws.amazon.com/efs/latest/ug/API_DeleteFileSystem.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_efs_fileshare_modified_or_deleted.yml)
