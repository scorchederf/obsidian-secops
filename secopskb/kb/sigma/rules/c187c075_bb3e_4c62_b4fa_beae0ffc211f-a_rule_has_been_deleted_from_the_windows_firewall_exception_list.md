---
sigma_id: "c187c075-bb3e-4c62-b4fa-beae0ffc211f"
title: "A Rule Has Been Deleted From The Windows Firewall Exception List"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_delete_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_delete_rule.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "windows / firewall-as"
aliases:
  - "c187c075-bb3e-4c62-b4fa-beae0ffc211f"
  - "A Rule Has Been Deleted From The Windows Firewall Exception List"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# A Rule Has Been Deleted From The Windows Firewall Exception List

Detects when a single rules or all of the rules have been deleted from the Windows Defender Firewall

## Metadata

- Rule ID: c187c075-bb3e-4c62-b4fa-beae0ffc211f
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-19
- Modified: 2024-08-29
- Source Path: rules/windows/builtin/firewall_as/win_firewall_as_delete_rule.yml

## Logsource

- product: windows
- service: firewall-as

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection:
  EventID:
  - 2006
  - 2052
filter_main_generic:
  ModifyingApplication|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\WinSxS\
filter_main_svchost:
  ModifyingApplication: C:\Windows\System32\svchost.exe
filter_optional_msmpeng:
  ModifyingApplication|startswith: C:\ProgramData\Microsoft\Windows Defender\Platform\
  ModifyingApplication|endswith: \MsMpEng.exe
filter_main_null:
  ModifyingApplication: null
filter_main_empty:
  ModifyingApplication: ''
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd364427(v=ws.10)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_delete_rule.yml)
