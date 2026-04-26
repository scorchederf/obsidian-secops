---
sigma_id: "54b9a76a-3c71-4673-b4b3-2edb4566ea7b"
title: "AWS EC2 VM Export Failure"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_ec2_vm_export_failure.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_vm_export_failure.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "low"
logsource: "aws / cloudtrail"
aliases:
  - "54b9a76a-3c71-4673-b4b3-2edb4566ea7b"
  - "AWS EC2 VM Export Failure"
attack_technique_ids:
  - "T1005"
  - "T1537"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWS EC2 VM Export Failure

An attempt to export an AWS EC2 instance has been detected. A VM Export might indicate an attempt to extract information from an instance.

## Metadata

- Rule ID: 54b9a76a-3c71-4673-b4b3-2edb4566ea7b
- Status: test
- Level: low
- Author: Diogo Braz
- Date: 2020-04-16
- Modified: 2022-10-05
- Source Path: rules/cloud/aws/cloudtrail/aws_ec2_vm_export_failure.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]
- [[kb/attack/techniques/T1537-transfer_data_to_cloud_account|T1537]]

## Detection

```yaml
selection:
  eventName: CreateInstanceExportTask
  eventSource: ec2.amazonaws.com
filter1:
  errorMessage|contains: '*'
filter2:
  errorCode|contains: '*'
filter3:
  responseElements|contains: Failure
condition: selection and not 1 of filter*
```

## References

- https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html#export-instance

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_ec2_vm_export_failure.yml)
