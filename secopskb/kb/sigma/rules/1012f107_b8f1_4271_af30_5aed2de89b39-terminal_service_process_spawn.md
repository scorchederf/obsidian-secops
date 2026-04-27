---
sigma_id: "1012f107-b8f1-4271-af30-5aed2de89b39"
title: "Terminal Service Process Spawn"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_svchost_termserv_proc_spawn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_termserv_proc_spawn.yml"
build_date: "2026-04-27 19:13:57"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a process spawned by the terminal service server process (this could be an indicator for an exploitation of CVE-2019-0708)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[kb/attack/techniques/T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]

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
