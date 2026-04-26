---
sigma_id: "69ca12af-119d-44ed-b50f-a47af0ebc364"
title: "LSASS Process Memory Dump Creation Via Taskmgr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_taskmgr_lsass_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_taskmgr_lsass_dump.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "69ca12af-119d-44ed-b50f-a47af0ebc364"
  - "LSASS Process Memory Dump Creation Via Taskmgr.EXE"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LSASS Process Memory Dump Creation Via Taskmgr.EXE

Detects the creation of an "lsass.dmp" file by the taskmgr process. This indicates a manual dumping of the LSASS.exe process memory using Windows Task Manager.

## Metadata

- Rule ID: 69ca12af-119d-44ed-b50f-a47af0ebc364
- Status: test
- Level: high
- Author: Swachchhanda Shrawan Poudel
- Date: 2023-10-19
- Source Path: rules/windows/file/file_event/file_event_win_taskmgr_lsass_dump.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - :\Windows\system32\taskmgr.exe
  - :\Windows\SysWOW64\taskmgr.exe
  TargetFilename|contains|all:
  - \AppData\Local\Temp\
  - \lsass
  - .DMP
condition: selection
```

## False Positives

- Rare case of troubleshooting by an administrator or support that has to be investigated regardless

## References

- https://github.com/redcanaryco/atomic-red-team/blob/987e3ca988ae3cff4b9f6e388c139c05bf44bbb8/atomics/T1003.001/T1003.001.md#L1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_taskmgr_lsass_dump.yml)
