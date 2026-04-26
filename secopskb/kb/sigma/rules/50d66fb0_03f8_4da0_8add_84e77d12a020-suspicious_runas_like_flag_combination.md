---
sigma_id: "50d66fb0-03f8-4da0-8add-84e77d12a020"
title: "Suspicious RunAs-Like Flag Combination"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_privilege_escalation_cli_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_privilege_escalation_cli_patterns.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "50d66fb0-03f8-4da0-8add-84e77d12a020"
  - "Suspicious RunAs-Like Flag Combination"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious RunAs-Like Flag Combination

Detects suspicious command line flags that let the user set a target user and command as e.g. seen in PsExec-like tools

## Metadata

- Rule ID: 50d66fb0-03f8-4da0-8add-84e77d12a020
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-11-11
- Source Path: rules/windows/process_creation/proc_creation_win_susp_privilege_escalation_cli_patterns.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_user:
  CommandLine|contains:
  - ' -u system '
  - ' --user system '
  - ' -u NT'
  - ' -u "NT'
  - ' -u ''NT'
  - ' --system '
  - ' -u administrator '
selection_command:
  CommandLine|contains:
  - ' -c cmd'
  - ' -c "cmd'
  - ' -c powershell'
  - ' -c "powershell'
  - ' --command cmd'
  - ' --command powershell'
  - ' -c whoami'
  - ' -c wscript'
  - ' -c cscript'
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.trendmicro.com/en_us/research/22/k/hack-the-real-box-apt41-new-subgroup-earth-longzhi.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_privilege_escalation_cli_patterns.yml)
