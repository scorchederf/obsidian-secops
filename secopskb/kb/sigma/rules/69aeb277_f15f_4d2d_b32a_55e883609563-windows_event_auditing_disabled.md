---
sigma_id: "69aeb277-f15f-4d2d-b32a-55e883609563"
title: "Windows Event Auditing Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_disable_event_auditing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_disable_event_auditing.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "69aeb277-f15f-4d2d-b32a-55e883609563"
  - "Windows Event Auditing Disabled"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Event Auditing Disabled

Detects scenarios where system auditing (i.e.: Windows event log auditing) is disabled.
This may be used in a scenario where an entity would want to bypass local logging to evade detection when Windows event logging is enabled and reviewed.
Also, it is recommended to turn off "Local Group Policy Object Processing" via GPO, which will make sure that Active Directory GPOs take precedence over local/edited computer policies via something such as "gpedit.msc".
Please note, that disabling "Local Group Policy Object Processing" may cause an issue in scenarios of one off specific GPO modifications - however, it is recommended to perform these modifications in Active Directory anyways.

## Metadata

- Rule ID: 69aeb277-f15f-4d2d-b32a-55e883609563
- Status: test
- Level: low
- Author: @neu5ron, Nasreddine Bencherchali (Nextron Systems)
- Date: 2017-11-19
- Modified: 2023-11-15
- Source Path: rules/windows/builtin/security/win_security_disable_event_auditing.yml

## Logsource

- definition: dfd8c0f4-e6ad-4e07-b91b-f2fca0ddef64
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection:
  EventID: 4719
  AuditPolicyChanges|contains:
  - '%%8448'
  - '%%8450'
filter_main_guid:
  SubcategoryGuid:
  - '{0CCE9210-69AE-11D9-BED3-505054503030}'
  - '{0CCE9211-69AE-11D9-BED3-505054503030}'
  - '{0CCE9212-69AE-11D9-BED3-505054503030}'
  - '{0CCE9215-69AE-11D9-BED3-505054503030}'
  - '{0CCE9217-69AE-11D9-BED3-505054503030}'
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
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://docs.google.com/presentation/d/1dkrldTTlN3La-OjWtkWJBb4hVk6vfsSMBFBERs6R8zA/edit

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_disable_event_auditing.yml)
