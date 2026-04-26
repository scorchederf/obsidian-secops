---
sigma_id: "3940b5f1-3f46-44aa-b746-ebe615b879e0"
title: "AWS Route 53 Domain Transfer Lock Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_lock_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_lock_disabled.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "3940b5f1-3f46-44aa-b746-ebe615b879e0"
  - "AWS Route 53 Domain Transfer Lock Disabled"
attack_technique_ids:
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Route 53 Domain Transfer Lock Disabled

Detects when a transfer lock was removed from a Route 53 domain. It is recommended to refrain from performing this action unless intending to transfer the domain to a different registrar.

## Metadata

- Rule ID: 3940b5f1-3f46-44aa-b746-ebe615b879e0
- Status: test
- Level: low
- Author: Elastic, Austin Songer @austinsonger
- Date: 2021-07-22
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_lock_disabled.yml

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
  eventName: DisableDomainTransferLock
condition: selection
```

## False Positives

- A domain transfer lock may be disabled by a system or network administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment. Activity from unfamiliar users or hosts should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://github.com/elastic/detection-rules/blob/c76a39796972ecde44cb1da6df47f1b6562c9770/rules/integrations/aws/persistence_route_53_domain_transfer_lock_disabled.toml
- https://docs.aws.amazon.com/Route53/latest/APIReference/API_Operations_Amazon_Route_53.html
- https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DisableDomainTransferLock.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_route_53_domain_transferred_lock_disabled.yml)
