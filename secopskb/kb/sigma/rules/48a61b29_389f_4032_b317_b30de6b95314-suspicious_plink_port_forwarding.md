---
sigma_id: "48a61b29-389f-4032-b317-b30de6b95314"
title: "Suspicious Plink Port Forwarding"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_plink_port_forwarding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_plink_port_forwarding.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "48a61b29-389f-4032-b317-b30de6b95314"
  - "Suspicious Plink Port Forwarding"
attack_technique_ids:
  - "T1572"
  - "T1021.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Plink Port Forwarding

Detects suspicious Plink tunnel port forwarding to a local port

## Metadata

- Rule ID: 48a61b29-389f-4032-b317-b30de6b95314
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-01-19
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_plink_port_forwarding.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]
- [[kb/attack/techniques/T1021-remote_services|T1021.001]]

## Detection

```yaml
selection:
  Description: Command-line SSH, Telnet, and Rlogin client
  CommandLine|contains: ' -R '
condition: selection
```

## False Positives

- Administrative activity using a remote port forwarding to a local port

## References

- https://www.real-sec.com/2019/04/bypassing-network-restrictions-through-rdp-tunneling/
- https://medium.com/@informationsecurity/remote-ssh-tunneling-with-plink-exe-7831072b3d7d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_plink_port_forwarding.yml)
