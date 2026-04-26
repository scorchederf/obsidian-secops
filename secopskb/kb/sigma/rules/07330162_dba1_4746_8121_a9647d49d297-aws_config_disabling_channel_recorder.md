---
sigma_id: "07330162-dba1-4746-8121-a9647d49d297"
title: "AWS Config Disabling Channel/Recorder"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_config_disable_recording.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_config_disable_recording.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "07330162-dba1-4746-8121-a9647d49d297"
  - "AWS Config Disabling Channel/Recorder"
attack_technique_ids:
  - "T1562.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS Config Disabling Channel/Recorder

Detects AWS Config Service disabling

## Metadata

- Rule ID: 07330162-dba1-4746-8121-a9647d49d297
- Status: test
- Level: high
- Author: vitaliy0x1
- Date: 2020-01-21
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_config_disable_recording.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Detection

```yaml
selection:
  eventSource: config.amazonaws.com
  eventName:
  - DeleteDeliveryChannel
  - StopConfigurationRecorder
condition: selection
```

## False Positives

- Valid change in AWS Config Service

## References

- https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-log-files-for-aws-config.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_config_disable_recording.yml)
