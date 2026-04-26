---
sigma_id: "b3e6418f-7c7a-4fad-993a-93b65027a9f1"
title: "DNS Query To Visual Studio Code Tunnels Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_vscode_tunnel_communication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_vscode_tunnel_communication.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "b3e6418f-7c7a-4fad-993a-93b65027a9f1"
  - "DNS Query To Visual Studio Code Tunnels Domain"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query To Visual Studio Code Tunnels Domain

Detects DNS query requests to Visual Studio Code tunnel domains. Attackers can abuse that feature to establish a reverse shell or persistence on a machine.

## Metadata

- Rule ID: b3e6418f-7c7a-4fad-993a-93b65027a9f1
- Status: test
- Level: medium
- Author: citron_ninja
- Date: 2023-10-25
- Modified: 2023-11-20
- Source Path: rules/windows/dns_query/dns_query_win_vscode_tunnel_communication.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  QueryName|endswith: .tunnels.api.visualstudio.com
condition: selection
```

## False Positives

- Legitimate use of Visual Studio Code tunnel will also trigger this.

## References

- https://ipfyx.fr/post/visual-studio-code-tunnel/
- https://badoption.eu/blog/2023/01/31/code_c2.html
- https://cydefops.com/vscode-data-exfiltration

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_vscode_tunnel_communication.yml)
