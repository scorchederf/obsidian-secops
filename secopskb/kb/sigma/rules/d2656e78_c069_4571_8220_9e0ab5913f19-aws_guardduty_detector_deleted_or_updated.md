---
sigma_id: "d2656e78-c069-4571-8220-9e0ab5913f19"
title: "AWS GuardDuty Detector Deleted Or Updated"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/aws/cloudtrail/aws_cloudtrail_guardduty_detector_deleted_or_updated.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_guardduty_detector_deleted_or_updated.yml"
build_date: "2026-04-26 15:01:43"
status: "experimental"
level: "high"
logsource: "aws / cloudtrail"
aliases:
  - "d2656e78-c069-4571-8220-9e0ab5913f19"
  - "AWS GuardDuty Detector Deleted Or Updated"
attack_technique_ids:
  - "T1562.001"
  - "T1562.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS GuardDuty Detector Deleted Or Updated

Detects successful deletion or disabling of an AWS GuardDuty detector, possibly by an attacker trying to avoid detection of its malicious activities.
Upon deletion, GuardDuty stops monitoring the environment and all existing findings are lost.
Verify with the user identity that this activity is legitimate.

## Metadata

- Rule ID: d2656e78-c069-4571-8220-9e0ab5913f19
- Status: experimental
- Level: high
- Author: suktech24
- Date: 2025-11-27
- Source Path: rules/cloud/aws/cloudtrail/aws_cloudtrail_guardduty_detector_deleted_or_updated.yml

## Logsource

- product: aws
- service: cloudtrail

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Detection

```yaml
selection_event_source:
  eventSource: guardduty.amazonaws.com
selection_action_delete:
  eventName: DeleteDetector
selection_action_update:
  eventName: UpdateDetector
  requestParameters.enable: 'false'
selection_status_success:
  errorCode: Success
selection_status_null:
  errorCode: null
condition: selection_event_source and 1 of selection_action_* and 1 of selection_status_*
```

## False Positives

- Legitimate detector deletion by an admin (e.g., during account decommissioning).
- Temporary disablement for troubleshooting (verify via change management tickets).
- Automated deployment tools (e.g. Terraform) managing GuardDuty state.

## References

- https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteDetector.html
- https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html
- https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html
- https://docs.datadoghq.com/security/default_rules/719-39f-9cd/
- https://docs.prismacloud.io/en/enterprise-edition/policy-reference/aws-policies/aws-general-policies/ensure-aws-guardduty-detector-is-enabled
- https://docs.stellarcyber.ai/5.2.x/Using/ML/Alert-Rule-Based-Potentially_Malicious_AWS_Activity.html
- https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/Amazon%20Web%20Services/Analytic%20Rules/AWS_GuardDutyDisabled.yaml
- https://github.com/elastic/detection-rules/blob/main/rules/integrations/aws/defense_evasion_guardduty_detector_deletion.toml
- https://help.fortinet.com/fsiem/Public_Resource_Access/7_4_0/rules/PH_RULE_AWS_GuardDuty_Detector_Deletion.htm
- https://research.splunk.com/sources/5d8bd475-c8bc-4447-b27f-efa508728b90/
- https://suktech24.com/2025/07/17/aws-threat-detection-rule-guardduty-detector-disabled-or-suspended/
- https://www.atomicredteam.io/atomic-red-team/atomics/T156001#atomic-test-46---aws---guardduty-suspension-or-deletion

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/aws/cloudtrail/aws_cloudtrail_guardduty_detector_deleted_or_updated.yml)
