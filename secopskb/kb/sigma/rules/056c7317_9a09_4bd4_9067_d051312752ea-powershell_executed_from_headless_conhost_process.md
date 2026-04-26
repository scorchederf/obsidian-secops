---
sigma_id: "056c7317-9a09-4bd4-9067-d051312752ea"
title: "Powershell Executed From Headless ConHost Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_conhost_headless_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_headless_powershell.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "056c7317-9a09-4bd4-9067-d051312752ea"
  - "Powershell Executed From Headless ConHost Process"
attack_technique_ids:
  - "T1059.001"
  - "T1059.003"
  - "T1564.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Executed From Headless ConHost Process

Detects the use of powershell commands from headless ConHost window.
The "--headless" flag hides the windows from the user upon execution.

## Metadata

- Rule ID: 056c7317-9a09-4bd4-9067-d051312752ea
- Status: test
- Level: medium
- Author: Matt Anderson (Huntress)
- Date: 2024-07-23
- Source Path: rules/windows/process_creation/proc_creation_win_conhost_headless_powershell.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \conhost.exe
- OriginalFileName: CONHOST.EXE
selection_cli:
  CommandLine|contains|all:
  - --headless
  - powershell
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.huntress.com/blog/fake-browser-updates-lead-to-boinc-volunteer-computing-software

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_headless_powershell.yml)
