---
sigma_id: "0e4164da-94bc-450d-a7be-a4b176179f1f"
title: "Firewall Configuration Discovery Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_rules_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_rules_discovery.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "0e4164da-94bc-450d-a7be-a4b176179f1f"
  - "Firewall Configuration Discovery Via Netsh.EXE"
attack_technique_ids:
  - "T1016"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Firewall Configuration Discovery Via Netsh.EXE

Adversaries may look for details about the network configuration and settings of systems they access or through information discovery of remote systems

## Metadata

- Rule ID: 0e4164da-94bc-450d-a7be-a4b176179f1f
- Status: test
- Level: low
- Author: frack113, Christopher Peacock '@securepeacock', SCYTHE '@scythe_io'
- Date: 2021-12-07
- Modified: 2025-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_rules_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
  CommandLine|contains|all:
  - netsh
  - 'show '
  - 'firewall '
  CommandLine|contains:
  - 'config '
  - 'state '
  - 'rule '
  - name=all
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1016/T1016.md#atomic-test-2---list-windows-firewall-rules
- https://ss64.com/nt/netsh.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_rules_discovery.yml)
