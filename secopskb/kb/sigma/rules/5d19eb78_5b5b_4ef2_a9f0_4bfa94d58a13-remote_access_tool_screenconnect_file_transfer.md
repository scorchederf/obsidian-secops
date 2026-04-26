---
sigma_id: "5d19eb78-5b5b-4ef2-a9f0-4bfa94d58a13"
title: "Remote Access Tool - ScreenConnect File Transfer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_file_transfer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_file_transfer.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / application"
aliases:
  - "5d19eb78-5b5b-4ef2-a9f0-4bfa94d58a13"
  - "Remote Access Tool - ScreenConnect File Transfer"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - ScreenConnect File Transfer

Detects file being transferred via ScreenConnect RMM

## Metadata

- Rule ID: 5d19eb78-5b5b-4ef2-a9f0-4bfa94d58a13
- Status: test
- Level: low
- Author: Ali Alwashali
- Date: 2023-10-10
- Source Path: rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_file_transfer.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection:
  Provider_Name: ScreenConnect
  EventID: 201
  Data|contains: Transferred files with action
condition: selection
```

## False Positives

- Legitimate use of ScreenConnect

## References

- https://www.huntandhackett.com/blog/revil-the-usage-of-legitimate-remote-admin-tooling
- https://github.com/SigmaHQ/sigma/pull/4467

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_file_transfer.yml)
