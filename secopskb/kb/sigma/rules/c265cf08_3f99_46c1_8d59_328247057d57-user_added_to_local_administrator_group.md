---
sigma_id: "c265cf08-3f99-46c1-8d59-328247057d57"
title: "User Added to Local Administrator Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_user_added_to_local_administrators.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_added_to_local_administrators.yml"
build_date: "2026-04-26 14:14:38"
status: "stable"
level: "medium"
logsource: "windows / security"
aliases:
  - "c265cf08-3f99-46c1-8d59-328247057d57"
  - "User Added to Local Administrator Group"
attack_technique_ids:
  - "T1078"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Added to Local Administrator Group

Detects the addition of a new member to the local administrator group, which could be legitimate activity or a sign of privilege escalation activity

## Metadata

- Rule ID: c265cf08-3f99-46c1-8d59-328247057d57
- Status: stable
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-14
- Modified: 2021-01-17
- Source Path: rules/windows/builtin/security/win_security_user_added_to_local_administrators.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection_eid:
  EventID: 4732
selection_group:
- TargetUserName|startswith: Administr
- TargetSid: S-1-5-32-544
filter_main_computer_accounts:
  SubjectUserName|endswith: $
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Legitimate administrative activity

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4732
- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_user_added_to_local_administrators.yml)
