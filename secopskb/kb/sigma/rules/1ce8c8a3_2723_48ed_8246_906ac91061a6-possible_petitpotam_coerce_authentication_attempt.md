---
sigma_id: "1ce8c8a3-2723-48ed-8246-906ac91061a6"
title: "Possible PetitPotam Coerce Authentication Attempt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_petitpotam_network_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_petitpotam_network_share.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "1ce8c8a3-2723-48ed-8246-906ac91061a6"
  - "Possible PetitPotam Coerce Authentication Attempt"
attack_technique_ids:
  - "T1187"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Possible PetitPotam Coerce Authentication Attempt

Detect PetitPotam coerced authentication activity.

## Metadata

- Rule ID: 1ce8c8a3-2723-48ed-8246-906ac91061a6
- Status: test
- Level: high
- Author: Mauricio Velazco, Michael Haag
- Date: 2021-09-02
- Modified: 2022-08-11
- Source Path: rules/windows/builtin/security/win_security_petitpotam_network_share.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1187-forced_authentication|T1187]]

## Detection

```yaml
selection:
  EventID: 5145
  ShareName|startswith: \\\\
  ShareName|endswith: \IPC$
  RelativeTargetName: lsarpc
  SubjectUserName: ANONYMOUS LOGON
condition: selection
```

## False Positives

- Unknown. Feedback welcomed.

## References

- https://github.com/topotam/PetitPotam
- https://github.com/splunk/security_content/blob/0dd6de32de2118b2818550df9e65255f4109a56d/detections/endpoint/petitpotam_network_share_access_request.yml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_petitpotam_network_share.yml)
