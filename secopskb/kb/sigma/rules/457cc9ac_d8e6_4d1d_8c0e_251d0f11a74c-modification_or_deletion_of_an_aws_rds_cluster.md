---
sigma_id: "457cc9ac-d8e6-4d1d-8c0e-251d0f11a74c"
title: "Modification or Deletion of an AWS RDS Cluster"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_rds_dbcluster_actions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_rds_dbcluster_actions.yml"
build_date: "2026-04-26 14:14:29"
status: "experimental"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "457cc9ac-d8e6-4d1d-8c0e-251d0f11a74c"
  - "Modification or Deletion of an AWS RDS Cluster"
attack_technique_ids:
  - "T1020"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Modification or Deletion of an AWS RDS Cluster

Detects modifications to an RDS cluster or its deletion, which may indicate potential data exfiltration attempts, unauthorized access, or exposure of sensitive information.

## Metadata

- Rule ID: 457cc9ac-d8e6-4d1d-8c0e-251d0f11a74c
- Status: experimental
- Level: high
- Author: Ivan Saakov
- Date: 2024-12-06
- Source Path: rules/cloud/aws/cloudtrail/aws_rds_dbcluster_actions.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020]]

## Detection

```yaml
selection:
  eventSource: rds.amazonaws.com
  eventName:
  - ModifyDBCluster
  - DeleteDBCluster
condition: selection
```

## False Positives

- Verify if the modification or deletion was performed by an authorized administrator.
- Confirm if the modification or deletion was part of a planned change or maintenance activity.

## References

- https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html
- https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBCluster.html
- https://cloud.hacktricks.xyz/pentesting-cloud/aws-security/aws-privilege-escalation/aws-rds-privesc#rds-modifydbinstance

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_rds_dbcluster_actions.yml)
