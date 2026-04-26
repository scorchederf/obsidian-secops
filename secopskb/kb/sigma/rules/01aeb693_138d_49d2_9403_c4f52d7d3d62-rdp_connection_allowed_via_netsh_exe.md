---
sigma_id: "01aeb693-138d-49d2-9403-c4f52d7d3d62"
title: "RDP Connection Allowed Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_allow_rdp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_allow_rdp.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "01aeb693-138d-49d2-9403-c4f52d7d3d62"
  - "RDP Connection Allowed Via Netsh.EXE"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RDP Connection Allowed Via Netsh.EXE

Detects usage of the netsh command to open and allow connections to port 3389 (RDP). As seen used by Sarwent Malware

## Metadata

- Rule ID: 01aeb693-138d-49d2-9403-c4f52d7d3d62
- Status: test
- Level: high
- Author: Sander Wiebing
- Date: 2020-05-23
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_allow_rdp.yml

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
  - 'firewall '
  - 'add '
  - 'tcp '
  - '3389'
  CommandLine|contains:
  - portopening
  - allow
condition: all of selection_*
```

## False Positives

- Legitimate administration activity

## References

- https://labs.sentinelone.com/sarwent-malware-updates-command-detonation/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_allow_rdp.yml)
