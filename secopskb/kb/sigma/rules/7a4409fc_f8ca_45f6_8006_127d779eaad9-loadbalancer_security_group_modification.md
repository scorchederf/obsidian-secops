---
sigma_id: "7a4409fc-f8ca-45f6-8006-127d779eaad9"
title: "LoadBalancer Security Group Modification"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_loadbalancer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_loadbalancer.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "7a4409fc-f8ca-45f6-8006-127d779eaad9"
  - "LoadBalancer Security Group Modification"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LoadBalancer Security Group Modification

Detects changes to the security groups associated with an Elastic Load Balancer (ELB) or Application Load Balancer (ALB).
This can indicate that a misconfiguration allowing more traffic into the system than required, or could indicate that an attacker is attempting to enable new connections into a VPC or subnet controlled by the account.

## Metadata

- Rule ID: 7a4409fc-f8ca-45f6-8006-127d779eaad9
- Status: test
- Level: medium
- Author: jamesc-grafana
- Date: 2024-07-11
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_loadbalancer.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  eventSource: elasticloadbalancing.amazonaws.com
  eventName:
  - ApplySecurityGroupsToLoadBalancer
  - SetSecurityGroups
condition: selection
```

## False Positives

- Repurposing of an ELB or ALB to serve a different or additional application
- Changes to security groups to allow for new services to be deployed

## References

- https://www.gorillastack.com/blog/real-time-events/important-aws-cloudtrail-security-events-tracking/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_security_group_change_loadbalancer.yml)
