---
sigma_id: "5f87308a-0a5b-4623-ae15-d8fa1809bc60"
title: "Suspicious Files in Default GPO Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_default_gpo_dir_write.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_default_gpo_dir_write.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "5f87308a-0a5b-4623-ae15-d8fa1809bc60"
  - "Suspicious Files in Default GPO Folder"
attack_technique_ids:
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Files in Default GPO Folder

Detects the creation of copy of suspicious files (EXE/DLL) to the default GPO storage folder

## Metadata

- Rule ID: 5f87308a-0a5b-4623-ae15-d8fa1809bc60
- Status: test
- Level: medium
- Author: elhoim
- Date: 2022-04-28
- Source Path: rules/windows/file/file_event/file_event_win_susp_default_gpo_dir_write.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
  TargetFilename|contains: \Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\
  TargetFilename|endswith:
  - .dll
  - .exe
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/intelligence-insights-november-2021/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_default_gpo_dir_write.yml)
