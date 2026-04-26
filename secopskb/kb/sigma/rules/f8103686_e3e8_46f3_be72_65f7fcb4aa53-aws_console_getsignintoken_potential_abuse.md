---
sigma_id: "f8103686-e3e8-46f3-be72-65f7fcb4aa53"
title: "AWS Console GetSigninToken Potential Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_console_getsignintoken.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_console_getsignintoken.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "f8103686-e3e8-46f3-be72-65f7fcb4aa53"
  - "AWS Console GetSigninToken Potential Abuse"
attack_technique_ids:
  - "T1021.007"
  - "T1550.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Console GetSigninToken Potential Abuse

Detects potentially suspicious events involving "GetSigninToken".
An adversary using the "aws_consoler" tool can leverage this console API to create temporary federated credential that help obfuscate which AWS credential is compromised (the original access key) and enables the adversary to pivot from the AWS CLI to console sessions without the need for MFA using the new access key issued in this request.

## Metadata

- Rule ID: f8103686-e3e8-46f3-be72-65f7fcb4aa53
- Status: test
- Level: medium
- Author: Chester Le Bron (@123Le_Bron)
- Date: 2024-02-26
- Source Path: rules/cloud/aws/cloudtrail/aws_console_getsignintoken.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.007]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.001]]

## Detection

```yaml
selection:
  eventSource: signin.amazonaws.com
  eventName: GetSigninToken
filter_main_console_ua:
  userAgent|contains: Jersey/${project.version}
condition: selection and not 1 of filter_main_*
```

## False Positives

- GetSigninToken events will occur when using AWS SSO portal to login and will generate false positives if you do not filter for the expected user agent(s), see filter. Non-SSO configured roles would be abnormal and should be investigated.

## References

- https://github.com/NetSPI/aws_consoler
- https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_console_getsignintoken.yml)
