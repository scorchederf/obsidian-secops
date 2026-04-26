---
sigma_id: "e386b9b5-af12-450e-afff-761730fb8a98"
title: "AWS VPC Flow Logs Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_vpc_flow_logs_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_vpc_flow_logs_deleted.yml"
build_date: "2026-04-26 14:14:20"
status: "experimental"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "e386b9b5-af12-450e-afff-761730fb8a98"
  - "AWS VPC Flow Logs Deleted"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS VPC Flow Logs Deleted

Detects the deletion of one or more VPC Flow Logs in AWS Elastic Compute Cloud (EC2) through the DeleteFlowLogs API call.
Adversaries may delete flow logs to evade detection or remove evidence of network activity, hindering forensic investigations and visibility into malicious operations.

## Metadata

- Rule ID: e386b9b5-af12-450e-afff-761730fb8a98
- Status: experimental
- Level: high
- Author: Ivan Saakov
- Date: 2025-10-19
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_vpc_flow_logs_deleted.yml

## Logsource

- product: aws
- service: cloudtrail

## Detection

```yaml
selection_event_name:
  eventName: DeleteFlowLogs
selection_status_success:
  errorCode: Success
selection_status_null:
  errorCode: null
condition: selection_event_name and 1 of selection_status_*
```

## False Positives

- During maintenance operations or testing, authorized administrators may delete VPC Flow Logs as part of routine network management or cleanup activities.

## References

- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFlowLogs.html
- https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-flow-logs.html
- https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/integrations/aws/defense_evasion_ec2_flow_log_deletion

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_vpc_flow_logs_deleted.yml)
