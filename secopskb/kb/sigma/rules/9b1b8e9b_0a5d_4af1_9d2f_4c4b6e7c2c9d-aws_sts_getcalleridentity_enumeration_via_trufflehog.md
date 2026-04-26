---
sigma_id: "9b1b8e9b-0a5d-4af1-9d2f-4c4b6e7c2c9d"
title: "AWS STS GetCallerIdentity Enumeration Via TruffleHog"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_sts_getcalleridentity_trufflehog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_sts_getcalleridentity_trufflehog.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "9b1b8e9b-0a5d-4af1-9d2f-4c4b6e7c2c9d"
  - "AWS STS GetCallerIdentity Enumeration Via TruffleHog"
attack_technique_ids:
  - "T1087.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS STS GetCallerIdentity Enumeration Via TruffleHog

Detects the use of TruffleHog for AWS credential validation by identifying GetCallerIdentity API calls where the userAgent indicates TruffleHog.
Threat actors leverage TruffleHog to enumerate and validate exposed AWS keys.
Successful exploitation allows threat actors to confirm the validity of compromised AWS credentials, facilitating further unauthorized access and actions within the AWS environment.

## Metadata

- Rule ID: 9b1b8e9b-0a5d-4af1-9d2f-4c4b6e7c2c9d
- Status: experimental
- Level: medium
- Author: Adan Alvarez @adanalvarez
- Date: 2025-10-12
- Source Path: rules/cloud/aws/cloudtrail/aws_sts_getcalleridentity_trufflehog.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.004]]

## Detection

```yaml
selection:
  eventSource: sts.amazonaws.com
  eventName: GetCallerIdentity
  userAgent|contains: TruffleHog
condition: selection
```

## False Positives

- Legitimate internal security scanning or key validation that intentionally uses TruffleHog. Authorize and filter known scanner roles, IP ranges, or assumed roles as needed.

## References

- https://www.rapid7.com/blog/post/tr-crimson-collective-a-new-threat-group-observed-operating-in-the-cloud/
- https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html
- https://github.com/trufflesecurity/trufflehog

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_sts_getcalleridentity_trufflehog.yml)
