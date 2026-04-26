---
sigma_id: "e212d415-0e93-435f-9e1a-f29005bb4723"
title: "Suspicious Remote Child Process From Outlook"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes_remote.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes_remote.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e212d415-0e93-435f-9e1a-f29005bb4723"
  - "Suspicious Remote Child Process From Outlook"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Remote Child Process From Outlook

Detects a suspicious child process spawning from Outlook where the image is located in a remote location (SMB/WebDav shares).

## Metadata

- Rule ID: e212d415-0e93-435f-9e1a-f29005bb4723
- Status: test
- Level: high
- Author: Markus Neis, Nasreddine Bencherchali (Nextron Systems)
- Date: 2018-12-27
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes_remote.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  ParentImage|endswith: \outlook.exe
  Image|startswith: \\\\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/sensepost/ruler
- https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html
- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=49

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes_remote.yml)
