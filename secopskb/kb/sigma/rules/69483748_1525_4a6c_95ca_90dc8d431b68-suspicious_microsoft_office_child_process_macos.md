---
sigma_id: "69483748-1525-4a6c-95ca-90dc8d431b68"
title: "Suspicious Microsoft Office Child Process - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_office_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_office_susp_child_processes.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "69483748-1525-4a6c-95ca-90dc8d431b68"
  - "Suspicious Microsoft Office Child Process - MacOS"
attack_technique_ids:
  - "T1059.002"
  - "T1137.002"
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious child processes spawning from microsoft office suite applications such as word or excel. This could indicates malicious macro execution

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]]
- [[kb/attack/techniques/T1137-office_application_startup#^t1137002-office-test|T1137.002: Office Test]]
- [[kb/attack/techniques/T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]

## Detection

```yaml
selection:
  ParentImage|contains:
  - Microsoft Word
  - Microsoft Excel
  - Microsoft PowerPoint
  - Microsoft OneNote
  Image|endswith:
  - /bash
  - /curl
  - /dash
  - /fish
  - /osacompile
  - /osascript
  - /sh
  - /zsh
  - /python
  - /python3
  - /wget
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/applescript/
- https://objective-see.org/blog/blog_0x4B.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_office_susp_child_processes.yml)
