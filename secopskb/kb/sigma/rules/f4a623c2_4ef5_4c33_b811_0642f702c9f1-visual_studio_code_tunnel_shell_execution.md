---
sigma_id: "f4a623c2-4ef5-4c33-b811-0642f702c9f1"
title: "Visual Studio Code Tunnel Shell Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vscode_tunnel_remote_shell_.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_remote_shell_.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f4a623c2-4ef5-4c33-b811-0642f702c9f1"
  - "Visual Studio Code Tunnel Shell Execution"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Visual Studio Code Tunnel Shell Execution

Detects the execution of a shell (powershell, bash, wsl...) via Visual Studio Code tunnel. Attackers can abuse this functionality to establish a C2 channel and execute arbitrary commands on the system.

## Metadata

- Rule ID: f4a623c2-4ef5-4c33-b811-0642f702c9f1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-10-25
- Source Path: rules/windows/process_creation/proc_creation_win_vscode_tunnel_remote_shell_.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection_parent:
  ParentImage|contains: \servers\Stable-
  ParentImage|endswith: \server\node.exe
  ParentCommandLine|contains: .vscode-server
selection_child_1:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains: \terminal\browser\media\shellIntegration.ps1
selection_child_2:
  Image|endswith:
  - \wsl.exe
  - \bash.exe
condition: selection_parent and 1 of selection_child_*
```

## False Positives

- Legitimate use of Visual Studio Code tunnel and running code from there

## References

- https://ipfyx.fr/post/visual-studio-code-tunnel/
- https://badoption.eu/blog/2023/01/31/code_c2.html
- https://code.visualstudio.com/docs/remote/tunnels

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_remote_shell_.yml)
