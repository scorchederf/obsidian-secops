---
sigma_id: "dde85b37-40cd-4a94-b00c-0b8794f956b5"
title: "Remote Task Creation via ATSVC Named Pipe - Zeek"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "zeek / smb_files"
aliases:
  - "dde85b37-40cd-4a94-b00c-0b8794f956b5"
  - "Remote Task Creation via ATSVC Named Pipe - Zeek"
attack_technique_ids:
  - "T1053.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Task Creation via ATSVC Named Pipe - Zeek

Detects remote task creation via at.exe or API interacting with ATSVC namedpipe

## Metadata

- Rule ID: dde85b37-40cd-4a94-b00c-0b8794f956b5
- Status: test
- Level: medium
- Author: Samir Bousseaden, @neu5rn
- Date: 2020-04-03
- Modified: 2022-12-27
- Source Path: rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml

## Logsource

- product: zeek
- service: smb_files

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.002]]

## Detection

```yaml
selection:
  path: \\\*\IPC$
  name: atsvc
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20230409194125/https://blog.menasec.net/2019/03/threat-hunting-25-scheduled-tasks-for.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_smb_converted_win_atsvc_task.yml)
