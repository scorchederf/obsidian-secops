---
sigma_id: "34275eb8-fa19-436b-b959-3d9ecd53fa1f"
title: "Loaded Module Enumeration Via Tasklist.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tasklist_module_enumeration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tasklist_module_enumeration.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "34275eb8-fa19-436b-b959-3d9ecd53fa1f"
  - "Loaded Module Enumeration Via Tasklist.EXE"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Loaded Module Enumeration Via Tasklist.EXE

Detects the enumeration of a specific DLL or EXE being used by a binary via "tasklist.exe".
This is often used by attackers in order to find the specific process identifier (PID) that is using the DLL in question.
In order to dump the process memory or perform other nefarious actions.

## Metadata

- Rule ID: 34275eb8-fa19-436b-b959-3d9ecd53fa1f
- Status: test
- Level: medium
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-02-12
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_tasklist_module_enumeration.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection_img:
- Image|endswith: \tasklist.exe
- OriginalFileName: tasklist.exe
selection_flags:
  CommandLine|contains|windash: -m
selection_module:
  CommandLine|contains: rdpcorets.dll
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.n00py.io/2021/05/dumping-plaintext-rdp-credentials-from-svchost-exe/
- https://pentestlab.blog/tag/svchost/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tasklist_module_enumeration.yml)
