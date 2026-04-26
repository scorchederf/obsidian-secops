---
sigma_id: "c3f265c7-ff03-4056-8ab2-d486227b4599"
title: "Restore Public AWS RDS Instance"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_rds_public_db_restore.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_rds_public_db_restore.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "c3f265c7-ff03-4056-8ab2-d486227b4599"
  - "Restore Public AWS RDS Instance"
attack_technique_ids:
  - "T1020"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Restore Public AWS RDS Instance

Detects the recovery of a new public database instance from a snapshot. It may be a part of data exfiltration.

## Metadata

- Rule ID: c3f265c7-ff03-4056-8ab2-d486227b4599
- Status: test
- Level: high
- Author: faloker
- Date: 2020-02-12
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_rds_public_db_restore.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020]]

## Detection

```yaml
selection_source:
  eventSource: rds.amazonaws.com
  responseElements.publiclyAccessible: 'true'
  eventName: RestoreDBInstanceFromDBSnapshot
condition: selection_source
```

## False Positives

- Unknown

## References

- https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2c5b181/pacu/modules/rds__explore_snapshots/main.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_rds_public_db_restore.yml)
