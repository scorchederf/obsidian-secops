---
sigma_id: "0900463c-b33b-49a8-be1d-552a3b553dae"
title: "Potential Hidden Directory Creation Via NTFS INDEX_ALLOCATION Stream - CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_hidden_dir_index_allocation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_hidden_dir_index_allocation.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0900463c-b33b-49a8-be1d-552a3b553dae"
  - "Potential Hidden Directory Creation Via NTFS INDEX_ALLOCATION Stream - CLI"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Hidden Directory Creation Via NTFS INDEX_ALLOCATION Stream - CLI

Detects command line containing reference to the "::$index_allocation" stream, which can be used as a technique to prevent access to folders or files from tooling such as "explorer.exe" or "powershell.exe"

## Metadata

- Rule ID: 0900463c-b33b-49a8-be1d-552a3b553dae
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Scoubi (@ScoubiMtl)
- Date: 2023-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_hidden_dir_index_allocation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection:
  CommandLine|contains: ::$index_allocation
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_hidden_dir_index_allocation.yml)
