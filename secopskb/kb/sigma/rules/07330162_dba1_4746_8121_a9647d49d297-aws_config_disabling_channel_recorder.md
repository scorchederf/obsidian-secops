---
sigma_id: "07330162-dba1-4746-8121-a9647d49d297"
title: "AWS Config Disabling Channel/Recorder"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_config_disable_recording.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_config_disable_recording.yml"
build_date: "2026-04-27 19:13:50"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects AWS Config Service disabling

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562008-disable-or-modify-cloud-logs|T1562.008: Disable or Modify Cloud Logs]]

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
