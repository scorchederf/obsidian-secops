---
sigma_id: "7ec15688-fd24-4177-ba43-1a950537ee39"
title: "The Windows Defender Firewall Service Failed To Load Group Policy"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_failed_load_gpo.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_failed_load_gpo.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / firewall-as"
aliases:
  - "7ec15688-fd24-4177-ba43-1a950537ee39"
  - "The Windows Defender Firewall Service Failed To Load Group Policy"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# The Windows Defender Firewall Service Failed To Load Group Policy

Detects activity when The Windows Defender Firewall service failed to load Group Policy

## Metadata

- Rule ID: 7ec15688-fd24-4177-ba43-1a950537ee39
- Status: test
- Level: low
- Author: frack113
- Date: 2022-02-19
- Modified: 2023-01-17
- Source Path: rules/windows/builtin/firewall_as/win_firewall_as_failed_load_gpo.yml

## Logsource

- product: windows
- service: firewall-as

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection:
  EventID: 2009
condition: selection
```

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd364427(v=ws.10)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_failed_load_gpo.yml)
