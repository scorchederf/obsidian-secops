---
sigma_id: "a840e606-7c8c-4684-9bc1-eb6b6155127f"
title: "PUA - AWS TruffleHog Execution"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_pua_trufflehog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_pua_trufflehog.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "a840e606-7c8c-4684-9bc1-eb6b6155127f"
  - "PUA - AWS TruffleHog Execution"
attack_technique_ids:
  - "T1555"
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - AWS TruffleHog Execution

Detects the execution of TruffleHog, a popular open-source tool used for scanning repositories for secrets and sensitive information, within an AWS environment.
It has been reported to be used by threat actors for credential harvesting. All detections should be investigated to determine if the usage is authorized by security teams or potentially malicious.

## Metadata

- Rule ID: a840e606-7c8c-4684-9bc1-eb6b6155127f
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-10-21
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_pua_trufflehog.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection:
  userAgent: TruffleHog
condition: selection
```

## False Positives

- Legitimate use of TruffleHog by security teams for credential scanning.

## References

- https://github.com/trufflesecurity/trufflehog
- https://www.rapid7.com/blog/post/tr-crimson-collective-a-new-threat-group-observed-operating-in-the-cloud/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_pua_trufflehog.yml)
