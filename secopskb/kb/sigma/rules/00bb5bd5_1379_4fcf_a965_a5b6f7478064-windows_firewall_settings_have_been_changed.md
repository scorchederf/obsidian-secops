---
sigma_id: "00bb5bd5-1379-4fcf-a965-a5b6f7478064"
title: "Windows Firewall Settings Have Been Changed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_setting_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_setting_change.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "low"
logsource: "windows / firewall-as"
aliases:
  - "00bb5bd5-1379-4fcf-a965-a5b6f7478064"
  - "Windows Firewall Settings Have Been Changed"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Firewall Settings Have Been Changed

Detects activity when the settings of the Windows firewall have been changed

## Metadata

- Rule ID: 00bb5bd5-1379-4fcf-a965-a5b6f7478064
- Status: test
- Level: low
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-02-19
- Modified: 2023-04-21
- Source Path: rules/windows/builtin/firewall_as/win_firewall_as_setting_change.yml

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
  - 2002
  - 2083
  - 2003
  - 2082
  - 2008
condition: selection
```

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd364427(v=ws.10)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_setting_change.yml)
