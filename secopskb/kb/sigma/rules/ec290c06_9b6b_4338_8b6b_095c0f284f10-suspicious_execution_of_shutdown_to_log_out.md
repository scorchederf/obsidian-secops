---
sigma_id: "ec290c06-9b6b-4338-8b6b-095c0f284f10"
title: "Suspicious Execution of Shutdown to Log Out"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_shutdown_logoff.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_shutdown_logoff.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ec290c06-9b6b-4338-8b6b-095c0f284f10"
  - "Suspicious Execution of Shutdown to Log Out"
attack_technique_ids:
  - "T1529"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Execution of Shutdown to Log Out

Detects the rare use of the command line tool shutdown to logoff a user

## Metadata

- Rule ID: ec290c06-9b6b-4338-8b6b-095c0f284f10
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-10-01
- Source Path: rules/windows/process_creation/proc_creation_win_shutdown_logoff.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1529-system_shutdown_reboot|T1529]]

## Detection

```yaml
selection:
  Image|endswith: \shutdown.exe
  CommandLine|contains: /l
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/9e5b12c4912c07562aec7500447b11fa3e17e254/atomics/T1529/T1529.md
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_shutdown_logoff.yml)
