---
sigma_id: "e1f7febb-7b94-4234-b5c6-00fb8500f5dd"
title: "New Network ACL Entry Added"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_new_acl_entries.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_new_acl_entries.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "e1f7febb-7b94-4234-b5c6-00fb8500f5dd"
  - "New Network ACL Entry Added"
attack_technique_ids:
  - "T1562.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Network ACL Entry Added

Detects that network ACL entries have been added to a route table which could indicate that new attack vectors have been opened up in the AWS account.

## Metadata

- Rule ID: e1f7febb-7b94-4234-b5c6-00fb8500f5dd
- Status: test
- Level: low
- Author: jamesc-grafana
- Date: 2024-07-11
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_new_acl_entries.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.007]]

## Detection

```yaml
selection:
  eventSource: ec2.amazonaws.com
  eventName: CreateNetworkAclEntry
condition: selection
```

## False Positives

- Legitimate use of ACLs to enable customer and staff access from the public internet into a public VPC

## References

- https://www.gorillastack.com/blog/real-time-events/important-aws-cloudtrail-security-events-tracking/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_new_acl_entries.yml)
