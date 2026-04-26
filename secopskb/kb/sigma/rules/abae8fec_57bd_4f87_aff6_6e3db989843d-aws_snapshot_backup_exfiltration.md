---
sigma_id: "abae8fec-57bd-4f87-aff6-6e3db989843d"
title: "AWS Snapshot Backup Exfiltration"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_snapshot_backup_exfiltration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_snapshot_backup_exfiltration.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "abae8fec-57bd-4f87-aff6-6e3db989843d"
  - "AWS Snapshot Backup Exfiltration"
attack_technique_ids:
  - "T1537"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Snapshot Backup Exfiltration

Detects the modification of an EC2 snapshot's permissions to enable access from another account

## Metadata

- Rule ID: abae8fec-57bd-4f87-aff6-6e3db989843d
- Status: test
- Level: medium
- Author: Darin Smith
- Date: 2021-05-17
- Modified: 2021-08-19
- Source Path: rules/cloud/aws/cloudtrail/aws_snapshot_backup_exfiltration.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1537-transfer_data_to_cloud_account|T1537]]

## Detection

```yaml
selection_source:
  eventSource: ec2.amazonaws.com
  eventName: ModifySnapshotAttribute
condition: selection_source
```

## False Positives

- Valid change to a snapshot's permissions

## References

- https://www.justice.gov/file/1080281/download

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_snapshot_backup_exfiltration.yml)
