---
sigma_id: "38e7f511-3f74-41d4-836e-f57dfa18eead"
title: "Potential Malicious Usage of CloudTrail System Manager"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_ssm_malicious_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_ssm_malicious_usage.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "38e7f511-3f74-41d4-836e-f57dfa18eead"
  - "Potential Malicious Usage of CloudTrail System Manager"
attack_technique_ids:
  - "T1566"
  - "T1566.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Malicious Usage of CloudTrail System Manager

Detect when System Manager successfully executes commands against an instance.

## Metadata

- Rule ID: 38e7f511-3f74-41d4-836e-f57dfa18eead
- Status: test
- Level: high
- Author: jamesc-grafana
- Date: 2024-07-11
- Modified: 2025-12-08
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_ssm_malicious_usage.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566]]
- [[kb/attack/techniques/T1566-phishing|T1566.002]]

## Detection

```yaml
selection_event:
  eventName: SendCommand
  eventSource: ssm.amazonaws.com
selection_status_success:
  errorCode: Success
selection_status_null:
  errorCode: null
condition: selection_event and 1 of selection_status_*
```

## False Positives

- There are legitimate uses of SSM to send commands to EC2 instances
- Legitimate users may have to use SSM to perform actions against machines in the Cloud to update or maintain them

## References

- https://github.com/elastic/detection-rules/blob/v8.6.0/rules/integrations/aws/initial_access_via_system_manager.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_ssm_malicious_usage.yml)
