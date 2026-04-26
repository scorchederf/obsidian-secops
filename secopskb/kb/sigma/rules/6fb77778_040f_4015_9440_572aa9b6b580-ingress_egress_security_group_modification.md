---
sigma_id: "6fb77778-040f-4015-9440-572aa9b6b580"
title: "Ingress/Egress Security Group Modification"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_ingress_egress.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_ingress_egress.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "6fb77778-040f-4015-9440-572aa9b6b580"
  - "Ingress/Egress Security Group Modification"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Ingress/Egress Security Group Modification

Detects when an account makes changes to the ingress or egress rules of a security group.
This can indicate that an attacker is attempting to open up new attack vectors in the account, that they are trying to exfiltrate data over the network, or that they are trying to allow machines in that VPC/Subnet to contact a C&C server.

## Metadata

- Rule ID: 6fb77778-040f-4015-9440-572aa9b6b580
- Status: test
- Level: medium
- Author: jamesc-grafana
- Date: 2024-07-11
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_ingress_egress.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  eventSource: ec2.amazonaws.com
  eventName:
  - AuthorizeSecurityGroupEgress
  - AuthorizeSecurityGroupIngress
  - RevokeSecurityGroupEgress
  - RevokeSecurityGroupIngress
condition: selection
```

## False Positives

- New VPCs and Subnets being setup requiring a different security profile to those already defined
- A single port being opened for a new service that is known to be deploying
- Administrators closing unused ports to reduce the attack surface

## References

- https://www.gorillastack.com/blog/real-time-events/important-aws-cloudtrail-security-events-tracking/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_ingress_egress.yml)
