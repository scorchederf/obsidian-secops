---
sigma_id: "f01d1f70-cd41-42ec-9c0b-26dd9c22bf29"
title: "Process Deletion of Its Own Executable"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_delete_own_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_own_image.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "f01d1f70-cd41-42ec-9c0b-26dd9c22bf29"
  - "Process Deletion of Its Own Executable"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Process Deletion of Its Own Executable

Detects the deletion of a process's executable by itself. This is usually not possible without workarounds and may be used by malware to hide its traces.

## Metadata

- Rule ID: f01d1f70-cd41-42ec-9c0b-26dd9c22bf29
- Status: test
- Level: medium
- Author: Max Altgelt (Nextron Systems)
- Date: 2024-09-03
- Source Path: rules/windows/file/file_delete/file_delete_win_delete_own_image.yml

## Logsource

- category: file_delete
- product: windows

## Detection

```yaml
selection:
  TargetFilename|fieldref: Image
condition: selection
```

## False Positives

- Some false positives are to be expected from uninstallers.

## References

- https://github.com/joaoviictorti/RustRedOps/tree/ce04369a246006d399e8c61d9fe0e6b34f988a49/Self_Deletion

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_delete_own_image.yml)
