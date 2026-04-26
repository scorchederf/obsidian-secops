---
sigma_id: "a8f866e1-bdd4-425e-a27a-37619238d9c7"
title: "Potential Hidden Directory Creation Via NTFS INDEX_ALLOCATION Stream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_hidden_dir_index_allocation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_hidden_dir_index_allocation.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "a8f866e1-bdd4-425e-a27a-37619238d9c7"
  - "Potential Hidden Directory Creation Via NTFS INDEX_ALLOCATION Stream"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Hidden Directory Creation Via NTFS INDEX_ALLOCATION Stream

Detects the creation of hidden file/folder with the "::$index_allocation" stream. Which can be used as a technique to prevent access to folder and files from tooling such as "explorer.exe" and "powershell.exe"

## Metadata

- Rule ID: a8f866e1-bdd4-425e-a27a-37619238d9c7
- Status: test
- Level: medium
- Author: Scoubi (@ScoubiMtl)
- Date: 2023-10-09
- Source Path: rules/windows/file/file_event/file_event_win_susp_hidden_dir_index_allocation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection:
  TargetFilename|contains: ::$index_allocation
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/pfiatde/status/1681977680688738305
- https://soroush.me/blog/2010/12/a-dotty-salty-directory-a-secret-place-in-ntfs-for-secret-files/
- https://sec-consult.com/blog/detail/pentesters-windows-ntfs-tricks-collection/
- https://github.com/redcanaryco/atomic-red-team/blob/5c3b23002d2bbede3c07e7307165fc2a235a427d/atomics/T1564.004/T1564.004.md#atomic-test-5---create-hidden-directory-via-index_allocation
- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/c54dec26-1551-4d3a-a0ea-4fa40f848eb3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_hidden_dir_index_allocation.yml)
