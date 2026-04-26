---
sigma_id: "ab6bffca-beff-4baa-af11-6733f296d57a"
title: "Potential AD User Enumeration From Non-Machine Account"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_ad_user_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_ad_user_enumeration.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "ab6bffca-beff-4baa-af11-6733f296d57a"
  - "Potential AD User Enumeration From Non-Machine Account"
attack_technique_ids:
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential AD User Enumeration From Non-Machine Account

Detects read access to a domain user from a non-machine account

## Metadata

- Rule ID: ab6bffca-beff-4baa-af11-6733f296d57a
- Status: test
- Level: medium
- Author: Maxime Thiebaut (@0xThiebaut)
- Date: 2020-03-30
- Modified: 2022-11-08
- Source Path: rules/windows/builtin/security/win_security_ad_user_enumeration.yml

## Logsource

- definition: Requirements: The "Read all properties" permission on the user object needs to be audited for the "Everyone" principal
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Detection

```yaml
selection:
  EventID: 4662
  ObjectType|contains: bf967aba-0de6-11d0-a285-00aa003049e2
  AccessMask|endswith:
  - 1?
  - 3?
  - 4?
  - 7?
  - 9?
  - B?
  - D?
  - F?
filter_main_machine_accounts:
  SubjectUserName|endswith: $
filter_main_msql:
  SubjectUserName|startswith: MSOL_
condition: selection and not 1 of filter_main_*
```

## False Positives

- Administrators configuring new users.

## References

- https://www.specterops.io/assets/resources/an_ace_up_the_sleeve.pdf
- http://www.stuffithoughtiknew.com/2019/02/detecting-bloodhound.html
- https://learn.microsoft.com/en-us/windows/win32/adschema/attributes-all
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4662

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_ad_user_enumeration.yml)
