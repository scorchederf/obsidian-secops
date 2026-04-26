---
sigma_id: "b056de1a-6e6e-4e40-a67e-97c9808cf41b"
title: "AWS Route 53 Domain Transferred to Another Account"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_to_another_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_to_another_account.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "b056de1a-6e6e-4e40-a67e-97c9808cf41b"
  - "AWS Route 53 Domain Transferred to Another Account"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Route 53 Domain Transferred to Another Account

Detects when a request has been made to transfer a Route 53 domain to another AWS account.

## Metadata

- Rule ID: b056de1a-6e6e-4e40-a67e-97c9808cf41b
- Status: test
- Level: low
- Author: Elastic, Austin Songer @austinsonger
- Date: 2021-07-22
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_to_another_account.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  eventSource: route53.amazonaws.com
  eventName: TransferDomainToAnotherAwsAccount
condition: selection
```

## False Positives

- A domain may be transferred to another AWS account by a system or network administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment. Domain transfers from unfamiliar users or hosts should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://github.com/elastic/detection-rules/blob/c76a39796972ecde44cb1da6df47f1b6562c9770/rules/integrations/aws/persistence_route_53_domain_transferred_to_another_account.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_to_another_account.yml)
