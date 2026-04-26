---
sigma_id: "79609c82-a488-426e-abcf-9f341a39365d"
title: "All Rules Have Been Deleted From The Windows Firewall Configuration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_delete_all_rules.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_delete_all_rules.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / firewall-as"
aliases:
  - "79609c82-a488-426e-abcf-9f341a39365d"
  - "All Rules Have Been Deleted From The Windows Firewall Configuration"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# All Rules Have Been Deleted From The Windows Firewall Configuration

Detects when a all the rules have been deleted from the Windows Defender Firewall configuration

## Metadata

- Rule ID: 79609c82-a488-426e-abcf-9f341a39365d
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-17
- Modified: 2024-01-22
- Source Path: rules/windows/builtin/firewall_as/win_firewall_as_delete_all_rules.yml

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
  - 2033
  - 2059
filter_main_svchost:
  ModifyingApplication|endswith: :\Windows\System32\svchost.exe
filter_optional_msmpeng:
  ModifyingApplication|contains|all:
  - :\ProgramData\Microsoft\Windows Defender\Platform\
  - \MsMpEng.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd364427(v=ws.10)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_delete_all_rules.yml)
