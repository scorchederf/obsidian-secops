---
sigma_id: "90d6bd71-dffb-4989-8d86-a827fedd6624"
title: "Visual Studio Code Tunnel Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vscode_tunnel_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "90d6bd71-dffb-4989-8d86-a827fedd6624"
  - "Visual Studio Code Tunnel Execution"
attack_technique_ids:
  - "T1071.001"
  - "T1219"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Visual Studio Code Tunnel Execution

Detects Visual Studio Code tunnel execution. Attackers can abuse this functionality to establish a C2 channel

## Metadata

- Rule ID: 90d6bd71-dffb-4989-8d86-a827fedd6624
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), citron_ninja
- Date: 2023-10-25
- Modified: 2025-10-29
- Source Path: rules/windows/process_creation/proc_creation_win_vscode_tunnel_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]
- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Detection

```yaml
selection_only_tunnel:
  OriginalFileName: null
  CommandLine|endswith: .exe tunnel
selection_tunnel_args:
  CommandLine|contains|all:
  - .exe tunnel
  - --accept-server-license-terms
selection_parent_tunnel:
  ParentCommandLine|endswith: ' tunnel'
  Image|endswith: \cmd.exe
  CommandLine|contains|all:
  - '/d /c '
  - \servers\Stable-
  - code-server.cmd
condition: 1 of selection_*
```

## False Positives

- Legitimate use of Visual Studio Code tunnel

## References

- https://ipfyx.fr/post/visual-studio-code-tunnel/
- https://badoption.eu/blog/2023/01/31/code_c2.html
- https://code.visualstudio.com/docs/remote/tunnels

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_execution.yml)
