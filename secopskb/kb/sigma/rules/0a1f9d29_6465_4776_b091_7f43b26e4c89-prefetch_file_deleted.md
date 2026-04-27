---
sigma_id: "0a1f9d29-6465-4776-b091-7f43b26e4c89"
title: "Prefetch File Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_prefetch.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_prefetch.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the deletion of a prefetch file which may indicate an attempt to destroy forensic evidence

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]

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
