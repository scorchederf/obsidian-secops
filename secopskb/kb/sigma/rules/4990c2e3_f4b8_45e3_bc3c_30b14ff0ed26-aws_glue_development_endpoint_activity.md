---
sigma_id: "4990c2e3-f4b8-45e3-bc3c-30b14ff0ed26"
title: "AWS Glue Development Endpoint Activity"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_passed_role_to_glue_development_endpoint.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_passed_role_to_glue_development_endpoint.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "4990c2e3-f4b8-45e3-bc3c-30b14ff0ed26"
  - "AWS Glue Development Endpoint Activity"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS Glue Development Endpoint Activity

Detects possible suspicious glue development endpoint activity.

## Metadata

- Rule ID: 4990c2e3-f4b8-45e3-bc3c-30b14ff0ed26
- Status: test
- Level: low
- Author: Austin Songer @austinsonger
- Date: 2021-10-03
- Modified: 2022-12-18
- Source Path: rules/cloud/aws/cloudtrail/aws_passed_role_to_glue_development_endpoint.yml

## Logsource

- product: aws
- service: cloudtrail

## Detection

```yaml
selection:
  eventSource: glue.amazonaws.com
  eventName:
  - CreateDevEndpoint
  - DeleteDevEndpoint
  - UpdateDevEndpoint
condition: selection
```

## False Positives

- Glue Development Endpoint Activity may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/
- https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDevEndpoint.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_passed_role_to_glue_development_endpoint.yml)
