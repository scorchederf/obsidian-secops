---
sigma_id: "9bd04a79-dabe-4f1f-a5ff-92430265c96b"
title: "Privilege Escalation via Named Pipe Impersonation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_priv_escalation_via_named_pipe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_priv_escalation_via_named_pipe.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9bd04a79-dabe-4f1f-a5ff-92430265c96b"
  - "Privilege Escalation via Named Pipe Impersonation"
attack_technique_ids:
  - "T1021"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Privilege Escalation via Named Pipe Impersonation

Detects a remote file copy attempt to a hidden network share. This may indicate lateral movement or data staging activity.

## Metadata

- Rule ID: 9bd04a79-dabe-4f1f-a5ff-92430265c96b
- Status: test
- Level: high
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-27
- Modified: 2022-12-30
- Source Path: rules/windows/process_creation/proc_creation_win_susp_priv_escalation_via_named_pipe.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021]]

## Detection

```yaml
selection_name:
- Image|endswith:
  - \cmd.exe
  - \powershell.exe
- OriginalFileName:
  - Cmd.Exe
  - PowerShell.EXE
selection_args:
  CommandLine|contains|all:
  - echo
  - '>'
  - \\\\.\\pipe\\
condition: all of selection*
```

## False Positives

- Other programs that cause these patterns (please report)

## References

- https://www.elastic.co/guide/en/security/current/privilege-escalation-via-named-pipe-impersonation.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_priv_escalation_via_named_pipe.yml)
