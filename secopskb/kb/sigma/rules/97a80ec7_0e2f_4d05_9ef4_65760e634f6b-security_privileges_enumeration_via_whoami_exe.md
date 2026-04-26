---
sigma_id: "97a80ec7-0e2f-4d05-9ef4-65760e634f6b"
title: "Security Privileges Enumeration Via Whoami.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_whoami_priv_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_priv_discovery.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "97a80ec7-0e2f-4d05-9ef4-65760e634f6b"
  - "Security Privileges Enumeration Via Whoami.EXE"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Security Privileges Enumeration Via Whoami.EXE

Detects a whoami.exe executed with the /priv command line flag instructing the tool to show all current user privileges. This is often used after a privilege escalation attempt.

## Metadata

- Rule ID: 97a80ec7-0e2f-4d05-9ef4-65760e634f6b
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-05-05
- Modified: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_whoami_priv_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection_img:
- Image|endswith: \whoami.exe
- OriginalFileName: whoami.exe
selection_cli:
  CommandLine|contains:
  - ' /priv'
  - ' -priv'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_priv_discovery.yml)
