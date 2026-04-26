---
sigma_id: "a607e1fe-74bf-4440-a3ec-b059b9103157"
title: "AWS SecurityHub Findings Evasion"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_securityhub_finding_evasion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_securityhub_finding_evasion.yml"
build_date: "2026-04-26 17:03:18"
status: "stable"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "a607e1fe-74bf-4440-a3ec-b059b9103157"
  - "AWS SecurityHub Findings Evasion"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS SecurityHub Findings Evasion

Detects the modification of the findings on SecurityHub.

## Metadata

- Rule ID: a607e1fe-74bf-4440-a3ec-b059b9103157
- Status: stable
- Level: high
- Author: Sittikorn S
- Date: 2021-06-28
- Source Path: rules/cloud/aws/cloudtrail/aws_securityhub_finding_evasion.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  eventSource: securityhub.amazonaws.com
  eventName:
  - BatchUpdateFindings
  - DeleteInsight
  - UpdateFindings
  - UpdateInsight
condition: selection
```

## False Positives

- System or Network administrator behaviors
- DEV, UAT, SAT environment. You should apply this rule with PROD environment only.

## References

- https://docs.aws.amazon.com/cli/latest/reference/securityhub/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_securityhub_finding_evasion.yml)
