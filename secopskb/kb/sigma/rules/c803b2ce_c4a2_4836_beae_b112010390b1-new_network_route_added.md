---
sigma_id: "c803b2ce-c4a2-4836-beae-b112010390b1"
title: "New Network Route Added"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_new_route_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_new_route_added.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "c803b2ce-c4a2-4836-beae-b112010390b1"
  - "New Network Route Added"
attack_technique_ids:
  - "T1562.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Network Route Added

Detects the addition of a new network route to a route table in AWS.

## Metadata

- Rule ID: c803b2ce-c4a2-4836-beae-b112010390b1
- Status: test
- Level: medium
- Author: jamesc-grafana
- Date: 2024-07-11
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_new_route_added.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.007]]

## Detection

```yaml
selection:
  eventSource: ec2.amazonaws.com
  eventName: CreateRoute
condition: selection
```

## False Positives

- New VPC Creation requiring setup of a new route table
- New subnets added requiring routing setup

## References

- https://www.gorillastack.com/blog/real-time-events/important-aws-cloudtrail-security-events-tracking/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_new_route_added.yml)
