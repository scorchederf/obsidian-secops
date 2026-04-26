---
sigma_id: "4c4af3cd-2115-479c-8193-6b8bfce9001c"
title: "PowerShell ICMP Exfiltration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_icmp_exfiltration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_icmp_exfiltration.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "4c4af3cd-2115-479c-8193-6b8bfce9001c"
  - "PowerShell ICMP Exfiltration"
attack_technique_ids:
  - "T1048.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell ICMP Exfiltration

Detects Exfiltration Over Alternative Protocol - ICMP. Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel.

## Metadata

- Rule ID: 4c4af3cd-2115-479c-8193-6b8bfce9001c
- Status: test
- Level: medium
- Author: Bartlomiej Czyz @bczyz1, oscd.community
- Date: 2020-10-10
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_icmp_exfiltration.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - New-Object
  - System.Net.NetworkInformation.Ping
  - .Send(
condition: selection
```

## False Positives

- Legitimate usage of System.Net.NetworkInformation.Ping class

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1048.003/T1048.003.md#atomic-test-2---exfiltration-over-alternative-protocol---icmp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_icmp_exfiltration.yml)
