---
sigma_id: "d3adb3ef-b7e7-4003-9092-1924c797db35"
title: "AWS Identity Center Identity Provider Change"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_sso_idp_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_sso_idp_change.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "d3adb3ef-b7e7-4003-9092-1924c797db35"
  - "AWS Identity Center Identity Provider Change"
attack_technique_ids:
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AWS Identity Center Identity Provider Change

Detects a change in the AWS Identity Center (FKA AWS SSO) identity provider.
A change in identity provider allows an attacker to establish persistent access or escalate privileges via user impersonation.

## Metadata

- Rule ID: d3adb3ef-b7e7-4003-9092-1924c797db35
- Status: test
- Level: high
- Author: Michael McIntyre @wtfender
- Date: 2023-09-27
- Source Path: rules/cloud/aws/cloudtrail/aws_sso_idp_change.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  eventSource:
  - sso-directory.amazonaws.com
  - sso.amazonaws.com
  eventName:
  - AssociateDirectory
  - DisableExternalIdPConfigurationForDirectory
  - DisassociateDirectory
  - EnableExternalIdPConfigurationForDirectory
condition: selection
```

## False Positives

- Authorized changes to the AWS account's identity provider

## References

- https://docs.aws.amazon.com/singlesignon/latest/userguide/app-enablement.html
- https://docs.aws.amazon.com/singlesignon/latest/userguide/sso-info-in-cloudtrail.html
- https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiamidentitycentersuccessortoawssinglesign-on.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_sso_idp_change.yml)
