---
sigma_id: "4b657234-038e-4ad5-997c-4be42340bce4"
title: "Network Connection Initiated To Visual Studio Code Tunnels Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_vscode_tunnel_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_vscode_tunnel_connection.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "4b657234-038e-4ad5-997c-4be42340bce4"
  - "Network Connection Initiated To Visual Studio Code Tunnels Domain"
attack_technique_ids:
  - "T1567"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Connection Initiated To Visual Studio Code Tunnels Domain

Detects network connections to Visual Studio Code tunnel domains initiated by a process on a system. Attackers can abuse that feature to establish a reverse shell or persistence on a machine.

## Metadata

- Rule ID: 4b657234-038e-4ad5-997c-4be42340bce4
- Status: test
- Level: medium
- Author: Kamran Saifullah
- Date: 2023-11-20
- Source Path: rules/windows/network_connection/net_connection_win_domain_vscode_tunnel_connection.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith: .tunnels.api.visualstudio.com
condition: selection
```

## False Positives

- Legitimate use of Visual Studio Code tunnel will also trigger this.

## References

- https://ipfyx.fr/post/visual-studio-code-tunnel/
- https://badoption.eu/blog/2023/01/31/code_c2.html
- https://cydefops.com/vscode-data-exfiltration

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_vscode_tunnel_connection.yml)
