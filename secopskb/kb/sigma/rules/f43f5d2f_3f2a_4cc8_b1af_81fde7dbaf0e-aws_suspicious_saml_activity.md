---
sigma_id: "f43f5d2f-3f2a-4cc8-b1af-81fde7dbaf0e"
title: "AWS Suspicious SAML Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_susp_saml_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_susp_saml_activity.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "f43f5d2f-3f2a-4cc8-b1af-81fde7dbaf0e"
  - "AWS Suspicious SAML Activity"
attack_technique_ids:
  - "T1078"
  - "T1548"
  - "T1550"
  - "T1550.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Suspicious SAML Activity

Identifies when suspicious SAML activity has occurred in AWS. An adversary could gain backdoor access via SAML.

## Metadata

- Rule ID: f43f5d2f-3f2a-4cc8-b1af-81fde7dbaf0e
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-09-22
- Modified: 2022-12-18
- Source Path: rules/cloud/aws/cloudtrail/aws_susp_saml_activity.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.001]]

## Detection

```yaml
selection_sts:
  eventSource: sts.amazonaws.com
  eventName: AssumeRoleWithSAML
selection_iam:
  eventSource: iam.amazonaws.com
  eventName: UpdateSAMLProvider
condition: 1 of selection_*
```

## False Positives

- Automated processes that uses Terraform may lead to false positives.
- SAML Provider could be updated by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- SAML Provider being updated from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateSAMLProvider.html
- https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_susp_saml_activity.yml)
