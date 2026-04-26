---
sigma_id: "8a63cdd4-6207-414a-85bc-7e032bd3c1a2"
title: "AWS RDS Master Password Change"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_rds_change_master_password.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_rds_change_master_password.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "8a63cdd4-6207-414a-85bc-7e032bd3c1a2"
  - "AWS RDS Master Password Change"
attack_technique_ids:
  - "T1020"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS RDS Master Password Change

Detects the change of database master password. It may be a part of data exfiltration.

## Metadata

- Rule ID: 8a63cdd4-6207-414a-85bc-7e032bd3c1a2
- Status: test
- Level: medium
- Author: faloker
- Date: 2020-02-12
- Modified: 2022-10-05
- Source Path: rules/cloud/aws/cloudtrail/aws_rds_change_master_password.yml

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
  responseElements.pendingModifiedValues.masterUserPassword|contains: '*'
  eventName: ModifyDBInstance
condition: selection_source
```

## False Positives

- Benign changes to a db instance

## References

- https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2c5b181/pacu/modules/rds__explore_snapshots/main.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_rds_change_master_password.yml)
