---
sigma_id: "13f2d3f5-6497-44a7-bf5f-dc13ffafe5dc"
title: "Azure Login Bypassing Conditional Access Policies"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/audit/microsoft365_bypass_conditional_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/audit/microsoft365_bypass_conditional_access.yml"
build_date: "2026-04-26 17:03:18"
status: "experimental"
level: "high"
logsource: "m365 / audit"
aliases:
  - "13f2d3f5-6497-44a7-bf5f-dc13ffafe5dc"
  - "Azure Login Bypassing Conditional Access Policies"
attack_technique_ids:
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure Login Bypassing Conditional Access Policies

Detects a successful login to the Microsoft Intune Company Portal which could allow bypassing Conditional Access Policies and InTune device trust using a tool like TokenSmith.

## Metadata

- Rule ID: 13f2d3f5-6497-44a7-bf5f-dc13ffafe5dc
- Status: experimental
- Level: high
- Author: Josh Nickels, Marius Rothenbücher
- Date: 2025-01-08
- Source Path: rules/cloud/m365/audit/microsoft365_bypass_conditional_access.yml

## Logsource

- product: m365
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection:
  Operation: UserLoggedIn
  ApplicationId: 9ba1a5c7-f17a-4de9-a1f1-6178c8d51223
  ResultStatus: Success
  RequestType: Cmsi:Cmsi
filter_main_bjectid:
  ObjectId: 0000000a-0000-0000-c000-000000000000
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://labs.jumpsec.com/tokensmith-bypassing-intune-compliant-device-conditional-access/
- https://github.com/JumpsecLabs/TokenSmith

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/audit/microsoft365_bypass_conditional_access.yml)
