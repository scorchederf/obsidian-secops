---
sigma_id: "4ae68615-866f-4304-b24b-ba048dfa5ca7"
title: "AWS ElastiCache Security Group Created"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_elasticache_security_group_created.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_elasticache_security_group_created.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "4ae68615-866f-4304-b24b-ba048dfa5ca7"
  - "AWS ElastiCache Security Group Created"
attack_technique_ids:
  - "T1136"
  - "T1136.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS ElastiCache Security Group Created

Detects when an ElastiCache security group has been created.

## Metadata

- Rule ID: 4ae68615-866f-4304-b24b-ba048dfa5ca7
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-07-24
- Modified: 2022-10-09
- Source Path: rules/cloud/aws/cloudtrail/aws_elasticache_security_group_created.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136]]
- [[kb/attack/techniques/T1136-create_account|T1136.003]]

## Detection

```yaml
selection:
  eventSource: elasticache.amazonaws.com
  eventName: CreateCacheSecurityGroup
condition: selection
```

## False Positives

- A ElastiCache security group may be created by a system or network administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment. Security group creations from unfamiliar users or hosts should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://github.com/elastic/detection-rules/blob/598f3d7e0a63221c0703ad9a0ea7e22e7bc5961e/rules/integrations/aws/persistence_elasticache_security_group_creation.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_elasticache_security_group_created.yml)
