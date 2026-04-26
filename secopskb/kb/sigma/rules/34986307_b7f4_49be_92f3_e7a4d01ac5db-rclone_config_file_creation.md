---
sigma_id: "34986307-b7f4-49be-92f3-e7a4d01ac5db"
title: "Rclone Config File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_rclone_config_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_rclone_config_files.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "34986307-b7f4-49be-92f3-e7a4d01ac5db"
  - "Rclone Config File Creation"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rclone Config File Creation

Detects Rclone config files being created

## Metadata

- Rule ID: 34986307-b7f4-49be-92f3-e7a4d01ac5db
- Status: test
- Level: medium
- Author: Aaron Greetham (@beardofbinary) - NCC Group
- Date: 2021-05-26
- Modified: 2023-05-09
- Source Path: rules/windows/file/file_event/file_event_win_rclone_config_files.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  TargetFilename|contains|all:
  - :\Users\
  - \.config\rclone\
condition: selection
```

## False Positives

- Legitimate Rclone usage

## References

- https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_rclone_config_files.yml)
