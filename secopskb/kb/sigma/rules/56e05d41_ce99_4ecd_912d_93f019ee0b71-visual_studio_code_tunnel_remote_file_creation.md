---
sigma_id: "56e05d41-ce99-4ecd-912d-93f019ee0b71"
title: "Visual Studio Code Tunnel Remote File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_vscode_tunnel_remote_creation_artefacts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_vscode_tunnel_remote_creation_artefacts.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "56e05d41-ce99-4ecd-912d-93f019ee0b71"
  - "Visual Studio Code Tunnel Remote File Creation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Visual Studio Code Tunnel Remote File Creation

Detects the creation of file by the "node.exe" process in the ".vscode-server" directory. Could be a sign of remote file creation via VsCode tunnel feature

## Metadata

- Rule ID: 56e05d41-ce99-4ecd-912d-93f019ee0b71
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-10-25
- Source Path: rules/windows/file/file_event/file_event_win_vscode_tunnel_remote_creation_artefacts.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|contains: \servers\Stable-
  Image|endswith: \server\node.exe
  TargetFilename|contains: \.vscode-server\data\User\History\
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_vscode_tunnel_remote_creation_artefacts.yml)
