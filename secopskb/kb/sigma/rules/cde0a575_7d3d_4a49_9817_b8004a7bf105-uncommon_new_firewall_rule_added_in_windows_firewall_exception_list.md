---
sigma_id: "cde0a575-7d3d-4a49-9817-b8004a7bf105"
title: "Uncommon New Firewall Rule Added In Windows Firewall Exception List"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_add_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_add_rule.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / firewall-as"
aliases:
  - "cde0a575-7d3d-4a49-9817-b8004a7bf105"
  - "Uncommon New Firewall Rule Added In Windows Firewall Exception List"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon New Firewall Rule Added In Windows Firewall Exception List

Detects when a rule has been added to the Windows Firewall exception list

## Metadata

- Rule ID: cde0a575-7d3d-4a49-9817-b8004a7bf105
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-19
- Modified: 2025-10-08
- Source Path: rules/windows/builtin/firewall_as/win_firewall_as_add_rule.yml

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
  - 2004
  - 2071
  - 2097
filter_main_block:
  Action: 2
filter_main_generic:
  ApplicationPath|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
filter_main_covered_paths:
  ApplicationPath|contains:
  - C:\PerfLogs\
  - C:\Temp\
  - C:\Tmp\
  - C:\Users\Public\
  - C:\Windows\Tasks\
  - C:\Windows\Temp\
  - \AppData\Local\Temp\
filter_main_system_dllhost:
  ApplicationPath: System
  ModifyingApplication: C:\Windows\System32\dllhost.exe
filter_main_tiworker:
  ModifyingApplication|startswith: C:\Windows\WinSxS\
  ModifyingApplication|endswith: \TiWorker.exe
filter_main_null:
  ApplicationPath: null
filter_optional_no_path:
  ModifyingApplication:
  - C:\Windows\System32\svchost.exe
  - C:\Windows\System32\dllhost.exe
  ApplicationPath: ''
filter_optional_msmpeng:
- ModifyingApplication|startswith:
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  - C:\Program Files\Windows Defender\
  ModifyingApplication|endswith: \MsMpEng.exe
- ApplicationPath|startswith:
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  - C:\Program Files\Windows Defender\
  ApplicationPath|endswith: \MsMpEng.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd364427(v=ws.10)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_add_rule.yml)
