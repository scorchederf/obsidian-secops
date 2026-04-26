---
sigma_id: "57c4bf16-227f-4394-8ec7-1b745ee061c3"
title: "Firewall Disabled via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_disable.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "57c4bf16-227f-4394-8ec7-1b745ee061c3"
  - "Firewall Disabled via Netsh.EXE"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Firewall Disabled via Netsh.EXE

Detects netsh commands that turns off the Windows firewall

## Metadata

- Rule ID: 57c4bf16-227f-4394-8ec7-1b745ee061c3
- Status: test
- Level: medium
- Author: Fatih Sirin
- Date: 2019-11-01
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_disable.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

### Software Tags

- S0108

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli_1:
  CommandLine|contains|all:
  - firewall
  - set
  - opmode
  - disable
selection_cli_2:
  CommandLine|contains|all:
  - advfirewall
  - set
  - state
  - 'off'
condition: selection_img and 1 of selection_cli_*
```

## False Positives

- Legitimate administration activity

## References

- https://www.winhelponline.com/blog/enable-and-disable-windows-firewall-quickly-using-command-line/
- https://app.any.run/tasks/210244b9-0b6b-4a2c-83a3-04bd3175d017/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004.md#atomic-test-1---disable-microsoft-defender-firewall

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_disable.yml)
