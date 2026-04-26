---
sigma_id: "30bf1789-379d-4fdc-900f-55cd0a90a801"
title: "Visual Studio Code Tunnel Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vscode_tunnel_service_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_service_install.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "30bf1789-379d-4fdc-900f-55cd0a90a801"
  - "Visual Studio Code Tunnel Service Installation"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Visual Studio Code Tunnel Service Installation

Detects the installation of VsCode tunnel (code-tunnel) as a service.

## Metadata

- Rule ID: 30bf1789-379d-4fdc-900f-55cd0a90a801
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-10-25
- Source Path: rules/windows/process_creation/proc_creation_win_vscode_tunnel_service_install.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - 'tunnel '
  - service
  - internal-run
  - tunnel-service.log
condition: selection
```

## False Positives

- Legitimate installation of code-tunnel as a service

## References

- https://ipfyx.fr/post/visual-studio-code-tunnel/
- https://badoption.eu/blog/2023/01/31/code_c2.html
- https://code.visualstudio.com/docs/remote/tunnels

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_service_install.yml)
