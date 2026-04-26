---
sigma_id: "9703792d-fd9a-456d-a672-ff92efe4806a"
title: "Backup Catalog Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/microsoft_windows_backup/win_susp_backup_delete.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/microsoft_windows_backup/win_susp_backup_delete.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / application"
aliases:
  - "9703792d-fd9a-456d-a672-ff92efe4806a"
  - "Backup Catalog Deleted"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Backup Catalog Deleted

Detects backup catalog deletions

## Metadata

- Rule ID: 9703792d-fd9a-456d-a672-ff92efe4806a
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Tom U. @c_APT_ure (collection)
- Date: 2017-05-12
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/application/microsoft_windows_backup/win_susp_backup_delete.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection:
  EventID: 524
  Provider_Name: Microsoft-Windows-Backup
condition: selection
```

## False Positives

- Unknown

## References

- https://technet.microsoft.com/en-us/library/cc742154(v=ws.11).aspx
- https://www.hybrid-analysis.com/sample/ed01ebfbc9eb5bbea545af4d01bf5f1071661840480439c6e5babe8e080e41aa?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/microsoft_windows_backup/win_susp_backup_delete.yml)
