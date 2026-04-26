---
sigma_id: "d0dae994-26c6-4d2d-83b5-b3c8b79ae513"
title: "PUA - WebBrowserPassView Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_webbrowserpassview.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_webbrowserpassview.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d0dae994-26c6-4d2d-83b5-b3c8b79ae513"
  - "PUA - WebBrowserPassView Execution"
attack_technique_ids:
  - "T1555.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - WebBrowserPassView Execution

Detects the execution of WebBrowserPassView.exe. A password recovery tool that reveals the passwords stored by the following Web browsers, Internet Explorer (Version 4.0 - 11.0), Mozilla Firefox (All Versions), Google Chrome, Safari, and Opera

## Metadata

- Rule ID: d0dae994-26c6-4d2d-83b5-b3c8b79ae513
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-20
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_pua_webbrowserpassview.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Detection

```yaml
selection:
- Description: Web Browser Password Viewer
- Image|endswith: \WebBrowserPassView.exe
condition: selection
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1555.003/T1555.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_webbrowserpassview.yml)
