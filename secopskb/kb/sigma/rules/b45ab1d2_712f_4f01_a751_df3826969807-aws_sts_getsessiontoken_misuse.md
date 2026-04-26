---
sigma_id: "b45ab1d2-712f-4f01-a751-df3826969807"
title: "AWS STS GetSessionToken Misuse"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_sts_getsessiontoken_misuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_sts_getsessiontoken_misuse.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "b45ab1d2-712f-4f01-a751-df3826969807"
  - "AWS STS GetSessionToken Misuse"
attack_technique_ids:
  - "T1548"
  - "T1550"
  - "T1550.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS STS GetSessionToken Misuse

Identifies the suspicious use of GetSessionToken. Tokens could be created and used by attackers to move laterally and escalate privileges.

## Metadata

- Rule ID: b45ab1d2-712f-4f01-a751-df3826969807
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-07-24
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_sts_getsessiontoken_misuse.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.001]]

## Detection

```yaml
selection:
  eventSource: sts.amazonaws.com
  eventName: GetSessionToken
  userIdentity.type: IAMUser
condition: selection
```

## False Positives

- GetSessionToken may be done by a system or network administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment. GetSessionToken from unfamiliar users or hosts should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://github.com/elastic/detection-rules/pull/1213
- https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_sts_getsessiontoken_misuse.yml)
