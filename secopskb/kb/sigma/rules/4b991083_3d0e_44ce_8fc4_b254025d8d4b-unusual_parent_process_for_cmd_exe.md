---
sigma_id: "4b991083-3d0e-44ce-8fc4-b254025d8d4b"
title: "Unusual Parent Process For Cmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_unusual_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_unusual_parent.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4b991083-3d0e-44ce-8fc4-b254025d8d4b"
  - "Unusual Parent Process For Cmd.EXE"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unusual Parent Process For Cmd.EXE

Detects suspicious parent process for cmd.exe

## Metadata

- Rule ID: 4b991083-3d0e-44ce-8fc4-b254025d8d4b
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-21
- Modified: 2023-12-05
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_unusual_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  Image|endswith: \cmd.exe
  ParentImage|endswith:
  - \csrss.exe
  - \ctfmon.exe
  - \dllhost.exe
  - \epad.exe
  - \FlashPlayerUpdateService.exe
  - \GoogleUpdate.exe
  - \jucheck.exe
  - \jusched.exe
  - \LogonUI.exe
  - \lsass.exe
  - \regsvr32.exe
  - \SearchIndexer.exe
  - \SearchProtocolHost.exe
  - \SIHClient.exe
  - \sihost.exe
  - \slui.exe
  - \spoolsv.exe
  - \sppsvc.exe
  - \taskhostw.exe
  - \unsecapp.exe
  - \WerFault.exe
  - \wermgr.exe
  - \wlanext.exe
  - \WUDFHost.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/unusual-parent-process-for-cmd.exe.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_unusual_parent.yml)
