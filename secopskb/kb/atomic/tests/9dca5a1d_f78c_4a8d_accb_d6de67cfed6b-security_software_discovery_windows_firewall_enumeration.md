---
atomic_guid: "9dca5a1d-f78c-4a8d-accb-d6de67cfed6b"
title: "Security Software Discovery - Windows Firewall Enumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "9dca5a1d-f78c-4a8d-accb-d6de67cfed6b"
  - "Security Software Discovery - Windows Firewall Enumeration"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enumerates windows firewall to retrieves firewall rules from the target computer.

when sucessfully executed, details of windows firewall is displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-NetFirewallProfile | Format-Table Name, Enabled
Get-NetFirewallSetting
Get-NetFirewallRule | select DisplayName, Enabled, Description
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
