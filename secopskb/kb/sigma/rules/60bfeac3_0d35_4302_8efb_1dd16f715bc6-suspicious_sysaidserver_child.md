---
sigma_id: "60bfeac3-0d35-4302-8efb-1dd16f715bc6"
title: "Suspicious SysAidServer Child"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_java_sysaidserver_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_sysaidserver_susp_child_process.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "60bfeac3-0d35-4302-8efb-1dd16f715bc6"
  - "Suspicious SysAidServer Child"
attack_technique_ids:
  - "T1210"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious SysAidServer Child

Detects suspicious child processes of SysAidServer (as seen in MERCURY threat actor intrusions)

## Metadata

- Rule ID: 60bfeac3-0d35-4302-8efb-1dd16f715bc6
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-26
- Source Path: rules/windows/process_creation/proc_creation_win_java_sysaidserver_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1210-exploitation_of_remote_services|T1210]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \java.exe
  - \javaw.exe
  ParentCommandLine|contains: SysAidServer
condition: selection
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/08/25/mercury-leveraging-log4j-2-vulnerabilities-in-unpatched-systems-to-target-israeli-organizations/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_java_sysaidserver_susp_child_process.yml)
