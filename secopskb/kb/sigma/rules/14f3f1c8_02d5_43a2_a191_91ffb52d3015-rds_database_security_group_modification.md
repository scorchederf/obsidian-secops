---
sigma_id: "14f3f1c8-02d5-43a2-a191-91ffb52d3015"
title: "RDS Database Security Group Modification"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_rds.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_rds.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "14f3f1c8-02d5-43a2-a191-91ffb52d3015"
  - "RDS Database Security Group Modification"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RDS Database Security Group Modification

Detects changes to the security group entries for RDS databases.
This can indicate that a misconfiguration has occurred which potentially exposes the database to the public internet, a wider audience within the VPC or that removal of valid rules has occurred which could impact the availability of the database to legitimate services and users.

## Metadata

- Rule ID: 14f3f1c8-02d5-43a2-a191-91ffb52d3015
- Status: test
- Level: medium
- Author: jamesc-grafana
- Date: 2024-07-11
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_rds.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  eventSource: rds.amazonaws.com
  eventName:
  - AuthorizeDBSecurityGroupIngress
  - CreateDBSecurityGroup
  - DeleteDBSecurityGroup
  - RevokeDBSecurityGroupIngress
condition: selection
```

## False Positives

- Creation of a new Database that needs new security group rules

## References

- https://www.gorillastack.com/blog/real-time-events/important-aws-cloudtrail-security-events-tracking/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_rds.yml)
