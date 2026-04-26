---
sigma_id: "ab4561b1-6c7e-48a7-ad08-087cfb9ce8f1"
title: "Important Windows Event Auditing Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_disable_event_auditing_critical.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_disable_event_auditing_critical.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "ab4561b1-6c7e-48a7-ad08-087cfb9ce8f1"
  - "Important Windows Event Auditing Disabled"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Important Windows Event Auditing Disabled

Detects scenarios where system auditing for important events such as "Process Creation" or "Logon" events is disabled.

## Metadata

- Rule ID: ab4561b1-6c7e-48a7-ad08-087cfb9ce8f1
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-20
- Modified: 2023-11-17
- Source Path: rules/windows/builtin/security/win_security_disable_event_auditing_critical.yml

## Logsource

- definition: dfd8c0f4-e6ad-4e07-b91b-f2fca0ddef64
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection_state_success_and_failure:
  EventID: 4719
  SubcategoryGuid:
  - '{0CCE9210-69AE-11D9-BED3-505054503030}'
  - '{0CCE9211-69AE-11D9-BED3-505054503030}'
  - '{0CCE9212-69AE-11D9-BED3-505054503030}'
  - '{0CCE9215-69AE-11D9-BED3-505054503030}'
  - '{0CCE921B-69AE-11D9-BED3-505054503030}'
  - '{0CCE922B-69AE-11D9-BED3-505054503030}'
  - '{0CCE922F-69AE-11D9-BED3-505054503030}'
  - '{0CCE9230-69AE-11D9-BED3-505054503030}'
  - '{0CCE9235-69AE-11D9-BED3-505054503030}'
  - '{0CCE9236-69AE-11D9-BED3-505054503030}'
  - '{0CCE9237-69AE-11D9-BED3-505054503030}'
  - '{0CCE923F-69AE-11D9-BED3-505054503030}'
  - '{0CCE9240-69AE-11D9-BED3-505054503030}'
  - '{0CCE9242-69AE-11D9-BED3-505054503030}'
  AuditPolicyChanges|contains:
  - '%%8448'
  - '%%8450'
selection_state_success_only:
  EventID: 4719
  SubcategoryGuid: '{0CCE9217-69AE-11D9-BED3-505054503030}'
  AuditPolicyChanges|contains: '%%8448'
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://docs.google.com/presentation/d/1dkrldTTlN3La-OjWtkWJBb4hVk6vfsSMBFBERs6R8zA/edit
- https://github.com/SigmaHQ/sigma/blob/ad1bfd3d28aa0ccc9656240f845022518ef65a2e/documentation/logsource-guides/windows/service/security.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_disable_event_auditing_critical.yml)
