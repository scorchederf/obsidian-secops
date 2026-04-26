---
sigma_id: "ec541962-c05a-4420-b9ea-84de072d18f4"
title: "New AWS Lambda Function URL Configuration Created"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_lambda_function_url.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_lambda_function_url.yml"
build_date: "2026-04-26 14:14:29"
status: "experimental"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "ec541962-c05a-4420-b9ea-84de072d18f4"
  - "New AWS Lambda Function URL Configuration Created"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New AWS Lambda Function URL Configuration Created

Detects when a user creates a Lambda function URL configuration, which could be used to expose the function to the internet and potentially allow unauthorized access to the function's IAM role for AWS API calls.
This could give an adversary access to the privileges associated with the Lambda service role that is attached to that function.

## Metadata

- Rule ID: ec541962-c05a-4420-b9ea-84de072d18f4
- Status: experimental
- Level: medium
- Author: Ivan Saakov
- Date: 2024-12-19
- Source Path: rules/cloud/aws/cloudtrail/aws_lambda_function_url.yml

## Logsource

- product: aws
- service: cloudtrail

## Detection

```yaml
selection:
  eventSource: lambda.amazonaws.com
  eventName: CreateFunctionUrlConfig
condition: selection
```

## False Positives

- Creating a Lambda function URL configuration may be performed by a system administrator. Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Creating a Lambda function URL configuration from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunctionUrlConfig.html
- https://cloud.hacktricks.xyz/pentesting-cloud/aws-security/aws-privilege-escalation/aws-lambda-privesc
- https://www.wiz.io/blog/how-to-set-secure-defaults-on-aws

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_lambda_function_url.yml)
