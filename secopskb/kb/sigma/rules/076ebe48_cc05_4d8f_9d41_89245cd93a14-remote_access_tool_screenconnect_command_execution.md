---
sigma_id: "076ebe48-cc05-4d8f-9d41-89245cd93a14"
title: "Remote Access Tool - ScreenConnect Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_command_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_command_exec.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / application"
aliases:
  - "076ebe48-cc05-4d8f-9d41-89245cd93a14"
  - "Remote Access Tool - ScreenConnect Command Execution"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - ScreenConnect Command Execution

Detects command execution via ScreenConnect RMM

## Metadata

- Rule ID: 076ebe48-cc05-4d8f-9d41-89245cd93a14
- Status: test
- Level: low
- Author: Ali Alwashali
- Date: 2023-10-10
- Source Path: rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_command_exec.yml

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
  EventID: 200
  Data|contains: Executed command of length
condition: selection
```

## False Positives

- Legitimate use of ScreenConnect

## References

- https://www.huntandhackett.com/blog/revil-the-usage-of-legitimate-remote-admin-tooling
- https://github.com/SigmaHQ/sigma/pull/4467

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/screenconnect/win_app_remote_access_tools_screenconnect_command_exec.yml)
