---
sigma_id: "eca81e8d-09e1-4d04-8614-c91f44fd0519"
title: "New Firewall Rule Added In Windows Firewall Exception List Via WmiPrvSE.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/firewall_as/win_firewall_as_add_rule_wmiprvse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_add_rule_wmiprvse.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / firewall-as"
aliases:
  - "eca81e8d-09e1-4d04-8614-c91f44fd0519"
  - "New Firewall Rule Added In Windows Firewall Exception List Via WmiPrvSE.EXE"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Firewall Rule Added In Windows Firewall Exception List Via WmiPrvSE.EXE

Detects the addition of a new "Allow" firewall rule by the WMI process (WmiPrvSE.EXE).
This can occur if an attacker leverages PowerShell cmdlets such as "New-NetFirewallRule", or directly uses WMI CIM classes such as "MSFT_NetFirewallRule".

## Metadata

- Rule ID: eca81e8d-09e1-4d04-8614-c91f44fd0519
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-05-10
- Source Path: rules/windows/builtin/firewall_as/win_firewall_as_add_rule_wmiprvse.yml

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
  Action: 3
  ModifyingApplication|endswith: :\Windows\System32\wbem\WmiPrvSE.exe
condition: selection
```

## False Positives

- Administrator scripts or activity.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.md#atomic-test-24---set-a-firewall-rule-using-new-netfirewallrule
- https://malware.news/t/the-rhysida-ransomware-activity-analysis-and-ties-to-vice-society/72170
- https://cybersecuritynews.com/rhysida-ransomware-attacking-windows/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/firewall_as/win_firewall_as_add_rule_wmiprvse.yml)
