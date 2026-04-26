---
sigma_id: "0f6da907-5854-4be6-859a-e9958747b0aa"
title: "Potential DLL Injection Via AccCheckConsole"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_acccheckconsole_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_acccheckconsole_execution.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0f6da907-5854-4be6-859a-e9958747b0aa"
  - "Potential DLL Injection Via AccCheckConsole"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Injection Via AccCheckConsole

Detects the execution "AccCheckConsole" a command-line tool for verifying the accessibility implementation of an application's UI.
One of the tests that this checker can run are called "verification routine", which tests for things like Consistency, Navigation, etc.
The tool allows a user to provide a DLL that can contain a custom "verification routine". An attacker can build such DLLs and pass it via the CLI, which would then be loaded in the context of the "AccCheckConsole" utility.

## Metadata

- Rule ID: 0f6da907-5854-4be6-859a-e9958747b0aa
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-06
- Modified: 2024-08-29
- Source Path: rules/windows/process_creation/proc_creation_win_acccheckconsole_execution.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \AccCheckConsole.exe
- OriginalFileName: AccCheckConsole.exe
selection_cli:
  CommandLine|contains:
  - ' -hwnd'
  - ' -process '
  - ' -window '
condition: all of selection_*
```

## False Positives

- Legitimate use of the UI Accessibility Checker

## References

- https://gist.github.com/bohops/2444129419c8acf837aedda5f0e7f340
- https://twitter.com/bohops/status/1477717351017680899?s=12
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/AccCheckConsole/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_acccheckconsole_execution.yml)
