---
sigma_id: "38e7f511-3f74-41d4-836e-f57dfa18eead"
title: "Potential Malicious Usage of CloudTrail System Manager"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_ssm_malicious_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_ssm_malicious_usage.yml"
build_date: "2026-04-27 19:13:54"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect when System Manager successfully executes commands against an instance.

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566: Phishing]]
- [[kb/attack/techniques/T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]

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
