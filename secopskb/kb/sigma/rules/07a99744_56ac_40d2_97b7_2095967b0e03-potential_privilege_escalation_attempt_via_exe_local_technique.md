---
sigma_id: "07a99744-56ac-40d2-97b7-2095967b0e03"
title: "Potential Privilege Escalation Attempt Via .Exe.Local Technique"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_system32_local_folder_privilege_escalation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_system32_local_folder_privilege_escalation.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "07a99744-56ac-40d2-97b7-2095967b0e03"
  - "Potential Privilege Escalation Attempt Via .Exe.Local Technique"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Privilege Escalation Attempt Via .Exe.Local Technique

Detects potential privilege escalation attempt via the creation of the "*.Exe.Local" folder inside the "System32" directory in order to sideload "comctl32.dll"

## Metadata

- Rule ID: 07a99744-56ac-40d2-97b7-2095967b0e03
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Subhash P (@pbssubhash)
- Date: 2022-12-16
- Modified: 2022-12-19
- Source Path: rules/windows/file/file_event/file_event_win_system32_local_folder_privilege_escalation.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|startswith:
  - C:\Windows\System32\logonUI.exe.local
  - C:\Windows\System32\werFault.exe.local
  - C:\Windows\System32\consent.exe.local
  - C:\Windows\System32\narrator.exe.local
  - C:\Windows\System32\wermgr.exe.local
  TargetFilename|endswith: \comctl32.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/binderlabs/DirCreate2System
- https://github.com/sailay1996/awesome_windows_logical_bugs/blob/60cbb23a801f4c3195deac1cc46df27c225c3d07/dir_create2system.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_system32_local_folder_privilege_escalation.yml)
