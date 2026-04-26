---
sigma_id: "ccd6a6c8-bb4e-4a91-9d2a-07e632819374"
title: "AWS SAML Provider Deletion Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_delete_saml_provider.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_delete_saml_provider.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "ccd6a6c8-bb4e-4a91-9d2a-07e632819374"
  - "AWS SAML Provider Deletion Activity"
attack_technique_ids:
  - "T1078.004"
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS SAML Provider Deletion Activity

Detects the deletion of an AWS SAML provider, potentially indicating malicious intent to disrupt administrative or security team access.
An attacker can remove the SAML provider for the information security team or a team of system administrators, to make it difficult for them to work and investigate at the time of the attack and after it.

## Metadata

- Rule ID: ccd6a6c8-bb4e-4a91-9d2a-07e632819374
- Status: experimental
- Level: medium
- Author: Ivan Saakov
- Date: 2024-12-19
- Source Path: rules/cloud/aws/cloudtrail/aws_delete_saml_provider.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]
- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  eventSource: iam.amazonaws.com
  eventName: DeleteSAMLProvider
  status: success
condition: selection
```

## False Positives

- Automated processes using tools like Terraform may trigger this alert.
- Legitimate administrative actions by authorized system administrators could cause this alert. Verify the user identity, user agent, and hostname to ensure they are expected.
- Deletions by unfamiliar users should be investigated. If the behavior is known and expected, it can be exempted from the rule.

## References

- https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteSAMLProvider.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_delete_saml_provider.yml)
