---
sigma_id: "33d50d03-20ec-4b74-a74e-1e65a38af1c0"
title: "AWS EKS Cluster Created or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_eks_cluster_created_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_eks_cluster_created_or_deleted.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "33d50d03-20ec-4b74-a74e-1e65a38af1c0"
  - "AWS EKS Cluster Created or Deleted"
attack_technique_ids:
  - "T1485"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS EKS Cluster Created or Deleted

Identifies when an EKS cluster is created or deleted.

## Metadata

- Rule ID: 33d50d03-20ec-4b74-a74e-1e65a38af1c0
- Status: test
- Level: low
- Author: Austin Songer
- Date: 2021-08-16
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_eks_cluster_created_or_deleted.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1485-data_destruction|T1485]]

## Detection

```yaml
selection:
  eventSource: eks.amazonaws.com
  eventName:
  - CreateCluster
  - DeleteCluster
condition: selection
```

## False Positives

- EKS Cluster being created or deleted may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- EKS Cluster created or deleted from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://any-api.com/amazonaws_com/eks/docs/API_Description

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_eks_cluster_created_or_deleted.yml)
