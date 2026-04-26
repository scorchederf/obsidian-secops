---
sigma_id: "327f48c1-a6db-4eb8-875a-f6981f1b0183"
title: "Port Forwarding Activity Via SSH.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ssh_port_forward.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ssh_port_forward.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "327f48c1-a6db-4eb8-875a-f6981f1b0183"
  - "Port Forwarding Activity Via SSH.EXE"
attack_technique_ids:
  - "T1572"
  - "T1021.001"
  - "T1021.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Port Forwarding Activity Via SSH.EXE

Detects port forwarding activity via SSH.exe

## Metadata

- Rule ID: 327f48c1-a6db-4eb8-875a-f6981f1b0183
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-12
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_ssh_port_forward.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]
- [[kb/attack/techniques/T1021-remote_services|T1021.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.004]]

## Detection

```yaml
selection:
  Image|endswith: \ssh.exe
  CommandLine|contains|windash: ' -R '
condition: selection
```

## False Positives

- Administrative activity using a remote port forwarding to a local port

## References

- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ssh_port_forward.yml)
