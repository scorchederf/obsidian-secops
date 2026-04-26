---
sigma_id: "962fe167-e48d-4fd6-9974-11e5b9a5d6d1"
title: "LSASS Access From Non System Account"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_lsass_access_non_system_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_lsass_access_non_system_account.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "962fe167-e48d-4fd6-9974-11e5b9a5d6d1"
  - "LSASS Access From Non System Account"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LSASS Access From Non System Account

Detects potential mimikatz-like tools accessing LSASS from non system account

## Metadata

- Rule ID: 962fe167-e48d-4fd6-9974-11e5b9a5d6d1
- Status: test
- Level: medium
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-06-20
- Modified: 2023-12-11
- Source Path: rules/windows/builtin/security/win_security_lsass_access_non_system_account.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  EventID:
  - 4663
  - 4656
  AccessMask:
  - '0x100000'
  - '0x1010'
  - '0x1400'
  - '0x1410'
  - '0x1418'
  - '0x1438'
  - '0x143a'
  - '0x1f0fff'
  - '0x1f1fff'
  - '0x1f2fff'
  - '0x1f3fff'
  - '0x40'
  - 143a
  - 1f0fff
  - 1f1fff
  - 1f2fff
  - 1f3fff
  ObjectType: Process
  ObjectName|endswith: \lsass.exe
filter_main_service_account:
  SubjectUserName|endswith: $
filter_main_generic:
  ProcessName|contains:
  - :\Program Files\
  - :\Program Files (x86)\
filter_main_wmiprvse:
  ProcessName: C:\Windows\System32\wbem\WmiPrvSE.exe
  AccessMask: '0x1410'
filter_optional_steam:
  ProcessName|contains: \SteamLibrary\steamapps\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/170105-LSASSMemoryReadAccess/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_lsass_access_non_system_account.yml)
