---
sigma_id: "322ed9ec-fcab-4f67-9a34-e7c6aef43614"
title: "New Port Forwarding Rule Added Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_port_forwarding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_port_forwarding.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "322ed9ec-fcab-4f67-9a34-e7c6aef43614"
  - "New Port Forwarding Rule Added Via Netsh.EXE"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Port Forwarding Rule Added Via Netsh.EXE

Detects the execution of netsh commands that configure a new port forwarding (PortProxy) rule

## Metadata

- Rule ID: 322ed9ec-fcab-4f67-9a34-e7c6aef43614
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), omkar72, oscd.community, Swachchhanda Shrawan Poudel
- Date: 2019-01-29
- Modified: 2023-09-01
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_port_forwarding.yml

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
selection_cli_1:
  CommandLine|contains|all:
  - interface
  - portproxy
  - add
  - v4tov4
selection_cli_2:
  CommandLine|contains|all:
  - 'i '
  - 'p '
  - 'a '
  - 'v '
selection_cli_3:
  CommandLine|contains|all:
  - connectp
  - listena
  - c=
condition: selection_img and 1 of selection_cli_*
```

## False Positives

- Legitimate administration activity
- WSL2 network bridge PowerShell script used for WSL/Kubernetes/Docker (e.g. https://github.com/microsoft/WSL/issues/4150#issuecomment-504209723)

## References

- https://www.fireeye.com/blog/threat-research/2019/01/bypassing-network-restrictions-through-rdp-tunneling.html
- https://adepts.of0x.cc/netsh-portproxy-code/
- https://www.dfirnotes.net/portproxy_detection/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_port_forwarding.yml)
