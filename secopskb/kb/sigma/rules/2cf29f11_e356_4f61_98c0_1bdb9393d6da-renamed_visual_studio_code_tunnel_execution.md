---
sigma_id: "2cf29f11-e356-4f61-98c0-1bdb9393d6da"
title: "Renamed Visual Studio Code Tunnel Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vscode_tunnel_renamed_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_renamed_execution.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2cf29f11-e356-4f61-98c0-1bdb9393d6da"
  - "Renamed Visual Studio Code Tunnel Execution"
attack_technique_ids:
  - "T1071.001"
  - "T1219"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed Visual Studio Code Tunnel Execution

Detects renamed Visual Studio Code tunnel execution. Attackers can abuse this functionality to establish a C2 channel

## Metadata

- Rule ID: 2cf29f11-e356-4f61-98c0-1bdb9393d6da
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-28
- Modified: 2025-10-29
- Source Path: rules/windows/process_creation/proc_creation_win_vscode_tunnel_renamed_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]
- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Detection

```yaml
selection_image_only_tunnel:
  OriginalFileName: null
  CommandLine|endswith: .exe tunnel
selection_image_tunnel_args:
  CommandLine|contains|all:
  - .exe tunnel
  - --accept-server-license-terms
selection_image_tunnel_service:
  CommandLine|contains|all:
  - 'tunnel '
  - service
  - internal-run
  - tunnel-service.log
selection_parent_tunnel:
  ParentCommandLine|endswith: ' tunnel'
  Image|endswith: \cmd.exe
  CommandLine|contains|all:
  - '/d /c '
  - \servers\Stable-
  - code-server.cmd
filter_main_parent_code:
  ParentImage|endswith:
  - \code-tunnel.exe
  - \code.exe
filter_main_image_code:
  Image|endswith:
  - \code-tunnel.exe
  - \code.exe
condition: (1 of selection_image_* and not 1 of filter_main_image_*) or (selection_parent_tunnel
  and not 1 of filter_main_parent_*)
```

## False Positives

- Unknown

## References

- https://ipfyx.fr/post/visual-studio-code-tunnel/
- https://badoption.eu/blog/2023/01/31/code_c2.html
- https://code.visualstudio.com/docs/remote/tunnels

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vscode_tunnel_renamed_execution.yml)
