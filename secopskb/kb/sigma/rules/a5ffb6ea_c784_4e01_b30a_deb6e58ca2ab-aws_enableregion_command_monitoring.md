---
sigma_id: "a5ffb6ea-c784-4e01-b30a-deb6e58ca2ab"
title: "AWS EnableRegion Command Monitoring"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_region_enabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_region_enabled.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "a5ffb6ea-c784-4e01-b30a-deb6e58ca2ab"
  - "AWS EnableRegion Command Monitoring"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS EnableRegion Command Monitoring

Detects the use of the EnableRegion command in AWS CloudTrail logs.
While AWS has 30+ regions, some of them are enabled by default, others must be explicitly enabled in each account separately.
There may be situations where security monitoring does not cover some new AWS regions.
Monitoring the EnableRegion command is important for identifying potential persistence mechanisms employed by adversaries, as enabling additional regions can facilitate continued access and operations within an AWS environment.

## Metadata

- Rule ID: a5ffb6ea-c784-4e01-b30a-deb6e58ca2ab
- Status: experimental
- Level: medium
- Author: Ivan Saakov, Sergey Zelenskiy
- Date: 2025-10-19
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_region_enabled.yml

## Logsource

- product: aws
- service: cloudtrail

## Detection

```yaml
selection:
  eventName: EnableRegion
  eventSource: account.amazonaws.com
condition: selection
```

## False Positives

- Legitimate use of the EnableRegion command by authorized administrators.

## References

- https://docs.aws.amazon.com/accounts/latest/reference/API_EnableRegion.html
- https://awscli.amazonaws.com/v2/documentation/api/2.14.0/reference/account/enable-region.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_region_enabled.yml)
