---
sigma_id: "60de9b57-dc4d-48b9-a6a0-b39e0469f876"
title: "Disabling Multi Factor Authentication"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/audit/microsoft365_disabling_mfa.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/audit/microsoft365_disabling_mfa.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "m365 / audit"
aliases:
  - "60de9b57-dc4d-48b9-a6a0-b39e0469f876"
  - "Disabling Multi Factor Authentication"
attack_technique_ids:
  - "T1556.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disabling Multi Factor Authentication

Detects disabling of Multi Factor Authentication.

## Metadata

- Rule ID: 60de9b57-dc4d-48b9-a6a0-b39e0469f876
- Status: test
- Level: high
- Author: Splunk Threat Research Team (original rule), Harjot Singh @cyb3rjy0t (sigma rule)
- Date: 2023-09-18
- Source Path: rules/cloud/m365/audit/microsoft365_disabling_mfa.yml

## Logsource

- product: m365
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.006]]

## Detection

```yaml
selection:
  Operation|contains: Disable Strong Authentication.
condition: selection
```

## False Positives

- Unlikely

## References

- https://research.splunk.com/cloud/c783dd98-c703-4252-9e8a-f19d9f5c949e/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/audit/microsoft365_disabling_mfa.yml)
