---
sigma_id: "1012f107-b8f1-4271-af30-5aed2de89b39"
title: "Terminal Service Process Spawn"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_svchost_termserv_proc_spawn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_termserv_proc_spawn.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1012f107-b8f1-4271-af30-5aed2de89b39"
  - "Terminal Service Process Spawn"
attack_technique_ids:
  - "T1190"
  - "T1210"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Terminal Service Process Spawn

Detects a process spawned by the terminal service server process (this could be an indicator for an exploitation of CVE-2019-0708)

## Metadata

- Rule ID: 1012f107-b8f1-4271-af30-5aed2de89b39
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-05-22
- Modified: 2023-01-25
- Source Path: rules/windows/process_creation/proc_creation_win_svchost_termserv_proc_spawn.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1210-exploitation_of_remote_services|T1210]]

## Detection

```yaml
selection:
  ParentCommandLine|contains|all:
  - \svchost.exe
  - termsvcs
filter_img:
  Image|endswith:
  - \rdpclip.exe
  - :\Windows\System32\csrss.exe
  - :\Windows\System32\wininit.exe
  - :\Windows\System32\winlogon.exe
filter_null:
  Image: null
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://securingtomorrow.mcafee.com/other-blogs/mcafee-labs/rdp-stands-for-really-do-patch-understanding-the-wormable-rdp-vulnerability-cve-2019-0708/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_termserv_proc_spawn.yml)
