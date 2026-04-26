---
sigma_id: "0a1f9d29-6465-4776-b091-7f43b26e4c89"
title: "Prefetch File Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_prefetch.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_prefetch.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / file_delete"
aliases:
  - "0a1f9d29-6465-4776-b091-7f43b26e4c89"
  - "Prefetch File Deleted"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Prefetch File Deleted

Detects the deletion of a prefetch file which may indicate an attempt to destroy forensic evidence

## Metadata

- Rule ID: 0a1f9d29-6465-4776-b091-7f43b26e4c89
- Status: test
- Level: high
- Author: Cedric MAURUGEON
- Date: 2021-09-29
- Modified: 2024-01-25
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_prefetch.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection:
  TargetFilename|contains: :\Windows\Prefetch\
  TargetFilename|endswith: .pf
filter_main_svchost:
  Image|endswith: :\windows\system32\svchost.exe
  User|contains:
  - AUTHORI
  - AUTORI
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research
- https://www.group-ib.com/blog/hunting-for-ttps-with-prefetch-files/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_prefetch.yml)
