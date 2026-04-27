---
sigma_id: "d102b8f5-61dc-4e68-bd83-9a3187c67377"
title: "Renamed VsCode Code Tunnel Execution - File Indicator"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_vscode_tunnel_renamed_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_vscode_tunnel_renamed_execution.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "d102b8f5-61dc-4e68-bd83-9a3187c67377"
  - "Renamed VsCode Code Tunnel Execution - File Indicator"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of a file with the name "code_tunnel.json" which indicate execution and usage of VsCode tunneling utility by an "Image" or "Process" other than VsCode.

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|endswith: \code_tunnel.json
filter_main_legit_name:
  Image|endswith:
  - \code-tunnel.exe
  - \code.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://ipfyx.fr/post/visual-studio-code-tunnel/
- https://badoption.eu/blog/2023/01/31/code_c2.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_vscode_tunnel_renamed_execution.yml)
