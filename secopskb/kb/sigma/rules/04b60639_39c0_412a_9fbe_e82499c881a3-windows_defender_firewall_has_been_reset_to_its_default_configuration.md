---
sigma_id: "04b60639-39c0-412a-9fbe-e82499c881a3"
title: "Windows Defender Firewall Has Been Reset To Its Default Configuration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_reset_config.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_reset_config.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "low"
logsource: "windows / firewall-as"
aliases:
  - "04b60639-39c0-412a-9fbe-e82499c881a3"
  - "Windows Defender Firewall Has Been Reset To Its Default Configuration"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Firewall Has Been Reset To Its Default Configuration

Detects activity when Windows Defender Firewall has been reset to its default configuration

## Metadata

- Rule ID: 04b60639-39c0-412a-9fbe-e82499c881a3
- Status: test
- Level: low
- Author: frack113
- Date: 2022-02-19
- Modified: 2023-04-21
- Source Path: rules/windows/builtin/firewall_as/win_firewall_as_reset_config.yml

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
  - 2032
  - 2060
condition: selection
```

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd364427(v=ws.10)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_reset_config.yml)
