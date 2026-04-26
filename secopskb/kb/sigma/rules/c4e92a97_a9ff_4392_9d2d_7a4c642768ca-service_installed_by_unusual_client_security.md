---
sigma_id: "c4e92a97-a9ff-4392-9d2d-7a4c642768ca"
title: "Service Installed By Unusual Client - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_service_installation_by_unusal_client.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_service_installation_by_unusal_client.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "c4e92a97-a9ff-4392-9d2d-7a4c642768ca"
  - "Service Installed By Unusual Client - Security"
attack_technique_ids:
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Installed By Unusual Client - Security

Detects a service installed by a client which has PID 0 or whose parent has PID 0

## Metadata

- Rule ID: c4e92a97-a9ff-4392-9d2d-7a4c642768ca
- Status: test
- Level: high
- Author: Tim Rauch (Nextron Systems), Elastic (idea)
- Date: 2022-09-15
- Modified: 2023-01-04
- Source Path: rules/windows/builtin/security/win_security_service_installation_by_unusal_client.yml

## Logsource

- definition: Requirements: The System Security Extension audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]]

## Detection

```yaml
selection_eid:
  EventID: 4697
selection_pid:
- ClientProcessId: 0
- ParentProcessId: 0
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/windows-service-installed-via-an-unusual-client.html
- https://www.x86matthew.com/view_post?id=create_svc_rpc
- https://twitter.com/SBousseaden/status/1490608838701166596

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_service_installation_by_unusal_client.yml)
