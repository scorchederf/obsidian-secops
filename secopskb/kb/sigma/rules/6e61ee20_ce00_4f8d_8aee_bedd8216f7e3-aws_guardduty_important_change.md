---
sigma_id: "6e61ee20-ce00-4f8d-8aee-bedd8216f7e3"
title: "AWS GuardDuty Important Change"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_guardduty_disruption.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_guardduty_disruption.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "6e61ee20-ce00-4f8d-8aee-bedd8216f7e3"
  - "AWS GuardDuty Important Change"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects updates of the GuardDuty list of trusted IPs, perhaps to disable security alerts against malicious IPs.

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection_source:
  eventSource: guardduty.amazonaws.com
  eventName: CreateIPSet
condition: selection_source
```

## False Positives

- Valid change in the GuardDuty (e.g. to ignore internal scanners)

## References

- https://github.com/RhinoSecurityLabs/pacu/blob/866376cd711666c775bbfcde0524c817f2c5b181/pacu/modules/guardduty__whitelist_ip/main.py#L9

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_guardduty_disruption.yml)
