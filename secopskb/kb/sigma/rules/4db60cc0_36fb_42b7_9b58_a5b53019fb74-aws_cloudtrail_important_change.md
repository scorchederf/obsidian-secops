---
sigma_id: "4db60cc0-36fb-42b7-9b58-a5b53019fb74"
title: "AWS CloudTrail Important Change"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_disable_logging.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_disable_logging.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "4db60cc0-36fb-42b7-9b58-a5b53019fb74"
  - "AWS CloudTrail Important Change"
attack_technique_ids:
  - "T1562.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS CloudTrail Important Change

Detects disabling, deleting and updating of a Trail

## Metadata

- Rule ID: 4db60cc0-36fb-42b7-9b58-a5b53019fb74
- Status: test
- Level: medium
- Author: vitaliy0x1
- Date: 2020-01-21
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_disable_logging.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Detection

```yaml
selection_source:
  eventSource: cloudtrail.amazonaws.com
  eventName:
  - StopLogging
  - UpdateTrail
  - DeleteTrail
condition: selection_source
```

## False Positives

- Valid change in a Trail

## References

- https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_disable_logging.yml)
