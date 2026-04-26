---
sigma_id: "782d6f3e-4c5d-4b8c-92a3-1d05fed72e63"
title: "RDP Port Forwarding Rule Added Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_port_forwarding_3389.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_port_forwarding_3389.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "782d6f3e-4c5d-4b8c-92a3-1d05fed72e63"
  - "RDP Port Forwarding Rule Added Via Netsh.EXE"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RDP Port Forwarding Rule Added Via Netsh.EXE

Detects the execution of netsh to configure a port forwarding of port 3389 (RDP) rule

## Metadata

- Rule ID: 782d6f3e-4c5d-4b8c-92a3-1d05fed72e63
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), oscd.community
- Date: 2019-01-29
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_port_forwarding_3389.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
  CommandLine|contains|all:
  - ' i'
  - ' p'
  - =3389
  - ' c'
condition: all of selection_*
```

## False Positives

- Legitimate administration activity

## References

- https://www.fireeye.com/blog/threat-research/2019/01/bypassing-network-restrictions-through-rdp-tunneling.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_port_forwarding_3389.yml)
