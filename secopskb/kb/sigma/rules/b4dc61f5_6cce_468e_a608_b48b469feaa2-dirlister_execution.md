---
sigma_id: "b4dc61f5-6cce-468e-a608-b48b469feaa2"
title: "DirLister Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dirlister_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dirlister_execution.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "b4dc61f5-6cce-468e-a608-b48b469feaa2"
  - "DirLister Execution"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DirLister Execution

Detect the usage of "DirLister.exe" a utility for quickly listing folder or drive contents. It was seen used by BlackCat ransomware to create a list of accessible directories and files.

## Metadata

- Rule ID: b4dc61f5-6cce-468e-a608-b48b469feaa2
- Status: test
- Level: low
- Author: frack113
- Date: 2022-08-20
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_dirlister_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection:
- OriginalFileName: DirLister.exe
- Image|endswith: \DirLister.exe
condition: selection
```

## False Positives

- Legitimate use by users

## Simulation

### Launch DirLister Executable

- atomic_guid: c5bec457-43c9-4a18-9a24-fe151d8971b7
- name: Launch DirLister Executable
- technique: T1083
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1083/T1083.md
- https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dirlister_execution.yml)
