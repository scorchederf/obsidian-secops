---
sigma_id: "347906f3-e207-4d18-ae5b-a9403d6bcdef"
title: "Netsh Allow Group Policy on Microsoft Defender Firewall"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_enable_group_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_enable_group_rule.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "347906f3-e207-4d18-ae5b-a9403d6bcdef"
  - "Netsh Allow Group Policy on Microsoft Defender Firewall"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Netsh Allow Group Policy on Microsoft Defender Firewall

Adversaries may modify system firewalls in order to bypass controls limiting network usage

## Metadata

- Rule ID: 347906f3-e207-4d18-ae5b-a9403d6bcdef
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-09
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_enable_group_rule.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
  CommandLine|contains|all:
  - advfirewall
  - firewall
  - set
  - rule
  - group=
  - new
  - enable=Yes
condition: all of selection_*
```

## False Positives

- Legitimate administration activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004.md#atomic-test-3---allow-smb-and-rdp-on-microsoft-defender-firewall
- https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/netsh-advfirewall-firewall-control-firewall-behavior

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_enable_group_rule.yml)
