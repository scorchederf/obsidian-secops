---
sigma_id: "a70dcb37-3bee-453a-99df-d0c683151be6"
title: "Firewall Rule Update Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_set_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_set_rule.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a70dcb37-3bee-453a-99df-d0c683151be6"
  - "Firewall Rule Update Via Netsh.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Firewall Rule Update Via Netsh.EXE

Detects execution of netsh with the "advfirewall" and the "set" option in order to set new values for properties of a existing rule

## Metadata

- Rule ID: a70dcb37-3bee-453a-99df-d0c683151be6
- Status: test
- Level: medium
- Author: X__Junior (Nextron Systems)
- Date: 2023-07-18
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_set_rule.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
  CommandLine|contains|all:
  - ' firewall '
  - ' set '
condition: all of selection_*
```

## False Positives

- Legitimate administration activity
- Software installations and removal

## References

- https://ss64.com/nt/netsh.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_set_rule.yml)
