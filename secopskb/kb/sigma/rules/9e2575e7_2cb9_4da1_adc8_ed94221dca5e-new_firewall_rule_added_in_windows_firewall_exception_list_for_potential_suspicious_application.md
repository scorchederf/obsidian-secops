---
sigma_id: "9e2575e7-2cb9-4da1-adc8-ed94221dca5e"
title: "New Firewall Rule Added In Windows Firewall Exception List For Potential Suspicious Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_add_rule_susp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_add_rule_susp_folder.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / firewall-as"
aliases:
  - "9e2575e7-2cb9-4da1-adc8-ed94221dca5e"
  - "New Firewall Rule Added In Windows Firewall Exception List For Potential Suspicious Application"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the addition of a new rule to the Windows Firewall exception list for an application located in a potentially suspicious location.

## Logsource

- product: windows
- service: firewall-as

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

## Detection

```yaml
selection:
  EventID:
  - 2004
  - 2071
  - 2097
  ApplicationPath|contains:
  - :\PerfLogs\
  - :\Temp\
  - :\Tmp\
  - :\Users\Public\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
filter_main_block:
  Action: 2
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd364427(v=ws.10)
- https://app.any.run/tasks/7123e948-c91e-49e0-a813-00e8d72ab393/#

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_add_rule_susp_folder.yml)
