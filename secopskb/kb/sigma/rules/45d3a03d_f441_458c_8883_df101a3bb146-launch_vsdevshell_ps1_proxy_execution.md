---
sigma_id: "45d3a03d-f441-458c-8883-df101a3bb146"
title: "Launch-VsDevShell.PS1 Proxy Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "45d3a03d-f441-458c-8883-df101a3bb146"
  - "Launch-VsDevShell.PS1 Proxy Execution"
attack_technique_ids:
  - "T1216.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Launch-VsDevShell.PS1 Proxy Execution

Detects the use of the 'Launch-VsDevShell.ps1' Microsoft signed script to execute commands.

## Metadata

- Rule ID: 45d3a03d-f441-458c-8883-df101a3bb146
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-19
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216.001]]

## Detection

```yaml
selection_script:
  CommandLine|contains: Launch-VsDevShell.ps1
selection_flags:
  CommandLine|contains:
  - 'VsWherePath '
  - 'VsInstallationPath '
condition: all of selection_*
```

## False Positives

- Legitimate usage of the script by a developer

## References

- https://twitter.com/nas_bench/status/1535981653239255040

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_launch_vsdevshell.yml)
