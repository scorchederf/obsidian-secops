---
sigma_id: "20f754db-d025-4a8f-9d74-e0037e999a9a"
title: "SES Identity Has Been Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_delete_identity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_delete_identity.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "aws / cloudtrail"
aliases:
  - "20f754db-d025-4a8f-9d74-e0037e999a9a"
  - "SES Identity Has Been Deleted"
attack_technique_ids:
  - "T1070"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SES Identity Has Been Deleted

Detects an instance of an SES identity being deleted via the "DeleteIdentity" event. This may be an indicator of an adversary removing the account that carried out suspicious or malicious activities

## Metadata

- Rule ID: 20f754db-d025-4a8f-9d74-e0037e999a9a
- Status: test
- Level: medium
- Author: Janantha Marasinghe
- Date: 2022-12-13
- Modified: 2022-12-28
- Source Path: rules/cloud/aws/cloudtrail/aws_delete_identity.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]

## Detection

```yaml
selection:
  eventSource: ses.amazonaws.com
  eventName: DeleteIdentity
condition: selection
```

## False Positives

- Unknown

## References

- https://unit42.paloaltonetworks.com/compromised-cloud-compute-credentials/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_delete_identity.yml)
