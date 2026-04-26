---
sigma_id: "7c797da2-9cf2-4523-ba64-33b06339f0cc"
title: "AWS ElastiCache Security Group Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_elasticache_security_group_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_elasticache_security_group_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "7c797da2-9cf2-4523-ba64-33b06339f0cc"
  - "AWS ElastiCache Security Group Modified or Deleted"
attack_technique_ids:
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS ElastiCache Security Group Modified or Deleted

Identifies when an ElastiCache security group has been modified or deleted.

## Metadata

- Rule ID: 7c797da2-9cf2-4523-ba64-33b06339f0cc
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-07-24
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_elasticache_security_group_modified_or_deleted.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  eventSource: elasticache.amazonaws.com
  eventName:
  - DeleteCacheSecurityGroup
  - AuthorizeCacheSecurityGroupIngress
  - RevokeCacheSecurityGroupIngress
  - AuthorizeCacheSecurityGroupEgress
  - RevokeCacheSecurityGroupEgress
condition: selection
```

## False Positives

- A ElastiCache security group deletion may be done by a system or network administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment. Security Group deletions from unfamiliar users or hosts should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://github.com/elastic/detection-rules/blob/7d5efd68603f42be5e125b5a6a503b2ef3ac0f4e/rules/integrations/aws/impact_elasticache_security_group_modified_or_deleted.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_elasticache_security_group_modified_or_deleted.yml)
