---
sigma_id: "97fbabf8-8e1b-47a2-b7d5-a418d2b95e3d"
title: "AWS New Lambda Layer Attached"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_new_lambda_layer_attached.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_new_lambda_layer_attached.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "97fbabf8-8e1b-47a2-b7d5-a418d2b95e3d"
  - "AWS New Lambda Layer Attached"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS New Lambda Layer Attached

Detects when a user attached a Lambda layer to an existing Lambda function.
A malicious Lambda layer could execute arbitrary code in the context of the function's IAM role.
This would give an adversary access to resources that the function has access to.

## Metadata

- Rule ID: 97fbabf8-8e1b-47a2-b7d5-a418d2b95e3d
- Status: test
- Level: low
- Author: Austin Songer
- Date: 2021-09-23
- Modified: 2025-03-17
- Source Path: rules/cloud/aws/cloudtrail/aws_new_lambda_layer_attached.yml

## Logsource

- product: aws
- service: cloudtrail

## Detection

```yaml
selection:
  eventSource: lambda.amazonaws.com
  eventName|startswith: UpdateFunctionConfiguration
  requestParameters.layers|contains: '*'
condition: selection
```

## False Positives

- Lambda Layer being attached may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Lambda Layer being attached from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionConfiguration.html
- https://github.com/clearvector/lambda-spy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_new_lambda_layer_attached.yml)
