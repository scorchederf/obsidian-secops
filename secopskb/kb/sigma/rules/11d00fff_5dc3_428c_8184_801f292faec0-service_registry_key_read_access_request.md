---
sigma_id: "11d00fff-5dc3-428c-8184-801f292faec0"
title: "Service Registry Key Read Access Request"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_registry_permissions_weakness_check.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_registry_permissions_weakness_check.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "11d00fff-5dc3-428c-8184-801f292faec0"
  - "Service Registry Key Read Access Request"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Registry Key Read Access Request

Detects "read access" requests on the services registry key.
Adversaries may execute their own malicious payloads by hijacking the Registry entries used by services.
Adversaries may use flaws in the permissions for Registry keys related to services to redirect from the originally specified executable to one that they control, in order to launch their own code when a service starts.

## Metadata

- Rule ID: 11d00fff-5dc3-428c-8184-801f292faec0
- Status: test
- Level: low
- Author: Center for Threat Informed Defense (CTID) Summiting the Pyramid Team
- Date: 2023-09-28
- Source Path: rules/windows/builtin/security/win_security_registry_permissions_weakness_check.yml

## Logsource

- definition: Requirements: SACLs must be enabled for "READ_CONTROL" on the registry keys used in this rule
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection:
  EventID: 4663
  ObjectName|contains|all:
  - \SYSTEM\
  - ControlSet\Services\
  AccessList|contains: '%%1538'
condition: selection
```

## False Positives

- Likely from legitimate applications reading their key. Requires heavy tuning

## References

- https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/analytics/service_registry_permissions_weakness_check/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1574.011/T1574.011.md#atomic-test-1---service-registry-permissions-weakness

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_registry_permissions_weakness_check.yml)
